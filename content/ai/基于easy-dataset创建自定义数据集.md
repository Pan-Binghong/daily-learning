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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627QWUIUV%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013102Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDXoobSCJBOh5mfhzsJ8nHM4xKdKY8v4j%2BFW8%2Bx6VsPuQIgecX%2Bsjep6foYLuR1NUFkeIGYpcSDOkRkjvN%2BzR1ZLg4qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOerOaGSuD0kn6kV4SrcAwK3frI%2BPV7gA%2FMhl5MwjgkTZmDz13J60ss3HkCk1b0b57isvYPYkJbdP3Jo9pqJRd9dKm8EYdq%2F44rsF6mLH4U9HalOSl6KZVUBFjrGWLVcnIL33qh7M1LeU0kdV75d4oog5KJ0pxJnaubQHjrHDE31t8%2BXL18KqSA8j3gzR4J9ObQxcAD3cMKJoKwU7lBOPCyYspljq8ZTbH8ClqyUlbhyPy8m4vq2mrhrBiD7Dpbhj2MF6vhGCr8kj75I6hZQein86eGYnzZn1%2FUYXxOFPhDDwxMrgV%2FCaAq2ONyp1ApuZQqm0bY8XWxxVIcqHPJm2CLSThu%2FFOLlfZR73Z8L%2FiXvgA8cwdPcrW8fZRmyQX8unIga6QhmyFI52BoeySKmBwZ3BO4C9%2BQG1l7IM1V%2BDC%2B%2FdkAP8PHwNExtOZOH4AUN3D1q8zHLc%2FKA35K%2BqJh651S5gT7eLUolGH8n5%2F5X7Azl5ly2Vh6ERNe10yLmSYvN5aS%2BvrCo%2FwqyNpD5GBpvq247aX3vLm0E9CwkmZgMCBrtUjHn3wznEairfLHn9WSqCOdMHanQ%2FbTCKpUyA5da5sCo4HXEnIyP%2BWsoALw66v3N4A8nXjK5P9VFg4o99bpYL4gAkkqbNII%2Fn6dZMMjxr8gGOqUB4XkinwHNR5ys9U1FgiLosiOUsSj7TQsCSA1UTuPUHppFU8zvucy0iFCsHFVsYnxpohXviRSwirJ9L7qCxDqd0INP%2B2D1kde3murDY4xbUlXvVhrUwrUYvWcluKWmSLbL9mTR2K%2FTL0a23PvgcOYhDNMVGA7%2Ff2xLinmsqil2h5iQBvA3rECPOZWynUYAR38NNrJZrhBFJp2dg0PQPuE3yQyJ8XZl&X-Amz-Signature=28156b9996642b98424c3b321ec868e99ad82669492b6fe08506836007fcc710&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

