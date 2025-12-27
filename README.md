# 広告用画像作成管理システム

広告用の静止画を作成する際の素材・背景・キャッチコピーを管理し、A/Bテストを効率的に進めるためのリポジトリです。

## 📁 ディレクトリ構造

```
creative/
├── assets/              # 素材（人物、商品画像など）
├── backgrounds/         # 背景素材
├── copy/                # キャッチコピー（テキストファイル）
├── combinations/        # A/Bテストの組み合わせ定義ファイル（JSON）
├── scripts/             # 自動化スクリプト
├── archive/             # 過去の素材（アーカイブ）
├── outputs/            # 完成した広告画像（プラットフォーム別）
│   ├── google/         # Google広告用
│   └── meta/           # Meta広告用
├── sample1/            # サンプル画像
└── .github/            # GitHubテンプレート
```

## 🚀 クイックスタート

### 1. 案出しスクリプトの実行

素材・背景・キャッチコピーの案を自動生成します。

```bash
# HANOWAブランド向けの案を生成（推奨）
python scripts/generate_hanowa_ideas.py --all --count 15

# 汎用的な案を生成
python scripts/generate_ideas.py --all --count 10
```

### 2. 組み合わせの作成

生成した案から組み合わせを作成します。

```bash
python scripts/create_combination.py \
  --name pattern-A \
  --material "若い女性（20代、笑顔）" \
  --background "グラデーション（青から紫）" \
  --copy "毎日がもっと自由に。" \
  --description "時短訴求、女性ターゲット向け"
```

### 3. 広告サイズ別の出力

各プラットフォームのサイズに対応した画像を作成します。

詳細は [AD_SIZES_GUIDE.md](AD_SIZES_GUIDE.md) を参照してください。

**対応サイズ:**
- **Google広告**: 300×250, 336×280, 300×300, 1200×628
- **Meta広告**: 1200×1200, 1080×1920

## 📝 運用フロー

### 月次サイクル

1. **月初め**: GitHub Issueで今月の制作タスクを作成
2. **案出し**: `generate_hanowa_ideas.py`で大量の案を生成
3. **選定**: 案から良さそうなものを選定
4. **組み合わせ**: `create_combination.py`でテストパターンを作成
5. **制作**: 外部ツール（Figma等）で実際の画像を作成
6. **出力**: 各プラットフォームのサイズに合わせて出力
7. **PR作成**: 変更をプルリクエストで提出し、Image Diffで比較
8. **テスト**: A/Bテストを実施
9. **記録**: 結果をIssueに記録し、次月に活かす

## 🛠️ Cursorでの使い方

### 案出しの指示例

```
「copy/ フォルダにある過去のコピーを参考にして、
20代女性向けの『時短』をテーマにした新しいキャッチコピーを10案出して。
採用したものは copy/2025-01-copy.txt として保存して。」
```

### 組み合わせの分析

```
「combinations/ 内の全てのパターンを分析して、
どの組み合わせが最も効果的そうか、理由と共に提案して。」
```

### 広告サイズ対応の指示

```
「pattern-AのデザインをGoogle広告の全サイズ
（300×250, 336×280, 300×300, 1200×628）に対応させて。
各サイズのレイアウト調整も含めて。」
```

## 📊 GitHub Projectsでの管理

以下の列でカンバンボードを管理します：

- **Backlog**: 来月以降のタスク
- **Todo**: 今月分のタスク
- **In Progress**: 制作中
- **Testing**: A/Bテスト中
- **Done**: 完了

## 🎨 命名規則

- **素材・背景**: `YYYY-MM-[要素名]-[識別子].png`
- **キャッチコピー**: `YYYY-MM-copy-[識別子].txt`
- **組み合わせ**: `pattern-[A-Z].json`
- **出力画像**: `[パターン名]_[platform]_[サイズ].png`

例：
- `2025-01-material-hero.png`
- `2025-01-background-gradient-blue.jpg`
- `2025-01-copy-short-time.txt`
- `pattern-A_google_300x250.png`
- `pattern-A_meta_1200x1200.png`

## 📦 Git LFSの設定（推奨）

大きな画像ファイルを扱う場合は、Git LFSを設定してください。

```bash
git lfs install
git lfs track "*.png"
git lfs track "*.jpg"
git lfs track "*.jpeg"
git add .gitattributes
```

## 🔄 外部ツールとの連携

### Figmaからの書き出し

1. Figmaで画像を書き出し
2. `outputs/` フォルダにプラットフォーム別・サイズ別に配置
3. 命名規則に従ってファイル名を変更

### A/Bテスト結果の記録

テスト結果はGitHub Issueに以下の形式で記録：

```markdown
## テスト結果

- **パターンA**: CTR 2.5%, CVR 1.2%
- **パターンB**: CTR 3.1%, CVR 1.5%

**Winner**: Pattern B

## 学んだこと

- オレンジ系の背景が青系より2割高いCTR
- 短いコピー（10文字以下）が効果的
```

## 📚 ドキュメント

- [AD_SIZES_GUIDE.md](AD_SIZES_GUIDE.md) - 広告サイズ別出力ガイド
- [USAGE.md](USAGE.md) - 詳細な使い方ガイド

## 🤝 コントリビューション

このリポジトリは広告制作チーム全体で管理します。
新しい案や改善提案は、IssueまたはPull Requestでお願いします。

