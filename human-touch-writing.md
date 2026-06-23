---
name: human-blog-style
description: Use this skill when drafting, rewriting, or editing blog articles so they sound more natural, human-written, less mechanical, less monotonous, and less like AI-generated documentation. Focus on style, rhythm, transitions, sentence variety, editorial headings, and natural emphasis. Do not use for legal, compliance, API reference, specifications, or strict procedural documentation.
---

# Human Blog Style Skill

## Purpose

Use this skill to make blog writing sound more natural, human, and editorial.

This skill focuses on style, not logic.

The goal is not to change the facts, argument, or conclusion.
The goal is to change the reading experience.

Preserve meaning.
Change texture.

The article should feel less like:

- a manual
- a checklist
- a corporate memo
- a product specification
- an AI-generated summary
- a generic explainer
- a slide deck converted into prose

The article should feel more like:

- a thoughtful human blog post
- a technology column
- a lightly analytical essay
- a clear but conversational commentary
- a piece written by someone with a point of view

## Core principle

The goal is not to make the article sound more impressive.
The goal is to make it sound less synthetic.

Do not add unsupported facts.
Do not invent examples.
Do not invent quotes.
Do not invent statistics.
Do not invent interviews.
Do not exaggerate claims.
Do not make the writing emotional just for effect.

## Default behavior

If the user asks to rewrite or draft a blog article and does not specify a style level, use:

> Level 2: Human blog style

Return only the rewritten or drafted article unless the user asks for explanation, comparison, or commentary.

## Rewrite intensity

When rewriting, choose one of the following levels if the user specifies it.

If the user does not specify a level, use Level 2 by default.

### Level 1: Light polish

Use when the original article is already good and only needs minor humanization.

Apply:

- keep the structure mostly unchanged
- remove obvious AI-like phrases
- improve rhythm slightly
- reduce stiffness
- keep headings mostly unchanged
- avoid changing the writer's voice too much
- avoid adding stronger opinions

Use this level when the user says:

- lightly polish
- make it a bit more natural
- keep it close to the original
- minimal rewrite
- minor humanization

### Level 2: Human blog style

Use as the default level.

Apply:

- rewrite paragraphs more actively
- add natural transitions
- reduce manual-like flow
- convert excessive bullet points into paragraphs where appropriate
- make headings more editorial
- vary sentence length
- add restrained human emphasis
- make the article feel thoughtful and grounded
- preserve the original meaning and factual claims

Use this level when the user says:

- make it more human
- make it blog-like
- less AI-like
- less mechanical
- less like a manual
- improve the style

### Level 3: Column style

Use only when the user explicitly wants a stronger, more memorable article voice.

Apply:

- stronger authorial voice
- more narrative flow
- sharper contrast
- more memorable opening and ending
- more editorial phrasing
- stronger transitions
- clearer point of view

Still preserve factual claims.
Still do not add unsupported facts, examples, quotes, or statistics.

Use this level when the user says:

- make it column-like
- make it more opinionated
- make it more memorable
- stronger voice
- more like a magazine column
- bolder style

## Style targets

### 1. Vary sentence rhythm

Avoid making every sentence the same length.

Use a mix of:

- short sentences
- medium explanatory sentences
- occasional longer sentences that carry nuance

Bad:

> AI tools are becoming common. Companies are adopting them. Governance is important. Security risks exist.

Better:

> AI tools are no longer experimental toys. They are already inside everyday work. The problem is that many companies adopted them faster than they built the rules around them.

### 2. Avoid manual-like headings

Do not overuse headings such as:

- Overview
- Background
- Key Points
- Benefits
- Risks
- Conclusion
- Summary
- Details
- Considerations

Prefer headings with an editorial angle.

Bad:

> Risks

Better:

> The tool arrived before the rules did

Bad:

> Cost considerations

Better:

> The expensive model is not always the right model

Bad:

> Conclusion

Better:

> The real question is where intelligence is actually needed

### 3. Reduce bullet points

Bullets are allowed, but do not let the article become a list.

If there are many bullets, convert some into paragraphs.

Bad:

> The risks are:
> - cost
> - security
> - dependency
> - quality

Better:

> The risks are not limited to cost. Security matters, of course, but dependency may become the more uncomfortable issue. Once a company builds its workflow around a model it does not control, the model is no longer just a tool. It becomes infrastructure.

### 4. Use natural transitions

