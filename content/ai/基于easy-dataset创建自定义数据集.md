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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IH2RCFG%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIFdmkG4XMniZALeB5uwkJgDJ15H7jk%2F%2FX9uf4Wb2JJ6uAiEA2z60vDrw%2BFDZQyeQ4FOz3KMs4f%2BraOPbDgb%2FarEoA8wqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKijG%2FtLvU60T%2BY0PCrcAwylg3JA5DNucK6EpwQrjtW7C1gT9nUB%2Bn96NVUCCjaetEciiSesZBwaLTTRxAYwtqFbBIHTQoLz5zxCK3%2FPrn7KO4AWQsvcLJPRQRFwfSvay1jrtulV5BMCQ5xowcI2mL0ntmzpVny%2FKDBpVKh8Ayd%2BBrdChzlnDKMZak21eIJ0NZBT7VC0EGx3tFCSTjD0HO%2FcmD9bANyIEO7Mx0SJhoyILY9TjSnk2Aw2tSz%2FEVJTRsWeJmk9ULf4lMj%2FOrfs%2FS0PQQFfXt8K9X47h7Ga%2B7yQOR7KDKS%2BH18AuFMeIC%2BbgNFjngCLJ%2BA4rfOIuTbg0HaBhcj2WxWrZhfdh17%2Fcx5hrn58bX2FgXgg576ltmmIfXYaa6n5JbDZndHMlaljXvOFuTROplv8pwbVCj3%2BWrX7257meTJd2HcaFg3sUbn%2F3fBASU4Pd8xjUpMJ%2BRw843qD%2F15t2BXyDMmXQ1BPZmvLTudvDI0RuMNYPyeZi5j1CEpwBTwaH%2FiThr9Rf7P2OYgxpGoIct1Gh034ovBIN2c7oYb3egMQfCxt6maBn27T56XaoY8ev%2FN3ln98gEkeuxyCdIgWM1QUpTh%2FJ4JAntx9qFOFWlDUhn6N9fgsSQwGj6CYAHqYL5aM8wDSMJL4nMoGOqUBmrnJ%2BMK%2B40MnpGzHvQDOUkhhyOvzztcjkIYJIld%2BodXrhQwr0xL2t5V3RO7C5RIC8ylLX6%2Fe4FI3CUJ%2BxpTgxtQMmeJhGr4dGxwQCzy91m23xsIHfs3My3OVSzinWymB8HupTmqWp2uGl87qr%2FG46gEC%2Fv%2FT23Dm3Q0GiXBOJfSDSlZn0kPH7Oovve7vPdUhDbikH67zO6aZ%2BYbO8c9%2B2ME1b8Hj&X-Amz-Signature=22cd0e117bb5164d1fbc8bdd5603aa971e358013ec4cb162dc5cee141b7225bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

