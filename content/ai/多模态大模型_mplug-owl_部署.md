---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ACZB3HC%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVfM%2FsvQgs0LO7SeiWUJV0Tc9%2FebvksKpCNJBXuR%2F%2BJAiEAwIVwErNl%2FatqkSnZS%2BN0EE0zzpivIFS4hmiYcK59tdQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeW5MYSbXQn8pLclSrcA0NU7j6mS1MCbBZJPYmAnI1k3R9R3xH%2F1a3RrjfvbbHnVCsUw%2B4z7I0SC%2B2gXhVQfbIKcR7MbOYqDAjOO161lK43FRAjjHtUxkzqH0OLqaAzaBa1CDOjx2Pre0m7S1Tl6B2S%2BzOnRGTfx5JgoySjBrfdvNQIGJgQi0lX0ejTrQntOpB2raUQRv9LuafWVe40zoystVYaRF%2FiUEdmJqOhDUekLMBwH6Xm5HS7BCeYWk1Mui4kDdHAyYR9pe1COy%2F8FPQTysobV1w7cWJV%2FoMFLpMG%2BM7U9%2BXpCVinfcU%2FVvcL6AzdkXLLtQkk1XJwc2yUZ1oJxjVeZ%2FPkdSJGsDm%2FKZfy820zFW7shQsAnWh4DxpIWtxbtnBMOYEsg4CTD143VvAoF%2BC9yezy2TjrowPiNhjEtETSIh9SXqRokMpqg10fEqYWke8NgKr7s8ET3Kb%2BSw%2BPf%2B7rLtzmIK2mSQEDFrq6IZhpM2U32iSJR11kQoWFT8opm2eTPWob%2FFJd8XC5pMZrzokzvxJapR%2FGfWZmhIka2P%2Faz%2BsTPxeg7libleao88cHXBoynHiPI%2F04ceUXs2s8TvoQ8llujVl65X4a266nw4plmBN3frflqw22p3p8gsIh%2BNU0YfL1M0WMMOnWzMoGOqUBP8YLnGIKLglgEZyEU2H6pkuIIk%2BO6XZo3jy1wGeL9EQ77NMidgFZw5k20Mo1eTJ401hX%2F4xEiCyrc8KSinMp5Q2gseOzKJ38qnxvm0mMuyw7snL922CcRI%2F%2FDjfjDVdWH6pVQCZz6rWnxLWTJZMcbQCZkDyD9GhM7kt0iA5ltoGJYh84PDzZm3VRXy4qfcNX7fzXFEBZFUp%2FvXl58Esf1zrnnOtl&X-Amz-Signature=f338058077569430552a0a53cb502d1d84d346a9f8f2ae47592f602dd1e64f14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ACZB3HC%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGVfM%2FsvQgs0LO7SeiWUJV0Tc9%2FebvksKpCNJBXuR%2F%2BJAiEAwIVwErNl%2FatqkSnZS%2BN0EE0zzpivIFS4hmiYcK59tdQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBeW5MYSbXQn8pLclSrcA0NU7j6mS1MCbBZJPYmAnI1k3R9R3xH%2F1a3RrjfvbbHnVCsUw%2B4z7I0SC%2B2gXhVQfbIKcR7MbOYqDAjOO161lK43FRAjjHtUxkzqH0OLqaAzaBa1CDOjx2Pre0m7S1Tl6B2S%2BzOnRGTfx5JgoySjBrfdvNQIGJgQi0lX0ejTrQntOpB2raUQRv9LuafWVe40zoystVYaRF%2FiUEdmJqOhDUekLMBwH6Xm5HS7BCeYWk1Mui4kDdHAyYR9pe1COy%2F8FPQTysobV1w7cWJV%2FoMFLpMG%2BM7U9%2BXpCVinfcU%2FVvcL6AzdkXLLtQkk1XJwc2yUZ1oJxjVeZ%2FPkdSJGsDm%2FKZfy820zFW7shQsAnWh4DxpIWtxbtnBMOYEsg4CTD143VvAoF%2BC9yezy2TjrowPiNhjEtETSIh9SXqRokMpqg10fEqYWke8NgKr7s8ET3Kb%2BSw%2BPf%2B7rLtzmIK2mSQEDFrq6IZhpM2U32iSJR11kQoWFT8opm2eTPWob%2FFJd8XC5pMZrzokzvxJapR%2FGfWZmhIka2P%2Faz%2BsTPxeg7libleao88cHXBoynHiPI%2F04ceUXs2s8TvoQ8llujVl65X4a266nw4plmBN3frflqw22p3p8gsIh%2BNU0YfL1M0WMMOnWzMoGOqUBP8YLnGIKLglgEZyEU2H6pkuIIk%2BO6XZo3jy1wGeL9EQ77NMidgFZw5k20Mo1eTJ401hX%2F4xEiCyrc8KSinMp5Q2gseOzKJ38qnxvm0mMuyw7snL922CcRI%2F%2FDjfjDVdWH6pVQCZz6rWnxLWTJZMcbQCZkDyD9GhM7kt0iA5ltoGJYh84PDzZm3VRXy4qfcNX7fzXFEBZFUp%2FvXl58Esf1zrnnOtl&X-Amz-Signature=ece0898e5605df42c9b7c8e7bd9581ffcc55e95fd9fd4efee3af7934f05048be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

