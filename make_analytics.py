import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
ITEMS = ROOT / "data" / "items_raw.json"
HEROES = ROOT / "data" / "heroes_raw.json"
OUT = pathlib.Path(__file__).resolve().parent / "analytics" / "item-stats.json"
API = "https://api.deadlock-api.com/v1/analytics"
HEADERS = {"User-Agent": "deadlock-rag-buildgen"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=180) as resp:
        return json.load(resp)


def main():
    heroes = json.loads(HEROES.read_text(encoding="utf-8"))
    items = json.loads(ITEMS.read_text(encoding="utf-8"))
    usable = [
        h for h in heroes
        if h.get("player_selectable") and not h.get("disabled")
        and not h.get("prerelease_only") and h.get("development_state") == "release"
    ]
    ids = ",".join(str(h["id"]) for h in usable)
    base = f"game_mode=normal&match_mode=ranked,unranked&hero_ids={ids}"

    hero_rows = get(f"{API}/hero-stats?bucket=no_bucket&{base}")
    item_rows = get(f"{API}/item-stats?bucket=hero&{base}")

    upgrade = {}
    for it in items:
        if it.get("type") == "upgrade" and it.get("shopable"):
            upgrade[it["id"]] = it

    out = {}
    for row in hero_rows:
        hid = row["hero_id"]
        matches = row.get("matches") or 0
        if matches < 1000:
            continue
        entry = {
            "hero_win": round(100.0 * row["wins"] / matches, 2),
            "matches": matches,
            "items": [],
        }
        picked = [
            r for r in item_rows
            if r["bucket"] == hid and r["item_id"] in upgrade
            and r.get("matches", 0) >= 500
        ]
        picked.sort(key=lambda r: r["players"], reverse=True)
        for r in picked[:36]:
            it = upgrade[r["item_id"]]
            win = 100.0 * r["wins"] / r["matches"] if r["matches"] else 0.0
            entry["items"].append(
                {
                    "id": r["item_id"],
                    "name": it["name"],
                    "pick": round(100.0 * r["players"] / matches, 2),
                    "win": round(win, 2),
                    "delta": round(win - entry["hero_win"], 2),
                    "tier": it.get("item_tier"),
                    "slot": it.get("item_slot_type"),
                    "cost": it.get("cost"),
                    "buy_s": round(r["avg_buy_time_s"], 0),
                }
            )
        out[str(hid)] = entry

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"{len(out)} heroes -> {OUT}")


if __name__ == "__main__":
    main()
