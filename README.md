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
  "id": "shijing_guofeng_guanju_s001",
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

Source references are stored in `sources.json`:

```json
{
  "src001": {
    "文献名": "毛诗传",
    "作者": "毛亨",
    "朝代": "西汉"
  }
}
```

### Annotation Types

The schema uses Chinese keys and values to preserve terminological fidelity to the source tradition. 

| 值 | Description |
|---|---|
| 训诂 | Lexical exegesis |
| 笺注 | Commentary on prior annotation |
| 句义 | Sentence-level interpretation |
| 考证 | Historical textual evidence |
| 音韵 | Phonology, fanqie, phonetic loan |
| 校勘 | Textual variants |

## Directory Structure

```
Shijing-dataset/
├── README.md
├── README.zh.md
├── LICENSE
├── sources.json
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

## Roadmap

- [ ] 周南 — complete 
- [ ] 风 — complete
- [ ] 诗经 — complete
- [ ] Extend schema to other pre-Qin classics

## Acknowledgements

Inspired by [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)

## Citation

If you use this dataset in your research, please cite:
```
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

