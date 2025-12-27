# 使い方ガイド

## 🎯 基本的な使い方

### 1. 案出しの実行

#### HANOWAブランド向けの案を生成（推奨）

```bash
# 各カテゴリから15件ずつ案を生成
python scripts/generate_hanowa_ideas.py --all --count 15

# 各カテゴリから20件ずつ案を生成（より多くの選択肢）
python scripts/generate_hanowa_ideas.py --all --count 20
```

#### 特定のカテゴリのみ

```bash
# 素材の案を15件生成
python scripts/generate_hanowa_ideas.py --type material --count 15

# 背景の案を15件生成
python scripts/generate_hanowa_ideas.py --type background --count 15

# キャッチコピーの案を15件生成（テーマ指定なし）
python scripts/generate_hanowa_ideas.py --type copy --count 15

# キャッチコピーの案を15件生成（「柔軟性」テーマ）
python scripts/generate_hanowa_ideas.py --type copy --count 15 --theme 柔軟性
```

#### 利用可能なキャッチコピーのテーマ

- `柔軟性`: 柔軟な働き方を訴求
- `時給`: 時給決定権を訴求
- `実績・信頼性`: 実績と信頼性を訴求
- `簡単さ`: 簡単さを訴求
- `メリット`: メリットを訴求

### 2. 生成された案の確認

生成されたファイルは以下の場所に保存されます：

- **素材**: `assets/YYYY-MM-hanowa-material-ideas-[タイムスタンプ].txt`
- **背景**: `backgrounds/YYYY-MM-hanowa-background-ideas-[タイムスタンプ].txt`
- **キャッチコピー**: `copy/YYYY-MM-hanowa-copy-ideas-[タイムスタンプ].txt`

ファイルを開いて、気に入った案を選びます。

### 3. 組み合わせの作成

選んだ案を組み合わせて、A/Bテスト用のパターンを作成します。

```bash
python scripts/create_combination.py \
  --name pattern-A \
  --material "スマートフォンを操作する歯科衛生士（笑顔、リラックスしたポーズ）" \
  --background "明るい水色の単色背景（シンプル、クリーン）" \
  --copy "歯科衛生士の 働き方を自由に あなたのペースで!" \
  --description "柔軟な働き方訴求、20代女性ターゲット向け"
```

複数のパターンを作成する場合：

```bash
# パターンA
python scripts/create_combination.py \
  --name pattern-A \
  --material "スマートフォンを操作する歯科衛生士" \
  --background "明るい水色の単色背景" \
  --copy "歯科衛生士の 働き方を自由に"

# パターンB
python scripts/create_combination.py \
  --name pattern-B \
  --material "複数の歯科衛生士が笑顔で並んでいる" \
  --background "淡い水色から濃いターコイズグリーンへのグラデーション" \
  --copy "歯科衛生士の 働き方を自由に"
```

### 4. 組み合わせの確認・比較

```bash
# 全ての組み合わせを一覧表示
python scripts/create_combination.py --list

# 2つのパターンを比較
python scripts/create_combination.py --compare pattern-A pattern-B
```

### 5. 広告サイズ別の出力

詳細は [AD_SIZES_GUIDE.md](AD_SIZES_GUIDE.md) を参照してください。

**対応サイズ:**
- **Google広告**: 300×250, 336×280, 300×300, 1200×628
- **Meta広告**: 1200×1200, 1080×1920

## 💡 Cursorでの活用例

### 案出しの指示

Cursorのチャット（Cmd+L）で以下のように指示します：

```
「copy/ フォルダにある過去のコピーを参考にして、
20代女性向けの『柔軟性』をテーマにした新しいキャッチコピーを20案出して。
採用したものは copy/2025-01-copy.txt として保存して。」
```

### 組み合わせの分析

```
「combinations/ 内の全てのパターンを分析して、
どの組み合わせが最も効果的そうか、理由と共に提案して。
前回のテスト結果（Issue #10）も参考にして。」
```

