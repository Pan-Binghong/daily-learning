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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6OHTC5K%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025658Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIQDhqNM0jm9bHFTFbiK87h9CsDqe9xufTsEGxlqNJurZMwIgSCMURKICMJL5%2B1tngZFks5Q6zPVuwCj0T6kn3Q1b5EEq%2FwMIMxAAGgw2Mzc0MjMxODM4MDUiDNLUvraJE1Pop%2FAq0CrcA%2BWilhO9V95%2BBtKAzKCGHoPheVhvs58R1NfVoL2eVyTWKiAvJXPfp5tiAtYK9Sj6mslLsB37jbZ3VwEvnzYBwIlgdUpbMOsgaKyYyPCllOgJ4MQQlU904jhqvJJk7M3RzpB6pMAbxRPTv1bfHSlkcg7Ppm%2BiuxK0nLhPpZByf9mT2QLw85NqGAF24VzsBUi1ty2Oig%2B77p1KLAlKXrs2Yd31vRzelntroh8ruBhlNiwXXdIiZcvU5S2uyR%2FJl6dlAAx4xlmN34Gdxk8m7xrzjkdewEdLeLSP5sG5W3Z3qRHoQRZF7ZHlpgoC71lCkWheK9tFGSK40MJMpnydwVaphAMNcaJX6Ddwf0mAKFezry0reddakfXP3Aai7sC6YBlRkRCnX5fstyFFDdKyqE5%2BqhEiicFmQFE%2BRXYfNBVi0vHrrgN%2FyNGAgAahVXuhHRvRGOEwZ1r2MNwiAS4oGiGOJ7O0NQA2ZVN9YKts%2BmGn%2BVCXCzSCzqPB7iEyF1A%2BOhDAfDQ%2BXrDtFgm6zJZEAG9js90nQDhIlbNtzwOMKzc3eSoeDea%2Flf0rED4SGlFyCZ4Xf9uZ0rX%2FAGRWLJQ6jFqDhRsokrMlYVeJ%2FzADkDbp83AXHIh%2B3k8qaVf1oyAHMKurssoGOqUB1afYcx0zBm4bJuFzMg9KjL00YGwlYNpft4dlUrmkpp74eTuClZaBbMdt4kZcTHAWdjIiDohLrO8tmJgxanqZm2kemf8sCbemJlgB3X%2Bi2Ts4rttqqj0ljuqT7Eg6UiszS5MHCRsBjPvN2ZOcrYP1ZYqGRgNXtQlofSUn%2F0U5mOCVmmGdtovERLnNoxav5OL3l1BuTrrAaYNBCpkJYWNjV2ijR1BV&X-Amz-Signature=b01366fe8daf86cda89b76258dbd988def584c0d67d2075cb22aa852648decf0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

