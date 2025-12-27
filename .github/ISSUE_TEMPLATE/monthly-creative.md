---
name: 月次制作タスク
about: 毎月の新素材・背景・キャッチコピー作成タスク
title: '[YYYY-MM] 新素材作成'
labels: 'monthly-task'
assignees: ''
---

## 📅 今月のテーマ

- **月**: YYYY-MM
- **テーマ**: [例：春の商戦に向けた時短訴求]
- **ターゲット**: [例：20代女性]

## 📋 要件

### 素材
- [ ] 案出し完了（`python scripts/generate_ideas.py --type material --count 15`）
- [ ] 選定完了
- [ ] 制作完了
- [ ] レビュー完了

**選定した素材**: 
- [素材の説明を記載]

### 背景
- [ ] 案出し完了（`python scripts/generate_ideas.py --type background --count 15`）
- [ ] 選定完了
- [ ] 制作完了
- [ ] レビュー完了

**選定した背景**: 
- [背景の説明を記載]

### キャッチコピー
- [ ] 案出し完了（`python scripts/generate_ideas.py --type copy --count 15 --theme [テーマ]`）
- [ ] 選定完了
- [ ] レビュー完了

**選定したコピー**: 
- [キャッチコピーを記載]

## 🧪 テストパターン

- [ ] 組み合わせ定義完了（`python scripts/create_combination.py`）
- [ ] 画像制作完了
- [ ] PR作成完了
- [ ] A/Bテスト開始

**パターンA**:
- 素材: 
- 背景: 
- コピー: 

**パターンB**:
- 素材: 
- 背景: 
- コピー: 

## 📊 前月のテスト結果からの学び

- [前月のIssue #XX の結果を参照]
- [改善点を記載]

## ✅ 完了条件

- [ ] 全ての素材・背景・コピーが作成され、リポジトリに保存されている
- [ ] 組み合わせが定義され、`combinations/` に保存されている
- [ ] PRが作成され、レビューが完了している
- [ ] A/Bテストが開始されている

