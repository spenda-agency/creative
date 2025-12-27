#!/usr/bin/env python3
"""
sample1フォルダ内の完成画像から素材・背景・キャッチコピーの情報を抽出して
管理システムに登録するスクリプト
"""

import json
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path(__file__).parent.parent
SAMPLE1_DIR = ROOT_DIR / "sample1"
COMBINATIONS_DIR = ROOT_DIR / "combinations"

# 添付された画像から抽出した情報（代表的な2枚の分析結果）
REPRESENTATIVE_IMAGES = {
    "sample1_pattern_1": {
        "filename_pattern": "1A",  # 1A_1080×1080.png など
        "description": "HANOWA - スポット採用訴求",
        "material": {
            "description": "スマートフォンを操作する男性と笑顔の女性のイラスト",
            "style": "親しみやすいモダンなイラストレーション、線画とフラットな塗り",
            "elements": [
                "水色のスクラブを着た男性（スマートフォン操作、笑顔）",
                "水色の髪と服の女性（笑顔、片手を上げて指差し）",
                "カレンダーアイコン（日付が黄色くハイライト）",
                "黄色い星のキラキラアイコン"
            ],
            "color_scheme": "水色、黄色、緑"
        },
        "background": {
            "description": "明るい水色を基調とした2段階のグラデーション",
            "style": "シンプルでクリーン",
            "colors": {
                "top": "明るい水色（薄いミントグリーン）",
                "bottom": "少し濃い水色（ティールグリーン）",
                "main": "水色系"
            },
            "layout": "水平な境界線で上下に分割"
        },
        "copy": {
            "main": "歯科衛生士の スポット採用 1回2時間でもOK!",
            "sub": "マッチング実績20万件!",
            "cta": "詳しくはこちら >",
            "theme": "柔軟な働き方（スポット採用、短時間勤務）",
            "target": "歯科衛生士"
        },
        "logo": "HANOWA（右上）"
    },
    "sample1_pattern_2": {
        "filename_pattern": "2509",  # 2509_1080_1080_A.png など
        "description": "HANOWA - 時給決定権訴求",
        "material": {
            "description": "喜びを表現する女性のイラストとお金のアイコン",
            "style": "親しみやすいモダンなイラストレーション",
            "elements": [
                "明るいピンクのスクラブを着た女性（金髪ポニーテール、笑顔、両腕を上げて開脚ポーズ）",
                "お金のアイコン（紙幣2枚とコインの山、¥マーク）",
                "黄色い四角い星のキラキラエフェクト",
                "IDカード（女性の胸元）"
            ],
            "color_scheme": "ピンク、黄色、ターコイズグリーン"
        },
        "background": {
            "description": "淡い水色の背景と下部のターコイズグリーンの波状の帯",
            "style": "クリーンでモダン",
            "colors": {
                "main": "非常に淡い水色（ほぼ白に近いライトブルー）",
                "band": "濃いターコイズグリーン（ティールグリーン）の波状の帯",
                "layout": "下部1/4を波状の帯が横切る"
            }
        },
        "copy": {
            "main": "歯科衛生士も 時給は自分で決められる!",
            "sub": "歯科医療従事者のスポット勤務ならハノワ",
            "theme": "時給決定権、経済的なメリット",
            "target": "歯科衛生士"
        },
        "logo": "HANOWA（右上、ターコイズグリーン）"
    }
}

def extract_common_elements():
    """既存画像から共通要素を抽出"""
    common = {
        "brand": "HANOWA",
        "target_audience": "歯科衛生士",
        "service_type": "スポット採用サービス",
        "common_colors": {
            "primary": "水色系（明るい水色、ターコイズグリーン）",
            "accent": "黄色",
            "text": "黒、白"
        },
        "common_styles": {
            "illustration": "親しみやすいモダンなイラストレーション、線画とフラットな塗り",
            "background": "シンプルでクリーン、水色系を基調"
        }
    }
    return common

