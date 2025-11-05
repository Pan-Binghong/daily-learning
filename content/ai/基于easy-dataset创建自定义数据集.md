---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DPD2GG6%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGTBE9oXxkuCmLof1k%2FCvLRxSh7NNE2FF%2FIUQMxDJ2%2BbAiEAiEWW2NZuKAfUXeUJd8iQGBkX01eTxvcWi%2BY7xsNjpZYqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGKIIvINqJPS%2F9b9iCrcA8hXnRnODfqab9R5WfS9BObx9l%2BPxQB%2FiAklXezBBmnG58IcsGdf6AsMnU2adkAkurS29uSq4KzlKTS4WQWwHzJ%2FmDv1UgzBKQFlSrKa1QEZ0CbQjOQKPTgmaCffzqe0SwgmfMwp7jfqFFP3%2Bydse45WEVTODw8eYvZ5lWAY%2FqnbrnftH1sVP7RddQIousxv5yAO0CG4xOH%2BgSJiqkHuTG%2BfQS64VZCxjHy3q93ER7rnZ0pXkrU%2B3v3oxIH8Ud8kAJZi5DCMgvIoDa5xoCnXne3hKENOQuWt%2BlA1FEOkx0p6MbJM%2BFVmrC%2BnDf%2FhMxGObq3Cyl0Dko5T5oqbTU4GdKxUF58xz0HRpviMFez0w0soqpVSNdYEm841YmCSYP%2BD65KNjB7zld2u8xEbPn9OY2Isjo2Yo9baNqeLJmqjd%2BWjKsz5nCbmoL7silbxbyfCLoKsQjq8uxcixKWlNnwiiXoBlN%2BqNFNFepPgTi2EutLo2A5IJ0RLpkSkc4cGvGnqfzBdi%2BlFwOVYjSwqJuGgGuce9ow%2FcskWLaTFwhjbWBipRrceEa0HCH0BaS4Mqwh91LHgMfZ5BeGjHZ68iv4LcJNHPB2oPqK7K4cArFsZlVpiBursu%2FrAb4LcJWH%2BMNmirMgGOqUBycIqt2M9s09%2FFp0kNLxfdqyIiu5nc4aKvpLcrcFk3SVYXFf%2BixMpb0dQD6HWKNEvQuLm4y4phS%2B869Qe6FGWk45FdxTj36SnpECF%2FMb2YvLS0NIZxjsZZm6r6d1b6mjoDCydjOt8QCeDqR6keXng9JRDPTzRrFhxwKXJFQtmaptLLZZhmQ03wwyFeWjnxwlbwECgA3rWGbQDp7qBNkLqQJLtu%2BJ4&X-Amz-Signature=1833fefb9868c6efdcd6a19b349ee4581354706ad0937db25286b6f1b63f61cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

