from pathlib import Path
from analyzer import analyze_code


def main():
    file_path = Path("samples/hospital_management.py")

    source_code = file_path.read_text(encoding="utf-8")

    print("OO METRICS TESTING TOOL")
    print("-----------------------")

    analyze_code(source_code)


if __name__ == "__main__":
    main()