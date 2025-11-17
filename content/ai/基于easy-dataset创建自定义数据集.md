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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWEWLFED%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCoL%2B7WzWSTvvcxplIKyPZ1GRM3fHDepYIk8weN55ArtAIgUx3ETz%2BmDRkQZmCk8%2FCDzXR8x%2Fp2cgfsblriaDD%2Ba04qiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBYeDBcYIQC0ayDvrCrcA1W4sYXmwZzg7TWc6v7GtZwt5wgNJEfiGMLwMiQfJZ1Yd8J7eJ48PC2Sd23%2F9ZCFFqD26F%2FTuQYuh0Jw0%2BZxTs80IPrmw6FMD4M2nXd6Ei2FVkTTg%2F%2BYrXCM3L5Z53VQ8o%2Blw8iej9y2ynK4ni6StYcMSUJynFNGn67b7dCmkKHWiEsP2k2TCs00RpTZ4hinXSMsTUTYGAk9qIVfXd7O0INHFuDpK1ZOWywTwK6eiLq%2FZnOl4e3bua8Y7%2FfyEPEl2cHLgo3CxER7rk12a1LmVTtg0I0rvMQDZsgWta1T3aYsdGt0%2BHejzjOZXHM4QLQ4tAOrVDmrYxfDjo6faRGDZKiqSyuqukyOf9R9%2Fo6C%2BeqwGp9qLyn3w2loNcXGLr67Xrxnsn%2By0HQY18%2FAqstjwaUmidTMm4faDZ8urMgzOWvmwoPShUBLXBp1sCI%2FgQe8SW5XzBcLD%2BIXzZmNCOZ52%2BZNDKHsVzI%2FeHYsXHi0DlJxWVACVkOkG0enqn%2BO7kBEqlHBIR13q4gyJ1YKHZ2N%2BY27Y7%2Fe5xFjdttnxMcVc9cdIo2S%2BvXu5lz2qXPrB57buyp08BrGNkQkIx3Nuif0J2rthG63IGUohC1ZrebgTUy8DDwvY9pVoz7Me2fNMOCC6sgGOqUBkzT59UrbXDTxz15tkZ89bYE3m2JrMIo6iOrEQvwpeKY96Hpx3E60nYVahvr7lBU6EidBHF7FOxfpQBZ803vKvHHqgR1wLngAwm9VV7WTE4wwQAeb0getX8T%2F3uz1szXsGPenEvZom6JdiwU4O%2F0b2AQHM5sypClD0fWW8w1rywfIJwkPH6EFsYKEXxUDIpl91WbyQGuCbrfejgY2Ucfl66B0MHnC&X-Amz-Signature=e308fff15b71fe76cf5c93abe838cb045083be091fb874ec1e6b64d4b748f322&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

