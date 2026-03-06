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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TE5KAYTE%2F20260306%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260306T032837Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIC96r2WzETV7M%2BrWp32%2BWDnpn5ZaKVF93TGMM6Cl0Cc%2BAiEA6StDKf%2BM95saqPZJF6KHpPHKVRGtUTgAIFMmjtpCABkqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDClsapF%2FI0s49R%2FS%2ByrcA5zmHOuMYWA1VN0EFIOzt%2BEASpjY3nlGf%2FoCA3nqiil7AhCKozmngPMsfB6Hl%2F6HDrhNC0%2BVWpxtUHgoLNPixHOuxWl%2FHPmrnkqpb38VAnm2DkUvTe9WK1JHHU%2BgfVFjdBnKt41lw1gCNpL2NGWPT%2FfxlofeSO%2BLiPuypzFXaAPK1uCeK0xZiu69UVP%2BhVRHXGppYMqu04rT26FygvPE%2FYiXywQCIXG4ybwZKD30erC7UnPRZCp6nhSTN7XgyyTNkYeqBKT7WHdxtt3Pdsf4rSt2JFu7%2Fsh%2BkfTqQPf5ofGpTNXjEgqPEbQvkargooLaw6Y6p2RMBjTBxh9MRoYLDohc3hBH38117j1Uvo%2BfKV2K1usrAd3xTNQc964PHbwcilJ8jCoIl6R1kTObSeSU14CzRmU3jx8exlIQK%2BxWMTz1Pet053l3FSL3%2B5OqtaTrQWev5J%2BH5dCkVWvw9nnXLSrq25yjmIjlOs6ij3p%2F1EbUJz9dv6tHdjXrWC%2FrRJUt16jaam9SPZP4wBcbXi4B4bb4kOfNjfyrPJsP88b5D9yC4pr3Z9FZ5T47ZyqRg8Nbc8Mfa0OQxSk08zVvcUNLWVLQE%2B2vXHg%2FOJE6K%2B%2B1na2e3ArgryNyy4o2yP0AMIHQqM0GOqUBR1U4R%2ByppPHZHbWGuiUa2vQV6p9DT1ALYWekrCx2xyU5RY0IZFBdzDiYNg1X6ADwoa0C1WxYb0WQRUfcDNcvleHKAWHrwxAawPjkhawrOpRJ%2F993kLKgml91CAfkvqMgKET%2FQTk3o6bD0r7gO9H%2BwK1kokugZD%2BR5muREZvMW4e%2FjQZhkRJphTy%2BQQoMcNAfMRxbgrAxIImNUUx7lXAkrQcAU%2FZm&X-Amz-Signature=f4de2aa62cd6826099e55f74f076a2c9282c32d984774fe8f57311f4892b3bc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

