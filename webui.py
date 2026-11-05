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
:root{
  color-scheme:light dark;
  --bg:#faf9f6;
  --surface:#ffffff;
  --panel:#f4f2ec;
  --line:#e3e0d8;
  --line-strong:#cec9bd;
  --ink:#1b1a17;
  --muted:#6f6b62;
  --accent:#8a5a12;
  --accent-ink:#fdfbf6;
  --ring:rgba(138,90,18,.18);
  --mono:ui-monospace,SFMono-Regular,"Cascadia Mono",Consolas,"Liberation Mono",monospace;
}
@media (prefers-color-scheme:dark){
  :root{
    --bg:#121211;
    --surface:#181817;
    --panel:#1d1d1b;
    --line:#2b2a27;
    --line-strong:#3a3832;
    --ink:#ecebe6;
    --muted:#9d988e;
    --accent:#d3a45c;
    --accent-ink:#14130f;
    --ring:rgba(211,164,92,.22);
  }
}
*{box-sizing:border-box}
body{
  margin:0;background:var(--bg);color:var(--ink);
  font:14px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}
.wrap{max-width:860px;margin:0 auto;padding:40px 24px 72px}
.masthead{position:relative;padding-bottom:24px;border-bottom:1px solid var(--line)}
.masthead::after{content:"";position:absolute;left:0;bottom:-1px;width:48px;height:2px;background:var(--accent)}
h1{margin:0 0 8px;font-size:22px;line-height:1.2;font-weight:600;letter-spacing:-.015em}
.sub{margin:0;max-width:64ch;color:var(--muted)}
.tool{display:grid;gap:16px;margin-top:32px}
.tool + .tool{padding-top:32px;border-top:1px solid var(--line)}
.toolhead{display:flex;align-items:baseline;justify-content:space-between;gap:16px}
h2{margin:0;font-size:14px;font-weight:600;letter-spacing:.01em}
.hint{font:11px/1.4 var(--mono);color:var(--muted);white-space:nowrap}
form{display:grid;gap:12px}
input:not([type=checkbox]),textarea{
  width:100%;padding:10px 12px;border:1px solid var(--line-strong);border-radius:8px;
  background:var(--surface);color:var(--ink);font:inherit;line-height:1.5;
}
textarea{min-height:96px;resize:vertical}
input:not([type=checkbox]):focus,textarea:focus{
  border-color:var(--accent);box-shadow:0 0 0 3px var(--ring);outline:none;
}
::placeholder{color:var(--muted);opacity:.85}
.fields{display:grid;grid-template-columns:1.6fr 1fr 1.2fr;gap:8px}
.row{display:flex;flex-wrap:wrap;align-items:center;gap:8px 20px;color:var(--muted);font-size:13px}
.row label{display:inline-flex;align-items:center;gap:8px;cursor:pointer}
input[type=checkbox]{accent-color:var(--accent);width:15px;height:15px;margin:0}
.num{margin-left:auto}
input[type=number]{width:64px;text-align:right;font-variant-numeric:tabular-nums}
.actions{display:flex;align-items:center;gap:16px;flex-wrap:wrap}
button{
  padding:8px 16px;border:1px solid transparent;border-radius:6px;
  background:var(--accent);color:var(--accent-ink);
  font:inherit;font-size:13.5px;font-weight:500;cursor:pointer;
  transition:filter .15s ease,transform .06s ease;
}
button:hover{filter:brightness(1.08)}
button:active{transform:translateY(1px)}
.status{display:inline-flex;align-items:center;gap:8px;font:12px/1.4 var(--mono);color:var(--muted)}
.status:not(:empty)::before{
  content:"";width:6px;height:6px;border-radius:50%;background:var(--accent);
  animation:pulse 1.4s ease-in-out infinite;
}
@keyframes pulse{50%{opacity:.25}}
.out{border:1px solid var(--line);border-radius:8px;background:var(--surface);overflow:hidden}
.outbar{
  display:flex;align-items:center;justify-content:space-between;gap:16px;
  padding:8px 12px;border-bottom:1px solid var(--line);background:var(--panel);
  font:11px/1.4 var(--mono);color:var(--muted);
}
.outbar .label{color:var(--ink);letter-spacing:.02em}
pre{
  margin:0;padding:16px;min-height:160px;max-height:60vh;overflow:auto;
  white-space:pre-wrap;overflow-wrap:anywhere;tab-size:2;
  font:12.5px/1.65 var(--mono);color:var(--ink);
}
pre:empty::before{content:"No output yet.";color:var(--muted)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
@media (max-width:600px){
  .wrap{padding:24px 16px 48px}
  .toolhead{display:block}
  .hint{display:block;margin-top:4px;white-space:normal}
  .fields{grid-template-columns:1fr}
  .num{margin-left:0}
}
@media (prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important}
}
</style>
</head>
<body>
<main class="wrap">
<header class="masthead">
<h1>Deadlock RAG</h1>
<p class="sub">A local RAG oracle over the Deadlock corpus, plus a build generator. Retrieval and validation run on this machine; only answer and build generation call a model endpoint.</p>
</header>
<section class="tool">
<div class="toolhead"><h2>Ask the corpus</h2><span class="hint">top-k chunks, then an answer</span></div>
<form id="q">
<textarea name="question" aria-label="Question" placeholder="Ask about Deadlock..."></textarea>
<div class="row">
<label><input type="checkbox" name="generate" checked> generate answer (OpenCode)</label>
<label><input type="checkbox" name="rewrite"> rewrite query</label>
<label class="num">top-k <input type="number" name="top_k" value="5" min="1" max="20"></label>
</div>
<div class="actions">
<button type="submit">Ask</button>
<span id="qstatus" class="status" role="status" aria-live="polite"></span>
</div>
</form>
<div class="out">
<div class="outbar"><span class="label">retrieval</span><span>plain text</span></div>
<pre id="out"></pre>
</div>
</section>
<section class="tool">
<div class="toolhead"><h2>Build generator</h2><span class="hint">takes about a minute</span></div>
<form id="b">
<div class="fields">
<input name="hero" aria-label="Hero" placeholder="Hero" required>
<input name="role" aria-label="Role" placeholder="role" value="default">
<input name="constraints" aria-label="Constraints" placeholder="constraints" value="none">
</div>
<div class="row">
<label><input type="checkbox" name="ability_order"> ability order</label>
</div>
<div class="actions">
<button type="submit">Generate build</button>
<span id="bstatus" class="status" role="status" aria-live="polite"></span>
</div>
</form>
<div class="out">
<div class="outbar"><span class="label">build document</span><span>plain text</span></div>
<pre id="buildout"></pre>
</div>
</section>
</main>
<script>
const form=document.getElementById('q');
const qstatus=document.getElementById('qstatus');
form.addEventListener('submit',async e=>{
  e.preventDefault();
  const fd=new FormData(form);
  const body={question:fd.get('question'),top_k:parseInt(fd.get('top_k')||'5',10),generate:fd.has('generate'),rewrite:fd.has('rewrite')};
  document.getElementById('out').textContent='...';
  qstatus.textContent='retrieving...';
  try{
    const r=await fetch('/api/query',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const j=await r.json();
    document.getElementById('out').textContent=j.answer||j.error||'no response';
  }catch(err){
    document.getElementById('out').textContent='request failed: '+err.message;
  }finally{qstatus.textContent='';}
});
</script>
<script>
const bform=document.getElementById('b');
const bstatus=document.getElementById('bstatus');
bform.addEventListener('submit',async e=>{
  e.preventDefault();
  const fd=new FormData(bform);
  const body={hero:fd.get('hero'),role:fd.get('role')||'default',constraints:fd.get('constraints')||'none',ability_order:fd.has('ability_order')};
  document.getElementById('buildout').textContent='...';
  bstatus.textContent='generating build, ~60s';
  try{
    const r=await fetch('/api/build',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body)});
    const j=await r.json();
    document.getElementById('buildout').textContent=j.output||j.error||'no response';
  }catch(err){
    document.getElementById('buildout').textContent='request failed: '+err.message;
  }finally{bstatus.textContent='';}
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
