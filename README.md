# Shijing-dataset

[中文版](README.zh.md) | English

A structured annotation dataset for the Book of Songs (《诗经》), 
designed for NLP research and AI training.

## Why This Project

Current AI models perform poorly on classical Chinese texts. The root cause
is simple: training corpora contain almost no structured annotation data —
only raw text, with the layers of 训诂 (exegesis) and 笺注 (commentary)
nearly absent.

This project takes the Book of Songs as a starting point, building a
reusable annotation schema that can be extended to other classical texts.
抛砖引玉 — a humble beginning, hoping others will follow.

## License

Copyright (c) 2025 KaffuAlcaid. This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Data Format

Each sentence corresponds to one JSON object:

​```json
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
​```

Source references are stored in `sources.json`:

​```json
{
  "src001": {
    "文献名": "毛诗传",
    "作者": "毛亨",
    "朝代": "西汉"
  }
}
​```

### Annotation Types

| 值 | Description |
|---|---|
| 训诂 | Lexical exegesis |
| 笺注 | Commentary on prior annotation |
| 句义 | Sentence-level interpretation |
| 考证 | Historical textual evidence |
| 音韵 | Phonology, fanqie, phonetic loan |
| 校勘 | Textual variants |

## Directory Structure

​```
Shijing-dataset/
├── README.md
├── README.zh.md
├── LICENSE
├── sources.json
├── schema/
│   └── schema.json
├── data/
│   ├── guofeng/
│   ├── xiaoya/
│   ├── daya/
│   └── song/
└── tools/
    └── validate.py
​```

## Roadmap

- [ ] 国风 — complete source text entry
- [ ] 国风 — Mao Commentary (毛传) annotations
- [ ] 国风 — Zheng Commentary (郑笺) annotations
- [ ] Extend schema to other pre-Qin classics

## Acknowledgements

Inspired by [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
and the broader open-source classical Chinese community.