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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UWB46TSD%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKpo1%2BvnT%2Fwvgo%2BeQBIOJcv3ZcNuU2P1jOIszKWZeUUwIgc8zphObfp68FEaKtJ8nTeneS%2B%2B0eroZtRe4%2F%2Fbpr%2F9Eq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDG5o90E7YqJH2%2F65rircA8LXM3qhjR8K84HzMNIbdWTpuuLRajQPeNfAnScimleiQc8rJYFlnv%2BxWd2JMKkNDcFNBwt3c6j6MrHM1d%2FmUrnuMkrO%2FZ8k75zAtB2F86lpi63kMqExtyJ7jkIe2GCOoTaKQGidbUOJWGu0SUpBu4j2%2FzWAfWaX7tLqczuNrDrkYlo1Uw9fIeR0Pa64oiJHES9Q%2BXg%2FwXPTNcoYjqdp%2BLo6ZqxejPgKVD0FSM063treOZnzAgBArtwb7gVZTi4e%2Bb6j7peKyIQhbtsOucaoubAFwrXf4M0ldkisDfnkAKj8MSDXgUtnHdtxgMzkqtZ8tc3zBzC5Q2QgSd3oNJX2jUA1IEy%2FBsAnLqUDraxF50JQFo4bE4CgcyHAsbtTxxrJt7KX6GqerFCDDKMvAsFHvBM36D8ip9WajCPDO6LgHPaVF6hVS9TJGjXFyBdFkeiiqA9i37vzk%2FrJraJ1meIXXqq6qw%2B6HQhkRmeTRrLF7eDLnJ9Kp%2BLmF3H1u%2FQuq8tG8wXgpnJ9LWom5wswFErrpkZbelVQ68ndSCzuiBzBFvn9aBsw4FsPGD7Noxc2Uu0nPWIG43ttjVtGIqUdQMjGQXAbrXHs1htwapZUNH7rM04rvcXU3P5fGO54BzpkMIeyyM0GOqUBFpzJodM7wrHgSQwGjvbuqI%2FdoDZRcE8RwiWs3a8BUPBMINaOhz0rg7rMKVt8wC3nPasGwVU1G9YNYYKKEtjm5YT2IAh3wPnZsHaq1YY0xrTx%2FLZAC4mzJMGpxNSt0d5fQ%2FwezWykfHlPl6FXv9U3hTZJ5D1%2BAAIiVmAqHZFp1bBO6SkuAEBOwrIaCB74jZXjRuAI7trylOgTjlCMq4St%2FeDyb1EQ&X-Amz-Signature=eedee0e53429b497299f684b50e1ad657e300dbe354541cf4c9b4d918606d0f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

