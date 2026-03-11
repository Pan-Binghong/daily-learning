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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RPO5JYP%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDW%2FAu4mQfeC4iaLum%2B7yuiJ4N0svVpU73hfdir3%2BwrWwIhAILTT%2FEGiV8ud5RR%2BgPlcLmyEJy3uou0ROp5588QyG9kKv8DCFQQABoMNjM3NDIzMTgzODA1IgzsNzZuo95jxzTlqxMq3ANPM2PAYBWQV5uo2k3qY%2Bxd2aSPyOjZSrktkhJnq1qs0MXFPtjj%2BN0x7tL8DZa%2BlIHSizDZj8Ugls6RH8PNLFCpQFi8AZLIcUtvw0dRm2h2tqtT61HFVhbwusVAWQ800FmPVXdmTkBha0S56gZd1AoPblTJeYru6MPapMYrMYjT1ufwq8MeOYAvUaerZ0OZx%2BNdA%2FWPjdfaL4rQzs9KFc36Yo%2FODrpqny6Oe1gUgbAQYPrMirIfHBg6CTd1en4cR0v2dF%2FgAOnhwkIuEoaVKbdf9PuwXAYCGCDK0ifv8XeN81NHMVeP1vMhoshYk%2BFKcXUnt8ZLKNvrS9pcnhw1cc5Gr12n78fixrcnGCxJGYhcspcboqD5RkYON93dATRc5LJDlkOCTS%2BJ82qvvcr6n%2FXgQAHjVoNf0Vm8da6uX6GfgmnQNKmUaIY9FSmIe9QXEAXIo1ST0MR3Euje8EYDK2pxXgowNsqK%2BpMEJqzzEE0%2BKpPitiPgpmTRqWvyuxqJOBHW2gSl1EpsHT5SW%2BwpglueP1sVsdx3XJnWsTlZBM8mrzPLH3GRoJ5Rb1ZFwt7XyckpzZuD93UzZle9iuqLFUyVWYTX472GjilGbtjMsZqG6mn28SZ%2BmSSF5yot0DDJwMPNBjqkARm1H3Y9JFmoeLaJIolzu8ZTg6Kirrd1YX1N1PMXDmNxagV56ZNSbJsfyyDQuKHJ%2Fseul45kB0L4Su%2BhTm5LxYQK2iYl6pO%2FZMq7%2Ff6rd3mABESkJ7kePopMlkIiLl5eyq31J252GNozZn4ZhLAVIb8FE02MwySO5v%2FEMlEbofBMYjf559E2ZIHc1uV3NXudGnXG0Fz2bF4cgoAgtdfQi6jTB4ow&X-Amz-Signature=4ad5d80a8357b4a582b410f99ef1267576dab46994b122df6836eca2d6e28c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

