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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KHBGKHR%2F20260325%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260325T033956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAKF%2FOtb2nwVR5gCfGpJRQfQRwG76mogRlpYdP5jJz6qAiBUyizUs5ch9g2FQs5Rr5xiel1L8iIUxLHFq2B4j%2Bo2LiqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMga4rehZxq0zy%2BwmRKtwDpt66uEQhQzXW36Y5GD49E77Q%2BvZsgsQKL2AE8IWM%2FIxSCpPW7Uz9Kffv2TO2aPVOWQv7ezbmiPUBugxdjtP%2Bzt5oAf5hY%2FgQIodjOgnuPCXWS9qJVy%2F41IPLsFkbr6KWQIelMdQJP28EoSU17Gsqc5oBZ9aKBLIlA0zcLdEqcLi%2BKkUaFKuJQlWD9H8kxu4Q7zwL5MKqwvGRj%2Fn0Fl1pNkadNAbXT4B2eOIvenOApSovYjhccq7JFXtyoBsp80%2FAo83dp08NTzqTScAX1Uchs9NYi6mDjybepTCZeSh9LzbPkFsrbZiBiAqBkxcVeD71P2NMeOmzf2tkhgy0g9tf3pSFcJbA1xzOLuZTEJsTRcYYzQL3iRave%2BB6Tu4ZYoYtvrFh66rCNvk%2FnW0ii%2FXuqBJg5fbKeZDz8Ix658sKgaKWJVncTdxYrNcQlZoep4wIGMdvqOAVfFUbRpoRtA4IGhqnpjKJslxGZ%2FWL1Tgrk4Y6C2zolRuMH1ObNHQT4tIR0V3u49HMQctclndo8P%2BooM2YAn1E2xdbP3FN3PWjoob0VH1fsuCbZCHBr8zVcpZTNdPdHkqKtr9LRkoLOPHtctFvR9U03Gu8DpE1XrkDP5%2Fy1PNnso7Epaf98hAw66SNzgY6pgERmWU2A%2B8PDnkawBrUtduX0XersVo0xNMwl%2FaruOSVMkazW0HrXCor48XC13io6%2F5osHdFLseHWwH3HXScw7yezeKS9lWMEe%2FBCeiKDG4BBE4a6Kd86p6LwXMhWr9Zd8O1mx2Dh6jtMqKj0C5FcZIoB%2F%2BZ6FjWcEA6UeL7gNFuc7hbIqKB6X1lCbr9pqM2efahuMZn4ED2LCVdARMKO1odGXX7vV4G&X-Amz-Signature=15d038b9db8fd18176290a6a5d232cc86873e4514576ed841d0ee437c64b3182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

