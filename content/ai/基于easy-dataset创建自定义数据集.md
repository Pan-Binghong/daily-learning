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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5GJLSCF%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043537Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCjsT8QqHIOz2w3jAaZDpddogBn1Fxj0ousJVhslRoJPQIhAP3K0Fsyl1zcSFpY28pXeHzBUF7IEF63CWT0jUvDxhuGKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw3BTM6sf5YOIN4Lg0q3AOZuNwiVV3Fpa%2BZNrI5YfMIaje6U8FLmWYAMB7DPokajK4spY3rIgvjCqS1wHN1DWlqg09rn%2FgSjJaIUbnVl%2FAmjp2hL4JHgVohdHKrCtXhhNTO4s1pR1baAAFNvSM7rjLc2fEGo3%2BYL2KI1XiSGCQcz17XmCr8gXsjm7vUUQjxFVtTKcd3qpmJOjdxU7DlkcPoJJjysqWShDKOtTHA2Zeh%2Ft76NSxX2kcifKTGqsZMk0L2%2FGGkHFkKVu7MTkunFVn3j5TcA5S6u4PMYa%2BsELoOBirxcv2tO%2Fh43Va9A8VbAdcr6KoNQvKcays5hST5aySM8aFkqu0vbPq%2BO%2FjKxwTp3fkAj5dAegiOmCB%2BeF1jUkeaOqeyyLJiSEkDU4hPzRa%2FOzENvIjjQJodU6z46Gr4FaCo0YXkwoydINsAunn%2Fa4fVspDBkRRjtRTKfm5vySsiFUnyvbiOCvEgQMdos5S65dqQQgNXUtabcS8WKwxZvN%2FlhF6PhhXS4%2FZy7ub%2FZCb6S3%2FW%2BEa8lV9uxcQUk6WmPDiK9JrQC2oigNOUlYTVrPj0V6p%2B2kWqLiuOqJc893kI3xDnNo6M1w%2B6FNQI6%2BF9fL4LSK7OzZ2pUXwXTdHKpqUidNijbDwVIAGYcTCh7sDPBjqkAQ0%2F%2BbA0qU6bQ%2FotumknuunVMhwt1E%2FrN%2Fc9PE5yEOlv1ONOC3PRCR7EGe3i%2B%2FpybBFWgj8d1nSsxcE%2F1yuH9DiDxyjAiSoNyH2zXRVQkAvAnUELfMsRfsC7Z%2FB%2FqNi%2FSEzFI14de2HQactH0Dha7cqZCi2Ubvl62a1HJGUBRFYen5Vh0TpNsreFNkyX22vZnvrPtDcV5Ig748CTEPYZN7XlXbIm&X-Amz-Signature=466293db4292d569e2b6f824647d05205c64de4f16aebfe202fd3f84d33d3c60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

