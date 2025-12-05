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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT4BFE2W%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T025004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICOA07oco8DHwiMfi5t16j5afVEgDeqfZ7lMT%2BzWPJlpAiA%2B3Sm4BWsOKbK6KPetDIdo247FOg9TludWJe1aDpPzKCr%2FAwhPEAAaDDYzNzQyMzE4MzgwNSIMzMT8%2Fx7KYdWTcCWpKtwDceYUXmo%2Fyqv%2F963HeAcU73Xjlqd61JLLhgHGYTgvW5Auzid332fvQposLXa%2BVhanUzpcYpHfDP0EmFULRqbyP7scaZesKH%2FIeLZYNcCkvz6EcqXfOSLdmuNjzIC7osBV02o9FaLtbyrx0MS37mzSXOsP%2Flml1u32gzWMfOOJCcYDpUAR3cjeXxk26mzL%2FAmU27THD8inICqLO0ydhyd1zwQ0wDeRnOklFLEZgZHf1yg3q77Ig%2Ba2ifaRpXNLfIm5P4PtBSyRP6dtDow05ywr6pXLMDnODS5TizOtLtKzeogopFINav0uTbnWn9natEG81fEB8p64ndRqQMmzlKL0bupFQcBDviKLA6Em4cKncVg03RSBhaVkwML3PTHVtYVac0BiKFFxSsU846YuLfV2yyEL8gSurgL%2BCXGcg36dchmpHGraEeqinnYI7fy4kpJwAJrwW6gGrJjICJg4UXLd1mAgNv%2FhNOieca4Q3z2ZW5KQE5NLKHAi1EeGAwssxZB8taWFnwPPwlUXigcCPJ7qbo9mr1a8pme2ISfbdXOrMPWIdTwpo7diUVaw8eQn%2Fr6UvLfjGF5BgZZV5lzp5V2QkV%2Fyl6tYpxMscvjC%2B6KCzA8FKDw1sNaERY0dV7cwrYzIyQY6pgG%2BmFEKKWClNClb%2F6f%2BaBu7APkKfDvzWl4DPvJbZL%2FbHFCi%2F2nUYgwmz9pij4qsG0rAGy%2F2fHTUMXk1lr63rY57rAKLqDiWOaUT%2FJ%2Fj%2FP8QMxuVOw0P0zxLgO8qjnVZdS6NwsZ2doNaUy9DpLQRy9aWpb4hwi%2BZ%2B%2BKX5xpydgqEWEzn%2F2blFhIVjxCRA9H4g%2FiOqGtr6Rhmx3XdNvlCyoqJPbWD1rl0&X-Amz-Signature=ad1bd0bd991f258f0bfc706127f4ac64c1c556346add71bd78152f91d4695039&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

