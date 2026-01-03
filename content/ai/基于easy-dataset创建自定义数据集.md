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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSW6NJ5J%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJIMEYCIQD5bKqJuRan%2FmlEOIaw%2FbBdnCf3dzI4ZuOsEXWBcwWd1AIhAIsNwz46NX%2BYUGAnKFZt%2BnVWvi2To5tEZG8kIOxWbmUzKv8DCAsQABoMNjM3NDIzMTgzODA1IgzQb6eS8FcVh0PIbJQq3API4xXUEWGx12UEYzUjKPLn5Eu1PNJ%2FZtxS%2FxJ1dB80dGHgzGmyHBk4MrKbCxUFAoeQJ67MNPhmhXYtmdxo5hJd0PGzUhcx5rK8BLptXYm08in2%2FhnA1cUwbBSr8ifGt2xHPaBfy12FupQ8igSuIeY1V5Ky1WjfQjvAnHnbWPiji1w0XuI92K7SmZ03%2F7udWfoqFQyulk7x6DKxckqeEw21k4StL8jWsCCwUY%2F%2FOIXjRSiBBw7jeYtY647QDLuF93DOMcs2P0FYwL31UhfffADoEhjmyRUQswsEQAv23%2FgFDE%2B2sM%2BlEbBRvI5ETEmVLM8XJOOf04AVC2o9NBzRRPTHNlwpnGpP8IIP3Ya2lDBAoxMuqokfBcptK5Kn%2FKr6TOKiv0yDdBApgDMmM1Y%2FLNeZtEpMePYM9H5LkN3oUvsFScohVkgK9T9JXU%2Bct8rZjMPwBzYa1Nl8C%2BXfeSDUIQmKtSDFVNgqFgiFG7DhHQOdQn4JAHhzjgubEwYuHJJssc%2BpAYYZLKIztyih0H3xB2CmhMeBdeDFS5Xr%2Fo7gvdhZmTm2ZoEzk8Gi38uv%2FQHtPn7h8gLJW83hwRrm5eDC1Voz15BBtOPLYdvEivjkyTROMOeFobteqJ9Vee4tkjDq7OHKBjqkAc%2FLyW9eqyteKuFTbmkGvlFCfiuHnQQ0W0c%2FgZtA5h5vp57gbJHX1dx7mtn8oSZXBWbrN8oadg4UJSSl%2BycitIULmFXHJr1IbtkPj4brkcgAT1nTOGub2QnZmVRTNB5nByva2v4QBjPvo0baSBbLLHs318zqgCsXPgpFnhu3Lqsvz9C9wD83hS9aLudp4R8bICqxdXHrMnrJjbMKpkv6I0iM8mtt&X-Amz-Signature=5c8bad010fe84405e5081705abd4b3ab052d8e51834ea35c9b36a4bcd8705eab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

