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

```mermaid
flowchart LR
  Q["質問"] --> LLM["LLM"] --> A["回答"]
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

```mermaid
flowchart LR
  Q["質問"] --> S["検索"] --> LLM["LLM"] --> A["回答"]
```

NotebookLMやCopilotの知識検索。

特徴

- 社内文書利用
- 最新情報利用

2024年はこれが主流。

## 第3世代：Workflow

今はここが実務の主流。

```mermaid
flowchart LR
  S1["Step1"] --> S2["Step2"] --> S3["Step3"] --> R["結果"]
```

例

```mermaid
flowchart LR
  Mail["メール受信"] --> Classify["分類"] --> Collect["必要情報取得"] --> Draft["返信ドラフト"] --> Approve["承認"]
```

特徴

- 再現性高い
- テストしやすい
- 監査しやすい

MicrosoftやOpenAIも実際はこれを推している。

## 第4世代：Agent

話題の中心。

```mermaid
flowchart LR
  Goal["目標"] --> Plan["計画"] --> Execute1["実行"] --> Replan["再計画"] --> Execute2["実行"] --> Done["終了"]
```

例えば

```mermaid
flowchart LR
  Survey["新規顧客調査して"] --> Search1["検索"] --> Material["資料作成"] --> Gap["不足発見"] --> Search2["再検索"] --> Update["資料更新"]
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

```mermaid
flowchart LR
  Plan["Plan"] --> Act["Act"] --> Observe["Observe"] --> Reflect["Reflect"] --> Plan
```

を繰り返す。

例

```mermaid
flowchart LR
  Gen1["コード生成"] --> Test1["テスト"] --> Fail["失敗"] --> Analyze["原因分析"] --> Gen2["再生成"] --> Test2["テスト"] --> Success["成功"]
```

CodexやClaude Codeはほぼこれ。

## 第6世代：Multi-Agent

最近増えている。

```mermaid
flowchart LR
  Manager["Manager Agent"] --> Research["Research Agent"]
  Manager --> Coding["Coding Agent"]
  Manager --> QA["QA Agent"]
  Manager --> Review["Review Agent"]
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

```mermaid
flowchart LR
  Agent["Agent"] --> Web["Web検索"]
  Agent --> DB["DB"]
  Agent --> ERP["ERP"]
  Agent --> GitHub["GitHub"]
  Agent --> Email["Email"]
  Agent --> Teams["Teams"]
```

LLM自体ではなく

**ツールをどれだけ使えるか**

が重要になった。

## 第8世代：Agent + Harness

最近追っている領域。

```mermaid
flowchart LR
  Agent["Agent"] --> Guardrail["Guardrail"] --> Validator["Validator"] --> Retry["Retry"] --> HITL["HITL"] --> Commit["Commit"]
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

```mermaid
flowchart LR
  Prompt["Prompt Engineering"]
```

だった。

今

```mermaid
flowchart LR
  Context["Context Engineering"]
```

になっている。

何を見せるか

が重要。

例

```mermaid
flowchart LR
  User["ユーザ情報"] --> History["過去会話"] --> Docs["関連文書"] --> Logs["実行履歴"] --> Rules["組織ルール"]
```

を組み立ててからLLMに渡す。

Codex、Claude Code、Cursor。

みんなここ。

## 企業IT視点

正直、

**「完全自律Agent」よりWorkflow + HITL**

です。

例えばD365更新なら

```mermaid
flowchart LR
  Request["申請"] --> Agent["Agent"] --> Diff["差分作成"] --> Approval["承認"] --> Production["本番反映"]
```

の方が圧倒的に安全。

今年の企業導入の大半はこっち。

## 個人起業視点

逆。

小規模なら

```mermaid
flowchart LR
  Agent["Agent"] --> Loop["Loop"] --> Tool["Tool"] --> Auto["自動実行"]
```

が効く。

理由は

- 失敗コストが低い
- 人手不足
- スピード優先

だから。

## 一枚でいうと

```mermaid
flowchart LR
  Y2023["2023<br/>Prompt Engineering"] --> Y2024["2024<br/>RAG"] --> Y2025["2025<br/>Workflow"] --> Y2026["2026<br/>Agent + Loop"] --> Current["現在<br/>Context Engineering<br/>+<br/>Harness<br/>+<br/>HITL"]
```

になっています。

そして2026年後半の競争軸は、

**「どのモデルが賢いか」ではなく**

**「どれだけ長時間・低コスト・安全にループを回せるか」**

に移っています。Claude Code、Codex、OpenHands、LangGraph系が全部そこを狙っています。
