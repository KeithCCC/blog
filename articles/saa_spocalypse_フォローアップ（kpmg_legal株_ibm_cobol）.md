# [Saaspocalypseは、一般ユーザ企業の現場ではもう始まっている](https://keithccc.github.io/blog/articles/EndofSaaS.html) フォローアップ

## 目的

前回の「Saaspocalypseは、一般ユーザ企業の現場ではもう始まっている（SaaS的前提の崩れ）」の続編として、

- **KPMG（プロフェッショナルファーム側の動き）**
- **法務・リーガル領域の企業／市場の反応（株価と事業側の対抗策）**
- **IBM/COBOL（レガシー価値の再評価）**
  を一本の線でつなぐ。

中心メッセージは1つ：

> **AIの影響は、これまで人類が経験したことのないスピードで市場と現場を動かしている。**

---

## 1. KPMGは「AIを使った」ではなく「AI前提の仕事設計」に踏み込んだ

### 1-1. KPMGの象徴的な動き：巨大プロンプトで“業務を1日化”

KPMG（豪州）が、**100ページ級のプロンプト（設計資産）**************************************************で“TaxBot”を構築し、従来**************************************************2週間かかっていた税務アドバイス作業を1日規模に短縮**した事例が報じられている。

- これは「AIを試した」ではなく、**AIに合わせて業務を再設計した**話。
- 価値はモデルそのものより、
  - 何をインプットにするか
  - どこまでをAIに任せるか
  - どの形式でアウトプットさせるか
  - 品質保証と責任境界をどう取るか
    という\*\*設計（＝仕事の型）\*\*にある。

参考：

- KPMGの100ページプロンプトTaxBot（The Register）
- 同件を扱うTechRadar等

### 1-2. KPMGは「法務部門のAI導入」も“ユースケース設計”から支援

KPMGはMicrosoftと連携し、企業法務部門向けに

- **生成AIユースケースの作り方**
- **リスクやガバナンスを踏まえた導入の進め方**
  をワークショップ型で支援していると報じられている。
  ここでもテーマは「ツール紹介」ではなく、
  **法務プロセスにAIをどう埋め込むか（運用設計）**。

参考：

- KPMG×Microsoftによる法務部門向け支援（Legal Dive）
- KPMG×MicrosoftのAI提携（KPMG公式／Microsoft公式）

---

## 2. 法務系企業（リーガル／データ／SaaS）の反応：株価急落 → “反撃”と再評価

### 2-1. きっかけ：Anthropicの法務向けプラグインが「市場売り」を引き起こす

Reutersは、Anthropicの\*\*法務自動化ツール（legal tool / legal plug-in）\*\*が引き金となり、
ソフトウェア・データ企業に大きな売りが出たと報じた。

- **世界のソフトウェア／サービス株で大規模な売り（約1兆ドル規模と報じられるケースも）**
- 欧州のデータ／法務関連銘柄（RELX、Wolters Kluwer、Sageなど）に売り
- 米Thomson Reutersも大きく下落

参考：

- Reuters（2/4）：Anthropicのlegal toolが引き金になったソフトウェア株の大規模売り
- Reuters（2/3）：欧州ソフトウェア・データ株への売り圧力（RELX等）
- Guardian（2/3）：欧州のデータ／法務関連企業の株価下落の報道
- Morningstar（2/5）：Anthropic法務プラグイン発表後の主要銘柄下落まとめ

### 2-2. 企業側の反撃：Thomson Reutersの「CoCounsel 1Mユーザー」

興味深いのは、その後の“揺り戻し”。
Reutersは、Thomson ReutersがAI法務アシスタント**CoCounselの利用者100万人**を公表し、
株価が大きく上昇したと報じた。

- ここでの主張は「AIに負けない」ではなく、
  - **独自コンテンツ（法令・判例など）**
  - 資本力
  - 既存ワークフローへの統合
    で**AI時代の勝ち筋を作れる**という論理。

参考：

- Reuters（2/24）：CoCounsel 1MユーザーでThomson Reuters株が上昇

### 2-3. 重要な読み：市場が恐れたのは“機能追加”ではなく「価格モデルの崩壊」

法務領域のAIは、単なる自動化ではなく、

- **課金根拠（席課金・データ課金・時間課金）**
- **専門家の作業時間（billable hours）**
- **検索・調査の囲い込み（データベース）**
  といった“収益モデルの前提”に触れる。

市場の急落は、

> 「AIが業務を代替するか」
> よりも
> **「既存の値付けが崩れるか」**
> を先に織り込みにいった、と読むのが自然。

