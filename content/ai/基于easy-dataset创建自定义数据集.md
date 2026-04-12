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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PI4AF5%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuGjfqkIOnA0Bc5kGxqE0ts%2FS9g93q9x%2FXWmfmLMkTRgIhANR4%2Frz5lFj7goq0%2BdiUUxuI6dBswrZQJCWsha2w2CFnKv8DCFQQABoMNjM3NDIzMTgzODA1IgwPJOuILVGg7dbRn9Uq3ANkSQvSAtGt8o1X9bZqLMmTbkEJaUEqhO9KY3LQZE2BcuFgdezyJxbTHjNX02yO%2B%2FQyNoHYUzbulxXmDBH3i75JDdj3D6uH6ojyTOd%2FgzrB3dgLTXKp7RfqCvO4yqFG0pkUq1TmIx78xVsoOh27ZO1PPHn9ib7zFaomNVEDb4pdigRCHbOUHRtxbgaZRzJM8LhGaKMVxawxP%2BtQyPJI29I%2B7PmAMEgLatWtgUoD6mlseQ2YaWCpTVOZhrsYTQG%2F42MpHZiFraB1aMQ6J3NR76uyIWTSSeqG41Nv8SiX3WHFLeamIi0oxjA%2FTwJB4B%2BpraOWjhPHZrLUgKzomAAgmY6M5T8aO%2FpMWsT9eB0O3LvNe%2BtTUtgaAcF29GM70tMfxJnl5lSqHKhCiaQx7OipjTeC9LeoR8XSdo9p9tnAn8AafauAm0xOFmuH3ty%2BemTAdRIiD%2FSLJYEzNepQyHHIzkqhuEuBvNxfm%2Fsj%2F%2FvfAqam70bwv3cZhvNsTvKYu%2FMMajgJNlod67jflx%2FM1uLOsa3jV%2BkZnnwEfM7Rm5ayWy7NeMPzu2d10eF8%2F7LomyJK7jxoOaScVi71aPpHillYvYPGoi2WUaNQnMs9aDiJb%2FJC0c3SVAIp9UXw9mhf4TC4iezOBjqkAasfbgJQMD86VHvDR8UNAROtHx080d2NyzziaCftCdf8gkZybod%2BTQAeuiHuJ20pIAAdPGAUBE341PV3ru1AI4ONcaoQZrgoLfvJC%2BRz%2FJzDBXiOmXbGK404UXffv24g9cCsTl1jYRSO0kTLOQRVzL2yB1ECfGM2B3QlNbQuj70IltGnduPNPHgW2n%2BaYyRiwdgTuqVrYbSqtzrJxXAFvlcC9zta&X-Amz-Signature=4f538affa8b36509984ece529d3627c130ba1c7a59dbcd80dca6dec7053e5518&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