### 広告サイズ対応の指示

```
「pattern-AのデザインをGoogle広告の全サイズ
（300×250, 336×280, 300×300, 1200×628）に対応させて。
各サイズのレイアウト調整も含めて。
Figmaで作成して、outputs/google/2025-01/ に保存して。」
```

### 大量の案出し

```
「素材・背景・キャッチコピーそれぞれ30件ずつ案を出して。
テーマは『柔軟な働き方』で、ターゲットは20代女性です。」
```

その後、スクリプトを実行：

```bash
python scripts/generate_hanowa_ideas.py --all --count 30
```

## 📊 月次ワークフロー例

### 1週目：案出し

```bash
# 大量の案を生成
python scripts/generate_hanowa_ideas.py --all --count 30

# 生成されたファイルを確認
# assets/, backgrounds/, copy/ フォルダ内の最新ファイルを開く
```

### 2週目：選定と組み合わせ

```bash
# 選んだ案で組み合わせを作成
python scripts/create_combination.py --name pattern-A ...
python scripts/create_combination.py --name pattern-B ...

# 組み合わせを確認
python scripts/create_combination.py --list
```

### 3週目：制作と出力

- Figmaなどのツールで実際の画像を作成
- 各プラットフォームのサイズに合わせて出力
- `outputs/` フォルダに整理

### 4週目：PR作成とテスト

- 変更をコミットしてプルリクエストを作成
- GitHubのImage Diff機能で比較
- A/Bテストを開始

## 🔧 カスタマイズ

### 新しい素材案を追加

`scripts/generate_hanowa_ideas.py` の `HANOWA_MATERIAL_IDEAS` リストに追加：

```python
HANOWA_MATERIAL_IDEAS = [
    # 既存の案...
    "新しい素材案（説明）",
]
```

### 新しい背景案を追加

`scripts/generate_hanowa_ideas.py` の `HANOWA_BACKGROUND_IDEAS` リストに追加：

```python
HANOWA_BACKGROUND_IDEAS = [
    # 既存の案...
    "新しい背景案（説明）",
]
```

### 新しいキャッチコピーテーマを追加

`scripts/generate_hanowa_ideas.py` の `HANOWA_COPY_IDEAS` 辞書に追加：

```python
HANOWA_COPY_IDEAS = {
    # 既存のテーマ...
    "新しいテーマ": [
        "コピー案1",
        "コピー案2",
    ],
}
```

## ❓ よくある質問

### Q: もっと多くの案を出したい

`--count` の値を大きくしてください。ただし、テンプレートの数以上の案を生成すると、重複や組み合わせ案が生成されます。

```bash
python scripts/generate_hanowa_ideas.py --all --count 50
```

### Q: 過去の案を参考にしたい

`assets/`, `backgrounds/`, `copy/` フォルダ内の過去のファイルをCursorに読み込ませて、それを参考に新しい案を生成させることができます。

```
「@assets/2024-12-hanowa-material-ideas-*.txt を参考にして、
同じようなトーンで新しい素材案を10件出して。」
```

### Q: 組み合わせのステータスを更新したい

`combinations/` フォルダ内のJSONファイルを直接編集するか、Cursorに指示します：

```
「combinations/pattern-A.json のステータスを 'testing' に更新して。
テスト結果も追加して：CTR 3.1%, CVR 1.5%」
```

### Q: 広告サイズごとに異なるレイアウトが必要？

はい、各サイズに最適化されたレイアウトを作成することを推奨します。
詳細は [AD_SIZES_GUIDE.md](AD_SIZES_GUIDE.md) を参照してください。

## 🚀 次のステップ

- [README.md](README.md) で全体の運用フローを確認
- [AD_SIZES_GUIDE.md](AD_SIZES_GUIDE.md) で広告サイズ別の出力手順を確認
- GitHub Issueテンプレートを使って月次タスクを管理
- プルリクエストテンプレートでImage Diffを活用

