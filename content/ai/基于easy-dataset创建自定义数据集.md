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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SPOYYSVN%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025349Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDdjKZhMGfVlHXZSPN77DoheqsJQh5eox%2FzrWRnmhf8%2BAiA9vdIGo4rYlZVTdbhAcX5SpHVQJ9nwsNflevdF6rr70SqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMclkYvwcDaJOL2BKKKtwD2irOzf3AdaTp%2F9SxjNBukdXMfTIV8IyBhZF1lsNWUOQbxLaUfHLGYTRSJIgtxCfEB1isVQ33DgzO3T6vO3uM95spYAmVRKxlD%2FBX4sLkmonB9pRIEcgMvFaStIZrUAnKnMbt3OLbw8%2Fqf84zHJqftGMZ9SoFI3poWocJRzrGe%2BOJ3ivKzdh0kBijBAYcnB%2BCLs90KUl%2Bvp7hiq%2FclIuOwWcYtNgzqRx%2FjeMznz75fNm6nnYzf85LFNLzrwvMoLEuA%2FA%2FoRjt4Gfb95UyJU6hdI9oGpiDQCdqQRAhSKs2czIr1dF1zNMnjyL0eGAbEV2FLUfr7S7lsdGmkHNMA7zuANXZ4yy6icfM4MbeGHBe4QStcqHefs6BNjFn039gO9Z2KOn%2BrbNFbfKSUDWZBl%2Bj0z8eyFITx%2F4yzfBkQYY%2FeTefH9FL91MeQwtcMzXQJzSfiC%2BpHRE5%2FyESsOwsKm%2Fom7hMa5pLBL8G9lAY1l7aELS0SyiaiR2A5JLKIAo9x8KnGAL5t3co8tmnSRVh7nchP4IYR1LKddJqW2s3bn1R1Xe0yYxZJ3P9nWcvd2go3DsOO%2Ftfen3qoYKCDpWf%2BWh%2F6Hs98BhXXYIdLRnQmDbufsnqjhTCnT%2FnzldJ%2BoIwkfmGywY6pgH4wtihijc%2FETtpGnvaAFalMBm71KRdfn2XDZSZnKo6UHlazqxTLz%2B03nh1m2onFeudmGavuLRZJ%2BlSxr0f%2FpeMn%2BbuS%2FfInbBkQcRfsfyHWpHB%2F%2F%2BFk%2B1B3peh0V1Jx24alV5Tya7%2Bnco94XeEDMSOPOrpNmFyeKzTCbSbg0Q7NapL2Ys6XeVEWnR%2B%2BPwWGt52G7IXPFWQuK%2BMVBxvb25JZYb%2BZI4f&X-Amz-Signature=21f97fdb83a876b4b55300481fe69b571069a2df1509e64df4eac66075065603&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

