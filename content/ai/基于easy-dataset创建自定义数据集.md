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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TVIPS4K%2F20260116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260116T030121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDnibRU6cbzyDYtSzzF0mf61abKYjvurJYgNpVOTd3ArAIhANouRik%2B%2FZrpYqmm%2FAEncFwgGYJBtS9ufkxiGfZAhoWYKv8DCEMQABoMNjM3NDIzMTgzODA1Igy%2Bxy0py%2FIZmucEjYUq3AMLbE8DvccJE8h7lqgu%2FRXXMzz1sI%2BLhIloSAFTVJ7c7275zci5We%2Br6G%2FKxLxXg6PIDmydUhGfVPNeoXkBdgB48Q78tkAcKpIdMAPgVuaQAvmxjlh45GQuhRh%2FuI5adVLJD5dTtMwZndJacGPCxrO6NuPa4R%2F54MbwloGRkCaxHETdrloXBU%2BB1OV2tjcPoZpyuKD1cZEQEIHDvXjFfugtYESwXV%2F32qCgHb%2FVfHtuyyPgSyhNqpcwAl1zBdWC5zrbEkQXRIwu3xYyk%2FKzPXg0DrFtv1f%2BTMD%2FANTRLy%2BLwxs8SnLsu%2BU6fSWW9owceWlzWq%2BBfsLaZh5nlaQKN42tnjfBNe6ASeNsrERgE1QhKN1ejm%2BiKHBBoCPpU0DiW6JkE4FrYj4E6YeSaehi5M%2BqMVT9Wm%2FazfmrVOfYn1f14GDCFjHkE8lr8gaZdjXXI88fOCMd%2FmH%2FrxEsVDkaK8Jg0G4XUrd5bME6BWPl31jgKdBFUOvUBA9pePK5itZtLJ40%2FTcANaEenRMR8EFqpLFG27DYhcW9Tgizki5xSE6zo1hA%2FiaAGVP2JUSs4hnmbaMjsFeJy1bJSPM%2FF8hIG7YHrwXM5hDhBDITY2yxHolCb1ghrexGkS%2F39V2MYjCAwKbLBjqkAYyX4R5RWV5muSZKTGfT5gcucRnlGQ1zuO7wvqp9RflFqSv4r9JdMLG0wJuTgOsUAoXTuQysvf8ludsBASbkZ3b3pqaLAtwp5LclNY9ci8in%2BHEeKqYaGrYi2kRncLYf%2F8m%2FzgRV6D6950GxrPtdfUZW2G3%2BpuDdLStQaq0paZOhcuhuPnScjVOcuGCroWTGVL%2F5838q4YTEx2FlrdX7OaFpf%2FAn&X-Amz-Signature=f162eb3a424e3bc23b35bcd76f78ef5f9f8b2f23a3297ce94abf6d311806878f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

