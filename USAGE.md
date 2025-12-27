# 使い方ガイド

## 🎯 基本的な使い方

### 1. 案出しの実行

#### 全てのカテゴリから案を生成

```bash
# 各カテゴリから10件ずつ案を生成
python scripts/generate_ideas.py --all --count 10

# 各カテゴリから20件ずつ案を生成（より多くの選択肢）
python scripts/generate_ideas.py --all --count 20
```

#### 特定のカテゴリのみ

```bash
# 素材の案を15件生成
python scripts/generate_ideas.py --type material --count 15

# 背景の案を15件生成
python scripts/generate_ideas.py --type background --count 15

# キャッチコピーの案を15件生成（テーマ指定なし）
python scripts/generate_ideas.py --type copy --count 15

# キャッチコピーの案を15件生成（「時短」テーマ）
python scripts/generate_ideas.py --type copy --count 15 --theme 時短
```

#### 利用可能なキャッチコピーのテーマ

- `時短`: 時間短縮・効率化を訴求
- `品質`: 品質の高さを訴求
- `価格`: 価格の魅力を訴求
- `新しさ`: 新商品・新機能を訴求
- `便利さ`: 利便性を訴求
- `感情`: 感情に訴えかける

### 2. 生成された案の確認

生成されたファイルは以下の場所に保存されます：

- **素材**: `assets/YYYY-MM-material-ideas-[タイムスタンプ].txt`
- **背景**: `backgrounds/YYYY-MM-background-ideas-[タイムスタンプ].txt`
- **キャッチコピー**: `copy/YYYY-MM-copy-ideas-[タイムスタンプ].txt`

ファイルを開いて、気に入った案を選びます。

### 3. 組み合わせの作成

選んだ案を組み合わせて、A/Bテスト用のパターンを作成します。

```bash
python scripts/create_combination.py \
  --name pattern-A \
  --material "若い女性（20代、笑顔、カジュアルな服装）" \
  --background "グラデーション（青から紫、上品な印象）" \
  --copy "毎日がもっと自由に。" \
  --description "時短訴求、20代女性ターゲット向け"
```

複数のパターンを作成する場合：

```bash
# パターンA
python scripts/create_combination.py \
  --name pattern-A \
  --material "若い女性（20代、笑顔）" \
  --background "グラデーション（青から紫）" \
  --copy "毎日がもっと自由に。"

# パターンB
python scripts/create_combination.py \
  --name pattern-B \
  --material "若い女性（20代、笑顔）" \
  --background "グラデーション（オレンジからピンク）" \
  --copy "毎日がもっと自由に。"
```

### 4. 組み合わせの確認・比較

```bash
# 全ての組み合わせを一覧表示
python scripts/create_combination.py --list

# 2つのパターンを比較
python scripts/create_combination.py --compare pattern-A pattern-B
```

## 💡 Cursorでの活用例

### 案出しの指示

Cursorのチャット（Cmd+L）で以下のように指示します：

```
「copy/ フォルダにある過去のコピーを参考にして、
20代女性向けの『時短』をテーマにした新しいキャッチコピーを20案出して。
採用したものは copy/2025-01-copy.txt として保存して。」
```

### 組み合わせの分析

```
「combinations/ 内の全てのパターンを分析して、
どの組み合わせが最も効果的そうか、理由と共に提案して。
前回のテスト結果（Issue #10）も参考にして。」
```

### 大量の案出し

```
「素材・背景・キャッチコピーそれぞれ30件ずつ案を出して。
テーマは『春の新生活』で、ターゲットは20代女性です。」
```

その後、スクリプトを実行：

```bash
python scripts/generate_ideas.py --all --count 30
```

## 📊 月次ワークフロー例

### 1週目：案出し

```bash
# 大量の案を生成
python scripts/generate_ideas.py --all --count 30

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

### 3週目：制作

- Figmaなどのツールで実際の画像を作成
- 作成した画像を `assets/` と `backgrounds/` に保存

### 4週目：PR作成とテスト

- 変更をコミットしてプルリクエストを作成
- GitHubのImage Diff機能で比較
- A/Bテストを開始

## 🔧 カスタマイズ

### 新しい素材案を追加

`scripts/generate_ideas.py` の `MATERIAL_IDEAS` リストに追加：

```python
MATERIAL_IDEAS = [
    # 既存の案...
    "新しい素材案（説明）",
]
```

### 新しい背景案を追加

`scripts/generate_ideas.py` の `BACKGROUND_IDEAS` リストに追加：

```python
BACKGROUND_IDEAS = [
    # 既存の案...
    "新しい背景案（説明）",
]
```

### 新しいキャッチコピーテーマを追加

`scripts/generate_ideas.py` の `COPY_TEMPLATES` 辞書に追加：

```python
COPY_TEMPLATES = {
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
python scripts/generate_ideas.py --all --count 50
```

### Q: 過去の案を参考にしたい

`assets/`, `backgrounds/`, `copy/` フォルダ内の過去のファイルをCursorに読み込ませて、それを参考に新しい案を生成させることができます。

```
「@assets/2024-12-material-ideas-*.txt を参考にして、
同じようなトーンで新しい素材案を10件出して。」
```

### Q: 組み合わせのステータスを更新したい

`combinations/` フォルダ内のJSONファイルを直接編集するか、Cursorに指示します：

```
「combinations/pattern-A.json のステータスを 'testing' に更新して。
テスト結果も追加して：CTR 3.1%, CVR 1.5%」
```

## 🚀 次のステップ

- [README.md](README.md) で全体の運用フローを確認
- GitHub Issueテンプレートを使って月次タスクを管理
- プルリクエストテンプレートでImage Diffを活用

