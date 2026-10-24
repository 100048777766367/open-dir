import os, json

WORKSPACE = "/tmp/bodhi_dissector"
os.chdir(WORKSPACE)

print("📁 [OPEN-DIR REAL ENGINE] Đang bóc tách độ sâu và đếm file từng thư mục...")
dir_result = {"directories": []}

try:
    with open("tree_out.json", "r") as f: paths = json.load(f)["paths"]
    # Tìm tên repo từ thư mục hiện tại trong workspace
    repos = [d for d in os.listdir(".") if os.path.isdir(d) and d not in ["storage"]]
    target_repo = repos[0] if repos else "retina"

    for p in paths:
        full_p = os.path.join(target_repo, p)
        if os.path.isdir(full_p):
            fc = len([x for x in os.listdir(full_p) if os.path.isfile(os.path.join(full_p, x))])
            dir_result["directories"].append({"path": p, "depth": p.count(os.sep) + 1, "file_count": fc})

    with open("dir_out.json", "w") as f: json.dump(dir_result, f)
    print(f"✅ [OPEN-DIR] Đã bóc tách xong {len(dir_result['directories'])} thư mục vào `dir_out.json`.")
except Exception as e:
    print(f"🔴 Lỗi ở open-dir: {e}")
