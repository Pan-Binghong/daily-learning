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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UK3AVMZ%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042444Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHiK02%2FQlBOvcB2%2Fp0tkrwCIbdgpcMz9M1nLY3a9H%2Fa4AiEAjSYuTDFhke0ocYreWZAj%2F%2Fsr2M6Hb7Sc3j%2B2xh67%2FRcqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIgYmI0bU5t2m2FyEircAyPoQD%2BwjKEt0Qp%2Fs%2BffqSnCEjdNMKeU%2BYoCNah1x3bDNd%2BhmTLvgpbGpEO9gIWFKkHb%2BkwCorSI%2BpSFE1VHogIZgdTnj89r%2BejHfk4q2LZvRWOhCJ0uFiYn5Ixdg%2B%2BKTntSEwDzaVqjLfA1%2BT7YvME0p9OKbZKGJUULSIRiuUx8tNawZb%2FVMnxE2eDSP9Me8JXV6N%2BHV1Xgx6JbWzr%2FaRbKiWfQJK5pJ7ee3TqjNhj36WDkZ846nSvV6hfTOCiE88g4n653q8KbdaxhJRSbEiyj4wYdtrq2EZDh7QxnRjViJUpjgr6zagdsxPTJVnuGy%2BWqEOXeSr%2Barmv%2F4JwgeRzXorZ%2Bm3vgePTzDOLdYcAUpmMY0iJz%2Boa0e6rVHqzT1D%2BSaHUIwug8vCTzAd7gYNgewQ1Ai5xkmXFSq751wjeDJxGQ1CBD2G9xuwKw2aWUwKdydgy52SZNBm8Yfu5zovwdJgp8Qy3JQ1ZM3N%2Bh0t4D6rqvwwyOf1D6HEKgfLfS6kca5vUJNavboUnD3jk4Ru8yzTSaXrBJWICxcECWHAdxALqtlU%2FhF%2FNhLE1WNkHPh21N8kaOWybZ6HZ3OlX4R2eYizUv6SCuwLXpM5Kcc%2Bfup0oKdO0gKV0cUzFQMMiRts8GOqUBVp7IqEXHtczEhroX0ugSaPpzOJUflZPwZEdmILsoPgMMNeVJdkJ6RagUlGlrQQWovM0pcfkeoze5SrVR8oAK6iYVH7z6V6lJudjQMDUVLWksOxYU3%2FUSYLx6%2Fvjxx%2FyJWoVBeP39M7LeWA0m6fytYDuxicpexY6rcTfh5XtC1Ao%2BpTQoadyyrSIJKUSJjuWpeJxNhWvl7NMKqfYFGMXDBpiynKFA&X-Amz-Signature=aed4a52c1651f47c3c0d5a744fe815b4e0eb17cf5c94159c9b1d3c04ebd600df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

