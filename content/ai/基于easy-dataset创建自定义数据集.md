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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HR2YGEZ%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHVrEQUi6Ow6GlXxihAYGiTNP61GUaA6%2B6rCihFwqbf1AiAAhXA%2FVYS01%2FIpDvJz%2Bam0%2FXgZhpHpyzsAOtPyhAWsgSqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsygCVK8m6YGzoz5KKtwDtbqHHKnrRbCdBuNotVYdSoTYWMXakkAX%2B9k9b61VoTtsFGvZ%2FV5UR0QusXGF8D90hFQFc2GKpFFgwDUQV6HRY1MVjzYIvf3eOmXWqUJv%2FmLAOqTHEqn2W0Xc2XsduHMQTsFnH9KdY%2FxHToGrF9rxZlPD2VKA0KhRxdDqQOpNbMF8tib33B%2FavabXb2JPUiZRQ6cwmiExwnybX0lpjxJXcyQy7g7VOBm7epD4IeAPB2PinQULkuq%2F5HrFYztoZr2bdZ3dd68vZ8U3Mm%2FXxdPH3qMXutMFC9nYXdA0kTyI0Va4mv56WL7GvnmIhkU0zqzpo4LPuJfYQBedCT%2FyPH82zRk1O0iA1PSRA5nNNOPwlfbCDpwcgk5%2FjhUogv8ZeZPUeP4zvGC61KX%2B%2F9kzd2sjYMhUPnBASTInEeM4QiLIkmRG4QWxifXvy3V2qFWl8ZV6kF0KjNgKcnLThjpD7HJWihNXHsEN4RMVvUqDtPi79tyPDQyp0ernoLh1PM9EoEU1GK%2FRX6omxeD16daHl1VjQL8xFCHWNHNuijzTjHooQqFzoC6%2FXbUDyj5phBJAUBeclmng%2BMDjGUnrGi%2F%2F3F0tJib4Br8ng3bj3MGE4jsLZ5%2BAAHmlP19ZG1gaRL4w9pDYzQY6pgFG%2FT1IvdI5Zb77Z1AFAWdE96UN8OwGiLPCNi%2FXrBim83OvPXDparVdletmF6M2V%2FiVRGld0hNjqFGVQhZC31CI4rdGKxT%2FMNLHoiAjUkcdT6Y6FR4TrQJdFZMnGKMKqu6aNHZhVQV4d82ri2nG5lHy97O4tU7Yhq6BYL9iaFtR%2B2prz79PqU%2FrJx9jwFdOjxzBunTb1IFU0xKjBF4l%2FaG%2Bf%2FuWMzXg&X-Amz-Signature=0d4edc49ee3ed2bec05afb09c47f0767b8527b721423a9514c63b9f8e8f35bf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

