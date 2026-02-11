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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD4JSWP3%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIGexl229UAcV4OgvcpwUiHr%2FY%2FousQqdMLyokDr43rrNAh9XEgHPeYiQva4On3spDFXuVMTDWNPmSbQc1nO1kFdHKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSMUs1WdzHnGIG5zYq3AN6hlMhB9IfKco5wE0Vqphq6mhm%2Ftze%2Fgl7knjUJU24Cyzp2d%2FUAIVqcP1BJOwrcNqz9sdC2uFQsecJ65p6cxXh3DlC5r%2BVKBmW2Af6xGruEYpyLebCftLUtgGadP90slbECsVTPcyrDwNqPrlspfU96oYdL6ioVIWhLUG08ovVvBh5Yz0qWWsMWvky2vG%2BddbjBLM%2Bq7u9E94v7HrCTLp%2BXoUjgwGgo3Cgx8foJ%2FuUL44b7btvbilCX2KwcMJLHIJ6PueIcDFnoPdcoNJiUTFa1HLionmdUV5qxe4jPDhJp4bmGGZe%2BeVm9bqy0jH4pa2awH7qL71G959EAfQ2aN%2B%2Fuka5%2FDp2e%2BZjAoYVShTOVAiZpW4VlG8zZOeDqL%2FDsf9ZrVXaODAiy9vpSYtC2ajRyc5H3UjQg9%2FH5M%2F%2BGLaVyYaLyCndGy2C3cknmCoxfQozq7sAcn4c5tHoi7%2Bdno3Cs2xQjZSr0QyAGRXHtYWB4xxy35hlF%2FOarqMYqEzU7%2FMnP%2FATE8p8jIozrztejpmBPZuENdU6%2F5lbudXsdWINTbaw1kc0GPYnZJ18ciCkoWacZr56qMQu1M1XyOHKUjyzgBUZ%2BxlZZlqArtI03QXoyByuX7ZVcYXBxgPztzCpzK%2FMBjqnASCVE%2Fz94yIRZ7Cp62Z8s8c5j2x6ijMYgUltKCkmTk3wC43bg8HX0bHYlY46LLLK7f88Xoz9R%2BZDG0%2FzZXKG1w3yrRqyU090Q6QsmpuEBh6krK%2BxKSr0D63jLU447mDClwKFWkJ%2BahfD5bc7g7iFc5xa%2F8GFHZrrLyIYmKwSq6ZMZrV90GgZ7UxmTrxx9qytE3igQLsNxh7ZQjc5Y49hycuB40ghw7hN&X-Amz-Signature=fcc17d267306046322dc92895a7022a2e8fcd0336c741e0ca8efa4de1342119b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD4JSWP3%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCIGexl229UAcV4OgvcpwUiHr%2FY%2FousQqdMLyokDr43rrNAh9XEgHPeYiQva4On3spDFXuVMTDWNPmSbQc1nO1kFdHKogECLP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwSMUs1WdzHnGIG5zYq3AN6hlMhB9IfKco5wE0Vqphq6mhm%2Ftze%2Fgl7knjUJU24Cyzp2d%2FUAIVqcP1BJOwrcNqz9sdC2uFQsecJ65p6cxXh3DlC5r%2BVKBmW2Af6xGruEYpyLebCftLUtgGadP90slbECsVTPcyrDwNqPrlspfU96oYdL6ioVIWhLUG08ovVvBh5Yz0qWWsMWvky2vG%2BddbjBLM%2Bq7u9E94v7HrCTLp%2BXoUjgwGgo3Cgx8foJ%2FuUL44b7btvbilCX2KwcMJLHIJ6PueIcDFnoPdcoNJiUTFa1HLionmdUV5qxe4jPDhJp4bmGGZe%2BeVm9bqy0jH4pa2awH7qL71G959EAfQ2aN%2B%2Fuka5%2FDp2e%2BZjAoYVShTOVAiZpW4VlG8zZOeDqL%2FDsf9ZrVXaODAiy9vpSYtC2ajRyc5H3UjQg9%2FH5M%2F%2BGLaVyYaLyCndGy2C3cknmCoxfQozq7sAcn4c5tHoi7%2Bdno3Cs2xQjZSr0QyAGRXHtYWB4xxy35hlF%2FOarqMYqEzU7%2FMnP%2FATE8p8jIozrztejpmBPZuENdU6%2F5lbudXsdWINTbaw1kc0GPYnZJ18ciCkoWacZr56qMQu1M1XyOHKUjyzgBUZ%2BxlZZlqArtI03QXoyByuX7ZVcYXBxgPztzCpzK%2FMBjqnASCVE%2Fz94yIRZ7Cp62Z8s8c5j2x6ijMYgUltKCkmTk3wC43bg8HX0bHYlY46LLLK7f88Xoz9R%2BZDG0%2FzZXKG1w3yrRqyU090Q6QsmpuEBh6krK%2BxKSr0D63jLU447mDClwKFWkJ%2BahfD5bc7g7iFc5xa%2F8GFHZrrLyIYmKwSq6ZMZrV90GgZ7UxmTrxx9qytE3igQLsNxh7ZQjc5Y49hycuB40ghw7hN&X-Amz-Signature=f329c347aeb4d0179f7b527d881eabcd52127d8a05874232b96f853f40be1c4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

