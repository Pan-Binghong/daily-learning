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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TP4L7JKR%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAT0E2opmbFM0L3uKb0IfCxxW0W%2FWH2x2Jw4do2CBV3uAiAEfWO9%2Bj0H5eWa6Ef6JUhUsfeA4IeMsxSy500pCO9zGiqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW%2FK%2BKTys6SvNvJoZKtwDP3WGqb9O17gNw6Cd0PIwqFZ64bKrWgCDszvJYEp2nXAB4ZM5YxZ89gaVePmRAwYBAPoDdPe3zQYGXUAa%2B919FvaMe2KXqLAKtEtyuYG9r4yzmwEA43EqFNLaU8d1p8c3pma8UjeurkZ0PihlbFG5fmAmqnB8KFoLxxi6dORJJNVnyua73cqXrqv7LR2GZh%2Fmta2m5GvOGvJoCQQ277eOW0pgjvd23EeL0wmD6%2B6IqbMwenO7LccYDDQ9hoLuunkdZGKZhm02pWMkqhXHg3zhvK8pZzeGiCNkpeUAMiXfqkheHHWUuGRRobDGkght9Bz%2BK2rPliYSy1UPU3tAwR1zX0rgWTTxwPaCeuClX%2Fe6yjd3knLoiL53bIOT2iG6AEUg5zDhIe8auKUhixNaHOXC4x6ETr3a4mgHy0galVgwlgmWknQmuMMOLtHybC3O%2Fx6FikEm5BeT3%2FRx1fP3Na88%2FBU8sxvG25gSYsTGzwTU52T0VG0dRxhXKkFWD9Q1%2FN8ANL51QLLiLOVFf1GxhCh3qIFjOyu8UNHJsljgH1rg2T2MRahS0KhxgL7Ho0NtlMvkw7w6z4WwMDtB4%2Fi4%2B%2BDgf1hpPs4f8sk9Im7xi05vGok92FgVoo9Zrl%2B0o%2B8wnbW1yAY6pgHSJcmaQAAj%2BHls9fLljkmODj1epg5nGaXQzeYsx9yD0NmguPLk6jlOAlQqNdhbDpljfdPdvXOA%2BlBBEPxx38nP2dDLfbson3zwFl5robzRnYdWpHvEDqcsyugKq6psolO67HqjYbRbepg66tsg76NPYfEFIBORdEh8TNHdyK6ApC5NSCq3O%2BzV2ouwZ14m%2BvAa2g6qGJOuy8RO%2BgzSJdAabooTgsIv&X-Amz-Signature=2e812dc5ff4365e3a4d767fa72cb5410b05a94bb5642cf85d73713f4d3247526&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