---

## 3. IBM/COBOL：レガシーの“時間価値”がAIで溶けた

Reutersは、AnthropicがCOBOL近代化を支援できると示した後、
**IBM株が大きく下落**したと報じた。

- COBOLやメインフレーム周辺は、長年
  - 保守
  - 移行
  - モダナイゼーション
    という“長期・高単価”の時間価値で成立していた
- AIがそこを短縮する可能性を示すと、
  **価値の源泉（時間）が再評価される**

参考：

- Reuters（2/24）：IBM株下落とAnthropicのCOBOL近代化言及
- Reuters（2/24）：ソフトウェア株の戻りとIBMショックへの言及

---

## 4. まとめ：SaaSpocalypseの本質は「SaaSが終わる」ではなく“時間の価値が崩れる速度”

今回の3点（KPMG／法務市場／IBMレガシー）をつなぐと、共通点は1つ。

- 価値は「機能」ではなく
- 価値は「時間」でもなくなりつつあり
- 価値は **“AI前提で再設計できるか”** に移動している

そして何より、

> **その移動が、これまでの技術変化より桁違いに速い。**

---

## Reference URLs（引用元）

- Reuters（Thomson Reuters：CoCounsel 1M users）: [https://www.reuters.com/business/thomson-reuters-shares-rally-after-cocounsel-ai-tool-draws-1-million-users-2026-02-24/](https://www.reuters.com/business/thomson-reuters-shares-rally-after-cocounsel-ai-tool-draws-1-million-users-2026-02-24/)

- Reuters（Anthropic legal plug-in → ソフトウェア株大規模売り）: [https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/](https://www.reuters.com/business/media-telecom/global-software-stocks-hit-by-anthropic-wake-up-call-ai-disruption-2026-02-04/)

- Reuters（欧州ソフトウェア・データ株への売り）: [https://www.reuters.com/business/media-telecom/ai-concerns-pummel-european-software-stocks-2026-02-03/](https://www.reuters.com/business/media-telecom/ai-concerns-pummel-european-software-stocks-2026-02-03/)

- Reuters（Anthropic 新AIツール、legal plug-in後の市場動揺に言及）: [https://www.reuters.com/business/finance/anthropic-touts-new-ai-tools-weeks-after-legal-plug-in-spurred-market-rout-2026-02-24/](https://www.reuters.com/business/finance/anthropic-touts-new-ai-tools-weeks-after-legal-plug-in-spurred-market-rout-2026-02-24/)

- Guardian（Anthropic legal tool → 欧州データ/法務株下落）: [https://www.theguardian.com/technology/2026/feb/03/anthropic-ai-legal-tool-shares-data-services-pearson](https://www.theguardian.com/technology/2026/feb/03/anthropic-ai-legal-tool-shares-data-services-pearson)

- Morningstar（主要銘柄：Thomson Reuters/RELX/Wolters等の下落まとめ）: [https://global.morningstar.com/ja/stocks/thomson-reuters-relx-wolters-stocks-crushed-after-anthropic-debuts-claude-legal-plug-in](https://global.morningstar.com/ja/stocks/thomson-reuters-relx-wolters-stocks-crushed-after-anthropic-debuts-claude-legal-plug-in)

- KPMG 100ページプロンプトTaxBot（The Register）: [https://www.theregister.com/2025/08/20/kpmg\_giant\_prompt\_tax\_agent/](https://www.theregister.com/2025/08/20/kpmg_giant_prompt_tax_agent/)

- KPMG×Microsoft 法務部門向けAI支援（Legal Dive）: [https://www.legaldive.com/news/kpmg-microsoft-ai-collaboration-ai-use-cases-legal-departments/702328/](https://www.legaldive.com/news/kpmg-microsoft-ai-collaboration-ai-use-cases-legal-departments/702328/)

- KPMG×Microsoft AI提携（KPMG公式）: [https://kpmg.com/us/en/media/news/kpmg-microsoft-agreement-2023.html](https://kpmg.com/us/en/media/news/kpmg-microsoft-agreement-2023.html)

- KPMG×Microsoft AI提携（Microsoft公式）: [https://news.microsoft.com/source/2023/07/11/kpmg-and-microsoft-enter-landmark-agreement-to-put-ai-at-the-forefront-of-professional-services/](https://news.microsoft.com/source/2023/07/11/kpmg-and-microsoft-enter-landmark-agreement-to-put-ai-at-the-forefront-of-professional-services/)

---

##

