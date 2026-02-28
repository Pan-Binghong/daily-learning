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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TNEHWCI%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031121Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7gzkZ27MPy83PxefRjbbgRTsCGY46q0uHD1aRHr6dAiB0L7QeSmlk2k5t5OxBBU3MKrl7r%2FvzEsea6RpuW1PtgCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMhNnzmZjWzvY3VTlhKtwD48OlcHw%2FMrANRbtgJFoc3kN6QFAvajLYInSyeS6%2FcoiKQ9R4SUCkKFHv2A%2FkXbXACo6ccuq5LyZnaFuNVsBMg2gDDqLbRzgs%2F4Za4qXZZMrMIc%2FWgrlcEl5BOl0S7aYjNoklQrFBwk4ETos88waIWUIAGIkZZkbFKw%2FVV9Uzk0VU5BvXsZwnE2v2XSGxGwbV2MZe9APDWToT%2Fo6iM1qUdTcv1f9xVroqGkl6h5Aon8x667J0WLiygtMwEtwobztA1ApJevBcy2GpgMoHBwK9HdScZD76tum31XEKDVYf5A5Y5OllASVpq0WpGnGCgXM8ulh8V2vwJ80sWxZZWO2VsPE%2BgxqZhSTGVq02NEvy27p1qo2g%2FrGE1ygbQ%2FQ0ZS3UWePGycFr6gkGw3EpMilxnbVN8EUj53ETvUvpak8naNnaXVGusT4qc8%2Buql6J2YtHTmeyTduVNesu%2B2VYSuPM3Hr4kzSV%2BO1RqaGBEiyo%2FxfrpO3uzxZpUr%2FYNPVcz%2FH9kxWdNeFUYXoShr5mfpo8PfhXUtMvnpbWxOakmgaSBMTZQjeyG%2F5HVO%2BMXApBDs00C3d9quV1zMFEiojk8mhAiQf07xroMnDCa6WtaKBl%2BjDsnjhlDENFJ7cT4jsww5aJzQY6pgGUbix1HRd1jOd4bBLeIAqU5XH6fRVlx%2Fb21OAx7JOXBXLI21mE94Px8ZR13b6dHFa7hxT97ozfV4uEcXLzbuyINWJhqsHTI%2B6LeVx7mOT%2BJ1fjjJZik4xPyJpkjxvICm2mppidY8Nj4MfzyPAh6bVeCdP4vk7%2FGAjQ%2FFA5mkNj%2FrfOI%2B%2Fj2uVMVYZaPzYLKpH6Iqca5Xgj6Kzg3LkR1XzGqzBB5yDC&X-Amz-Signature=90f1ef47149d66cced3f8f04251b3212086d38cbdb3f553138ef777220e8f4b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

