#!/usr/bin/env python3
"""
sample1フォルダ内の画像を分析して、素材・背景・キャッチコピーの情報を抽出するスクリプト
"""

import os
from pathlib import Path
from PIL import Image
import json

ROOT_DIR = Path(__file__).parent.parent
SAMPLE1_DIR = ROOT_DIR / "sample1"

def analyze_image(image_path: Path):
    """画像ファイルを分析"""
    try:
        img = Image.open(image_path)
        width, height = img.size
        
        return {
            "filename": image_path.name,
            "size": f"{width}×{height}",
            "width": width,
            "height": height,
            "format": img.format,
            "mode": img.mode,
            "file_size_kb": round(image_path.stat().st_size / 1024, 2)
        }
    except Exception as e:
        return {
            "filename": image_path.name,
            "error": str(e)
        }

def extract_pattern_info(filename: str):
    """ファイル名からパターン情報を抽出"""
    # 1A, 1B, 2509_A, 2510_a などのパターンを抽出
    parts = filename.replace('.png', '').split('_')
    
    pattern_info = {
        "base_name": None,
        "pattern": None,  # A, B, a, b
        "size": None
    }
    
    # サイズ情報を抽出（最後の部分）
    if len(parts) > 0:
        last_part = parts[-1]
        if '×' in last_part or 'x' in last_part.lower():
            pattern_info["size"] = last_part
            parts = parts[:-1]
    
    # パターン情報を抽出
    if len(parts) > 0:
        last_part = parts[-1]
        if last_part in ['A', 'B', 'a', 'b']:
            pattern_info["pattern"] = last_part
            parts = parts[:-1]
        
        if parts:
            pattern_info["base_name"] = '_'.join(parts)
    
    return pattern_info

def main():
    if not SAMPLE1_DIR.exists():
        print(f"❌ {SAMPLE1_DIR} が見つかりません")
        return
    
    image_files = list(SAMPLE1_DIR.glob("*.png"))
    
    if not image_files:
        print(f"❌ {SAMPLE1_DIR} にPNG画像が見つかりません")
        return
    
    print(f"\n📊 {SAMPLE1_DIR} 内の画像分析結果\n")
    print(f"総画像数: {len(image_files)}個\n")
    
    # パターンごとにグループ化
    patterns = {}
    for img_path in sorted(image_files):
        info = analyze_image(img_path)
        pattern_info = extract_pattern_info(img_path.name)
        
        base = pattern_info["base_name"] or "unknown"
        if base not in patterns:
            patterns[base] = []
        
        patterns[base].append({
            **info,
            **pattern_info
        })
    
    # 結果を表示
    for base_name, images in patterns.items():
        print(f"【{base_name}】")
        for img in images:
            pattern = img.get("pattern", "-")
            size = img.get("size", "-")
            print(f"  - パターン{pattern}: {img['filename']} ({size})")
        print()
    
    # JSON形式でも保存
    output_file = ROOT_DIR / "sample1_analysis.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({
            "total_images": len(image_files),
            "patterns": patterns
        }, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 分析結果を {output_file} に保存しました")
    print("\n💡 画像の内容（素材・背景・キャッチコピー）を確認するには、")
    print("   画像ファイルを開いて視覚的に確認する必要があります。")

if __name__ == "__main__":
    main()

