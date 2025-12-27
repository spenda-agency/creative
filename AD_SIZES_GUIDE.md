# 広告サイズ別出力ガイド

Google広告とMeta広告の各サイズに対応した画像作成・出力の手順をまとめています。

## 📐 対応サイズ一覧

### Google広告（Google Ads）
- **300×250** - レクタングル（中サイズ）
- **336×280** - レクタングル（大サイズ）
- **300×300** - スクエア
- **1200×628** - 画像広告（推奨サイズ）

### Meta広告（Facebook/Instagram）
- **1200×1200** - スクエア（Instagram投稿、Facebook投稿）
- **1080×1920** - ストーリーズ（縦型）

## 🎨 制作手順

### 1. 案出しと組み合わせの決定

```bash
# HANOWAブランド向けの案を生成
python scripts/generate_hanowa_ideas.py --all --count 15

# 選んだ案で組み合わせを作成
python scripts/create_combination.py \
  --name pattern-new-1 \
  --material "選んだ素材の説明" \
  --background "選んだ背景の説明" \
  --copy "選んだキャッチコピー"
```

### 2. デザインツールでの制作

#### Figmaでの制作手順

1. **新規ファイルを作成**
   - ファイル名: `YYYY-MM-pattern-[A-Z]-[platform]-[size].fig`
   - 例: `2025-01-pattern-A-google-300x250.fig`

2. **アートボードのサイズ設定**
   - Google広告: 各サイズに合わせてアートボードを作成
   - Meta広告: 各サイズに合わせてアートボードを作成

3. **デザイン要素の配置**
   - 背景: `backgrounds/` フォルダの案を参考に配置
   - 素材: `assets/` フォルダの案を参考に配置
   - キャッチコピー: `copy/` フォルダの案を配置
   - ロゴ: HANOWAロゴを配置（右上推奨）

4. **各サイズへの最適化**
   - レイアウトを各サイズに合わせて調整
   - 文字サイズを読みやすく調整
   - 重要な要素が切れないように注意

#### Adobe Express / Canvaでの制作手順

1. **テンプレート選択**
   - 各プラットフォームの推奨サイズのテンプレートを選択

2. **デザイン要素の配置**
   - 背景、素材、キャッチコピーを配置

3. **エクスポート設定**
   - 形式: PNG（推奨）またはJPG
   - 解像度: 72dpi以上（推奨: 150dpi）
   - ファイルサイズ: 各プラットフォームの制限内

### 3. ファイル命名規則

#### Google広告
```
[パターン名]_google_[サイズ].png
例: pattern-A_google_300x250.png
例: pattern-A_google_1200x628.png
```

#### Meta広告
```
[パターン名]_meta_[サイズ].png
例: pattern-A_meta_1200x1200.png
例: pattern-A_meta_1080x1920.png
```

### 4. 出力と保存

#### ローカルでの保存先
```
creative/
├── outputs/
│   ├── google/
│   │   ├── 2025-01/
│   │   │   ├── pattern-A_google_300x250.png
│   │   │   ├── pattern-A_google_336x280.png
│   │   │   ├── pattern-A_google_300x300.png
│   │   │   └── pattern-A_google_1200x628.png
│   │   └── ...
│   └── meta/
│       ├── 2025-01/
│       │   ├── pattern-A_meta_1200x1200.png
│       │   └── pattern-A_meta_1080x1920.png
│       └── ...
```

## 📋 サイズ別チェックリスト

### Google広告 300×250（レクタングル中）
- [ ] キャッチコピーが読みやすいサイズか
- [ ] ロゴが適切なサイズで配置されているか
- [ ] CTAボタンがクリックしやすいサイズか
- [ ] ファイルサイズが150KB以下か（推奨）

### Google広告 336×280（レクタングル大）
- [ ] 300×250より広いスペースを活用できているか
- [ ] 素材が適切に配置されているか
- [ ] ファイルサイズが150KB以下か（推奨）

### Google広告 300×300（スクエア）
- [ ] 正方形のレイアウトに最適化されているか
- [ ] 中央配置が効果的か
- [ ] ファイルサイズが150KB以下か（推奨）

### Google広告 1200×628（画像広告）
- [ ] 横長のレイアウトに最適化されているか
- [ ] 高解像度で鮮明か
- [ ] ファイルサイズが5MB以下か（推奨）

### Meta広告 1200×1200（スクエア）
- [ ] Instagram投稿として最適化されているか
- [ ] 正方形のレイアウトに最適化されているか
- [ ] ファイルサイズが30MB以下か（推奨）

### Meta広告 1080×1920（ストーリーズ）
- [ ] 縦型レイアウトに最適化されているか
- [ ] 上部と下部の安全領域を考慮しているか
- [ ] ストーリーズのUIと重ならないか
- [ ] ファイルサイズが30MB以下か（推奨）

## 🔄 ワークフロー

### 月次制作フロー

1. **案出し**（1週目）
   ```bash
   python scripts/generate_hanowa_ideas.py --all --count 15
   ```

2. **選定と組み合わせ**（1-2週目）
   ```bash
   python scripts/create_combination.py --name pattern-A ...
   ```

3. **デザイン制作**（2-3週目）
   - Figma/Adobe Express/Canvaで各サイズを作成
   - 各サイズのチェックリストを確認

4. **出力と保存**（3週目）
   - 命名規則に従ってファイルを保存
   - `outputs/` フォルダに整理

5. **GitHubへのアップロード**（3-4週目）
   ```bash
   git add outputs/
   git commit -m "Add outputs for YYYY-MM pattern-A"
   git push
   ```

6. **広告プラットフォームへのアップロード**（4週目）
   - Google広告: Google Adsにアップロード
   - Meta広告: Facebook広告マネージャー/Instagramにアップロード

## 📊 A/Bテストの実施

### テストパターンの作成

各サイズごとに複数のパターンを作成：

```
pattern-A_google_300x250.png
pattern-B_google_300x250.png
pattern-C_google_300x250.png
```

### テスト結果の記録

GitHub Issueに以下の形式で記録：

```markdown
## A/Bテスト結果 - Google広告 300×250

- **パターンA**: CTR 2.5%, CVR 1.2%
- **パターンB**: CTR 3.1%, CVR 1.5%
- **パターンC**: CTR 2.8%, CVR 1.3%

**Winner**: Pattern B

## 学んだこと
- オレンジ系の背景が青系より2割高いCTR
- 短いコピー（10文字以下）が効果的
```

## 🛠️ 便利なツールとスクリプト

### 画像リサイズスクリプト（作成予定）

```bash
# メイン画像から各サイズを自動生成
python scripts/resize_for_platforms.py \
  --input pattern-A_main.png \
  --pattern pattern-A
```

### ファイル整理スクリプト（作成予定）

```bash
# outputs/フォルダを整理
python scripts/organize_outputs.py --month 2025-01
```

## 📚 参考資料

- [Google広告の画像要件](https://support.google.com/google-ads/answer/1722096)
- [Meta広告の画像要件](https://www.facebook.com/business/help/120325381656392)
- [Instagram広告の仕様](https://www.facebook.com/business/help/163525017206956)

## 💡 ベストプラクティス

1. **一貫性の維持**: ブランドカラー（水色系）を維持
2. **読みやすさ**: 各サイズでキャッチコピーが読みやすいか確認
3. **ファイルサイズ**: 各プラットフォームの推奨サイズを遵守
4. **テスト**: 必ず複数パターンを作成してA/Bテストを実施
5. **記録**: テスト結果を必ずGitHub Issueに記録

