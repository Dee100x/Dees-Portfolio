import os

def load_oui_database():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, "oui.txt")

    oui_db = {}

    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if "(hex)" in line:
                parts = line.split()
                prefix = parts[0].lower().replace("-", ":")
                vendor = " ".join(parts[2:])
                oui_db[prefix] = vendor

    return oui_db

OUI_DB = load_oui_database()

def get_manufacturer(mac):
    return OUI_DB.get(mac[:8].lower(), "Unknown")
