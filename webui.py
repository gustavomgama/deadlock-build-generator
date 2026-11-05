import json
import os
import pathlib
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import rag

RAG_DIR = pathlib.Path(__file__).resolve().parent
ROOT = RAG_DIR.parent
DEFAULT_HOST = os.getenv("RAG_WEB_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("RAG_WEB_PORT", "8000"))
INDEX = pathlib.Path(os.getenv("RAG_INDEX", str(rag.DEFAULT_INDEX)))

HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Deadlock RAG</title>
<style>
body{font-family:system-ui,sans-serif;max-width:900px;margin:2rem auto;padding:0 1rem}
textarea{width:100%;min-height:6rem}
button{padding:.5rem 1rem;margin:.5rem 0}
pre{white-space:pre-wrap;background:#f6f6f6;padding:1rem;border-radius:.5rem;max-height:60vh;overflow:auto}
input{margin:.25rem}
</style>
</head>
<body>
<h1>Deadlock RAG</h1>
<form id="q">
<textarea name="question" placeholder="Ask about Deadlock..."></textarea><br>
<label><input type="checkbox" name="generate" checked> generate answer (OpenCode)</label>
<label><input type="checkbox" name="rewrite"> rewrite query</label>
<label>top-k <input type="number" name="top_k" value="5" min="1" max="20"></label><br>
<button type="submit">Ask</button>
</form>
<pre id="out"></pre>
<script>
const form=document.getElementById('q');
form.addEventListener('submit',async e=>{
  e.preventDefault();
  const fd=new FormData(form);
  const body={question:fd.get('question'),top_k:parseInt(fd.get('top_k')||'5',10),generate:fd.has('generate'),rewrite:fd.has('rewrite')};
  document.getElementById('out').textContent='...';
  const r=await fetch('/api/query',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const j=await r.json();
  document.getElementById('out').textContent=j.answer||j.error||'no response';
});
</script>
<h2>Build generator</h2>
<form id="b">
<input name="hero" placeholder="Hero" required>
<input name="role" placeholder="role" value="default">
<input name="constraints" placeholder="constraints" value="none">
<label><input type="checkbox" name="ability_order"> ability order</label>
<button type="submit">Generate build</button>
</form>
<pre id="buildout"></pre>
<script>
const bform=document.getElementById('b');
bform.addEventListener('submit',async e=>{
  e.preventDefault();
  const fd=new FormData(bform);
  const body={hero:fd.get('hero'),role:fd.get('role')||'default',constraints:fd.get('constraints')||'none',ability_order:fd.has('ability_order')};
  document.getElementById('buildout').textContent='...';
  const r=await fetch('/api/build',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
  const j=await r.json();
  document.getElementById('buildout').textContent=j.output||j.error||'no response';
});
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path.startswith("/index"):
            body = HTML.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length) if length > 0 else b""
        try:
            payload = json.loads(raw.decode("utf-8")) if raw else {}
        except Exception:
            payload = {}
        if self.path == "/api/query":
            self._handle_query(payload)
        elif self.path == "/api/build":
            self._handle_build(payload)
        else:
            self._json(404, {"error": "not found"})

    def _handle_query(self, payload):
        question = (payload.get("question") or "").strip()
        if not question:
            self._json(400, {"error": "missing question"})
            return
        top_k = int(payload.get("top_k") or 5)
        cmd = [sys.executable, str(RAG_DIR / "rag.py"), "query", question, "--top-k", str(top_k)]
        if not payload.get("generate", True):
            cmd.append("--no-generate")
        if payload.get("rewrite"):
            cmd.append("--rewrite")
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=300)
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "query timed out"})
            return
        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()
        if proc.returncode != 0:
            self._json(500, {"error": err or "query failed"})
            return
        self._json(200, {"answer": out})

    def _handle_build(self, payload):
        hero = (payload.get("hero") or "").strip()
        if not hero:
            self._json(400, {"error": "missing hero"})
            return
        role = payload.get("role") or "default"
        constraints = payload.get("constraints") or "none"
        cmd = [sys.executable, str(RAG_DIR / "buildgen.py"), hero, "--role", role, "--constraints", constraints, "--timeout", "300"]
        if payload.get("ability_order"):
            cmd.append("--ability-order")
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=600)
        except subprocess.TimeoutExpired:
            self._json(504, {"error": "build timed out"})
            return
        out = (proc.stdout or "").strip()
        err = (proc.stderr or "").strip()
        if proc.returncode != 0:
            self._json(500, {"error": err or out or "build failed"})
            return
        self._json(200, {"output": out})

    def _json(self, status, obj):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        return


def main():
    server = ThreadingHTTPServer((DEFAULT_HOST, DEFAULT_PORT), Handler)
    print(f"Web UI listening on http://{DEFAULT_HOST}:{DEFAULT_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
