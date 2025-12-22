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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2PPM6RD%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQDcYYREhQ8Ig9gXjKBayArXbcx%2FqAzRC%2FCl2%2FEBoy%2FLbgIgSnys2c0U%2BwoySFsa3B2qfNBGJ%2F2eOhTAL2Vayd3wx0oqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLIX4eOKBxQCevUzyircA%2BTRhPtQA8z5ru7PbthP5LrFkD26qRHdADhY6fB%2FpP8UPTCxXYQ7KhNnN2orruNt%2B%2FtRsB7QVrDQWXZrzK2MqRkAoqUB1bK2vo0QmZy2tQZ3MCCEZdBYK256PPSOVEfKzKWbg9J%2BtNJFXBzh%2BEa1nZJ8ROXuZGhWgjYGEK%2F%2BdhOz5xg%2Fpsex8O2BbUPu1XRwcialUIk8Pv0P1VJx316zH%2BDqrwVuet1cpYrefmmmN4r2sNgeEjVBCJupJQamcA8pbBUaT4854ba4zVvl8H1D1LX1nLL1FttomRMfId7UqwH2jleWBbhvy%2Bq4VQfleLrUTEjxn0wgVoIeTVugVdTQK7mGXm1KPTxvAvCmg%2FyJGQFTksy31xYUmpqzpVkioSYTIqOy0IOlzAq3jEPLiuYf3B2MwT8n72u2Q1KdlDKOfiMEpiWRfEMuq6jFJyaPKha5qJw8VR2idBuG5ksaqTPkZ9OUhvgvb9D72KxigaWhJkt5wI5mSTfCjSlP1DSYUsL5ZIcEDOMJLRn77dg84VjYofJ%2BaPLcAlRl9P9Y%2Bnd11knPOdZpc42P1yPkN4FaUiBLDT3V4XTZ7ZxrdDEXYXwDABnzrcUkdCiCjTxSwNzCZAKNYmPDBOfKP8coTfMHMKflosoGOqUBlm8wJ5ShzAeAwXrxuiHgh0Z23VmvSIOL6B29Do24VKtv2F5pfkh1xXYUz8B4Uzs56jY%2Bex%2BWRWFks1C%2B6ejBuBcwB%2FzWDH0IMQpc4fokN2S96WfV9T1yY5mNpFAh2FKTecGVjruC5EnXQF%2FlT%2BhDrQZNlCA65jctZTnmDDG7l5UBHdVeqMbJSgVFX7NFAOJG%2BlK3VRdkngb2qsysuwTDDoZqmIvI&X-Amz-Signature=c2b63a742841760dba7557e959ec62292dbf151dca2c980e846ecc97988dcadb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

