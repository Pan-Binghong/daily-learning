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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMUFRXI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4t1wQKb92IlaQE0lgHn3DIUJNBBqASfRqHNjxwXDGLAiAn1Txedl7QzkO7CDHtAriTUzv2WwMs0bzXD0kYxzHemir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM1k8uQSD98koWyQ26KtwDGKIITvxKPkGOicahYE0SLU6UxQ%2B4bfgu9GQEeaqrb5rgF8GaOKygVX9vecMMqOJnPp3ZF%2BnBRmf4a3JSxYQaZBuB45RLTTxvCycThL9YvOJumYSMjcwqoDO%2BxbQ5vjnS3J8zvb4Q2hAjFJV3HBMcdL1wfYYVQZLaoVoHBzEAeSaToA0MyF4C%2B1gCs5q15%2FvFgArw7bnzGk6%2FHaSiPui56eWddtbH35mtTEuz0%2FiLbdS1MaeE6Dp8xxCXLFeB1bCer6rf6N6tykI91o7Vb5lIecIwhv0yZ22n48MnE4PYU2RgcI6v9rGYXHNjSn%2BWXhgPulTVvLrI3dIXmQAI3nrhtt37ql8He1%2B1BG8%2BjYatxRVnNMEuGoMouL7yv0qTog84YK%2Firh2FefE0BmiaU7SmBa%2B66hED7C2OmLmNpV9fZiqZstrrcgqQOPdthMCYl2Ic2WLkMLuOLcixd%2BvNP2mga1yMlYP%2FHMKDXMx0897E0Ly7fv6TKq0ze4x%2FCmqRH1chq%2Bn%2FjYSybJwr3TT84rwC%2FgOG9YAS3d4eXgI1QF5uSmnTr%2BYP%2FLNdkS982s0fZ6dlU7RYDLE5TAe%2BWUZPnKrEN4F46%2BtJjgV0OcqeQKBUSQ9LUlkfae21vIWTSmcww629zgY6pgG8Kun1uXmsGRl2Tl7Prn7qZMYNwJymwaznw4l0MpXYSviWDsi7bY1Glif1FsmMS%2FMrpnc9KdD4csBQ4rmjnyFs%2BhgWeOi%2BnwzUFl0MUYvumCGdB7HkBGOQdhRtbBnPQBpF5hvjaq7B9tCJczqwzNmXlBeEsH1EFeZibkuL5sH%2BgA2fpWETIPj2dUXMM3MfdfWigIfRHbTaQKIcZtHOwvC5M%2Fj8p2ct&X-Amz-Signature=a9f63d503c5f467d4f4daa6d8f5391422b422840f7a6cfd07b21fe4eb87764af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMUFRXI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA4t1wQKb92IlaQE0lgHn3DIUJNBBqASfRqHNjxwXDGLAiAn1Txedl7QzkO7CDHtAriTUzv2WwMs0bzXD0kYxzHemir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIM1k8uQSD98koWyQ26KtwDGKIITvxKPkGOicahYE0SLU6UxQ%2B4bfgu9GQEeaqrb5rgF8GaOKygVX9vecMMqOJnPp3ZF%2BnBRmf4a3JSxYQaZBuB45RLTTxvCycThL9YvOJumYSMjcwqoDO%2BxbQ5vjnS3J8zvb4Q2hAjFJV3HBMcdL1wfYYVQZLaoVoHBzEAeSaToA0MyF4C%2B1gCs5q15%2FvFgArw7bnzGk6%2FHaSiPui56eWddtbH35mtTEuz0%2FiLbdS1MaeE6Dp8xxCXLFeB1bCer6rf6N6tykI91o7Vb5lIecIwhv0yZ22n48MnE4PYU2RgcI6v9rGYXHNjSn%2BWXhgPulTVvLrI3dIXmQAI3nrhtt37ql8He1%2B1BG8%2BjYatxRVnNMEuGoMouL7yv0qTog84YK%2Firh2FefE0BmiaU7SmBa%2B66hED7C2OmLmNpV9fZiqZstrrcgqQOPdthMCYl2Ic2WLkMLuOLcixd%2BvNP2mga1yMlYP%2FHMKDXMx0897E0Ly7fv6TKq0ze4x%2FCmqRH1chq%2Bn%2FjYSybJwr3TT84rwC%2FgOG9YAS3d4eXgI1QF5uSmnTr%2BYP%2FLNdkS982s0fZ6dlU7RYDLE5TAe%2BWUZPnKrEN4F46%2BtJjgV0OcqeQKBUSQ9LUlkfae21vIWTSmcww629zgY6pgG8Kun1uXmsGRl2Tl7Prn7qZMYNwJymwaznw4l0MpXYSviWDsi7bY1Glif1FsmMS%2FMrpnc9KdD4csBQ4rmjnyFs%2BhgWeOi%2BnwzUFl0MUYvumCGdB7HkBGOQdhRtbBnPQBpF5hvjaq7B9tCJczqwzNmXlBeEsH1EFeZibkuL5sH%2BgA2fpWETIPj2dUXMM3MfdfWigIfRHbTaQKIcZtHOwvC5M%2Fj8p2ct&X-Amz-Signature=e14a86551ccbaa0b73b3997612f0ba76506d4eec04b489aa4376e18b6b7ebb49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

