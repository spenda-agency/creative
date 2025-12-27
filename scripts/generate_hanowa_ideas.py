#!/usr/bin/env python3
"""
HANOWAブランド向けの素材・背景・キャッチコピーの案出しスクリプト
既存のsample1画像の特徴を踏まえて、新しいバリエーションを生成
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
import random

ROOT_DIR = Path(__file__).parent.parent

# HANOWAブランドの特徴を踏まえた素材案
HANOWA_MATERIAL_IDEAS = [
    "スマートフォンを操作する歯科衛生士（笑顔、リラックスしたポーズ）",
    "複数の歯科衛生士が笑顔で並んでいる（多様性を表現）",
    "カレンダーと時計を操作する女性（スケジュール管理の自由さ）",
    "家族と過ごす時間を楽しむ女性（ワークライフバランス）",
    "お金のアイコンと笑顔の女性（経済的なメリット）",
    "両腕を上げて喜びを表現する女性（達成感、自由）",
    "カレンダーに黄色いハイライト（柔軟なスケジュール）",
    "スマートフォンアプリを見ている歯科衛生士（簡単な登録）",
    "リラックスしたポーズの女性（ストレスフリー）",
    "複数の歯科医院のシルエット（選択肢の多さ）",
    "時計とカレンダーが組み合わさったアイコン（時間の自由）",
    "笑顔の歯科衛生士と患者（やりがい）",
    "家事をしながらスマートフォンを見る女性（柔軟性）",
    "星やキラキラのエフェクトと笑顔の女性（ポジティブな印象）",
    "IDカードとスマートフォン（簡単な登録プロセス）",
]

# HANOWAブランドの特徴を踏まえた背景案
HANOWA_BACKGROUND_IDEAS = [
    "明るい水色の単色背景（シンプル、クリーン）",
    "淡い水色から濃いターコイズグリーンへのグラデーション（上から下）",
    "明るい水色とターコイズグリーンの2段階背景（水平分割）",
    "非常に淡い水色（ほぼ白）の背景に下部にターコイズグリーンの波状の帯",
    "水色のグラデーション背景（左から右）",
    "明るい水色の背景に白い幾何学模様（モダン）",
    "ターコイズグリーンを基調とした背景（濃淡のグラデーション）",
    "水色と白のストライプ（シンプル、清潔感）",
    "明るい水色の背景に小さな円形パターン（親しみやすさ）",
    "水色系のぼかし背景（被写体を際立たせる）",
]

# HANOWAブランドの特徴を踏まえたキャッチコピー案
HANOWA_COPY_IDEAS = {
    "柔軟性": [
        "歯科衛生士の 働き方を自由に あなたのペースで!",
        "歯科衛生士も 好きな時間に働ける スポット勤務",
        "歯科衛生士の 新しい働き方 1回からOK!",
        "歯科衛生士も 時給もスケジュールも 自分で決める",
        "歯科衛生士の 柔軟な働き方 あなたのライフスタイルに合わせて",
        "歯科衛生士の スポット採用 1回2時間でもOK!",
        "歯科衛生士も 働く時間も場所も 選べる",
    ],
    "時給": [
        "歯科衛生士も 時給は自分で決められる!",
        "歯科衛生士の 理想の時給を 実現しよう",
        "歯科衛生士も 時給交渉OK あなたの価値を",
        "歯科衛生士の 時給アップ 自分で決める働き方",
        "歯科衛生士も 高時給の仕事を 選べる",
    ],
    "実績・信頼性": [
        "歯科衛生士の スポット勤務なら マッチング実績20万件!",
        "歯科医療従事者のスポット勤務ならハノワ",
        "歯科衛生士の 選ばれる理由 実績と信頼",
        "歯科衛生士も 安心して働ける 実績のあるサービス",
    ],
    "簡単さ": [
        "歯科衛生士の 登録は簡単 すぐに始められる",
        "歯科衛生士も スマホで簡単 スポット勤務",
        "歯科衛生士の 新しい働き方 今すぐ始めよう",
    ],
    "メリット": [
        "歯科衛生士も ワークライフバランス 実現できる",
        "歯科衛生士の 理想の働き方 見つかる",
        "歯科衛生士も もっと自由に もっと楽しく",
    ],
}

def generate_material_ideas(count: int) -> list[str]:
    """素材の案を生成"""
    ideas = []
    base_ideas = HANOWA_MATERIAL_IDEAS.copy()
    random.shuffle(base_ideas)
    
    for i in range(count):
        if base_ideas:
            idea = base_ideas.pop()
        else:
            idea = f"新しい素材案 {i+1}（HANOWAブランドに合わせた）"
        
        ideas.append(f"{i+1}. {idea}")
    
    return ideas

def generate_background_ideas(count: int) -> list[str]:
    """背景の案を生成"""
    ideas = []
    base_ideas = HANOWA_BACKGROUND_IDEAS.copy()
    random.shuffle(base_ideas)
    
    for i in range(count):
        if base_ideas:
            idea = base_ideas.pop()
        else:
            idea = f"新しい背景案 {i+1}（水色系を基調とした）"
        
        ideas.append(f"{i+1}. {idea}")
    
    return ideas

def generate_copy_ideas(count: int, theme: str = None) -> list[str]:
    """キャッチコピーの案を生成"""
    ideas = []
    used = set()
    
    if theme and theme in HANOWA_COPY_IDEAS:
        templates = HANOWA_COPY_IDEAS[theme]
    else:
        # 全テーマからランダムに選択
        templates = []
        for theme_templates in HANOWA_COPY_IDEAS.values():
            templates.extend(theme_templates)
    
    random.shuffle(templates)
    
    for i in range(count):
        if templates:
            copy = templates.pop()
            if copy not in used:
                ideas.append(f"{i+1}. {copy}")
                used.add(copy)
            else:
                # バリエーションを生成
                ideas.append(f"{i+1}. {copy}（バリエーション）")
        else:
            ideas.append(f"{i+1}. 新しいキャッチコピー案 {i+1}")
    
    return ideas

def save_ideas(ideas: list[str], category: str, count: int):
    """案をファイルに保存"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m")
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    if category == "material":
        dir_path = ROOT_DIR / "assets"
        filename = f"{date_str}-hanowa-material-ideas-{timestamp}.txt"
    elif category == "background":
        dir_path = ROOT_DIR / "backgrounds"
        filename = f"{date_str}-hanowa-background-ideas-{timestamp}.txt"
    elif category == "copy":
        dir_path = ROOT_DIR / "copy"
        filename = f"{date_str}-hanowa-copy-ideas-{timestamp}.txt"
    else:
        return
    
    dir_path.mkdir(exist_ok=True)
    file_path = dir_path / filename
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# HANOWA {category.upper()} アイデア案 ({count}件)\n")
        f.write(f"生成日時: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"ブランド: HANOWA（歯科衛生士向けスポット採用サービス）\n")
        f.write(f"既存画像の特徴を踏まえた案出し\n\n")
        for idea in ideas:
            f.write(f"{idea}\n")
    
    print(f"✅ {category}の案を {file_path} に保存しました")
    return file_path

def generate_all(count: int, theme: str = None):
    """全てのカテゴリの案を生成"""
    print(f"\n📝 HANOWAブランド向けに {count}件ずつの案を生成します...\n")
    print("🎨 既存のsample1画像の特徴を踏まえた案出しです\n")
    
    # 素材
    print("🎨 素材の案を生成中...")
    material_ideas = generate_material_ideas(count)
    save_ideas(material_ideas, "material", count)
    
    # 背景
    print("🖼️  背景の案を生成中...")
    background_ideas = generate_background_ideas(count)
    save_ideas(background_ideas, "background", count)
    
    # キャッチコピー
    print("✍️  キャッチコピーの案を生成中...")
    copy_ideas = generate_copy_ideas(count, theme)
    save_ideas(copy_ideas, "copy", count)
    
    print("\n✨ 全ての案出しが完了しました！")
    print("\n💡 次のステップ:")
    print("   1. 生成された案から気に入ったものを選定")
    print("   2. python scripts/create_combination.py で組み合わせを作成")
    print("   3. 外部ツール（Figma等）で実際の画像を作成")

def main():
    parser = argparse.ArgumentParser(
        description="HANOWAブランド向けの素材・背景・キャッチコピーの案出し支援"
    )
    parser.add_argument(
        "--type",
        choices=["material", "background", "copy"],
        help="生成する案の種類"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="全てのカテゴリの案を生成"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=15,
        help="生成する案の数（デフォルト: 15）"
    )
    parser.add_argument(
        "--theme",
        choices=list(HANOWA_COPY_IDEAS.keys()),
        help="キャッチコピーのテーマ（copyタイプの場合）"
    )
    
    args = parser.parse_args()
    
    if args.all:
        generate_all(args.count, args.theme)
    elif args.type == "material":
        ideas = generate_material_ideas(args.count)
        save_ideas(ideas, "material", args.count)
    elif args.type == "background":
        ideas = generate_background_ideas(args.count)
        save_ideas(ideas, "background", args.count)
    elif args.type == "copy":
        ideas = generate_copy_ideas(args.count, args.theme)
        save_ideas(ideas, "copy", args.count)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

