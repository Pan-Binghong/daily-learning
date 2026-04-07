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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGPBO5LS%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDJShxxrbJmRJCLoSTohcqP3hYHmbWjtbmyBWTSE4bRXAIhANHOqUo0dbvuYpAqWBW5E833xQutYH7VDjcCBBU%2Bun1aKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw2nJyOP8g7MWTNcGMq3AP1fw4Esyfb50saIGnu9PcggGsuwBrPfrv4MQVYMvfNecYY8N%2FV8h0JVEk8JXjeVtJnZHg95PCZ8G0%2BZ90D5nfAmET2SQzBU5KXa9oioUmqOOZcg7YKGlm2ukFbWaVbs3%2FWcQc3SIgeHnREcJeiofWbrZzK9HlYtieYrkAIF5OAFuDHarYpmiueW67d8lfeyZrE5GpUO%2F9DMMScZSJDYgbe9YqKBUa0kyCFAgCPT7HX%2BONcrpqppmYuZ5G2ooJnEa7rQzqo6hQqVKVnuZ9%2B1aE6CPVJM1ZsmjB5BexntXX1Y%2BHhkcVj139jQ22t%2FOr%2BXvMQd0IZ26fJ8KhoX0ArdA87S4B3MY7XxcLuWM%2FoXKtCmEdO1wxf6OFCM%2FQLCn85o5k0QdUmNLQ4BS7z0vdg9%2B0MefgBtQvYXnGTQPkUUsgXd%2F4rbUMX%2BzCqGxt2vnJu56RiNSqoWy7u9dODIVCGoV7a0Zq1ZzTh362%2F8dxYhrdlFFxzVSHTiwLm6C0wYglv7ho36HCVhntA5wS%2F6elIh82k7inww2zgNuUD7%2BAXyHgl6bb57MNPj1rMFUfYchJ619Jy0PrtZdB741BR0TE1O2R%2BeoHOaRA%2BDn3P37mVZHfMXZgsrE4E3fXL1AxHwzDO9dHOBjqkAcCXi4WXgmTe4ERAZLFM9dgeluAP4g6%2FWwlzb2B%2FDv20ftxVGbJxuQPVNpqh43xgpeoAQuuj%2BaCTJ7S%2BDSutr33DrhUlxNTd5EBkqlWcTXRxumBfvnk%2BZs72sVSJNYJ4t6gAYTSzCCIB%2FPDyrlLiGBVZhmpTHlG9gPF9rNmVPyEMvnYGBiuj%2BKjvApMszcz3v%2BiFwSUsHB9sg1voVdNLkpI0lxWn&X-Amz-Signature=8b12be6be957f45054ec5c6284760a058b42ae8e2218c4bb6b789baef9a07ea7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

