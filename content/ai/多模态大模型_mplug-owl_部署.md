---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MBW5TY6%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQC5S1XTnaJTdB9iAGoNBIsvMX0Ro55u%2Bhl80mBGV3rAQwIgRtWVkifaklgIHuMYKp%2BpeZiRw6pB2kEtdAUIqqQLbMkq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFIFxOkwerXsLp0PFyrcA8m6OP%2FzzlF7yI3h58fq%2BfWIRtb6Axb6P5CEh6n%2BqtLjMU5PaMQ4%2FG6idvgaiulm84gIdrV2Rqb9bfCO4N0PSHY76yCknnoyjrBPJFX0KQNLJA5Wj9b34M34u%2BtLTaikKGH6GZNOYWXDPQGIou3rAZRz9PS9avxxtgRo57BQA8ZmePn6L3Y8Zs5MVm5vLrSeT4yCd8RZwSNYKGDFaF%2Fxp9iajVlO%2Fj3%2FWY6MkdOqQnxjObf4k7Zym1KnEm7ItJiOOB%2Fx3IDjCf8kAhqVo%2F8YxsbAQv%2F5gbmBERJTik761FKjfpee%2BGOIrkTKYW7fJMN%2Fyk%2FfFkUE8YVVeNkRa9ftMjeAzqnGc%2BaWK4x3gwpIACzTIkJ7eZx4GGJaJdQxrqjLIgGHSwbAUcvjdNb0njeSawer7pRbfw3h1SNJJjmRTE%2FALLG%2BmCDOMrpO4pXDkVVusCwk4hXRSW0ntsE9qvzAuLUL64Yl2VNaa3yvoNIX05Xap3NgOUTk6xLwsd%2BT%2BtCl8VHx43khrmJ3MAv856SqtSGCVSTH0pe1NMpJSCqmg07YF%2BqZpeMkIh9nD0KefyDbsPJO4IPtXbU1bmaymI0uMjbZ6w6Vrz804frFGzGGtBPSBIsDelYN0cMsssKwMP2E1ssGOqUBZvzQ9MCPIsaw%2FqyYPEMLogA2XYqP%2Fkh8pYdQkBTTmOc0EXorKDdgTt8B1LNeuNtDj4ZvMUOhkFzvO80aibfwbR%2BjBE3A5eRYlr%2FKy1XUmHoGAbFkp47fm50ZQloGhYrUb9rMJcy4gH4XIJXTtwSPEH9QuI1nQ3DoWF1SVigFi3TKuqJu1f%2BqyeUMQrOezhJWk0lTrBUa9uSLC7K6yLOyhPvTbO%2By&X-Amz-Signature=3ba5be4f584b6eecb357add385869ade6c2fd32a01307b7110bd1c52a6568527&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MBW5TY6%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031244Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQC5S1XTnaJTdB9iAGoNBIsvMX0Ro55u%2Bhl80mBGV3rAQwIgRtWVkifaklgIHuMYKp%2BpeZiRw6pB2kEtdAUIqqQLbMkq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDFIFxOkwerXsLp0PFyrcA8m6OP%2FzzlF7yI3h58fq%2BfWIRtb6Axb6P5CEh6n%2BqtLjMU5PaMQ4%2FG6idvgaiulm84gIdrV2Rqb9bfCO4N0PSHY76yCknnoyjrBPJFX0KQNLJA5Wj9b34M34u%2BtLTaikKGH6GZNOYWXDPQGIou3rAZRz9PS9avxxtgRo57BQA8ZmePn6L3Y8Zs5MVm5vLrSeT4yCd8RZwSNYKGDFaF%2Fxp9iajVlO%2Fj3%2FWY6MkdOqQnxjObf4k7Zym1KnEm7ItJiOOB%2Fx3IDjCf8kAhqVo%2F8YxsbAQv%2F5gbmBERJTik761FKjfpee%2BGOIrkTKYW7fJMN%2Fyk%2FfFkUE8YVVeNkRa9ftMjeAzqnGc%2BaWK4x3gwpIACzTIkJ7eZx4GGJaJdQxrqjLIgGHSwbAUcvjdNb0njeSawer7pRbfw3h1SNJJjmRTE%2FALLG%2BmCDOMrpO4pXDkVVusCwk4hXRSW0ntsE9qvzAuLUL64Yl2VNaa3yvoNIX05Xap3NgOUTk6xLwsd%2BT%2BtCl8VHx43khrmJ3MAv856SqtSGCVSTH0pe1NMpJSCqmg07YF%2BqZpeMkIh9nD0KefyDbsPJO4IPtXbU1bmaymI0uMjbZ6w6Vrz804frFGzGGtBPSBIsDelYN0cMsssKwMP2E1ssGOqUBZvzQ9MCPIsaw%2FqyYPEMLogA2XYqP%2Fkh8pYdQkBTTmOc0EXorKDdgTt8B1LNeuNtDj4ZvMUOhkFzvO80aibfwbR%2BjBE3A5eRYlr%2FKy1XUmHoGAbFkp47fm50ZQloGhYrUb9rMJcy4gH4XIJXTtwSPEH9QuI1nQ3DoWF1SVigFi3TKuqJu1f%2BqyeUMQrOezhJWk0lTrBUa9uSLC7K6yLOyhPvTbO%2By&X-Amz-Signature=ed50f5a04c0da1890287ca0ea1dd95379f8ae00dcdfe0317516b2a1a4965c3c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

