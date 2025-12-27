#!/usr/bin/env python3
"""
素材・背景・キャッチコピーの組み合わせを作成・管理するスクリプト

使い方:
    python scripts/create_combination.py --name pattern-A --material "素材1" --background "背景1" --copy "コピー1"
    python scripts/create_combination.py --list
    python scripts/create_combination.py --compare pattern-A pattern-B
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

# プロジェクトのルートディレクトリ
ROOT_DIR = Path(__file__).parent.parent
COMBINATIONS_DIR = ROOT_DIR / "combinations"


def load_combinations():
    """既存の組み合わせを読み込む"""
    COMBINATIONS_DIR.mkdir(exist_ok=True)
    combinations = {}
    
    for file_path in COMBINATIONS_DIR.glob("*.json"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            combinations[data["name"]] = data
    
    return combinations


def save_combination(name: str, material: str, background: str, copy: str, description: str = ""):
    """組み合わせを保存"""
    COMBINATIONS_DIR.mkdir(exist_ok=True)
    
    combination = {
        "name": name,
        "material": material,
        "background": background,
        "copy": copy,
        "description": description,
        "created_at": datetime.now().isoformat(),
        "status": "draft",  # draft, testing, done
        "test_results": {}
    }
    
    file_path = COMBINATIONS_DIR / f"{name}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(combination, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 組み合わせ '{name}' を {file_path} に保存しました")
    return file_path


def list_combinations():
    """全ての組み合わせを一覧表示"""
    combinations = load_combinations()
    
    if not combinations:
        print("📝 組み合わせがまだ作成されていません")
        return
    
    print("\n📋 組み合わせ一覧:\n")
    for name, data in combinations.items():
        print(f"【{name}】")
        print(f"  素材: {data['material']}")
        print(f"  背景: {data['background']}")
        print(f"  コピー: {data['copy']}")
        print(f"  ステータス: {data.get('status', 'draft')}")
        print(f"  作成日: {data.get('created_at', 'N/A')}")
        print()


def compare_combinations(name1: str, name2: str):
    """2つの組み合わせを比較"""
    combinations = load_combinations()
    
    if name1 not in combinations:
        print(f"❌ 組み合わせ '{name1}' が見つかりません")
        return
    
    if name2 not in combinations:
        print(f"❌ 組み合わせ '{name2}' が見つかりません")
        return
    
    c1 = combinations[name1]
    c2 = combinations[name2]
    
    print(f"\n🔍 組み合わせ比較: {name1} vs {name2}\n")
    print(f"{'項目':<15} {'pattern-A':<30} {'pattern-B':<30}")
    print("-" * 75)
    print(f"{'素材':<15} {c1['material']:<30} {c2['material']:<30}")
    print(f"{'背景':<15} {c1['background']:<30} {c2['background']:<30}")
    print(f"{'コピー':<15} {c1['copy']:<30} {c2['copy']:<30}")
    print(f"{'ステータス':<15} {c1.get('status', 'draft'):<30} {c2.get('status', 'draft'):<30}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="素材・背景・キャッチコピーの組み合わせを作成・管理"
    )
    parser.add_argument(
        "--name",
        help="組み合わせの名前（例: pattern-A）"
    )
    parser.add_argument(
        "--material",
        help="素材の説明"
    )
    parser.add_argument(
        "--background",
        help="背景の説明"
    )
    parser.add_argument(
        "--copy",
        help="キャッチコピー"
    )
    parser.add_argument(
        "--description",
        default="",
        help="組み合わせの説明・意図"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="全ての組み合わせを一覧表示"
    )
    parser.add_argument(
        "--compare",
        nargs=2,
        metavar=("PATTERN1", "PATTERN2"),
        help="2つの組み合わせを比較"
    )
    
    args = parser.parse_args()
    
    if args.list:
        list_combinations()
    elif args.compare:
        compare_combinations(args.compare[0], args.compare[1])
    elif args.name and args.material and args.background and args.copy:
        save_combination(
            args.name,
            args.material,
            args.background,
            args.copy,
            args.description
        )
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

