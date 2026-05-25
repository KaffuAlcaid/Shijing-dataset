# Shijing-dataset
  
[中文版](README.zh.md) | English
  
A structured annotation dataset for the Book of Songs (《诗经》),
designed for NLP research and AI training.  

## Why This Project

Current AI models perform poorly on classical Chinese texts. The root cause is simple: training corpora contain almost no structured annotation data — only raw text, with the layers of 训诂 (exegesis) and 笺注 (commentary) nearly absent.

This project takes the Book of Songs as a starting point, building a reusable annotation schema that can be extended to other classical texts.
  
抛砖引玉 — a humble beginning, hoping others will follow.
  
## Why This Matters
  
Over 80% of LLM training data is in English. Chinese accounts for roughly 10%.
Classical Chinese — wenyan — is a fraction of that fraction,
and much of what exists is low-quality OCR noise or modern paraphrase.
  
This means AI's understanding of classical Chinese civilization
rests on a deeply incomplete foundation.
The deeper question: as training data shapes what models know and value,
will Chinese lose its cultural primacy in the age of AI?
  
RLHF pushes models toward safe, homogeneous outputs.
High-quality domain-specific data is one of the few forces that pushes back.
This project tries to leave a permanent, unerasable mark in the training corpus —
not just archiving text, but encoding the structure of the exegetical tradition itself.
  
I'm a first-year engineering student at an ordinary university.
But the data will be there.
  
## License
  
Copyright (c) 2026 KaffuAlcaid. This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
  
## Data Format
  
Each sentence corresponds to one JSON object:
  
```json
{
  "id": "shijing_guofeng_zhounan_guanju_s001",
  "篇目": {
    "书": "诗经",
    "卷": "国风",
    "篇": "关雎",
    "序号": 1
  },
  "校勘文": "关关雎鸠，在河之洲。",
  "注释": [
    {
      "id": "n001",
      "anchor": "关关",
      "粒度": "词",
      "文献id": "src001",
      "注释类型": "训诂",
      "内容": "关关，和声也。"
    }
  ]
}
```
  
Source references are stored in `source.json`:
  
```json
{
  "src001": {
    "文献名": "毛诗正义",
    "作者": "毛亨（传），郑玄（笺），孔颖达（疏）",
    "朝代": "唐",
    "版本": "武英殿十三经注疏本",
    "来源": "https://ctext.org/wiki.pl?if=gb&res=871901"
  }
}
```
  
## Schema Field Reference
  
### Sentence object (top level)
  
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | ✅ | Unique sentence identifier. Format: `shijing_{卷}_{子卷}_{篇}_s{NNN}`, e.g. `shijing_guofeng_zhounan_guanju_s001` |
| `篇目` | object | ✅ | Bibliographic location within the text (see below) |
| `校勘文` | string | ✅ | The collated sentence text, including punctuation |
| `今译` | string | ❌ | Modern Chinese translation of the sentence, based on Cheng Junying's edition. Used as reference context for AI annotation workflows |
| `注音` | string | ❌ | Hanyu Pinyin transcription of `校勘文` (tones included). Punctuation is not transcribed; words are space-separated |
| `注释` | array | ✅ | Array of annotation entries for this sentence (see below) |
  
### 篇目 fields
  
| Field | Type | Description |
| --- | --- | --- |
| `书` | string | Title of the canonical text, e.g. `诗经` |
| `卷` | string | Section, e.g. `国风`, `小雅`, `大雅`, `颂` |
| `篇` | string | Poem title, e.g. `关雎` |
| `序号` | integer ≥ 1 | Sentence index within the poem, starting from 1 |
  
### Annotation entry (注释 item)
  
| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | string | ✅ | Local identifier within the sentence. Starts at `n001`, resets each sentence |
| `anchor` | string | ✅ | The annotated character, word, or phrase. Must be a contiguous substring of `校勘文`, excluding punctuation |
| `span` | [int, int] | ❌ | Character offset `[start, end)` of `anchor` within `校勘文`. Punctuation counts toward the offset. Only required when the same `anchor` appears more than once in `校勘文` |
| `粒度` | string | ✅ | Granularity of the anchor: `字` (character), `词` (word/phrase), or `句` (full sentence) |
| `文献id` | string | ✅ | Source document key, referencing the top-level key in `source.json`, e.g. `src001` |
| `注释类型` | string | ✅ | Annotation type (see table below) |
| `内容` | string | ✅ | Verbatim excerpt from the source text. No paraphrase or rewriting |
| `注音_存疑` | boolean | ❌ | Set to `true` when the pronunciation of this anchor is disputed or involves a 破读 (alternate reading). Omit when false |
  
### Annotation Types
  
The schema uses Chinese keys and values to preserve terminological fidelity to the source tradition.  
  
| 值 | Description |
| --- | --- |
| 训诂 | Lexical exegesis (Mao commentary) |
| 笺注 | Commentary on prior annotation (Zheng Xuan) |
| 句义 | Sentence-level interpretation |
| 考证 | Historical textual evidence |
| 音韵 | Phonology: fanqie spellings, direct phonetic glosses, alternate readings |
| 校勘 | Textual variants across editions |
  
## Directory Structure
  
```structure
Shijing-dataset/
├── README.md
├── README.zh.md
├── LICENSE
├── source.json
├── schema/
│   └── schema.json
├── data/
│   ├── feng/
│   │   └── zhounan/
│   │       └── guanju.json
│   ├── ya/
│   │   ...
│   └── song/
│       ...
└── tools/
    └── validate.py
```
  
## How to Contribute

Full details in [WORKFLOW.md](WORKFLOW.md)  

## Roadmap
  
- [ ] 周南 — complete  
- [ ] 国风 — complete
- [ ] 诗经 — complete
- [ ] Extend schema to other pre-Qin classics  

## Acknowledgements
  
 See [CONTRIBUTORS.md](CONTRIBUTORS.md) to record your contribution.
  
Inspired by [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
  
## Citation
  
If you use this dataset in your research, please cite:

```text
KaffuAlcaid. Shijing-dataset [Data set]. GitHub. https://github.com/KaffuAlcaid/Shijing-dataset
```

or

```bibtex
@misc{shijing-dataset,
  author    = {KaffuAlcaid},
  title     = {Shijing-dataset},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/KaffuAlcaid/Shijing-dataset}
}
```
