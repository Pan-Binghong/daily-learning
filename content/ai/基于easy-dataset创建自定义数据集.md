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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667P5I2VJL%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJHMEUCIH5MVSDp3zIA7nlbsnnq1n3t2bCqoyYqmasAmbpJ03%2FfAiEAizSHgMBtTKWErs4eXr6xKjJvxKMoD5J85yjykCZk8Z4q%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDKh75XdUslwaiQfjzCrcA5dDtJqvpK1zKa8%2Fv5meR3Wbuh5thAkjFdyWfhwQDyKZ48ZESo%2Fl%2B3%2F5Yhxu2jn9vNz22FG1ZQvlCAmNIUEzBYZmrd1wosJ576KNVMAkkBUghVCbs3yIBV%2BvSEWM8TYzWRdpc3%2FZoKHyHSdc15tTuuIHxYKwYELpmk%2Bi7RQDgpMsWNicrHB5UYqYyoJO9OCES1TZSlHj6WWLVM6jKRICsPRQhODpv8i7qqc%2B0sqpRT9nn%2BUwDFT%2BnAXSt1MzOq8eujYPyHGiKXluoUeSI5GpJhmGn7DGQe40f8PbAsQdxkAsoObj3gRkHAOuD2ZFSpat4VqaQaVUEKN8mH1w8FMuWMUCP99UP63Aivl2T4ubKbmUeKFBAU8t9PSxyE2%2B1HJD%2Ff8sH4wU39WdO%2Bojlz9gy17xm5I%2FQXfSZofDYTaQs9hULsneARppRrve%2B1Zmu03gzS4602mPZSfymBNHvuTxriavtuevrnIBvhfr2bAAyQTo4fUQvBEv5SBxXO%2FnoiDHVxkjES5T0uX5zKCRcQh7ZL66487f%2FhB%2BDkGWV8C2rN3Ba%2FcsE8s%2BjkHguOtsjrK8BWlABiyFML5DtBroK8OSmXo33qKWtplvPa7RynuC9eudy9FJY7cJyMk3msN1MJ%2BhhMkGOqUBIe%2F4Y4UD2ChZCeTmoGekyOQOJX4iUTSWtPZbEHdLzJtjoyJ8yU9MbkJmHr9wxSYy7SEuxfepb%2FKwgWS57P06TRqTNdhox%2FFD2ua0x70%2FHp5Wv21zkZPrzIYfkj3jYg9wjwM%2BEL%2Bms7RJpjdt4T7N1kCLUrMvSgM%2FGr0ODmiESs49FH8t9lR%2FGgNsXMiM%2FaWHSK%2FlQKaIN0Xdm0PQz%2BLpvWqX8GWY&X-Amz-Signature=c87751ba096357d5d72dde8a5394d13faeefcbe8d27af60db5c832c3766e63dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

