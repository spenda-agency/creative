#!/usr/bin/env python3
"""
広告用画像の素材・背景・キャッチコピーの案出し支援スクリプト

使い方:
    python scripts/generate_ideas.py --type material --count 10
    python scripts/generate_ideas.py --type background --count 10
    python scripts/generate_ideas.py --type copy --count 10
    python scripts/generate_ideas.py --all --count 5
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path

# プロジェクトのルートディレクトリ
ROOT_DIR = Path(__file__).parent.parent

# 素材の案出しテンプレート
MATERIAL_IDEAS = [
    "若い女性（20代、笑顔、カジュアルな服装）",
    "ビジネスパーソン（30代、スーツ、自信のある表情）",
    "家族（親子、幸せそうな雰囲気）",
    "商品単体（シンプルな背景、プロダクトフォーカス）",
    "商品使用シーン（実際の使用状況、リアルな場面）",
    "抽象的なアイコン（シンプル、モダンなデザイン）",
    "動物（ペット、かわいい、親しみやすい）",
    "自然（植物、花、緑）",
    "テクノロジー（デバイス、画面、未来感）",
    "料理・食品（美味しそう、食欲をそそる）",
    "スポーツ（アクティブ、エネルギッシュ）",
    "アート・クリエイティブ（色彩豊か、独創的）",
    "リラックスシーン（癒し、安らぎ）",
    "都市・建物（モダン、洗練された）",
    "季節感（春夏秋冬の要素）",
]

# 背景の案出しテンプレート
BACKGROUND_IDEAS = [
    "グラデーション（青から紫、上品な印象）",
    "グラデーション（オレンジからピンク、温かみ）",
    "グラデーション（緑から青、自然・清潔感）",
    "単色背景（白、ミニマル）",
    "単色背景（黒、高級感）",
    "単色背景（パステルブルー、優しい）",
    "単色背景（パステルピンク、女性向け）",
    "テクスチャ（紙、質感のある）",
    "テクスチャ（布、柔らかい）",
    "幾何学模様（シンプル、モダン）",
    "ぼかし背景（被写体を際立たせる）",
    "自然（空、雲、開放感）",
    "自然（森、木、落ち着き）",
    "都市（ビル、夜景、都会的）",
    "抽象的なパターン（流れるような線）",
    "抽象的なパターン（点、ドット）",
    "抽象的なパターン（波、動き）",
]

# キャッチコピーの案出しテンプレート（テーマ別）
COPY_TEMPLATES = {
    "時短": [
        "毎日がもっと自由に。",
        "時間を、あなたのために。",
        "忙しい毎日を、もっと快適に。",
        "時短で、もっと豊かな時間を。",
        "効率的に、もっと楽しく。",
    ],
    "品質": [
        "本物の品質を、あなたに。",
        "妥協しない、選ばれる理由。",
        "品質へのこだわりが、違いを生む。",
        "選ばれる理由は、ここにある。",
        "本物だから、自信を持って。",
    ],
    "価格": [
        "お手頃価格で、本格的な品質を。",
        "コスパ最強。選ばれる理由。",
        "リーズナブルに、もっと豊かに。",
        "価格以上の価値を。",
        "お得な今が、始まりの時。",
    ],
    "新しさ": [
        "新しい、あなたの始まり。",
        "次世代の、新しい選択。",
        "今までにない、新しい体験を。",
        "新しい発見が、ここにある。",
        "進化した、新しい価値を。",
    ],
    "便利さ": [
        "もっと簡単に、もっと便利に。",
        "あなたの毎日を、もっと快適に。",
        "手間を省いて、時間を生み出す。",
        "シンプルに、もっと効率的に。",
        "便利さが、選ばれる理由。",
    ],
    "感情": [
        "毎日が、もっと楽しくなる。",
        "幸せを、もっと身近に。",
        "あなたの笑顔が、私たちの喜び。",
        "心が温まる、特別な時間を。",
        "もっと豊かな、毎日を。",
    ],
}


def generate_material_ideas(count: int) -> list[str]:
    """素材の案を生成"""
    import random
    ideas = []
    base_ideas = MATERIAL_IDEAS.copy()
    
    for i in range(count):
        if base_ideas:
            idea = random.choice(base_ideas)
            base_ideas.remove(idea)
        else:
            # アイデアが尽きた場合は組み合わせを生成
            idea = f"組み合わせ素材案 {i+1}"
        
        ideas.append(f"{i+1}. {idea}")
    
    return ideas


def generate_background_ideas(count: int) -> list[str]:
    """背景の案を生成"""
    import random
    ideas = []
    base_ideas = BACKGROUND_IDEAS.copy()
    
    for i in range(count):
        if base_ideas:
            idea = random.choice(base_ideas)
            base_ideas.remove(idea)
        else:
            idea = f"組み合わせ背景案 {i+1}"
        
        ideas.append(f"{i+1}. {idea}")
    
    return ideas


def generate_copy_ideas(count: int, theme: str = None) -> list[str]:
    """キャッチコピーの案を生成"""
    import random
    
    if theme and theme in COPY_TEMPLATES:
        templates = COPY_TEMPLATES[theme]
    else:
        # 全テーマからランダムに選択
        templates = []
        for theme_templates in COPY_TEMPLATES.values():
            templates.extend(theme_templates)
    
    ideas = []
    used = set()
    
    for i in range(count):
        if templates:
            copy = random.choice(templates)
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
        filename = f"{date_str}-material-ideas-{timestamp}.txt"
    elif category == "background":
        dir_path = ROOT_DIR / "backgrounds"
        filename = f"{date_str}-background-ideas-{timestamp}.txt"
    elif category == "copy":
        dir_path = ROOT_DIR / "copy"
        filename = f"{date_str}-copy-ideas-{timestamp}.txt"
    else:
        return
    
    dir_path.mkdir(exist_ok=True)
    file_path = dir_path / filename
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"# {category.upper()} アイデア案 ({count}件)\n")
        f.write(f"生成日時: {now.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for idea in ideas:
            f.write(f"{idea}\n")
    
    print(f"✅ {category}の案を {file_path} に保存しました")
    return file_path


def generate_all(count: int, theme: str = None):
    """全てのカテゴリの案を生成"""
    print(f"\n📝 {count}件ずつの案を生成します...\n")
    
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


def main():
    parser = argparse.ArgumentParser(
        description="広告用画像の素材・背景・キャッチコピーの案出し支援"
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
        default=10,
        help="生成する案の数（デフォルト: 10）"
    )
    parser.add_argument(
        "--theme",
        choices=list(COPY_TEMPLATES.keys()),
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

