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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BL4DNDA%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIHVNCACh2ScODdNna2A0SNGwB6MPV1w268Q6XsfsNPcZAiEA62VgA5Gf3Yul%2B62JneiiuauvynjThkqaaoepw3a07M8qiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq3CWRgS9RP0CpdpircA%2FY4NbKL3McKGOSBMrA0yql2olllcTe7wrHGUn05DiqXs2NlZ%2FpHP0srsJk5ADygA0PMIObendF2GEjBJBGEyiIDGLxfPq6%2Bpt6bt8ut09WkN0Kc2b96vxTGusxfm0YR6X4XpCyNhOx5fblfJBoJpqEhhxUiVpYLiKvYnQ%2BCfxnzzHW%2Frcj3VNPvZRsGJIqaMFy%2BSSXZ4FxKu48GCjmgXbv5zZl9FaORZOF27eClcgwcIE9E8AViUlVuMe%2B5DKl%2BRqTPO1Q6xTVQOijOh1itpSVj626NWo0tzGsluSV4XSzCbVIHmWAIf6qxnRwa5zjVOBlDN%2BDlZ0NLg0DL8OAHkZpG2ol5lRqaabhTJz9rrQz3vdbBygT0P9Fc05Ssjc7PQ5wztVUl6Qrze22mLOPOQsJO2jgwtSz5WOiLMbuZyILvWz78mGk8uiRDTUtka5TjOjFZzIkb%2BeOCF6jdl0rBD4guU%2FM0UE85luhhzoBQRYnQ%2Fzh7bB8vL6%2B8xjkWrRtEvgeugiorQ1PKCP1RTmTMhKv%2FnoyH7uYuhuATGuvldgD2%2B%2BcvRYMOqLtjRXUGZ2wkHtcUsuDd5v9V5E%2FsSHv7d%2B1%2Bh5DGKy0VHiY%2FzH%2FVYDqHbsIILxhzrPGqLGedMIbmosoGOqUBliU9LYN90XAIl1aAb9Jal82vH%2BL2aDD7RbL0LkcMFIyjh%2FxdPxCPHcDDfO30boXdieRrClSJ0RsXjYiQfX5x9w0MVP01%2F3sZKBVYmjAIF3PoJi%2BxNP1h23B2AQ4pBkJFN0AtRxhj7YN6YINvACuz9mccwT7KE1X22PFpINKQC6SjNl4tvYFKN3y8rn%2FELOnMVcugkKJT%2FoKa6YuzmXFKk%2Fgpf63z&X-Amz-Signature=69310c0394b85a683e8bcb0288feafcc7f4439f4758f03fda613489734036304&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BL4DNDA%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIHVNCACh2ScODdNna2A0SNGwB6MPV1w268Q6XsfsNPcZAiEA62VgA5Gf3Yul%2B62JneiiuauvynjThkqaaoepw3a07M8qiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDq3CWRgS9RP0CpdpircA%2FY4NbKL3McKGOSBMrA0yql2olllcTe7wrHGUn05DiqXs2NlZ%2FpHP0srsJk5ADygA0PMIObendF2GEjBJBGEyiIDGLxfPq6%2Bpt6bt8ut09WkN0Kc2b96vxTGusxfm0YR6X4XpCyNhOx5fblfJBoJpqEhhxUiVpYLiKvYnQ%2BCfxnzzHW%2Frcj3VNPvZRsGJIqaMFy%2BSSXZ4FxKu48GCjmgXbv5zZl9FaORZOF27eClcgwcIE9E8AViUlVuMe%2B5DKl%2BRqTPO1Q6xTVQOijOh1itpSVj626NWo0tzGsluSV4XSzCbVIHmWAIf6qxnRwa5zjVOBlDN%2BDlZ0NLg0DL8OAHkZpG2ol5lRqaabhTJz9rrQz3vdbBygT0P9Fc05Ssjc7PQ5wztVUl6Qrze22mLOPOQsJO2jgwtSz5WOiLMbuZyILvWz78mGk8uiRDTUtka5TjOjFZzIkb%2BeOCF6jdl0rBD4guU%2FM0UE85luhhzoBQRYnQ%2Fzh7bB8vL6%2B8xjkWrRtEvgeugiorQ1PKCP1RTmTMhKv%2FnoyH7uYuhuATGuvldgD2%2B%2BcvRYMOqLtjRXUGZ2wkHtcUsuDd5v9V5E%2FsSHv7d%2B1%2Bh5DGKy0VHiY%2FzH%2FVYDqHbsIILxhzrPGqLGedMIbmosoGOqUBliU9LYN90XAIl1aAb9Jal82vH%2BL2aDD7RbL0LkcMFIyjh%2FxdPxCPHcDDfO30boXdieRrClSJ0RsXjYiQfX5x9w0MVP01%2F3sZKBVYmjAIF3PoJi%2BxNP1h23B2AQ4pBkJFN0AtRxhj7YN6YINvACuz9mccwT7KE1X22PFpINKQC6SjNl4tvYFKN3y8rn%2FELOnMVcugkKJT%2FoKa6YuzmXFKk%2Fgpf63z&X-Amz-Signature=1bef538d604b01d20af75b5685c0cd22dde9fe5219a2ef5b83d26d22184f76a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

