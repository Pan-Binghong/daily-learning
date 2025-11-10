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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466356EKEPG%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJGMEQCIG9uAA7rNir0Q3fgarq40TI62%2Fck7vaoZHndb1WeyFKhAiBoGlm0NWazvKSEtomhcfX6v0tmZgqmCKVpL55CDGapPyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLaa%2BHSm3SIbsiz0IKtwDu5xpaFk2pEV%2FWCIfcRPLZVu8QiqU%2BPV62u%2F1rte4QqNmqF%2FSZt6iidhmUCuHzTqmwolAEgo7T6lIx9lOIeQjdVZZOPhvC8tupK1whcvmi%2FDYU7Snp3bgKaJHq5WmxPkc0PKuz0xjG0mO4KZzK%2F0GZFBeV3zmrS9QGKA1HQJC2QKO%2FyxG47pYYPR1hSVAvZ87QXGhwZJ6EjLWkyO7GJVEjE8Cd%2FJu%2B%2FSL1U5nndtGh%2FS8Ss0S4ipBRnGOOz6YSZeqW3WrPSkkCno53gjINJ8l1zSdDoIuMdTLK6wNYfHXipgK9hpNj2oU0%2B7hONnW1Js5OG4Txre4jhZqKCTGnQc0YumfMKPsbHpGEjTwX0tIZJGufVyBi%2Fxzn4Str9%2B8ux9m%2BbYXSGnsz01dzQb%2FULu7OfbQ3jvTGBjn%2B3yFXRqGZ3HCzSSAg9w7qi%2FcSt9Kn%2Fp%2BTwW8XolX%2FUIcfvfscYbI3%2F%2BsZ6uREqRdFnwC%2BK6d00%2B3uL5TPdjbluMuETL4eycAaWdcqT2ZNMc9zgbxtODiqi6fFP2blHbGQNAEVwYwkPDaGkM0Fh5Sl5V6bmXMTdZlEUr9fQ1lQjBeo%2FIFToZdvlUzTCmyhV43F5YSXACH4zvaZ7Wa26%2FzB1iiaqYwybnEyAY6pgGQlCh8vWs%2Bn5TcNdgUpEY6ov3DLcFPduy%2FIPxj4YBBRLJ%2BsHxFCoRIEE9LcAq2AC3DPjIXWTGLPrU4XZ8dFeSTJVdFyEm9qqzpUBrn2n2IuJe7xyxMCIZQSDOwLbXQSlmaYAzJTQhvYZFGmrXCInuZ%2FLYBxOBEQPQRMoAwyJ%2BFL4dwIfLAC1sTJG7uAZc%2F24XPcJZzCRzyso9ZNlHjBwz8gH7Ep8Gt&X-Amz-Signature=82c9f190d23b8fc9d0fc0791aa3faf6cc54e8a6012fdfef53e301ad1a58df6b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

