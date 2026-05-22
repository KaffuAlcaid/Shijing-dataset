# Shijing-dataset

English | [中文版](README.zh.md)

《诗经》校注结构化数据集 | A Structured Annotation Dataset for the Book of Songs

## 项目简介

当前AI在中文古典文献领域能力薄弱，根本原因在于训练语料中几乎只有原文，
训诂、笺注等注释层基本缺失。

本项目以《诗经》为起点，将历代校注整理为结构化JSON数据集，
探索一套可复用于其他古籍的标注方案。抛砖引玉，希望以后有人
能把这套方法推广到更多古籍上去。

## 许可证

本数据集以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 协议开源。
使用须注明来源。

## 数据格式

每个句子对应一个JSON对象：

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

文献信息统一存放于 `sources.json`：

​```json
{
  "src001": {
    "文献名": "毛诗传",
    "作者": "毛亨",
    "朝代": "西汉"
  }
}
​```

### 注释类型枚举

| 值 | 说明 |
|---|---|
| 训诂 | 字词本义解释 |
| 笺注 | 对前人注释的延展 |
| 句义 | 整句语义解释 |
| 考证 | 历史文献依据 |
| 音韵 | 注音、反切、通假 |
| 校勘 | 版本异文说明 |

## 目录结构

​```
Shijing-dataset/
├── README.md
├── README.zh.md
├── LICENSE
├── sources.json
├── schema/
│   └── schema.json
├── data/
│   ├── guofeng/          # 国风
│   ├── xiaoya/           # 小雅
│   ├── daya/             # 大雅
│   └── song/             # 颂
└── tools/
    └── validate.py       # 数据校验脚本
​```

## 路线图

- [ ] 完成国风原文录入
- [ ] 完成国风毛传注释
- [ ] 完成国风郑笺注释
- [ ] 推广至其他先秦典籍

## 致谢

受 [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)
及开源古籍社区启发。

---

*往大了说是让AI更好地理解人类文明，往小了说是青史留名。*