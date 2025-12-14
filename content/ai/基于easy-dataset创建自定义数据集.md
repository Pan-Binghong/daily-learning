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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ULMJO4Y%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC5kD1ez8CFwBOHdrDY2KzG4IZave%2FZysgnebcFmee6dgIhAPmqOHhjPrIWCrBHCkzlgCM%2FErdqSPHhvMx%2BbmXKSHIFKv8DCCsQABoMNjM3NDIzMTgzODA1Igyh3vRvvpcp12SgOFkq3AN7Dgur792Vah3ABChl8j9rnSOw8ByyJzpfI%2F09dTZ8sY9d56FLKFdhqwOWYyUwV6mQ5Prr5VYcLBx42HQhFv7rPoBF%2F22OCSvYBUWDv1pSiK1lR25F5KTVUmpXaROkqULNu1J%2FirHUIiz5T2yR48JUdcXIFQ5YvUrrOYlDpei%2Be8s4sZU8EJyZrWahLIimb3pNxolorTjEO8pAod8SDkeEDqf0tG31W5hOKAzIWxFvMhyG0mem%2F7e1aLDeeROdJuQFNZAuQLTmaIJxb5mzq2vyRPC2h4K3hkTI3ujV2f%2FnroeH5ydRCnt4XQkybi4TYKtdLuF082WRnc%2FRzrqH92rAEvjiH7xQRrvc6q6qXN2%2BcS9F34KfPqxwzaAkYeVODATUSy0bt%2BCvs5VMwODrg4HZGDw0SgBpHTIWhl2AYFni2XhV%2FigPjQyyHjhianJnLZRGCd9f1mDN4ikRCcWWaS74lLGHTEK6LMuZ1OQyTVaLB6X3NDAlFNj8uiagvg%2F04%2FZAfDuVgbnI%2Bq3Nnv0%2B%2FyPX8MoFjmJZueR7i5TJsZvR4Z13J7c%2Bk90jvyMq2MTPbr9QfyUq%2B5SAQ9SomQt1r69CkcG0Pf%2BEn3qLhD%2FrhZCgRzmfDJFXXh65Jbi1LDDxr%2FjJBjqkASckI5UtbCUg5XW%2Fitnr0h2U%2BhywpoWJSsu03JRimmXdXqhNxcOL4zBRCLPJKoVdIk4L%2Biu%2BV%2F77uXjD4CnJIG4EqVmisPSeQHeuoMqy8l2AtBOJwwv%2F1o7COxe330ayfDsO23bDtiM7b4nXw0QrpT4cqHG6Efwm3Yy9BucYYi6kLJ1%2FI81IwdNS6lBSQvq1bgttqQIcrD%2FvgYWw14MvCwj9hiKT&X-Amz-Signature=a863104a22027cc10ab27bb3df1a0fed0147ff483a3b1a346f5f66825408a1a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

