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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQBRIUYR%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQC0v4wt4zmiVzXAxXPlJMeHnpw%2F6eJMp6YE76w7ePyCsAIhAPyxlrBvcRGU0Zj9LYNKh4QvzEhVic%2FpFITRew1usDfuKv8DCAMQABoMNjM3NDIzMTgzODA1IgxiMhDnZOG%2BkGWOO%2FEq3APXm7jhTrYkOEd7fuJbcxEKjqqOO3lmmPBKpCVMEgJvntUnAN9sB4E1%2FVVIDx3%2B9lDm7ksDbA5dfwBfLmCI4UJD%2Bl4kBTcPTV4uF4dvz%2Fyxt30%2BT%2Bftv4lnrwTqYv9L1HgoduQl6CLkIuBjK%2FENcv3X9SVl1FDVJu%2FUSEXftOMpOoFT4EgBWI5i6bvBPBs1THDkvRImT1cB1OocFsa2EFrmwV0d3xVdJOiNr9T%2F8V4QzM%2FlmOXoB4k%2FKq0qWivWPZgRk7nybcDpeMhdUBre7mjYMqTSLyf05cYDPxV9o%2F6Q%2F%2FsGkviAQDn6E6X1ZyxeC5NyJpd%2BCYbot4RDhUb9tehiOWkwE%2FxjWFaxp9rk9ikMD9rN7VbftbRGQPlEZvpGnmCpWubE0hZ7LNxODkDmi%2Bx0xezVRlZo%2F9yuwo9yKsDFNP4vIO3lnzV1cJs93cjFlEThFqXERmFG2YZLgIz4sAHOJTkOZSmt1MvPXZTuOAwMOB%2FIfEiw2LXlYdvSsFGxLdEYgaiR46o0QvDYp6U3aSYqoKYrTZHlI1k04VohNKbbtJzIamNBwQzXX6ZULrO044Z5BIV5WJ2%2F4OAsPzVJq3qkUBDNUNVikPwkesUsXwxWbfKq%2Fqipez1t1s%2F34jCZ%2FKfKBjqkAbGAvx3uLAI%2BiUSMGtjVKeu8AJ5VuSvtN76%2BLmHjPrIXf%2FY4Hp0liY8SWj4LEY%2BgC%2FAx5kgvruTNplAoz9xlpC%2FgqHhbX7kZKox7PZvctdjlh81%2FeoAHT0fgW7qpxpRhGk8REsybc4q6xPVIKa8kGDNY5ip1dbSpt0fIAwDuDgaaFOiT%2BjPP1iLDPJBvoE0K7WRZDUyMs0C7AVexvi5sE6ojpt3h&X-Amz-Signature=5f809b272215eda1758208771ea335083010970a094632e73f443e94182876d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

