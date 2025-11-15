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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGNYGC7J%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPiQr2wx0xu71tdkMwfoCcRJ47Dpk60PXiZA0H3X3hdAiAGj6wjrarfgfb7FCiy2Ronv49RhwnNfEUTRMxQfWYDgir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIM6OccjuCxx%2Bpmi1AHKtwD%2FFEgkMyAsHqSi86ZOE8dY%2FOV5SH2tMDwRyCSyyh0vsYhi4%2FJST87mr1HYWho5%2FbMl9T1A9XcfzPoa8i7nIO5L0Fk3KcbGS8DX2EjRWXGHTkWH8CStXKadpPPy%2BIQUdKLwabfNVzUD8qNu9xeMdRnJoHJZq986S4%2BvG2SDXrKC9VUIcgs%2BqNGtZawDfo0kyQXcnSiKfn2BqbKzU%2FfqqbFCAuDz6HlfkV0XKrkRjuRrU1%2Fk68I9Sg5B1a9zfGU36ajm2KDDeALk8SJ5l1PRC9hssdUgPEFbObTVuEg%2BJKK2Eq1gazSAURpvg9QIT2gEfi8YOsmqdjYPeLAY%2Fdjv18Qlc6LR3eIxEOSpM0icOeupQPdEtp6B0O0RG0kRnUjGTf60G6geTG2aXC4kkC88il89XInM30Z6YKrUiNamYqCBDm7hrOjeNiMK%2ByPRxpIR2kcU%2FbJL1S3bennVd4ED54ohvAvBNeIqBxyPBaDvGemLNJYF1nOFI6AXfH6p%2BpuZTY1LXPmlatSZZmiwzsPcWUstL8eN59n23fiq%2F7rYBv1BRZir37urenLTC0McRoPFyTnTTq3cDJfPLnGgtO2X6cIvdgvAv66JTPOMeP1F%2FM2GRFlLll6U3zLW%2BR2HiAwpsDfyAY6pgH%2Fc8WKxxQhUDJi1a%2Bz%2Fx1w%2Flc6P6%2BFDH4PKhCmbzbFSJm8T26Et6JrJ38%2FKCxFvYJgXuwPcimOxn2oXnNtYs1w1yI3DGgc9%2Fi03DC%2FCjXhsEe5P9NwEAN8fvPl3d8ehmmNaP5wPiXNcu06Ct862D0fP5fn36eKI1IWkUUms%2BK%2BYBUg%2F23BJUBhnoNGOOGT5L91uXAZhDSLKyEqFljkFKPRI%2BV%2FR1ib&X-Amz-Signature=031aa006bd2e0fa44d592437e44a3fa7e6ea9c8d847f679f0ca8df28b54de486&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGNYGC7J%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPiQr2wx0xu71tdkMwfoCcRJ47Dpk60PXiZA0H3X3hdAiAGj6wjrarfgfb7FCiy2Ronv49RhwnNfEUTRMxQfWYDgir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIM6OccjuCxx%2Bpmi1AHKtwD%2FFEgkMyAsHqSi86ZOE8dY%2FOV5SH2tMDwRyCSyyh0vsYhi4%2FJST87mr1HYWho5%2FbMl9T1A9XcfzPoa8i7nIO5L0Fk3KcbGS8DX2EjRWXGHTkWH8CStXKadpPPy%2BIQUdKLwabfNVzUD8qNu9xeMdRnJoHJZq986S4%2BvG2SDXrKC9VUIcgs%2BqNGtZawDfo0kyQXcnSiKfn2BqbKzU%2FfqqbFCAuDz6HlfkV0XKrkRjuRrU1%2Fk68I9Sg5B1a9zfGU36ajm2KDDeALk8SJ5l1PRC9hssdUgPEFbObTVuEg%2BJKK2Eq1gazSAURpvg9QIT2gEfi8YOsmqdjYPeLAY%2Fdjv18Qlc6LR3eIxEOSpM0icOeupQPdEtp6B0O0RG0kRnUjGTf60G6geTG2aXC4kkC88il89XInM30Z6YKrUiNamYqCBDm7hrOjeNiMK%2ByPRxpIR2kcU%2FbJL1S3bennVd4ED54ohvAvBNeIqBxyPBaDvGemLNJYF1nOFI6AXfH6p%2BpuZTY1LXPmlatSZZmiwzsPcWUstL8eN59n23fiq%2F7rYBv1BRZir37urenLTC0McRoPFyTnTTq3cDJfPLnGgtO2X6cIvdgvAv66JTPOMeP1F%2FM2GRFlLll6U3zLW%2BR2HiAwpsDfyAY6pgH%2Fc8WKxxQhUDJi1a%2Bz%2Fx1w%2Flc6P6%2BFDH4PKhCmbzbFSJm8T26Et6JrJ38%2FKCxFvYJgXuwPcimOxn2oXnNtYs1w1yI3DGgc9%2Fi03DC%2FCjXhsEe5P9NwEAN8fvPl3d8ehmmNaP5wPiXNcu06Ct862D0fP5fn36eKI1IWkUUms%2BK%2BYBUg%2F23BJUBhnoNGOOGT5L91uXAZhDSLKyEqFljkFKPRI%2BV%2FR1ib&X-Amz-Signature=32f2de883b6e7dd2fc2b10173280c41e79588dd74c9c425281c27c0d06172860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

