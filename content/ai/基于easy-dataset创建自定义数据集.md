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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQKXXTWV%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025757Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQDY86gvueLXSNOZcBaFRUFJnRtXWTa5o0XAixS3xkQ%2BeAIgXKzBbQQbbdmGh%2Flczr%2BZJs6lzvNbaTQ5jFzsWOCzO8AqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1DEVsPz8wGW3F%2FoSrcA8eRoI9%2B1zJUBzUEKZMnWOCiLNlGVrlMPHSS0ZZl3JPL1awP46LBRrgDNUT6%2FqgVKwbzLEclSzS5OhgaJEydCP%2B2iQb06L%2BBKM1itqryrXGf9LEzr%2F7ZSz4m2AYOOUPBvJwZG2OOA5af41i4td%2B5K2ovwolM8jVhJdDW8USfCkVUB0AVRpha6ktb74Y5JQ%2BrM7NnHdDGUuY9lRG7FEZ8cqfGRf9Vexnn4d40UQS5FObBW8eSGj3T99DSbNjQrmmGsIUa7Z9UgZ%2BOMpoLf2BEQGHAw6nc7yyq0K25FoPnHn4PRmRQ2acVd1RoxbGT16qli6jck1d9Xcm%2B%2BG9u%2BiFO7dVZfWoeM8HTMbqm3D7k7Qolkahoc93tN0mnuLg26RG0mgF3GWgv08w8CRuRxGgK2gwRhKs2DwhhBkfxSw1%2BQ5lrvX8DT6dssFPSN%2FJD1NbdqjaMd2d2FvhXbZAjA1uVBXpoTo47DFS7NFMaq%2BP93ipia6TlQuyR54xZVzaM0%2FYQ3Y10%2Ffkw0usqLC0VYZp6XCSVM70QwNZgNzIkZjiohR1wR060CEqZYw8TfKTyKG8IMr%2FoLF2GmfhVxcC5n9i8hZ3Q4L97Hvoh7EoKh7SwqsazegfuJt5fRIHHXv5XMPHUrckGOqUBoITeihWb0QZE8fQfPC3kyx1FXm4lUPyVndng4sTOILnt8v64jxynEaaaohLehBcGPFUVuQga2%2FgW9XUNoC%2Fz%2B9%2Bjzw5%2FqyXWUbnfm8rI3ScBfkeRhEecCXSZTNpdB8%2Bo7t6g8nGfWxtA9OePrij1bMdwcK5n7KPtYlpm7JozhfgFvbAdUjfRwjXEiRDvOajO0TiiIB4zoNYEwTtuOUsPbWNUNMWW&X-Amz-Signature=1eac9feeaa942b966889f9475955cfaf3370a21981f8ce71113f61c6df04aa31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

