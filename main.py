
import argparse
from datetime import datetime
import pathlib

def run(name: str):
    msg = f"Hello, {name}! Time: {datetime.utcnow().isoformat()}Z"
    print(msg)
    out = pathlib.Path("output.txt")
    out.write_text(msg + "\n", encoding="utf-8")
    print(f"[OK] Saved to {out.resolve()}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kuponex demo script")
    parser.add_argument("--name", type=str, default="Kuponex", help="Vardas arba pavadinimas")
    args = parser.parse_args()
    run(args.name)
