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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7GR6FKH%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDnzGmOzcu7jAGd6snSKMPw733p8mqTYUUbar%2B4ZhGIpQIgBtyLxNL75iza5BHsWHeryyx2O9g2Q4oTUbFU0LeiLEIq%2FwMIVBAAGgw2Mzc0MjMxODM4MDUiDGTuvGAHTxhTe3ac7CrcAwyJFGIOkHbirQ0nkDKmf4Js0h1Bj%2B0mHkilILutpQhueR7urJVC5Gq1u4vbvAYW2tzl31Tm4SgNLeiOnD6mRAq%2B3w4kl7yQ4eici9NGTU5BZ2XZ26ddb1ItyaER1LgKV3lJu8mQrcXHxsqFF0Ta%2BvvJT3EUjJ0qcxPflM1raeN4U%2F0Iq4XJGXYaYiK%2FWXeTdcNJgLpHuKnmM4Twd8SD%2F6VkzxE9K76rlwzh93Mp1lvD%2B%2FPMPlVW7%2BY%2BXJTLwSVsFatkQk%2F9h6XhqxFnpyMsr6Db4tirCMyP%2FPA3h8k9Lof72pugThN0YgT%2F3fmvqagRYBqNI7ryJ6UUKKl89%2BueckCj0jr7aRTSawlc4GRa3Y3Rj2WWlCeVYOkoYi3p7NoLRozEDKs0BoY3kVy0yfwyOB1CrkCVQQj0aRJELKsxuB%2FwSQ8j5Cahe9sOMA69PbYsvjpx4h7Q5MSnxgWcfd2IrZDQBv%2Bt2Y1GZpsZLRNwl8JAqVLviSxpg7PuTDOmTbH%2B2FQbbzTzXw%2BrpsZUjjxQyMF3IgwcdX%2FapzQWkC5I1Rka5YMW2utASDSfoZ74TNHkEpjLr6qLHt9F3ekupmx%2B1f%2Bw2hDaimlWrLuPXeCS0LEHxNA%2Bi3Vzww0c5cDLMOLl8coGOqUBvk6VswxV%2FMlr%2FVtJ4YUJKJczq2W8yHuemOKMWVAqMM3V7JPZ4gc%2FhV3O21CX1nXlFQksrwPj5TLyb%2FsQNE87EFkeIyYefQqq82GhIxdf9envS84rgQ84U4JpHyOr8Z5LJVPszU7vXaygxwQmPVE%2BjMXPjkWcfGS18syWOIbpT3iH9zl8nGSF%2BRYOVZdqSmXTRiL3%2FVFGYjxugcTBJFcclm4CtV1z&X-Amz-Signature=69ec69707ab6c2b2529f0adb39af273f9d30f898523f00f223c4bff08d169964&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

