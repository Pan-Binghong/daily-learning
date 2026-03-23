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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMKRPSAP%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034550Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDtUnx1XfO7ByjP8ZhXT2k5yqJSHC%2FWLCh8LRZ0VjzdHAIhAJo0U1vZx8h3xee2K%2BL%2BpQab2cGKf3LQ7FY%2BxY5NchTaKv8DCHQQABoMNjM3NDIzMTgzODA1IgzaeYWmDumYISKwM2wq3AOn9jKer6ac4km%2BASNx4hwHrCHEyvKc6n21DlDiSQw0k%2BHqnN8o85cpWHr7PB3ACsWp69I%2BFIMcVWHEi8%2BGUexMxeP4IZTJUnlgP7g8lMKiax5qTL1IlsuLUj7%2FTPWLkO1BD3H8EwFrWGXmwPcx5%2ByLAVaMLvJbULdzFinntGlcJWG1CmGxBxxZEcBNHTyEydehe3Hw78tiK2tpbCz0eH1ruVQ3rWTp9rVRiUPmuJNpZRDIKtBF3%2BH4q%2Bo6YxEWefHl6uvGKRv3XnruusPhG1ADAmMN9Ydw0bSsfMs7qKvR8zGlSbcSdBuGnWSkfNVlslTcxFNvOuY%2Bl0%2BOX%2FJL%2FezDsWqWn99bGgEy87%2FS4rF3uFcFgnjFQ2brGhCjelB70P%2FMw6gKq3EdG8njOUAifV9fbIPrJimmWj5CFL64gbV3fXZqqvwChwaiiSUtK3tVeH%2BhoRrro10QUqFtXVSHCZT7XspCcpSKb7kMiaf06BPQnUshAF9UWZVoMbRq%2BfZxyrmAogOexM4XBX%2BhlEiS1I8t7%2FqH1VgOG%2FyHQ6x7akX3cD%2BmTVB5FhUb0E%2Fn9fX%2Fo9z1bzpKdBwbxx90bhVM1y3KyS%2B9uvmiKY06Y%2FqiAXqtPdT2TWMBWPwWk2O8rDDT44LOBjqkAQ1vRUT%2F4fiCJsh4IGodc7zW%2FrAURT2AjJ86CtefFt5%2BwkiJM%2Fd7WR01km5D8lHHZhOMTuIAhBGWB6NrYxwdwwHshG8TdaxD60jQc2Q8407Bm8X4sV7gEOCqqEG6a1chi327j4zYK%2FYwRz9Zil0Jp2tTS%2F9Qf0EL6GvYLdxlTPABWNbhg3KgRn3BEGbaQ3RBOtifxwaMMuaWHS%2FvtMMQi%2BOL%2Bw%2Be&X-Amz-Signature=63be4fb26bf0b6d663ffb512b50638f34c3fab9ba7219fe13f171995cc5b88a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

