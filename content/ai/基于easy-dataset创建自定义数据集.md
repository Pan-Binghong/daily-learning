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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6W5MLZE%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEFLlj%2Bg%2BmPR6ju7P2Me9G2NXkbyPJZQHZAEU4wiGaQUAiEAh6X2Dh6vARoIfU46e%2Fhpx5DIx8nkpugIRpXk2Qe%2BsbAq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDM7ErSxToU1ZipB2XyrcA%2FHDdisrkOV%2Brc9yw%2FFxcL6byo04Lfk6QialI1FEM5vCgGg9WJPpb0qUMLlkGUc69HKtoy79NFoAlUY9crA92dAUlQH36COQ09pEz2qQfnt1NuE%2FPhFJfUJR0M%2BOP%2BjdyyudlAhj8vC2O4i%2Bn1GZowPPbVXPQaI9tStMW3aT0fkZ9AQxvlxn4ZB%2BJPM2DGK%2F5QSSuVbwUT6UqXfbp7bSy%2BMZvTzxTbWumNNhtSxIJMoWvnmlS%2BSsaBsM26E0BfN24xbSpsF%2BAqnd7pSJbkCcNBgdjKjhBn9rDCP3Ni%2BoUnchteYa8gsILqu98un6yAlRbeXu%2FbvMq0%2FjuoDuZwv%2FckvDxBoyKr83K2mSDw%2FTZC%2BlS3UulnTnrt%2Bt6qpkNTPEVA6LSX17LrY03q%2FSo9lN0ZZPihMxph%2BNNXRnlxkWlElNco4GP8yrI5z6gRE56ZtUCus8x7EZEcZ542F0wTqxvJhHg4v1jHgcrotveidJKPpl7cdxfLBFUTepYvMvhKmz6ruc2W%2FIM85UXwaPbz90Yd%2FdmWd2oiTu4XYKGmB6TH0S65VECZaJVVbkkbN5uwXxnsq%2BEumYzAn9UraoiW9I6VFQ8%2F%2F7pMO%2BENEkNQTEeUL6aggtEvvSKGJfk%2FNVMOfA38gGOqUBpRZ9GvUdTR0AAZBU%2BafgRBEONI2LeryUpC2GSLw6HohVwx4GbXoVs7j4sOJumxDouMpIUPAGBC1cqoLCkaN%2BJBRRRmQCy5IGGXm71MbLQW33Gx9hEF54GO0t5uTj3Zd0qmJH%2BumAsP%2F67pINcqXFaAZza6GfX46sjA0O1eCp%2BRxX9sVRZuOYptYCic0EaBKry8Hd2aNSTf0j9OyqwdhQNyDQJE%2FY&X-Amz-Signature=5bbb06dff984076b47ab8b22b514cc5d91e1033e2c4ada44e9e8d95130994421&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

