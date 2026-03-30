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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTVIWEKQ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDCBHbD78nAncN0QONMoXw5k7pZEFY1Hx8ujlcjd9qcygIhAMTs5e3ar5AWyJWBss7oINoOCUSgTfkVdYXkLZLfxzU3Kv8DCBwQABoMNjM3NDIzMTgzODA1IgzCkrf4YFwc%2FGpsdEUq3AOxDWp0zDZzXzpogXbgvCBafmoV4eQn2rivAgow4h549pJxyFyrk4H%2BNvlhmCwbAbbm%2BgyhZtpCQL6awA3s9EP3Kz0Cf%2BuleumCHV9mOc85Z9wK2vtuLbR1PKP8m53D%2B7fGPSydFYeNj7dlO4ng8ak9%2BBcvg795H1zHY%2FLe2H%2BhgoAvglAnq8OCyA1xbxx%2F%2FTNFhMG%2BLKzrhghV0EtiGJi3Vv0omqvud916fF4mO3HuE4KRyB8DoEgBmdnSBPSoqWXpxu6CBUruiPgoXslFeLvrJdWYd%2BfiflsYQFBdTcBPd0IG1mD1kBHXwZbvEaxnPislMwTMaqBNHkZVzWe2r066pHsudFzgbyjL4Z8oPEeGFdZQQampoGCpYsb%2FROcKffLDkZLcTp%2FpBWUcgLIiSjALbUnC4S2GrZdahizzQkutD38qsEV%2BbywzzkOVgh2gwkXv4G9n%2Bk0zgCCN4vg8cExxLrvqG1BLRyP%2FoLiaFipyMvkcoZsTOr5iG9IOB86f8UPVV9gWZczscQRo07vlt3asScSCtz%2Fo2uY%2B1gRVwEvp22993tycYb1vM9%2F2cqFxNLS3fJ1hhE2kLbojNMH8gFgBe4NOSYrjkJWgKsL4LWtalI%2FXV7GAigWBRzDr2zCHyafOBjqkATeOCz8Igv7kTsryJltembz4mpoxrogUPkuUPm52bZHIijQHBL5ZOZ8QhZp2qtrMQ5VpUYsaeMduV7SLJO3C5lAyjDfVLDkaK3KChkhJwjUTI4Pbu3KRkrziNHeD%2BzvRJTBZ8sbBCyDZF3f9TOFFp4yFUcFF4PqLydZKc1FkTw96najVz%2FjZkP60HYMdyENblts2NQgMGnUUEQN1jA5MR0SFbUmY&X-Amz-Signature=cf297bb40c5f837ccf56c6559f4d9956330f7825775801b73ba11a1930a10213&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

