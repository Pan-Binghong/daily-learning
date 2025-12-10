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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTF3WUK3%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVzhS20yCfd7Lw%2B7GinY4%2Beu2aEK3IeLBqaw4FMYHMVgIgRbRPZCYd%2ByBlQVnbDxZCkn28%2Bjhg9SzwfL3oaZ4Xl7gqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJxpdkuVVoHMI%2BUySircAx5rHFFIsAub9WrC%2BABlyyiQL3MbFbjztY7YUdcPGQYadT0HspQKdJ8WeUsGwabhs3IQwQgPDthj3ltyfpoAvjjpFEmRXqJufUtmJEY5GbhPIM0%2FsYDTb6fSxkv8jhrkmBf03ytkzE2FDFtC%2FCgs84KeeSRbV1FFh%2F1aK88MVIyHMejbL4aL%2BaJ6EApnwMNfv8CAg9lXHQARg4Qjb%2Ff3Q9BR15UO8D5g7L3VSInmZYVBTHVAbVD3S7fykImNB3s9IlCAtyHK%2FiElLPoiePWPGZxZhiTSiYtR5OCYHb%2BFYiB8cyJ1BS26FCh6gCeQx3EZGNEGPFdM9QF3ZTrg58ZXT%2FH3CpTC4THkDk8rCVEiZzLILxJtim2EFrYYdfzyEVhZzytLHTnvspjqSDILRG%2BWqezwl2x%2F5jiAA%2BCBU31L2jomS7Hz6QKk12F4uBxHS9w%2BeBjfy27EKnZSq0YBXNlRmtizpaVX3VZRsqwWEqDGknIqrYjoyPy6xOK2qDwDaKOwIhXJ26sZEybBZWcaBqezcz0wX8rqU5zgeCSc8tXTUNT0pKo0zYNrnc2w0PFiyNmbmgOiqkcxraUXfdN3jpgvOfdX3KtitobfVBAnvOD%2BvrUUhPy0jgmnKMxTiilVMOzD4skGOqUB4qt37cWngM%2FTbcgQzCvI%2FhTTEo5Kph%2FykX5ELoJ%2BnfuwK25WGpBo4CZP3xwNdjhmMjYSVyNW5GxAuDb6ucojlfGWBOXOgO2ES9Ukg0f7OfevGoeNFxckSy82NsgJ8h42g5dKSfYMgqhjt7bqq0LmifFFXcAW6E4ODFIOqE%2BTp2olIu9x4%2FujM3fZ%2B%2BcBXSsB%2F1y1sSL0I9OjRx8in9a2hbqrsKW0&X-Amz-Signature=051b3dc1e3b9d5df492bf0a35d54c4bef2c033e2396f1e5e4724e8ed4ed57516&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

