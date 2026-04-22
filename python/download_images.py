import json
import os
import urllib.request
import urllib.error

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "images")
JSON_PATH = os.path.join(SCRIPT_DIR, "ppt.json")

with open(JSON_PATH, "r", encoding="utf-8") as f:
    DATA = json.load(f)



def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pages = DATA["pages"]
    total = len(pages)
    for page in pages:
        idx = page["page_index"]
        url = page["export_image_url"]
        filename = f"page_{idx:02d}.jpeg"
        filepath = os.path.join(OUTPUT_DIR, filename)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            resp = urllib.request.urlopen(req, timeout=30)
            with open(filepath, "wb") as f:
                f.write(resp.read())
            print(f"[{idx + 1}/{total}] {filename} OK")
        except (urllib.error.URLError, OSError) as e:
            print(f"[{idx + 1}/{total}] {filename} FAILED: {e}")
    print("Done.")


if __name__ == "__main__":
    main()
