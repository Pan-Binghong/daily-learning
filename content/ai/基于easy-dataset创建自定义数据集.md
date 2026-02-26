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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJ7PJFZF%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033452Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQC9Q6QgdV9W4y%2BK9oReX3DljS%2B%2FP6PohpC67PUa7ZBBVgIhALZI8nyI0QRy%2B7oG1QxSNPNYSUqUGTQ2XOdhhnY7rVPoKv8DCBwQABoMNjM3NDIzMTgzODA1IgzFYYxNlInXDeOBgA8q3ANR4cZWzhRWkiBxL0%2F5DuM%2BigyCBeyUB06VUSxWjnBhN5Dor3XXWL8U%2BJlRCmKVgeSJnWzqjlC2Gk9c4FKNhH%2BKYwBEjND9gj1XVZTTLwoPalPynwiPjNTojrFHUV3qZwsBhdFlVHA4HCYhCRnl7PR6igdsdSxDnGMfkjs4Px%2BOfvMtXJYyZYRqs%2BLnzKvYLvOUeN76CywqK7CpOB3Ua0ByxnQ%2B5feI4N38JlbidEHSPUSQhiq3IsmiF3SkHZYrcFWaKFLC57WwoMCSD7353uI2hr24OJ3hS9%2FrHaNhVTxqvZ8Anen9RuqifuBMJ7UJByUd0mDMinVXqVGE3wNetvEQIifokUHw1DIF%2BJSgWE%2FFuJDbYck8p1FPdpoJsycB7QiHK%2BNRub5UEUxAwZrsKTRNSCsEYuMYb2nI3smGYbKwRQXOE94KFWUA%2BqJj5%2BKewt8KiuobJQaFhygE%2F8Zh%2Ft5APeSbbNYWP%2BltGmOYbXchbB0IduF3Xl8oRtNxAX3F6BVaG3ruCT%2F9lu%2BKOKQGd6LMG2hlDXL9KpIssQkEYIQvOacjpdogJuvAFGGf%2FTf2L2xG0D2KiMcbXqZ%2BTjNsm5JniYfBGlt4e4LhpuZ%2FUjFGz56VJr6%2BOteN8gpG7TDt9f7MBjqkAXxNHEYr5sVZYHzU7huKMamcMvQplPrld6bFess4reEjtD3l4mz12R4bYYGwC%2Fg%2BbJjCwGzP0siapFIU7uM0kf%2FrI4WdsOSdImXLcy8k8U8nziY%2BkKS5F9uIZ3g65FO83pbDGZU59xUM%2B4URXe065bqLkaa7QAwLHxtjFfX1LJoMx6aQ3U1r0PT9q3%2BC7wOs2Jov3XmzreQn9oDCECN1hP%2Fy2C7q&X-Amz-Signature=9b51d3842bec2fec3253a0181bdeaf5028c764023b7269130d63ac90836f1886&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

