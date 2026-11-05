import pathlib
import re
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "codec"))

from decode_build_code import decode_build_code  # noqa: E402
from encode_build_code import encode_build  # noqa: E402

DOC = ROOT / "docs" / "example-infernus.md"


def documented_code():
    text = DOC.read_text(encoding="utf-8")
    codes = re.findall(r"^[A-Za-z0-9+/=]{80,}$", text, flags=re.MULTILINE)
    return codes[-1]


def validate(code):
    proc = subprocess.run(
        [sys.executable, str(ROOT / "validate_build.py"), code],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


class BuildInvariantTest(unittest.TestCase):
    def test_frontmatter_is_hidden_from_display_snippets(self):
        import rag

        self.assertEqual(rag._visible('---\ntitle: "Zipline"\npageid: 676\n---\nTransit lines are fast.'), "Transit lines are fast.")

    def test_documented_code_decodes_and_validates(self):
        obj = decode_build_code(documented_code())
        self.assertIn("hero_id", obj)
        self.assertEqual(len(obj["details"]["mod_categories"]), 6)
        status, out = validate(documented_code())
        self.assertEqual(status, 0, out)
        self.assertIn("VALID", out)

    def test_reencode_round_trips(self):
        obj = decode_build_code(documented_code())
        again = decode_build_code(encode_build(obj))
        self.assertEqual(again, obj)

    def test_unknown_item_is_rejected(self):
        obj = decode_build_code(documented_code())
        obj["details"]["mod_categories"][0]["mods"].append(999999999)
        status, out = validate(encode_build(obj))
        self.assertNotEqual(status, 0)
        self.assertIn("unknown", out.lower())

    def test_duplicate_item_is_flagged(self):
        obj = decode_build_code(documented_code())
        first = obj["details"]["mod_categories"][0]["mods"][0]
        obj["details"]["mod_categories"][1]["mods"].append(first)
        _, out = validate(encode_build(obj))
        self.assertIn("duplicate item id", out.lower())


if __name__ == "__main__":
    unittest.main()
