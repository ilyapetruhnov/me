"""
Build script for petruhnov.me

Reads visited countries from countries.py (a pandas DataFrame),
and injects them into template.html to produce output/index.html.

Usage:
    python3 build.py

Re-run this any time you edit countries.py (or template.html) to
regenerate the site.
"""

import json
import shutil
from pathlib import Path

from countries import VISITED

HERE = Path(__file__).parent
TEMPLATE_PATH = HERE / "template.html"
OUTPUT_DIR = HERE / "output"
OUTPUT_PATH = OUTPUT_DIR / "index.html"
VENDOR_MAP_SRC_DIR = HERE / "vendor" / "map"
VENDOR_MAP_OUT_DIR = OUTPUT_DIR / "vendor" / "map"
CV_PATH = HERE / "files/CV.pdf"
CV_OUTPUT_PATH = OUTPUT_DIR / "CV.pdf"


def country_names(df):
    names = []
    for raw_name in df["country"]:
        name = str(raw_name).strip()
        if name:
            names.append(name)
    if not names:
        raise SystemExit("No countries found in VISITED.")
    return names


def main():
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    names = country_names(VISITED)

    html = template.replace("<!--VISITED_NAMES_JSON-->", json.dumps(names))

    OUTPUT_DIR.mkdir(exist_ok=True)

    if not VENDOR_MAP_SRC_DIR.exists():
        raise SystemExit(f"Missing local map assets: {VENDOR_MAP_SRC_DIR}")
    shutil.copytree(VENDOR_MAP_SRC_DIR, VENDOR_MAP_OUT_DIR, dirs_exist_ok=True)

    if CV_PATH.exists():
        shutil.copy2(CV_PATH, CV_OUTPUT_PATH)

    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Built {OUTPUT_PATH} — {len(names)} countries marked visited.")


if __name__ == "__main__":
    main()
