import os, json
SHARED_DIR = "/tmp/bodhi_workspace"
TARGET_REPO = os.environ.get("TARGET_REPO", "retina")

print(f"📁 [OPEN-DIR] Bắt đầu đo lường thư mục cho {TARGET_REPO}...")
dir_data = {"directories": []}

try:
    with open(f"{SHARED_DIR}/tree_data.json", "r") as f: paths = json.load(f)["all_paths"]
    for p in paths:
        full_p = os.path.join(SHARED_DIR, TARGET_REPO, p)
        if os.path.isdir(full_p):
            fc = len([x for x in os.listdir(full_p) if os.path.isfile(os.path.join(full_p, x))])
            dir_data["directories"].append({"path": p, "depth": p.count(os.sep) + 1, "file_count": fc})
    with open(f"{SHARED_DIR}/dir_data.json", "w") as f: json.dump(dir_data, f)
    print("✅ [OPEN-DIR] Đã bóc tách xong độ sâu thư mục.")
except Exception as e: print(f"⚠️ Lỗi: {e}")
