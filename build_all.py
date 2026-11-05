import concurrent.futures
import json
import os
import pathlib
import re
import subprocess
import sys

RAG = pathlib.Path(__file__).resolve().parent
ROOT = RAG
OUT = pathlib.Path(os.getenv("BUILD_OUT", str(RAG / "builds")))
ANALYTICS = RAG / "analytics" / "item-stats.json"
WORKERS = 4

ROLES = {
    "Infernus": "spirit burn carry, sustained area damage",
    "Seven": "spirit area carry, lightning teamfight",
    "Vindicta": "long-range sniper carry, execution",
    "Lady Geist": "spirit drain bruiser, self-sustain lane bully",
    "Abrams": "melee frontline tank, engage and charge",
    "Wraith": "weapon carry, single-target burst",
    "McGinnis": "turret zone control, gun and objective siege",
    "Paradox": "burst utility carry, pick and swap",
    "Dynamo": "support initiator, teamfight setup",
    "Kelvin": "support healer, area control",
    "Haze": "weapon carry, stealth flank sleeper",
    "Holliday": "gun brawler, mobile skirmish",
    "Bebop": "hook initiator, spirit burst pick",
    "Calico": "assassin carry, dive and escape",
    "Grey Talon": "long-range spirit carry, kiting",
    "Mo & Krill": "tank engage, dive and lockdown",
    "Shiv": "melee bruiser, rage and sustain",
    "Ivy": "support utility, save and reposition",
    "Warden": "gun bruiser, binding and duel",
    "Yamato": "melee spirit assassin, dive and execute",
    "Lash": "tank initiator, aerial engage",
    "Viscous": "tank disruptor, cube and split",
    "Pocket": "spirit burst assassin, dive and escape",
    "Mirage": "hybrid carry, gun pressure with spirit utility",
    "Vyper": "assassin gun carry, hyper-mobile",
    "Sinclair": "spirit utility carry, mind control",
    "Mina": "marksman harasser, poke and slow",
    "Drifter": "assassin stalker, isolate and execute",
    "Venator": "marksman tactical damage, long-range pressure",
    "Victor": "brawler frontliner, tanky sustained fight",
    "Paige": "support protector, saves and utility",
    "The Doorman": "mystic map control, disorient and reposition",
    "Billy": "brawler chaos frontline, close-range fight",
    "Graves": "spirit area denial, necromancer zone control",
    "Apollo": "assassin mobility carry, finesse pick",
    "Deadman Danny": "marksman reckless damage, explosive dive",
    "Rem": "mystic supportive utility, sleep and peel",
    "Silver": "brawler transforming fighter, long-range pressure",
    "Celeste": "mystic disruptive carry, burst and dazzle",
    "Rat King": "brawler scrappy frontline, tenacious fight",
    "Solomon": "mystic strategist carry, focused projectile damage",
    "Violet": "mystic creative carry, nimble projectile damage",
    "Nurse Harrow": "support healer, sustain and peel",
    "Baba": "mystic artillery, hexing area damage",
}


def hero_list():
    a = json.loads(ANALYTICS.read_text(encoding="utf-8"))
    heroes = json.loads((ROOT / "data" / "heroes_raw.json").read_text(encoding="utf-8"))
    names = {str(h["id"]): h["name"] for h in heroes}
    return [(hid, names[hid]) for hid in a]


def safe(name):
    return re.sub(r'[<>:"/\\|?*]', "", name)


def run(hero, role):
    path = OUT / f"{safe(hero)}.md"
    cmd = [
        sys.executable, str(RAG / "buildgen.py"), hero,
        "--role", role, "--analytics", str(ANALYTICS),
    ]
    last = ""
    for _ in range(3):
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=900)
        out = proc.stdout or ""
        if proc.returncode == 0 and "VALID" in out:
            path.write_text(out, encoding="utf-8")
            codes = re.findall(r"^[A-Za-z0-9+/=]{80,}$", out, flags=re.MULTILINE)
            return hero, True, (codes[-1] if codes else ""), ""
        last = ((proc.stdout or "") + (proc.stderr or "")).strip().splitlines()
        last = last[-1] if last else "unknown error"
    return hero, False, "", last


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    todo = []
    for hid, name in hero_list():
        if (OUT / f"{safe(name)}.md").exists():
            continue
        todo.append((name, ROLES.get(name, "carry, play to hero identity and analytics")))
    print(f"{len(todo)} builds to generate")
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(run, h, r) for h, r in todo]
        for fut in concurrent.futures.as_completed(futures):
            hero, ok, code, err = fut.result()
            print(f"{'ok ' if ok else 'FAIL'} {hero} {err}")
            results.append({"hero": hero, "ok": ok, "code": code, "error": err})

    index = pathlib.Path(OUT / "INDEX.md")
    lines = ["# Deadlock builds by helmet", ""]
    for hid, name in hero_list():
        p = OUT / f"{safe(name)}.md"
        if p.exists():
            m = re.findall(r"^[A-Za-z0-9+/=]{80,}$", p.read_text(encoding="utf-8"), flags=re.MULTILINE)
            lines.append(f"- {name}: `{m[-1] if m else 'MISSING'}`")
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"index -> {index}")


if __name__ == "__main__":
    main()
