# CET-6 Review Guide（六级复习指南）

个人备考资料：一篇用 LaTeX（ctex + Fandol 字体）排版的 CET-6 复习指南，包含

- 核心词汇与释义（按词性整理的高频词、易混词、固定搭配、词缀速查）
- 写译话题分类词汇与短语（十大话题 + 通用句式）
- 真题分类汇编（写作 / 翻译 / 选词填空 / 阅读 / 听力，题目以英文原文呈现，汉译英保留中文原文）
- 分题型解题策略、十周备考计划与资料来源

## 编译

需要 [tectonic](https://tectonic-typesetting.github.io/)（本地已安装，Tectonic 0.17 已测试通过）：

```bash
cd CET6-Review-Guide
tectonic -X compile cet6_review.tex
```

首次编译会自动下载所需宏包与 Fandol 字体（需联网）。产物为 `cet6_review.pdf`。

## 文件结构

```
cet6_review.tex                     主文件（宏包、样式、章节组织）
sections/00_front.tex               封面与使用说明
sections/01_overview.tex            第 1 章 考试概况
sections/02_vocabulary.tex          第 2 章 核心词汇与释义
sections/03_topics.tex              第 3 章 写译话题分类词汇与短语
sections/04a_writing.tex            第 4 章（上）写作真题（纯英文）
sections/04b_translation.tex        第 4 章（中）翻译真题
sections/04c_cloze_reading_listening.tex  第 4 章（下）选词填空·阅读·听力（纯英文）
sections/05_strategy.tex            第 5 章 分题型解题策略
sections/06_plan.tex                第 6 章 备考计划
sections/99_references.tex          第 7 章 参考资料
```

## 说明

- 真题题目、话题与词汇线索整理自公开网络资料，出处见文档第 7 章；仅用于个人备考练习。
- 参考译文、范文和模板为自编内容，不代表官方答案。
- 更新真题时，第 4 章各 `sections/04*.tex` 文件按年份增补条目即可，主文件无需改动。
