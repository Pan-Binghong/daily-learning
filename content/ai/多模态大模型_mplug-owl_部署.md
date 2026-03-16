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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466747S4XZQ%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDInsM9HFpmixXEgbITnuIuxoV9zmIImeALzRQ%2BU8%2F%2FGgIgVf0nlyiqLCrg%2BlVi9zmvdbXfOLAWZA9LSXP7wD4vYwcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD5Jpy%2B5PEZHwXJMoSrcA7ANdTVS3FKGcwU%2BLHzplnfBaI%2Fnk%2FsfnnOhfu1CplL%2FVAzJOMY39B9GcPDOEKw0ylgadAdk5mZ%2BjRi3NfHJq09PDuwCoY%2Fy5TMdjo7isYS%2BuwjA8CF9l73lqhIcfb%2FycPMbncaZqAv32lZ1LvSWOeC3OGmmnPbrO2ngn4qePc2aey5zo%2B3KrwKfQepvPMd3Kj%2BYIEuXP95p%2BEvD8zULvU7o9BXE4xqfdX8nTUaxlpDiO%2F5ThHmEmoCvyQhtPuwhOGv73U%2FiTKWGR%2BFjaRPjU81zeJMvHlCylDLPNlWdOrdFfVvty2Ud2YYhynoDZnAXxXrcINeUq8iY0nfo%2BmMBSFIuat8W7fEv2mG48Y6qrh18OVV7X6ZUmXbMRa0o5qb4DDpTUeOFiM0ukdQzrLJeI31hvGOtwqiYHfnJTuqWKlvgdHHqtsibZ12a%2BZyC28JxA22P%2BQByGC5%2Bt2%2B8TfZuF0a2rso6V%2BCwA0r%2BykHEshpGRx%2B9glSTO8x949%2BSGPBukYUreJ4wtE3bvF2%2BiQ4juqnICBxJzmhwIVgzvinbHHHDoHTcNXujKJF5QAsO4A8NtF0Eo2boz7OgYSNrloz2KgKNsafPbxXa%2B0GtnmT%2F6F2bhyZpae4eBqwGiCfqMKK%2F3c0GOqUBBm4pltBpRC%2B9BGzak9pAfaPUIakPkCw3FBS57h5XvVOwz1y8IMafXk%2B9v0P98QcFyj2SNlwNHgLS5ix%2BBRIkJGfM2o4M%2BSS0ZPDFcBvIslXHgodLtD1PbtYNtcGM3ZIcDgGqL8ywJQNE7k9bWNEbUMEmjgBBmyBV5jxQ1FlOCNEIxSJaUw1NNKalTEkbD6LLghir7RagUE4m26GcR3TWocYVlpBF&X-Amz-Signature=bc503872aa22cc08446a0cbca2ab1da69b651d947527f080e0ec6fc0a0cf2a8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466747S4XZQ%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDInsM9HFpmixXEgbITnuIuxoV9zmIImeALzRQ%2BU8%2F%2FGgIgVf0nlyiqLCrg%2BlVi9zmvdbXfOLAWZA9LSXP7wD4vYwcqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD5Jpy%2B5PEZHwXJMoSrcA7ANdTVS3FKGcwU%2BLHzplnfBaI%2Fnk%2FsfnnOhfu1CplL%2FVAzJOMY39B9GcPDOEKw0ylgadAdk5mZ%2BjRi3NfHJq09PDuwCoY%2Fy5TMdjo7isYS%2BuwjA8CF9l73lqhIcfb%2FycPMbncaZqAv32lZ1LvSWOeC3OGmmnPbrO2ngn4qePc2aey5zo%2B3KrwKfQepvPMd3Kj%2BYIEuXP95p%2BEvD8zULvU7o9BXE4xqfdX8nTUaxlpDiO%2F5ThHmEmoCvyQhtPuwhOGv73U%2FiTKWGR%2BFjaRPjU81zeJMvHlCylDLPNlWdOrdFfVvty2Ud2YYhynoDZnAXxXrcINeUq8iY0nfo%2BmMBSFIuat8W7fEv2mG48Y6qrh18OVV7X6ZUmXbMRa0o5qb4DDpTUeOFiM0ukdQzrLJeI31hvGOtwqiYHfnJTuqWKlvgdHHqtsibZ12a%2BZyC28JxA22P%2BQByGC5%2Bt2%2B8TfZuF0a2rso6V%2BCwA0r%2BykHEshpGRx%2B9glSTO8x949%2BSGPBukYUreJ4wtE3bvF2%2BiQ4juqnICBxJzmhwIVgzvinbHHHDoHTcNXujKJF5QAsO4A8NtF0Eo2boz7OgYSNrloz2KgKNsafPbxXa%2B0GtnmT%2F6F2bhyZpae4eBqwGiCfqMKK%2F3c0GOqUBBm4pltBpRC%2B9BGzak9pAfaPUIakPkCw3FBS57h5XvVOwz1y8IMafXk%2B9v0P98QcFyj2SNlwNHgLS5ix%2BBRIkJGfM2o4M%2BSS0ZPDFcBvIslXHgodLtD1PbtYNtcGM3ZIcDgGqL8ywJQNE7k9bWNEbUMEmjgBBmyBV5jxQ1FlOCNEIxSJaUw1NNKalTEkbD6LLghir7RagUE4m26GcR3TWocYVlpBF&X-Amz-Signature=a77793f89e96c6b77ec8bb58e039f175afc04b5a8941af4229dada8b8f999ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

