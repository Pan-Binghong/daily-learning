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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQRZU25F%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIHty0DqJrXt7UXoLNsjW1Owo2vaAvLZQlzcCqVkYaO0HAiBgllwi1%2BMqj89JKkwQSprUGIJieFPhnFVxFw%2FHXft%2F%2FCr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMD4QLqy0pAT32dNR4KtwD5Pmb6u7%2FtsnENH6omn8crhJ5l20Bhb8ydQrhcHe5Sa9GdhXJTXoRU8zDfOO%2B1y0qC0F65ocxZ6b2aWOPO5sfTUEC5RUk8LB%2FQmcLHXP1zq4e3iXZ12Ym1vBRbJJyeULiiefClGMAUAMZN%2BepTF7qW%2BLKnv6IyuNNf8WHt%2F9BpN9FNarusrzQSLwm5E5QpGHUgXKOFdQLamvvp9yUMeEjWP6W0xkhaa5j0ZUR777Kql%2FXj7bB2WwAmSBdhLWjjTGbaMjw7qZbcQWwUcDJ5zePPpiopcNYgWTzuHHHViTu8Xezp3WnT6s81Va2ArhI%2BA6%2FeZKqkUTtjLVDzenWCp91d7mXXqUJZivqGyUvZ%2BCOctkCZF1tLSq7WbCtD5CTCrxNIoBwzMv1%2FWGN0hwxLQV5KO5oqTIVxasLm9epyzB22JocaO02NDODmDTvyLBL5QmsSu2XklWv8iWXZawSMM5mGxDc5yFAGRZPnfuF8cqpUGcNFF3NtmS12tkZrPJPTKQ%2BEhsDHtmaBdAlUoHa2maZ4eO0c0rmAS6f10bhLQHfPdYRGGAaKoNpljIIb2O6K73rv97eLyy%2FXPEzcp9VWb%2BbbpP8tVco%2BzPstJiqP1Thb9xHHGIWwRXg7wZKfj0wrvCszgY6pgFQ0PePMjRltmZ7nBldl45TTO4XzuAupBAQF%2BImxu850saIcnhRMXATpkriFvq6HeWUuHfdZOjaK16kkRe4vgyFFG2REciAZ3kVo11q0xxwIEyrGM3A93YJlOh%2BmNN%2BLRnq97uPL2Cxa19wYag5ofN%2FnI0eAnGR1FNMncvfpzNtcBLxU8dWcdAkduUhvnaRbASCyZYoct2w9AnHvIwr8ZzYqomOCF1f&X-Amz-Signature=014f657783b1aa8ff2a5bb4a6f0c692c3785099581e132ba5f3341937f5a7053&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

