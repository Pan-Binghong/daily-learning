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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXEENDLZ%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032917Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDy4dV1TPQwCiKqr0WOw1a3VnM90TFvsP2bztnxb7foNwIgB4023tHk9h45pFL6Ul4yEeqyOR2ABae61KLK6ufGEokqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNyTly4J1%2BtuKMgCayrcA9tIiD83DgGlVOV9NFKcOqMRtJ%2BoZVOiHX0Z3ZzXBsDzOs8%2BwDAVPfV7XZ2XpeT56bKOZt%2F2uxGgTGi9%2B4s4eQrOAOa5FPq7UZem25LiREpYq4LBvFJVRjoKebwif7TkcTZIxgHypVsMcQNdATHLAF%2FU4UNkWdb1W07n711c8ZgPUymSO3r9HmGXEyow%2FEUedwczawBswXsRD8g9nj5iXBfvmAFg7bxYntRG4MYvr%2B6Mi7RFMS5vMTQ%2FHEB%2By6kF4woc1%2FKcxRufuBed31eD4z2MkCymiRKhB8NHLq33oShOIkmoGUBrOu8LTDb8tzIMwDfboHDlQNGpD1T21sUsSkTYgzHgvesoYgxjoSoDHl5ZfFWWBgoVGGYd87wxjo0MBZiA%2FBqF1BUAXYAdUzruWbwGDkS9oUyNr3FyZrQ9FEi3d45IJvmcZm%2BhMvHXPPUU7y1aYgfk6QIEWzthBJAFb5iyFHdXbZxvRFr90HE43YmUA%2F82ROCffpSBxMmqZd71FqcNNcfGchWWBEb24a%2FQPJW17vyBkR5lqrt1GE6oUEr82o4BV4XPf6rkidDHtwO54sxJ%2FnC5i1XFyYpjqmddVM7MOdIj1x0fTqgdiJKHbBEb4miS2rLQLhoq9k%2B1MNnI8MsGOqUBe72Dc1E9Sg4o1zjzlwKP9YLolgPDd5OwtN6MEPW1SlZHLDVTvgs12a93C0arm%2BKlArqFskXyaz9cT2W5%2BpdUUJSWZp5bXb2Fyk2u2bJ56PtHh2rX5pnSv4oLP40BakqwcZtzswSlCKUFiOyRcWBIl%2BG%2F7YDBSD6%2BPA%2BY31f%2BVHM%2Fe%2FH546Bp0%2F1CHwRvsIqNEGW1f7mZ5%2BW4aIQE3o0FdAfdndeJ&X-Amz-Signature=c66fb1c1e8a4d412cf77efd77077078b369f0cdf45d53c528d3b8db3cf5bb5b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

