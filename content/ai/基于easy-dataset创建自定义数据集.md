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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W2C67VFH%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDEP63ferryK0Kp85f%2BFhCW6av8y%2FnHU3X7KRU3PJDDnAIgCVJxg6GQY5y2%2BGMMUEFjIL5d1lxshTFBskC%2Bb4KcYz4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPn0JsHDJCycNSwZHSrcA%2FyREIYndb%2BJN4Pqj9Fj1X8k8h0%2BkRQRSMt7o252uUlPRy4sXcnWxOAqfyDU8%2BnjYf8RF7MJIIGnWTMSTMpy4kHv9qCuIXFNwTTB%2BC8EUTzrpCmDC8msE2uFru9Ck74aArSIjkoogorkRBI%2FvcIM9Jz9EEkjhpq%2Fs34NtcXPwIl3T4A0y9LPcFkEJXKm9VHUqKYrcDUhE1oZVDbJBD%2FMjRuVgrvScc3xVkcVBZepbKJ1ksApMwQJu3zmBGtVGuaE9Kd%2BEemBTOM6amHr9FZGG%2B%2FL7wqlFg%2BASvD1U4SNr8iLfXJoNUPjrnGlhcC7D0fWQDbdSEk4U2DPeRdlForaiVhdawXTkrOsrmaQdQGc7sjYtXyFAWbH3xUD4OXpFxlkwXqLgBl6EZGV7gyBOstZUqtaA1i6OTCnZJFFgT16J%2FeXUEwOylmi0tyvcxtA9MaD%2BMM2TwsBgkuLX1YhXIODnXiKf0PdYO2rG8vxp%2B212NZAXAMiIT0ZQmXICySaOIX%2BKbUVcYsC%2Bhx0hfDPX6XPtPWudg22D6FL1TuTW92QxgD%2B2Vh6EYQngwEof6hv714w3ScvQYOhR%2Fean%2B92XcEkQtSNj6y4WVIYyc7u%2B2eA7cQYptvm2y5ZeXN7ynMHMNL0ls4GOqUBvdUNXvXTujq1nJlBFWTvo9ZGc8MCIRGdFX4nInHRafvXXAioEzaWbDWaE5l0Z8q6spz2hUvKgxWufHWEr4L%2BcKcJmOgDcB%2BlhHrJ4xBVBegljh6h7XmUMlfqnhD6DspFYs1Fd3fPUryFE0KdTT1BhEPWvjK7BV3AwVFVSgmyJvG4y2gQ8SBSjkUcWyyLWHAsWlltoK%2FhFpW7Sdlnsk2GsjUzmA4S&X-Amz-Signature=f1d0d02c057a3c2eb3d17ad91f609b8663225615eb483e7b171313369c32f6ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

