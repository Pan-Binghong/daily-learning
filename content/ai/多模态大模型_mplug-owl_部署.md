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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227VVOCV%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC3sMyTZEqwo4o%2FECsQlAgWaTsfO9aZk5NKvUlz7SiKzQIhANw82ppzcVGLTq8016JQ68G39nXHMu3cpcrQOwLXG4dfKv8DCDQQABoMNjM3NDIzMTgzODA1IgzGjszMVW21TsQ06u8q3AMEqsFKsB9G8Byjo2Yqk6plffQ8w2KY2vWwtbmONiYGXxcklD0jg1hPUOBauqJEyxJKhB4XARbK%2FXK1Ke3mwFCX%2BWO%2BgSf%2FBs%2F7nQWqee8zmvAIpPsuI38xmmP1t%2FbHJauNLFAeMM0jVrLuZ3FxEE3TveOzdeS%2Fi4ybU45eNFzmWXVH6T1CMrsrhb%2BfQP8zusWfqyDlRjdzaNBFpX%2F%2FKbOsLcrp%2BuaLZVYdul7j03KjTpnWJypcyLdwhA4ug3HI4LvvEtevjqptKJ8%2BQ9sNT%2FnZoOWWsjNszqighnPYpUzsrB9Jk%2FlPcOi4BIICCAwb%2FKtfhhIe5ifHsYeCvHII%2FzYWeCrdrwazB99wdVFkQS4hW12uHizLHgZ4SmVEBWPcJDrM2j5Em8RLanuxe2SB9h%2FIWK6zuPR44AxGcmynUvVFx83BhXCPVP%2FQ5pYjU4e5iySVGzAkmUgCs6EBAS8BLBGgvT07ZoWNk3n5Oja6zudxEmD9j5NC1RYjUJ88J%2B7euc%2BJ7fCAAIjLmsm8ktZuukVfq3auZWaPNnZ8nFgU%2BriJmmUg2Dyp8t12NmpTObv2njE14o0s%2FEhpxm%2BeUl93DhRJwHEzdPEytAxSSYw9%2Fxeg3zSJGsXROkfxP%2B08RjCnh4TNBjqkAR9QanEawivfe5hT1qDYWq84lUone4a5WwysuzZ3%2F1Nei7ZhgMLesdeV5d7GtRl5IxR4WLSWXSsvUiL%2BIi27UT2q0NvXpSm9GYy5K4Vq4N%2BvO1YRY1nslUHzMwcLX0GO1PXOzzTGaoFQzUQdzHSqvxU3pFvtO0IKJF7%2F4D9X%2FTDOeS6HNBVLBqDhy5Kx%2F5G7TKIxfjbd5xWWZWLrUYbAid861Cat&X-Amz-Signature=ff66cb653c657dec2ef260f62434a79a716f48ea8e1c1fd5da46f395fa896ce4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227VVOCV%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033123Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQC3sMyTZEqwo4o%2FECsQlAgWaTsfO9aZk5NKvUlz7SiKzQIhANw82ppzcVGLTq8016JQ68G39nXHMu3cpcrQOwLXG4dfKv8DCDQQABoMNjM3NDIzMTgzODA1IgzGjszMVW21TsQ06u8q3AMEqsFKsB9G8Byjo2Yqk6plffQ8w2KY2vWwtbmONiYGXxcklD0jg1hPUOBauqJEyxJKhB4XARbK%2FXK1Ke3mwFCX%2BWO%2BgSf%2FBs%2F7nQWqee8zmvAIpPsuI38xmmP1t%2FbHJauNLFAeMM0jVrLuZ3FxEE3TveOzdeS%2Fi4ybU45eNFzmWXVH6T1CMrsrhb%2BfQP8zusWfqyDlRjdzaNBFpX%2F%2FKbOsLcrp%2BuaLZVYdul7j03KjTpnWJypcyLdwhA4ug3HI4LvvEtevjqptKJ8%2BQ9sNT%2FnZoOWWsjNszqighnPYpUzsrB9Jk%2FlPcOi4BIICCAwb%2FKtfhhIe5ifHsYeCvHII%2FzYWeCrdrwazB99wdVFkQS4hW12uHizLHgZ4SmVEBWPcJDrM2j5Em8RLanuxe2SB9h%2FIWK6zuPR44AxGcmynUvVFx83BhXCPVP%2FQ5pYjU4e5iySVGzAkmUgCs6EBAS8BLBGgvT07ZoWNk3n5Oja6zudxEmD9j5NC1RYjUJ88J%2B7euc%2BJ7fCAAIjLmsm8ktZuukVfq3auZWaPNnZ8nFgU%2BriJmmUg2Dyp8t12NmpTObv2njE14o0s%2FEhpxm%2BeUl93DhRJwHEzdPEytAxSSYw9%2Fxeg3zSJGsXROkfxP%2B08RjCnh4TNBjqkAR9QanEawivfe5hT1qDYWq84lUone4a5WwysuzZ3%2F1Nei7ZhgMLesdeV5d7GtRl5IxR4WLSWXSsvUiL%2BIi27UT2q0NvXpSm9GYy5K4Vq4N%2BvO1YRY1nslUHzMwcLX0GO1PXOzzTGaoFQzUQdzHSqvxU3pFvtO0IKJF7%2F4D9X%2FTDOeS6HNBVLBqDhy5Kx%2F5G7TKIxfjbd5xWWZWLrUYbAid861Cat&X-Amz-Signature=c92677805ab232b3e1770b22ec207276772a6ca2dc803d378fef88bd563ee0fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

