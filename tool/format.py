
"""
format.py — 格式化 JSON 文件
用法: python format.py <file.json> [file2.json ...]
      支持 glob:python format.py data/feng/zhounan/*.json
      原地格式化，覆盖原文件
"""

import json
import sys
from pathlib import Path


def format_file(path: Path) -> None:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ {path}")


def main():
    if len(sys.argv) < 2:
        print("用法: python format.py <file.json> [file2.json ...]")
        sys.exit(1)

    paths = [Path(p) for p in sys.argv[1:]]
    errors = []

    for path in paths:
        try:
            format_file(path)
        except json.JSONDecodeError as e:
            print(f"✗ {path} — JSON 解析错误: {e}")
            errors.append(path)
        except FileNotFoundError:
            print(f"✗ {path} — 文件不存在")
            errors.append(path)

    if errors:
        print(f"\n{len(errors)} 个文件处理失败")
        sys.exit(1)
    else:
        print(f"\n共格式化 {len(paths)} 个文件")


if __name__ == "__main__":
    main()
