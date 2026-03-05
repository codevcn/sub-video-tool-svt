import os
from pathlib import Path
from langdetect import detect, LangDetectException

# Thư mục result nằm ở root của project (2 cấp trên warehouse/)
ROOT_DIR = Path(__file__).resolve().parent.parent
RESULT_DIR = ROOT_DIR / "result"


def find_english_lines(file_path: Path):
    """Quét một file .srt và in ra các dòng bị phát hiện là tiếng Anh."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    subtitle_blocks = content.strip().split("\n\n")
    english_index_list = []

    for block in subtitle_blocks:
        lines = block.split("\n")
        if len(lines) >= 3:
            index_number = lines[0].strip()
            text = " ".join(lines[2:]).strip()
            try:
                if detect(text) == "en":
                    english_index_list.append(index_number)
                    print(f"  [EN] Index {index_number}: {text}")
            except LangDetectException:
                continue

    return english_index_list


def scan_result_dir():
    """Quét toàn bộ file .srt trong thư mục result/ và kiểm tra từng file."""
    if not RESULT_DIR.exists():
        print(f"Thư mục không tồn tại: {RESULT_DIR}")
        return

    srt_files = sorted(RESULT_DIR.glob("*.srt"))
    if not srt_files:
        print(f"Không tìm thấy file .srt nào trong: {RESULT_DIR}")
        return

    print(f"Tìm thấy {len(srt_files)} file .srt trong '{RESULT_DIR}'\n")

    for srt_file in srt_files:
        print(f"{'=' * 50}")
        print(f"File: {srt_file.name}")
        print(f"{'=' * 50}")

        english_indexes = find_english_lines(srt_file)

        print(f"--- Kết quả: {srt_file.name} ---")
        if english_indexes:
            print(f"Phát hiện {len(english_indexes)} dòng tiếng Anh.")
            print(f"Indexes: {', '.join(english_indexes)}")
        else:
            print("Tốt! Không phát hiện dòng tiếng Anh nào.")
        print()


scan_result_dir()
