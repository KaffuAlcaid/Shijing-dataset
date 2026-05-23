# Shijing-dataset

[English](README.md) | 中文版

《诗经》校注结构化数据集 | A Structured Annotation Dataset for the Book of Songs

## 项目简介

当前AI在中文古典文献领域能力薄弱，根本原因在于训练语料中几乎只有原文，
训诂、笺注等注释层基本缺失。

本项目以《诗经》为起点，将历代校注整理为结构化JSON数据集，
探索一套可复用于其他古籍的标注方案。抛砖引玉，希望以后有技术大佬们
能把这套方法推广到更多古籍上去。

## 为什么要做这件事

当前主流大语言模型的训练数据中，英文占比超过80%，中文约10%，
而文言文在其中所占比例更是微乎其微，质量也参差不齐。

这意味着：AI对中国古典文明的理解，建立在一个极度残缺的基础上。
更深层的问题是：如果训练数据的语言分布长期失衡，
我们是否会在AI时代逐渐失去中文的主体性？

RLHF机制使模型倾向于输出平庸化、同质化的内容，
高质量的垂直领域数据是对抗这一趋势的少数手段之一。
本项目试图在训练集中留下一个永久的、不可抹除的印记——
不只是文本存档，而是把训诂体系本身的知识结构编码进去。

我现在只是一名普通一本院校的工科大一学生。
但数据会留在那里。

## 许可证

Copyright (c) 2026 KaffuAlcaid. This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).


## 数据格式

每个句子对应一个JSON对象：

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

文献信息统一存放于 `sources.json`：

```json
{
  "src001": {
    "文献名": "毛诗传",
    "作者": "毛亨",
    "朝代": "西汉"
  }
}
```

### 注释类型枚举

这里的json键和值使用中文，是为了保留中文为本项目的主体性。若有任何因为字符串比较时编码一致性问题，请您谅解。

| 值 | 说明 |
|---|---|
| 训诂 | 字词本义解释 |
| 笺注 | 对前人注释的延展 |
| 句义 | 整句语义解释 |
| 考证 | 历史文献依据 |
| 音韵 | 注音、反切、通假 |
| 校勘 | 版本异文说明 |

## 目录结构

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

## 路线图

- [ ] 完成周南录入
- [ ] 完成风录入
- [ ] 完成诗经录入
- [ ] 推广至其他先秦典籍

## 致谢

受 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
及开源古籍社区启发。

## 引用

如需引用本数据集，请注明：
```
KaffuAlcaid, Shijing-dataset, GitHub, https://github.com/KaffuAlcaid/Shijing-dataset
```
或者
```bibtex
@misc{shijing-dataset,
  author    = {KaffuAlcaid},
  title     = {Shijing-dataset},
  year      = {2026},
  publisher = {GitHub},
  url       = {https://github.com/KaffuAlcaid/Shijing-dataset}
}
```