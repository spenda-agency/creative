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
└── .github/             # GitHubテンプレート
```

## 🚀 クイックスタート

### 1. 案出しスクリプトの実行

素材・背景・キャッチコピーの案を自動生成します。

```bash
# 全てのカテゴリから10件ずつ案を生成
python scripts/generate_ideas.py --all --count 10

# 特定のカテゴリのみ
python scripts/generate_ideas.py --type material --count 15
python scripts/generate_ideas.py --type background --count 15
python scripts/generate_ideas.py --type copy --count 15 --theme 時短
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

### 3. 組み合わせの確認

```bash
# 一覧表示
python scripts/create_combination.py --list

# 比較
python scripts/create_combination.py --compare pattern-A pattern-B
```

## 📝 運用フロー

### 月次サイクル

1. **月初め**: GitHub Issueで今月の制作タスクを作成
2. **案出し**: `generate_ideas.py`で大量の案を生成
3. **選定**: 案から良さそうなものを選定
4. **組み合わせ**: `create_combination.py`でテストパターンを作成
5. **制作**: 外部ツール（Figma等）で実際の画像を作成
6. **PR作成**: 変更をプルリクエストで提出し、Image Diffで比較
7. **テスト**: A/Bテストを実施
8. **記録**: 結果をIssueに記録し、次月に活かす

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

### PR作成の指示

```
「今回更新した assets/ と backgrounds/ 内の画像と、
copy/ 内の新コピーを元に、GitHubのプルリクエスト用の説明文を作成して。
前回のテスト結果（Issue #10）で『青色よりオレンジの方が反応が良かった』
という知見があったので、それを踏まえて今回の背景を選んだことも記載して。」
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

例：
- `2025-01-material-hero.png`
- `2025-01-background-gradient-blue.jpg`
- `2025-01-copy-short-time.txt`

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
2. `exports/` フォルダに配置
3. `scripts/sync_ads.py`（作成予定）で自動整理

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

## 📚 参考資料

- [GitHub Image Diffの使い方](https://docs.github.com/ja/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#adding-line-comments-to-a-pull-request)
- [Git LFSの設定](https://git-lfs.github.com/)

## 🤝 コントリビューション

このリポジトリは広告制作チーム全体で管理します。
新しい案や改善提案は、IssueまたはPull Requestでお願いします。

