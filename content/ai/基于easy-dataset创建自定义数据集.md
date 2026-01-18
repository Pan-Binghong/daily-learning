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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRGJYOQV%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFSURkg4uxfmp0wqsXITyebzlTbKe4JXqRMGLQB7up%2BAAiBA6U22gFSdVIX9IGOG9634rf%2F4Yul25IVU78VyjehEaSr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMxugtpW90jnRbr7J%2FKtwDmmQOu95u0raLyFJ6Ta51us2ziRhhLEjpZAWj8ClPSfrmfQSuec%2B1byfEKrK83wZlHu3C2JVPQu8rOAEf5m%2BO7odnFhg5Sx7zZLllaEwRchx2rcGmFkFZkOdN5zqfdUn11kkRIG7fgmf7JmO1n5EktiGbbuBLf40YJDOx2IjQPlkc9cR81aAEjZksKvanqP0Z5Op96%2BRjQlxQiu93j38Egi6Q1AbBYeXfvfuFvsRHnm19ZX6wJDje0derYXb8jOvIpm3mNF04nWZ7Iunh7Y9%2BWMAZqHuLTk2J0vADBjOwRZsSncijDfWAQBnQ%2Fp7uS%2FLmw4aQFc9aTQL99uuko74DEDV4OaDHSovSNdIKgCJUTCJvLCUaHIael9hMKXpqFyQEFPvWZv4Kzf1vul9SOGvQcPSL8Z0OATzfBskaeWRXtqImrJaZ9RGZGjaBy%2BDtqDQHY6eR8YNir460uJHwCBgA8LsOABoKzUwPw21cYnsmd2%2B6BXHyQVYi0JMMO3wl%2FIoxUHLmr%2BrQSqBcylT9ep8R%2BO4n3YnRaoF0EBg6fu5kFvzDNjiDjS3kSUTVsh2r65yAxxLYhYm5l974ubvb7GhtSWyP4b%2BqzpWIui1Jlq9EViIN9dGLQrkBBTBKktkwhIKxywY6pgG60rkw51IjGvYAAE22TdrYW8Qnp44XEGujx4mwl4Z1einaY3ySLTm%2BoMidUxDjLyZ4ptd50l6s10lXRFwcmY%2BcidZhnySvsc3ZdAV8MBFOIsaaKTILY0vX9gEZrTsUeE8qsdKNdCywmzqQs9%2FXSP6Zo6DrPhFXKBS2NfV7KToPqSHpgHdSEmZF3S9pL2LiLZd3vMzhUkLD88RenSniiVixBPKpLgxB&X-Amz-Signature=b41f8af8a6aa5f8b15e1f051949d39d3b9c982f5fdf33011d15ba32f8458b858&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

