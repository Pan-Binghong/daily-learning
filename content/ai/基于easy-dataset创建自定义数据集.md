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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJLFOVEZ%2F20260429%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260429T043154Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCID4mVuLJHIlntV98MsildBxK2Yz4Tkdyz7zMBgHcfAJpAiA7rtZLWwf6vQQcFwkr5dPYQefMxgyyzfWCi2%2Bm0ZcmfyqIBAju%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMb1o9ftO0hQ%2BHmy8HKtwDF1wGLjR%2FJyugeS%2F9bFTp0DKlAU2mmR%2FXPv64kkolhi%2BB0SjH%2BkRjeevSa1sLfK0ikFsCGMT1hfbPtWpHlaG6bnQGyqgRMVw9QEfPLPfMsA%2FeetK8kH4fDgKlEcgmWpmDq%2BRIAYGR%2FXEj%2Fa8m3O5peNh6svxKsOX1PTOwMOxCBKt5%2B3chVKqlLhVILqMVe1WoRLXdB%2B24vcAhjh64%2BwhGlSZFJCX4U3A2WKPU5r7E3UrM1ZhVsoFn2XmqooLqtvnPchPCkmaWiAFfKPBg%2FCGrCxhUrSN%2B9Bh78RH5PfxISOrv201GpvPPkslR5QuTVyEYzkhtN0v6yqC5Yy6E%2F1AoFHSZf%2BjluvGCVsWk1nFczJiEp8T2urqk8nLsiCc9QhS95dhtgI8slaqhvG1MFtxRIyIMASGpAWLvr%2FzaZkryCFapX2JSYmp62BuGQZGSEHT%2BDQyR4A1K7iqbX38dCOy3sUiJOnBuBKu8PI8OP76C4L7scusmLAXeBwlBVsvCFl21dtKnT2WLXSJ5ZtR4DuObhRb%2FlXT2rkmuiStMIhu%2FiCvlerc%2FX4lSLjg3L%2FH2daCsB0j6BGPxsVksgsnzNdlaVCYCzEO9Na%2FSoYU6u%2FbNE2tR5CFBS%2FujlZFbDGAwkpHGzwY6pgGnB%2FwfeRjTahq5HLFUjTkUcOE0sQlPOgeQVKPesbCGqLyjfiHfFx0pe3NMUuz8chCYxW7PyRp%2FD6En0H4kJp2KSIcBrWxLSUBruKZj4wxPig75IpbGOqiE2Ed%2FZIgEgtxDPH1LRZ7gnTWNd6NMRv1LkYedBvC4ihjM6zQNmUEK69lXuBunhSpnW7E5LIDDuYSqzfzk2VRtSt9ldRckzHhmsdwPsg7h&X-Amz-Signature=c7d0441d2d2181e71d3fccab18f7ed62f44cff337379d901c61d3905f5dbe169&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

