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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBPO4UDJ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070656Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEM6zw%2FbAYCw2WjJ2P%2BFnsq9pmLKFV2UxU%2BJgh7t4MWGAiB%2Fn%2FWJr34NqgI6FKvbvLod1IdhSFUNLpj4FxtddY0P5yr%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMJY1CYnrEP3ZEOpLcKtwDkwbqCSoCpJiX9k%2F1x0PLI8BAVoxo%2B1%2FFAZxppweMg%2BJ88naAAfFhVaBaJsMpKSVYONYVA6G6vdVFGNwAUKAwQRK315C1N6aiBMXbv%2BDQD5O98j29VHqSJQYsfXXJWfvkRAqkiz0NHC8URgaQE97HGPaVwb7IL5ImRQQZI3TUvQ8OeWwwqCEeHfpTwV0Plq3Xx%2Fd2EHYQ%2BOODPFlVouVlHNP%2Bwo7jZXQxlANhlE15f71oPNHi35pq%2FsJqZUJzFrNUAjn%2BquF%2Ftu50t9eV%2BHTaFUjukh06Qmbkql8H%2FKCFgIdsGrtRpdMPLpmq8mpprcYWHDor6m3ZAMot3LflZbsJfUU4tJAJXlnFGOABpbnJiOG782klKU0r7rQDNqm6VG38erl6tNeRI0t4D5tKQko82TK8NIc1%2BGDk6RCjpTJ0Wun4ARURe%2F8sgYzhjAh0xmeIuLUukZpI%2FzViuy44Q6ApprCIKDBDF8T0%2Fbg2664cQfUY24QbbSzFFxdZh0%2BZkznwu7FBhrPaBnHYWov%2BK5CEZfV9nKnftmA%2Bx%2Bz9dNlecit4LO3ZD3vk0VJHUAYLvlYXCvwdDk9bg9mn36IIWhKZPrXD878cDX1ktF%2F69f%2F3YlXUaJm5VNX0LsM4HgcwqK69zgY6pgEOBMu4UIeu0tWhlFpMk29EUHRegx35uZZiWAD%2B72qZK%2F9WrRdC1SyRCWAcgqMYK8iuSX8Hm9FjFs3zcI5h7e3n4L4lOvagHVnuvORDgHwDK0VMgPzpn8I1v06JQ8Bjdxa%2B4XhMNDynn1BuQ5w%2BWsFm%2FsQtOz2o%2Bnlv%2F5WaF%2BTcEToGrdXowSC5ylzVGfAbnk3SbTRmE2YM4gmniqMAeSHuWIigNPlR&X-Amz-Signature=7c48affc594c26f5983a42311a50980332a9c1217a505a7fb7cde23a4a6b16c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