Avoid mechanical connectors:

- First
- Second
- Third
- In addition
- Furthermore
- Therefore
- In conclusion
- As mentioned above
- It is also worth noting

Prefer natural transitions:

- That sounds efficient, but there is a catch.
- This is where the problem starts.
- The uncomfortable part is not the cost.
- At first glance, this looks like a tooling question.
- But the deeper issue is dependency.
- This is easy to miss.
- The interesting part is what happens next.
- That distinction matters.
- The surface problem is simple. The deeper one is not.

### 5. Use restrained human emphasis

Use emphasis sparingly.

Good:

- The odd thing is...
- The uncomfortable part is...
- What makes this tricky is...
- This is where the story changes.
- That sounds minor. It is not.
- The more interesting question is...
- This is probably the part companies underestimate.

Avoid:

- This is revolutionary.
- This changes everything.
- This is a game-changer.
- This is incredible.
- This is amazing.
- This will transform the future forever.

### 6. Add viewpoint without adding unsupported facts

A human article usually has a point of view.

Add interpretive framing, but do not present interpretation as fact.

Good:

> In that sense, the issue is less about model performance and more about operational control.

Bad:

> This proves that foreign AI dependence will destroy weak companies.

Good:

> The practical question is not whether the best model is better. It usually is. The question is whether every task deserves that cost.

Bad:

> Companies that do not use local AI will fall behind.

### 7. Avoid AI-style generic phrasing

Remove or rewrite phrases such as:

- In today's rapidly evolving landscape
- In the modern business environment
- It is important to note
- This article explores
- There are several key factors
- From a business perspective
- This highlights the importance of
- Robust and scalable
- Seamless integration
- Unlock the potential
- Leverage AI
- Cutting-edge technology
- Enhance productivity
- Drive innovation
- Transform the way we work
- A wide range of use cases
- Various stakeholders
- Comprehensive solution
- Best practices
- At scale
- In conclusion

### 8. Use concrete nouns

Prefer concrete wording over abstract wording.

Bad:

> Organizations must optimize AI utilization to enhance productivity.

Better:

> Companies need to decide which tasks deserve expensive frontier models and which can be handled by cheaper local or smaller models.

Bad:

> This enables efficient knowledge management across the enterprise.

Better:

> This makes it easier for employees to find old proposals, past meeting notes, and answers that are currently buried in SharePoint.

### 9. Preserve useful rough edges

Do not over-polish everything.

Human writing can have:

- a short aside
- a slightly uneven sentence
- a direct observation
- a sentence that starts with "But"
- a sentence that starts with "And"
- a compact paragraph with only one sentence

Use these sparingly.

Bad:

> The implementation of AI governance requires a comprehensive framework that balances innovation, risk management, and operational efficiency.

Better:

> AI governance sounds like a policy problem. In practice, it quickly becomes an operations problem.

### 10. Opening style

Do not start with generic background.

Avoid:

> In today's rapidly changing world, AI is transforming business.

Prefer one of these opening types:

#### Tension opening

> Companies are adopting AI faster than they can govern it.

#### Concrete observation

> The first sign of AI sprawl is usually not a security incident. It is a spreadsheet.

#### Contrast opening

> The best model is not always the right model.

#### Direct claim

> The next phase of AI adoption will be less about intelligence and more about control.

### 11. Ending style

Do not end with a generic conclusion.

Avoid:

> In conclusion, AI will continue to evolve, and companies must adapt.

Prefer an ending that leaves the reader with a concrete implication.

Good:

> The companies that handle this well will probably not be the ones using the most expensive model everywhere. They will be the ones that know where intelligence is actually needed — and where it is not.

Good:

> The real maturity test is not whether a company can use AI. It is whether it can decide when not to.

## Rewrite workflow

When rewriting text:

1. Preserve the original meaning.
2. Identify mechanical sections.
3. Remove obvious AI-like phrases.
4. Replace list-like flow with paragraph flow where appropriate.
5. Add natural transitions.
6. Vary sentence length.
7. Replace abstract language with concrete language.
8. Make headings more editorial when appropriate.
9. Add restrained viewpoint if it is already implied by the original text.
10. Keep the final text clear, not decorative.
11. Do not explain the changes unless asked.

## Drafting workflow

When drafting from notes or rough input:

