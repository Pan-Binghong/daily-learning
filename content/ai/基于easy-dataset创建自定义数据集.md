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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XGJWZDF%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T034511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQD8Wv3y%2FyNKKnkrvmwXV%2FElv%2BWvgDFKpY0MhspNNRB5CQIhAM74Kxz0PCcbaSKydaycoY8BOKjrhoLO7zx7dQnRWUyaKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzLxrXGbUuoyDhmBlMq3AMHq1UT%2FrOSWprINzu096y%2FaPRvLFRDBxyEADa84LuBPG2nIPwmfmg%2BRm9cr1i3QKXDVDiMEPliMbxCyxX%2BseCfGjnmkdHksBMxx1LA4LKlVbhhKcv%2FDzWSKDNgsrhtcrjNgzOB2egemqxPf3hR%2BKI6HQPFz42SwCZJ0ujbzMQ3aTaefcaAbuZuIDTc6kG9nv6e%2FWcqT4kz%2FHQk6AiYBrc8Iox7X8ugMYWa5LqaEL5itb%2FMtzNFrN%2B1vZQJXKQlp%2Fhteysjx1lOstjOMHOEQobg9orjKgSRBTPvjPG5Zf70iG7Px96PXG4%2FFn0yBceIRs0uQn9cv%2BsdGoRXC8EUSHhlZBowWhXHXkizwa7Ohpm6oFEK0ZzAa0yTpdOHIphQMr34vtVO4Ig3D8StyNP%2FxqUDI%2FznJ6S0hU%2Bvg59wp7jul4Fb6y31scIRe2StIEUK5tYGAOt8CmHLPKjSYA6vbK2CQgYwEzy%2FJY6jgyjHsgFE4UzUsV3wRjwNZa16eT0iRYyV5eGJ%2FX70IhmhKeB3k6Y03rP3V6vhwzk8dUltAV84vgvCbQXkK82vAm%2FpFf6kK23pA7KpNZespRryr4qQeotiB%2BiITrnn58xhA%2Bz59Sz%2BK5JJp5PhdZMHq00SETDukrXMBjqkAWn2l48FvUV6i%2BZ7YwgGYFU6gq74Ps8GCXlYzNm5ijPf%2FUfqxMdUyeg81pRc0pCV9hODEveVI%2FyZQEOnXMn38IrIC3nHuD%2F0%2BWVkXM0mV2NTTfvjOpv9pJStyrBiJ2W%2B1MRwiu%2FFvVztNI%2Bfp59m5ciFbbsVgn40Z18VVcWq0t85YbxFSmIF9ZbfMAn0t7eiMg5sMrXNSGRyWxXDW%2FDIajxB9xOJ&X-Amz-Signature=72c594730bc67ec3e2cc528359f65de47ada0a545489793fe71e4ed476817fa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

