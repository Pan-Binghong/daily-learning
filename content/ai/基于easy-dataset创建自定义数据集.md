---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOFYK7SH%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID0DsdwiB5z88Dxfao9YH1%2FincaAdDSzX22o6sxIAlo8AiB5w4OW%2BJlJrrAq2gcfzFDjILIVBstPdfyP8DEIvPJf0SqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FnyhZZ9yoXzaRbMyKtwDzgiXOE6LekCo7ftR6YX8CVu0bPrTu%2FMyfUz86C1oFGuEJIloDBkSF8uuHj2Xw24u0FsrcjgXZPSal%2FtRjQklHRRhPnUBXmW1T97NXrWFTSdseRdyzTtPYoFIKhrjqpzfnFvkTIBObqRkJw9W9ynovWkucvMdF21nQpOZZtM1Z3sQGmyO7MOORausjQuKcndEToo35Kb4zF04QXx%2BomVWE2zTgqkMs1odu3XKkzvhgWSU%2FeBu1Mv8Ph2j0BqWQzqGLyS6ThwNm9of4jhyB65ZYQ44muHHjG7KFbxw5l6SHOW9hr7IJDyt5o7%2FxSPJ45UOVPkhe1R38WHpu%2B4fbukys3%2FFe9dBo1PZpoRb1ofD3xaC7SrGncZWxvmEBboabSw7TS9zo9NxTDuJKjkXh2Gl%2BkkTCNzsXNYKFpQFnlBO32Y%2FgKx%2BeRW3sW5IHWwu5MtVDy833YKhu1yLo4uy%2B5wzZrfSHMhkEgVgkGlWVJcsduJ%2BMjh13YEliR0fQtkaRYZToP7rfu6bbtK%2FLdmXHl0Aw8%2BGET3XAARVwDTioc7Uip7SOtKcr5CB2Vm4P3wKVYXsWy75Y8bStGq0tCeOHNCp9I9mnleINbmFh3mG8PFBWu7FUrFPWZyaHdqBuCUw5KKsyAY6pgFNS%2FR0MlZlL3Gp7B6i1TvSGhalpndklZ7YUcEy3LKx1rPlDuAWmyv0R%2Fty0GRMcgfACXylw99vTjH6eECFsmXma95KDO7pa3opc074DDGWNfO1gdSJYIBgHioEyZVlD7HeqC0%2Fy2RyKGvXqaO4Wq1KOPe8CP4jMjwo1aUuoTl7PpNM6nPEMoCQyxHAiBbyvPmPNJo8EfP0WYDJvIfZfzG%2FWoTqKAn8&X-Amz-Signature=969754610bc3084357b193aa0b0d4a8b823674f0bfb2a430de1614302e2f398a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