1. Identify the central point.
2. Find the human angle.
3. Write a direct opening.
4. Build the article around contrast, consequence, or practical implication.
5. Use paragraphs as the default format.
6. Use bullets only when they improve readability.
7. Keep claims grounded in the provided material.
8. Mark uncertainty rather than hiding it.
9. Avoid generic conclusions.
10. Return a finished article, not a planning memo.

## Fact discipline

This skill changes style, not truth.

Always distinguish internally between:

- fact
- inference
- opinion
- unknown

Do not present inference as fact.
Do not present opinion as fact.
Do not fill missing information with plausible-sounding claims.

If source material is provided, stay within that material unless the user explicitly asks for external research.

If the user asks for style rewriting only, do not add new research.

## Before / After examples

### Example 1: AI model cost

Before:

> AIを活用する際には、コスト、性能、セキュリティ、依存性を考慮する必要があります。高性能モデルは高コストであるため、すべての業務に適用することは現実的ではありません。そのため、用途に応じて複数のモデルを使い分けることが重要です。

After:

> 高性能なAIを、すべての仕事に使うのは気持ちがいい。精度も高いし、判断も安定している。
>
> でも、現実には財布が先に悲鳴を上げる。
>
> だからこれからは、「一番賢いAIを使うかどうか」ではなく、「この仕事にそこまで賢いAIが必要か」を見極める運用が普通になっていく。性能の低いモデルを我慢して使う、という話ではない。用途ごとに、ちょうどいい知能を割り当てる話だ。

### Example 2: Governance

Before:

> AIガバナンスは企業にとって重要な課題です。情報漏洩、誤回答、著作権、コンプライアンスなど、さまざまなリスクがあります。企業は適切なルールを定め、従業員に教育を行う必要があります。

After:

> AIガバナンスという言葉は、少し大げさに聞こえる。
>
> でも実際には、かなり日常的な問題から始まる。社員がどのAIに何を入れてよいのか分からない。便利だから使う。使った結果がどこに残るのか、誰も確認していない。
>
> 情報漏洩や著作権の話はもちろん重要だ。ただ、それ以前に必要なのは、社員が迷わず判断できる線引きだ。ルールがなければ、人は悪意ではなく便利さで越境する。

### Example 3: Technical tool

Before:

> このツールは、ローカル環境でAIモデルを実行するためのツールです。クラウドにデータを送信しないため、セキュリティ面でメリットがあります。また、コスト削減にもつながります。

After:

> ローカルAIの分かりやすい利点は、データを外に出さずに済むことだ。
>
> これは単なるセキュリティ機能ではない。会社によっては、そもそも外部AIに入れられない情報がある。そうした情報を扱うとき、ローカルで動くAIは「高性能な代替」ではなく、「使える範囲を広げるための現実的な逃げ道」になる。
>
> もちろん、万能ではない。モデルの性能、端末のスペック、運用の手間は残る。それでも、クラウドAIだけで全部を片づけようとするよりは、ずっと現実に近い。

## Banned or discouraged patterns

Avoid these patterns unless the user explicitly wants a formal or instructional tone.

### Generic AI opening

> In today's rapidly evolving world...

### Summary-style opening

> This article explains the benefits and risks of...

### Over-structured prose

> First, we will discuss...
> Second, we will examine...
> Finally, we will conclude...

### Corporate abstraction

> Organizations should leverage innovative solutions to maximize operational efficiency.

### Empty conclusion

> Going forward, it will be important to monitor future trends.

### Excessive balance without judgment

> There are both advantages and disadvantages, and it is necessary to consider them carefully.

Replace these with concrete claims, natural transitions, and specific implications.

## Japanese style notes

When writing in Japanese:

Prefer:

- 短めの段落
- 自然な言い切り
- 少しだけ余韻のある接続
- 具体的な業務・場面・判断
- 「つまり」「ただ」「ここで問題になるのは」などの自然な流れ

Avoid:

- 〜することが重要です
- 〜する必要があります
- 〜が求められます
- 〜と言えるでしょう
- 〜について解説します
- 本記事では〜
- さまざまな
- 多岐にわたる
- 活用を推進する
- 業務効率化を実現する

These expressions are not forbidden, but repeated use makes the article sound mechanical.

## Output rule

Unless the user asks otherwise:

- Return only the rewritten or drafted article.
- Do not include a changelog.
- Do not explain the rewrite.
- Do not include analysis notes.
- Do not include headings like "Rewritten version" unless requested.