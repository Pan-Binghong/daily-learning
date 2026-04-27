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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQWPCSUP%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGt5laKL4x3tPOIH0IRr96PdcBAGH93NdRZ14MWP2c93AiEAnGPG0f7bZs0izWz9uG%2Bct6DWBrXFsusL%2BfbigZj5318qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPnKYEbzdR439U%2BZSCrcA9jD2gCoX5SCy7qRYE0Jz3i99m3Dx9%2B0P%2FMtQcLi9qov%2FfP9NtM%2F6hP5lUlHCXodGtIK6s4BBzo6XXrVfjZyXtGbHr9g90KrCG%2FBC5Qd07IHY1BwzIEH3V9fMHRXPkY30KYu3PUbjaSVCUjYSxZWuLdMSmepdie4GVLaO1KcSaIl%2FoaCUV%2B8rCCA7Q56fuU6U3DftomzJWWwHUAAqEbs32uv4b1SZdhnrI0gLOK6WpQuK9Gqz%2F4EMFwDZ4k%2FLt%2FdaAipLkOhnT9Ru1V%2BXjEAc6Koq8rBIYBrGnw5oWv%2FCeiMAC99aRKwEdCBUPEq0uW2lRG3mehWD2zHSN0SjnkK55Tea0R6YwYUSpORQC4seo0n4bSi2o9yJDI2Dnt9W%2B5yN6E%2F9PMQ9u%2FBF2wkhjYFy9iDZh3vKY5tVCz7MyT%2FJ3iH3BjRIBW8%2F%2BcktQqxMChfw%2Fh2uUkitflLOvziV667LrM8rG7b9sXyY%2B%2BfdBoQ3phFXuP4W2njdvIfaBDIz7wr17W%2BImk9y%2B9lrQEdZSENMyxFMLIKllgC7NQKeS%2BIOop%2FUz%2Bd%2FgRkUozG01Rdhc2oKGeZHbZ9%2BZxpVRK1RNLzkPhUAh8vzKNEAaX%2F8heakLfPRVz9aIhtE8YV7MvKMJu1u88GOqUBDF8FJ1YrXM%2BcUBOH3dRx%2B3TJ4NsIhIVg3X98tcknd4MV1r2zzNomM5uMB1CKPalHrszhRoHdUuo9bCjIME9ubQ7sWd7d2CHpP4qRmr7T8L6bBSu83hV2FOD%2BQhp4%2B9ke1z7IS511bm%2B%2BcpqSQNJK%2Bc03zkypT7FpOmxNLdw683HqnCC93TqmHNEUlgw4KJY1JiKoDKFa%2FQ9vVyrUU25eEwZ0Z5G1&X-Amz-Signature=e33e51dada65e3fc75b090b62275d036bb9f4b443483cdfd7cf9406669ac1f81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

