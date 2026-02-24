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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643F33JZE%2F20260224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260224T033747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQDZJtpHOWv375LsAFfOw7VJDszyKco0zfqelJ%2B10NiO%2BQIgN01UuAWs%2BIKIHN7gidZq0vxvSmvnXdcxP1hcQKI4hXcqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYYwHebI4MGSccM3SrcA1PdyDi8IOR29yMdSTwKZTfkOu6Ff41ilQbP1dW8TW94KwTfaxn07Lt01ypPSk%2F9oeOnOHEgcF0pRI%2F58mCrY3t%2BWGnsUORyHn4RsXCXZViVUP8CcSPgip4BpG9UoYhAdZQbLK1HZY4LjnwdPBpBM%2BAoveBoGkdiQHI32kxGnXThgSB5tlt5OuiWrFRAz2xjtHpju%2F%2BSV%2FFT5DTSmxf4k1jFWSG%2BGISCkFuFkxFMZtxha4%2BAmV6fN4aapWlE5%2FZZGf5pBz8EFLRlbRP%2FpQfHpCeb30mr1OCR3iAMTF3uJFKpBfMMs6T9SyCO29FtEHoAz%2F%2Fozc9oqbGsSPKITkWhOCxVeS3o6r9oJM2RphTgbGGT1sD0H2NW35hRfbAjVP91YlM9z16EOkyXs0FGzkMBe31wJVoHXyvH0Gg8gVO%2BjXS%2FWOEtaKz5SIdBt3k%2F2efII4VQdv%2BfUj2V6Xit1GldEvTHj8Zvj%2Fiojgq0j3WkbVnp5q9rpit%2BTyasOknN24WeSEVPT8lYvVmyFBoWTgWSB%2FIxq2dkQXqdrKBOMGax5uklnK4rOlB6gTo%2BU0Cm5ndpJgJWmHbkAXITPW5yoZeeOu%2BLxm9qenW3CklfYCnHYG01bIR6CaZdQ8IlFi2rMJO19MwGOqUBAoBenAIrmSXFSLbT9ynr3Ds1ME9ggCPIetASlkZYMzYwwVJLxnga0eRUnNUa2UQIWlG9haO388Vj1NnJuGHRyJh9Jk7Nh6cuykCJqWpKm%2FYUQ7t0GS5Q7gBXL4y8t5IY8f3sfGttkUnhW2ZZcAv9dArtJ%2BYJO1GE6SCZAheJyU%2FckPq1kATHaAMacrrFtZdI3%2BTpJxZ5VjoaHjV2u92Fkie2uIQH&X-Amz-Signature=d7bba0e07c8c5019136d01deb2b36c06309eb2715472f0709e5a2cb2eb82e70a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

