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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KWDO6SD%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T025338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIEbm2Ggozd90JmVTp0pLgCai10vQdqQWSZO7FhFWVCo%2FAiBrNpFEbCVbZnz39GzXNPcM%2Bn4r6A9Hl%2BeW%2Busfpu0YBir%2FAwgZEAAaDDYzNzQyMzE4MzgwNSIMCxZuUlTPz%2Bc2zlQsKtwDI55s%2FKIxRpie8za0wU4AmfIgToIY962FTm5QCJYk1rh9Wvja6YoNdxhHgDJ5Mxte0nuKfeLvkJTqZPPy60QoMuhRZjTLB2K74iO%2Fa%2FrwarAEM7sjiTz2C0%2BGqSbOGNV4Sdix7CFBMuDIy5liQpaaNEMv3VQRXAQv%2Fsxq1SVTrFRNsfgft9U7jHJRcQH%2FtswtgQkWqwclf5EUulvZpQkx5wtVi2lu86Kppkvqn%2BY2emzDl%2BrWCw3xawvQNLRCwvjAhIVcdHspIqIJ4TNaqwSu8JOty%2B7zaMXnOIp%2Fuw5quG9VaOF%2F7XQctHqkwzYS6Im8jbzmffqv1r5kb5jxq7KSFKAJNAET3lvPTlH8XCJNsUlOAPYXYBGhRW%2FLf324xyJfTFUhmijRN4OSccknyVW%2Fe2KxiBeb7jVmVVekDbZ%2BWRTTq%2Fe8NC%2BtLW4%2BH2m9cE4rO24KWOStCrgodxXNrNWLreuKW1J2lQfNa0fSvd1qIjh7i0dqtkaFRjl0V0dQylOpzttZ790hCUWxR57pdKsxWD2c0Gi1Fwl4ftL75GmLM%2FgPiAT8jKwJ5kUYU%2FqoRVBNcxp7izpxT1Q3VzGIEzS2epIJl2Qzkle1nboZqHUzDDQfxVNmY7B%2FnsxR20kwweGsygY6pgHGbXkAwwnYPGX3uVZY8DcwYtO3mrvm29e%2FGVaB7Gxy71d9Uji%2BmwFKoSuuIIPwO3RpawTRHFGEn3%2B9I60pVCAaNyE5m3o%2BWIQ1S%2FzPSOhxcwtu40qhKIkMYn%2F2ujKPkVa0WiH2kQ1xSAWSYVCl3c7Te9R8e2RPwHsU12o04HVbQLsN8gVlIRGSh%2FGoKP6OcEdEQNsKf2Ah76t6kZ5dJ%2FbgxMUVvR3W&X-Amz-Signature=a6e6afb24d28ba6ac9c10ea6a2e74c4d24f9850eff50421be26cb58eed7374a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

