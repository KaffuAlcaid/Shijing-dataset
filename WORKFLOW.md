# Annotation Workflow

This document describes the complete pipeline from raw source text to structured JSON, for collaborators.

---

## Overview

```
ctext.org source text
     ↓
Manual txt preparation
     ↓
AI annotation extraction (DS R1)
     ↓
Human review
     ↓
Write to JSON dataset
     ↓
render.py → Markdown (for non-technical review)
```

---

## Step 1: Obtain Source Text

Source: [Mao Shi Zhengyi (Wuyingdian Shisanjing Zhushu edition)](https://ctext.org/wiki.pl?if=gb&res=871901)

Copy the text poem by poem and organize into the following txt format. Separate each sentence with `---`:

```
句子id：shijing_guofeng_zhounan_getan_s001
校勘文：
葛之覃兮，施于中谷，维叶萋萋
注释：
传：兴也。葛所以为絺綌，女功之事烦辱者。
覃，延也。施，移也。中谷，谷中也。萋萋，茂盛貌。
笺云：葛者，妇人之所有事也……
○施，毛以豉反，郑如字，下同。
萋切兮反。
---
```

**ID naming convention:**

```
shijing_{section}_{subsection}_{poem}_s{NNN}
```

| Section | Pinyin |
|---|---|
| 国风 | guofeng |
| 小雅 | xiaoya |
| 大雅 | daya |
| 颂 | song |

Subsection examples: 周南 → zhounan, 召南 → zhaonan

Sentence index `s001` starts from 001, reset per poem.

---

## Step 2: AI Annotation Extraction

Feed the txt into DeepSeek R1 (Expert Mode) using the following prompt:

````
You are a specialist assistant in pre-Qin classical texts, familiar with the Book of Songs and its traditional commentaries.

## Task
Given a collated sentence from the Book of Songs and its commentary text, extract all annotated characters, words, and phrases, together with their annotation content, and output as a JSON array.

## Input Format
Each entry contains:
- Sentence id
- 校勘文 (collated text)
- 注释 (commentary, including Mao zhuan, Zheng jian, phonetic glosses, textual variants)
- 今译 (modern Chinese translation, for reference)
- 注音 (Pinyin transcription, for reference)

## Rules

1. **anchor** must be a contiguous substring of 校勘文 only. Do not use text from the commentary.
   - Terminal punctuation is excluded from anchor. Take only the character content.
   - If an annotation cannot be mapped to a specific character or word, set 粒度 to "句" and anchor to the full 校勘文 (without punctuation).

2. **内容** must be verbatim from the source text. No paraphrase or rewriting.

3. **Mao zhuan and Zheng jian must be listed separately**, one annotation per anchor.

4. **Annotation type (注释类型):**
   - Unmarked lexical gloss, or prefixed with "传：" → `训诂` (Mao zhuan)
   - Prefixed with "笺云：" → `笺注` (Zheng Xuan)
   - Institutional exposition (ritual systems, official ranks, clothing grades, etc.), not a single-character gloss → `句义`
   - Prefixed with "○", fanqie spellings or direct phonetic glosses → `音韵`
   - Textual variants, editorial notes → `校勘`

5. **id** is local to each sentence, starting from `n001`, reset per sentence.

6. **span**: if the same anchor appears more than once in 校勘文, fill `[start, end)` character offset. Punctuation counts toward the offset. Omit if anchor appears only once.

7. **文献id** is always `src001`.

8. **Multiple annotations for the same anchor** are allowed, as long as the annotation types differ.

9. **Output**: JSON array only, wrapped in a markdown code block.

## Output Schema

{
  "id": "n001",
  "anchor": "覃",
  "粒度": "字",          // "字" | "词" | "句"
  "文献id": "src001",
  "注释类型": "训诂",    // "训诂"|"笺注"|"句义"|"考证"|"音韵"|"校勘"
  "内容": "覃，延也。"
}
````

---

## Step 3: Human Review

After AI output, check each entry for the following:

| Check | Common errors |
|---|---|
| anchor is a substring of 校勘文 | Commentary text mixed in; punctuation included |
| 内容 is verbatim | Paraphrase, merging, truncation |
| Mao/Zheng separation is correct | Unlabeled entries misclassified as 笺注 |
| 句义 judgment | Institutional exposition mislabeled as 训诂 |
| Multiple annotations on same character | 音韵 entries missed or merged with 训诂 |
| span filled correctly | Repeated anchors missing offset |

Once reviewed, fill the annotation array into the corresponding sentence object in the JSON file.

---

## Step 4: Fill 今译 and 注音

At the top level of each sentence object:

```json
"今译": "葛藤延伸啊，蔓延到谷中，叶子长得茂盛。",
"注音": "gé zhī tán xī shī yú zhōng gǔ wéi yè qī qī"
```

- 今译 follows Cheng Junying's *Shijing Yizhu*
- 注音 follows Cheng Junying's transcription; mark disputed or alternate readings with `"注音_存疑": true` on the relevant annotation entry

---

## Step 5: Render for Review

```bash
python tools/render.py data/feng/zhounan/getan.json getan_rendered.md
```

Generates a human-readable Markdown file for non-technical collaborators. No JSON required.

---

## File Naming Convention

```
data/
├── feng/
│   ├── zhounan/
│   │   ├── 关雎.json
│   │   └── 葛覃.json
│   └── zhaonan/
├── ya/
│   ├── xiaoya/
│   └── daya/
└── song/
```

---

## Quick Reference

| Field | Required | Description |
|---|---|---|
| id | ✅ | Local n001+, reset per sentence |
| anchor | ✅ | Substring of 校勘文, no punctuation |
| span | ❌ | Fill when anchor repeats in 校勘文 |
| 粒度 | ✅ | 字 / 词 / 句 |
| 文献id | ✅ | Always src001 |
| 注释类型 | ✅ | See table above |
| 内容 | ✅ | Verbatim excerpt, no rewriting |
| 注音_存疑 | ❌ | true when reading is disputed |