def generate_variations(base_pattern: dict, variation_type: str = "copy"):
    """既存パターンからバリエーションを生成"""
    variations = []
    
    if variation_type == "copy":
        # キャッチコピーのバリエーション
        copy_variations = [
            "歯科衛生士の 働き方を自由に あなたのペースで!",
            "歯科衛生士も 好きな時間に働ける スポット勤務",
            "歯科衛生士の 新しい働き方 1回からOK!",
            "歯科衛生士も 時給もスケジュールも 自分で決める",
            "歯科衛生士の 柔軟な働き方 あなたのライフスタイルに合わせて",
        ]
        
        for copy_text in copy_variations:
            variation = base_pattern.copy()
            variation["copy"]["main"] = copy_text
            variations.append(variation)
    
    elif variation_type == "material":
        # 素材のバリエーション
        material_variations = [
            {
                "description": "複数の歯科衛生士が笑顔で並んでいるイラスト",
                "elements": ["3-4人の歯科衛生士（多様性を表現）", "笑顔", "スクラブ姿"]
            },
            {
                "description": "カレンダーと時計を操作する女性のイラスト",
                "elements": ["女性（スマートフォン操作）", "カレンダー", "時計アイコン"]
            },
            {
                "description": "家族と過ごす時間を楽しむ女性のイラスト",
                "elements": ["女性（リラックスしたポーズ）", "家族のシルエット", "ハートアイコン"]
            }
        ]
        
        for mat_var in material_variations:
            variation = base_pattern.copy()
            variation["material"].update(mat_var)
            variations.append(variation)
    
    elif variation_type == "layout":
        # レイアウト・配置のバリエーション
        layout_variations = [
            {
                "description": "キャッチコピーを中央配置、素材を左右に配置",
                "copy_position": "中央",
                "material_position": "左右"
            },
            {
                "description": "キャッチコピーを左側、素材を右側に大きく配置",
                "copy_position": "左",
                "material_position": "右（大きく）"
            }
        ]
        
        for layout_var in layout_variations:
            variation = base_pattern.copy()
            variation["layout"] = layout_var
            variations.append(variation)
    
    return variations

def save_to_combinations(pattern_data: dict, pattern_name: str):
    """パターンをcombinationsフォルダに保存"""
    COMBINATIONS_DIR.mkdir(exist_ok=True)
    
    combination = {
        "name": pattern_name,
        "material": pattern_data["material"]["description"],
        "background": pattern_data["background"]["description"],
        "copy": pattern_data["copy"]["main"],
        "description": pattern_data.get("description", ""),
        "created_at": datetime.now().isoformat(),
        "status": "draft",
        "source": "sample1",
        "details": pattern_data
    }
    
    file_path = COMBINATIONS_DIR / f"{pattern_name}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(combination, f, ensure_ascii=False, indent=2)
    
    print(f"✅ パターン '{pattern_name}' を {file_path} に保存しました")
    return file_path

def main():
    print("📊 sample1フォルダ内の完成画像から情報を抽出します...\n")
    
    # 共通要素を抽出
    common = extract_common_elements()
    print("🎨 共通要素:")
    print(f"  - ブランド: {common['brand']}")
    print(f"  - ターゲット: {common['target_audience']}")
    print(f"  - 主な色: {common['common_colors']['primary']}")
    print()
    
    # 代表的な2パターンを登録
    for key, pattern in REPRESENTATIVE_IMAGES.items():
        pattern_name = key.replace("sample1_", "")
        save_to_combinations(pattern, pattern_name)
    
    # バリエーションを生成
    print("\n🔄 バリエーションを生成します...\n")
    
    base_pattern = REPRESENTATIVE_IMAGES["sample1_pattern_1"]
    
    # キャッチコピーのバリエーション
    copy_variations = generate_variations(base_pattern, "copy")
    for i, var in enumerate(copy_variations[:3], 1):  # 最初の3つを保存
        pattern_name = f"variation-copy-{i}"
        save_to_combinations(var, pattern_name)
    
    # 素材のバリエーション
    material_variations = generate_variations(base_pattern, "material")
    for i, var in enumerate(material_variations[:2], 1):  # 最初の2つを保存
        pattern_name = f"variation-material-{i}"
        save_to_combinations(var, pattern_name)
    
    print("\n✨ 抽出とバリエーション生成が完了しました！")
    print("\n💡 次回のバナー作成のための案出しを開始できます:")
    print("   python scripts/generate_ideas.py --all --count 15")

if __name__ == "__main__":
    main()

