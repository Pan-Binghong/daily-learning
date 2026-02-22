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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XUXUS6H%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICXiGmTTLTaSjc3V%2BDxcFiKHBvhnKshp2Z%2BjsYiM6LmZAiBOTMW9jZ3ZFjMAmXnV7ShsOfQ1u3wIzauvPMs%2F49VylyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUuZifjo2F7Ma1DdhKtwDUww60RCoYSQwj0DRbMx0yzsHZO5X176lgQmI2cjnz41lciKhixaw7zLZZxjHi36pXlIwhJCAQ4dXezT6NwJO4BHZqkBSNasUze5QtQmrnid%2Fo%2FmHnLp8NxVE4uXYV4updUiVW1vGIerAU0ImwwuunNxESon%2FM50T%2F6LrDMpLYc%2BebRTzQxbuCY9q52oJh6sIi7%2FCvfjTT1AFOiXzw03GEGfBTzYNQjcuhUWhbrq5P7J1vs06QWr8bkz5Kj5JrsP1KTjG2h5O6a%2BQgOsyc4HkByRb5NjM9TrZjwGEPyyVfa6EqnBadJo0woXo6wnoj4NeJCRi8a%2BhfdlzTE7VCdMJ2Qwp9s82VVCr5cyK7pgZRVBH0pxUPz6W2Df29rRYnes3tzO1e2T%2BcxBSBXCqcX1FblIxNJ72GQlmQIWYXQJ%2B7OWq7O0w3K7EAd1apHoDOd%2Ba6T%2FP35CKapOMPaHxTHeBKJ3b7%2FL0LglsAOZ%2FozMfNNFNHEghK9H%2FnRFyEwDo6x%2Bdsg%2B5PYLD06xAcAOMG1v6%2FS6iOvCiF%2FF2LYgZ1z7lkAPLg1KP6xR4FCAKnK2i%2FQ0GYc8gjuozb1FJvG8QJkJeB9KUCKfas%2BOq63ZphT4qkZEP%2B%2BF%2Fxn06A1VUiLYw1czpzAY6pgHzxlhBFyWdhEfoI1huQfaY8znX90tTTsHSCJhktaefmpZbKRI7RF%2BrL8%2FUckOJWnrbwrMcsYCUsx2%2FISSLoBvxqfbNTzgVRyd4VFGlj76gj8kuX3A%2Bf2GdN%2BiU6qkvai1%2FKhylEsN%2FxnuQsIYyP2bxXp4sdMbtLuVNbzc%2BCjlmAvM1BENVa3gEgKnT%2FfxoSGajMpwTAELXIIlmt1Qy53wmNgIOqKXm&X-Amz-Signature=fb562c0a159cd41757a1e202a54ee7e96b6aff7deee18984ca015e66d1d8e134&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

