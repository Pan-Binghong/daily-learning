---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLZ5SVFA%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIDp3Q9x9pIqZbztnkCvwh4r%2F8bwFMvkxXwnO33uLRBDmAiEAtYIcsqfQ7mOR6jwi5Hf5bOS1wJeTjximCaY%2BhFC5PEwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDJ8QyKpI9pw38ActSrcA%2Blr%2BRGtPS7BJxZcmbLrSVhx16tbTR6gaXVmjCcRF4DOb6NZ4kfXZzqy5%2FJLChScTL6faA4fLYr2kSUkpRRAs2GKuxJzrItmgwpTDpLDKYZIR9dn3BXEhVePSCNYmrS6AOPd4fc3BlGThtp22YU5X6LnlhR7Q05H4JYGnZgaaY%2F%2BpprLY1BkmnKEvU6LwLSHFvDSER60JBNOgwRPosjmnYjtQZq9AK1iDjqllfXDQmV7jfRB9BMm4NE88fFbtm8wGy5EBuoJK72NnJeXAuRuSuF%2BcCRE16pQjKJfTNAV3VOIaSySnsWUAsxXrD3OBuhWtkDSeCkPieAjLk9uOeMPTPujZFDQMnVQX%2FtCFKXva5EwjLXLnYlISS1P5CQqhPryvMHMHZXuMTTQSDOjkjprtyXgxrBP04UcVCU3eeKYm7YeYtI3aW8FkOS4LUryOFRSc584ux1NJ22GFboW8L1y6LwAo4c1KOQ%2BDfCXjnYweA63weojqV6k3nvKJu%2BvO%2BQep%2FLBvsxaFRYmJAOA%2BeyXv5FyR3M7m%2BOFogrm77n6BQ1hRHka3JCTnUQ7%2Fq1rP%2BhxdPrgbwqwr%2B6d9wxo6rHSVQzjkqe3onbweN2ZnTdi7oR073ank%2FxgSXoNLu6gMLC%2F3c0GOqUBEhD3gJ099e%2BDnAtRau%2F5k6clHvvjoenHwMsuhQUOySL4Qs7KUW3eIiZbgPKIDb11ZUIqnippo3N%2BJILEUy2uUuQGkkINjOTc8Mfe%2FnYy8I%2FteWQYP3e5f5m9r7qIGCw2N3W8JIRwfyeYNoBkyWWLiFDGOgoJC1ay5dbf592TdTQPDrEkew8x6U%2FWnOpdc%2Fx2n9XZZvJYFKWO%2FSMkltivy%2Bbp7A5r&X-Amz-Signature=d85d1e50da6f558bc37713323022f7739b975f528807c88068b29c69ebc0cc8d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

