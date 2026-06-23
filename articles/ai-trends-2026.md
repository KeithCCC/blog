# 2026年時点のAIトレンドまとめ

ここ2年で流れがかなり変わりました。

## 2023〜2024

- LLMそのものの性能競争
- GPT-4、Claude、Gemini
- コンテキスト長競争
- RAGブーム

⬇

## 2025〜2026

- モデル単体より「システム化」
- エージェント
- ワークフロー
- ループ
- ハーネス
- コンテキスト管理

が主戦場になっています。

## 第1世代：単発LLM

```text
質問
 ↓
LLM
 ↓
回答
```

ChatGPTそのもの。

特徴

- シンプル
- 安定
- 安い

限界

- 長い作業が苦手
- ツール利用不可
- 記憶がない

## 第2世代：RAG

```text
質問
 ↓
検索
 ↓
LLM
 ↓
回答
```

NotebookLMやCopilotの知識検索。

特徴

- 社内文書利用
- 最新情報利用

2024年はこれが主流。

## 第3世代：Workflow

今はここが実務の主流。

```text
Step1
 ↓
Step2
 ↓
Step3
 ↓
結果
```

例

```text
メール受信

↓
分類

↓
必要情報取得

↓
返信ドラフト

↓
承認
```

特徴

- 再現性高い
- テストしやすい
- 監査しやすい

MicrosoftやOpenAIも実際はこれを推している。

## 第4世代：Agent

話題の中心。

```text
目標
 ↓
計画
 ↓
実行
 ↓
再計画
 ↓
実行
 ↓
終了
```

例えば

```text
新規顧客調査して

↓
検索

↓
資料作成

↓
不足発見

↓
再検索

↓
資料更新
```

特徴

- 自律性高い
- 柔軟

欠点

- 暴走する
- コスト高い
- 再現性低い

## 第5世代：Agent Loop

最近のトレンド。

単なるAgentではなく、

```text
Plan
 ↓
Act
 ↓
Observe
 ↓
Reflect
 ↓
Plan
```

を繰り返す。

例

```text
コード生成

↓
テスト

↓
失敗

↓
原因分析

↓
再生成

↓
テスト

↓
成功
```

CodexやClaude Codeはほぼこれ。

## 第6世代：Multi-Agent

最近増えている。

```text
Manager Agent

├─ Research Agent
├─ Coding Agent
├─ QA Agent
└─ Review Agent
```

役割分担。

メリット

- 品質向上
- 並列実行

デメリット

- コスト爆増
- オーケストレーションが大変

## 第7世代：Agent + Tool

現在の本命。

```text
Agent

├─ Web検索
├─ DB
├─ ERP
├─ GitHub
├─ Email
└─ Teams
```

LLM自体ではなく

**ツールをどれだけ使えるか**

が重要になった。

## 第8世代：Agent + Harness

最近追っている領域。

```text
Agent
 ↓
Guardrail
 ↓
Validator
 ↓
Retry
 ↓
HITL
 ↓
Commit
```

つまり

> AIを賢くする

ではなく

> AIが失敗しても壊れない

を目指す。

OpenAI、Anthropic、Microsoft。

全部この方向。

## 第9世代：Context Engineering

今もっとも熱い領域。

昔

```text
Prompt Engineering
```

だった。

今

```text
Context Engineering
```

になっている。

何を見せるか

が重要。

例

```text
ユーザ情報
＋
過去会話
＋
関連文書
＋
実行履歴
＋
組織ルール
```

を組み立ててからLLMに渡す。

Codex、Claude Code、Cursor。

みんなここ。

## 企業IT視点

正直、

**「完全自律Agent」よりWorkflow + HITL**

です。

例えばD365更新なら

```text
申請
 ↓
Agent
 ↓
差分作成
 ↓
承認
 ↓
本番反映
```

の方が圧倒的に安全。

今年の企業導入の大半はこっち。

## 個人起業視点

逆。

小規模なら

```text
Agent
 ↓
Loop
 ↓
Tool
 ↓
自動実行
```

が効く。

理由は

- 失敗コストが低い
- 人手不足
- スピード優先

だから。

## 一枚でいうと

```text
2023
Prompt Engineering

↓
2024
RAG

↓
2025
Workflow

↓
2026
Agent + Loop

↓
現在
Context Engineering
+
Harness
+
HITL
```

になっています。

そして2026年後半の競争軸は、

**「どのモデルが賢いか」ではなく**

**「どれだけ長時間・低コスト・安全にループを回せるか」**

に移っています。Claude Code、Codex、OpenHands、LangGraph系が全部そこを狙っています。
