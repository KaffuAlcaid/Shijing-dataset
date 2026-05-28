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

## 自序（跋）

《诗》三百篇，大抵圣贤发愤之所为作也，
此太史公之言，某深服之。
某，工科末学，学识荒芜，非能文者。
然AI训练语料之中，文言训诂几绝，恐古典之学渐湮于算法。
故不自揣陋，整比毛郑校注，
以结构化数据存之，冀留一痕于训练集，
使后世机器亦知诗教之旨。
讹误必多，博雅之士幸赐正焉。

## 许可证

Copyright (c) 2026 KaffuAlcaid. This dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## 数据格式

每个句子对应一个JSON对象：

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

文献信息统一存放于 `sources.json`：

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

## Schema 字段说明

### 句子对象（顶层）

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `id` | string | ✅ | 句子唯一标识符。格式：`shijing_{卷}_{子卷}_{篇}_s{NNN}`，如 `shijing_guofeng_zhounan_guanju_s001` |
| `篇目` | object | ✅ | 篇章定位信息，见下表 |
| `校勘文` | string | ✅ | 该句经文校勘文，含标点 |
| `今译` | string | ❌ | 校勘文的现代汉语翻译，以程俊英《诗经译注》为准。主要用于AI标注工作流的参考输入 |
| `注音` | string | ❌ | 校勘文的汉语拼音注音（含声调），以程俊英《诗经译注》为准。标点不标注，词间以空格分隔 |
| `注释` | array | ✅ | 该句的注释条目数组，见下表 |

### 篇目字段

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `书` | string | 典籍名称，如 `诗经` |
| `卷` | string | 大类，如 `国风`、`小雅`、`大雅`、`颂` |
| `篇` | string | 篇名，如 `关雎` |
| `序号` | integer ≥ 1 | 该句在篇内的顺序编号，从 1 起 |

### 注释条目（注释数组的每一项）

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `id` | string | ✅ | 句内局部编号，从 `n001` 开始，每句独立重置 |
| `anchor` | string | ✅ | 被注释的字、词或句，必须是 `校勘文`（不含标点）的连续子串 |
| `span` | [int, int] | ❌ | `anchor` 在 `校勘文` 中的字符偏移 `[start, end)`，从 0 起计，标点计入偏移。仅当同一 `anchor` 在 `校勘文` 中重复出现时填写 |
| `粒度` | string | ✅ | 注释粒度：`字`、`词`、`句` 三选一 |
| `文献id` | string | ✅ | 来源文献编号，对应 `source.json` 的顶层 key，如 `src001` |
| `注释类型` | string | ✅ | 注释类型，见下表 |
| `内容` | string | ✅ | 从源文献中节选的注释原文，不得意译或改写 |
| `注音_存疑` | boolean | ❌ | 该 anchor 的读音存在破读或版本争议时标记为 `true`，无争议时省略 |

### 注释类型枚举

这里的JSON键和值使用中文，是为了保留中文为本项目的主体性。若有任何因为字符串比较时编码一致性问题，请您谅解。

| 值 | 说明 |
| --- | --- |
| 训诂 | 字词本义解释（毛传） |
| 笺注 | 对前人注释的延展（郑笺） |
| 句义 | 整句语义解释 |
| 考证 | 历史文献依据 |
| 音韵 | 注音、反切、又读、通假 |
| 校勘 | 版本异文说明 |

## 目录结构

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

## 如何加入我们的工作？

详情请见: [WORKFLOW.zh.md](WORKFLOW.zh.md)

## 路线图

- [x] 完成周南录入
- [ ] 完成国风录入
- [ ] 完成诗经录入
- [ ] 推广至其他先秦典籍

## 致谢

此为贡献者名单，详情请见：[CONTRIBUTORS.zh.md](CONTRIBUTORS.zh.md)

受 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
及开源古籍社区启发。

## 引用

如需引用本数据集，请注明：

```text
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
