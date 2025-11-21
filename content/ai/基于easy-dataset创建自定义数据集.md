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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUSBKJAC%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD4ifwzR51vFzdF%2FirwwWcLz7sSYUIeH6Yrj0sAqFi1AgIhANhxiAZGx40zQnkuOkr9Y1gR%2FiRhrH4tPaoZTBXiNzUaKv8DCAQQABoMNjM3NDIzMTgzODA1IgyVmKFPSjU4JFlDS5Yq3AN5UdZuNWiKizBpaeMLvDkXZpUghOVfM5XVxrvm2sXpcu8wXtRZA4dc%2FtwApCzuJhiwFySIHYKcYmfwMCy3mMhimwAMM81lpCQHyXpGZRW7g7z9Ge9dvU5hiiDWM5Z2tbNwV%2BkmGH4Zu%2Bp9Ku0vsQCyG%2Fc%2F%2FjF%2BzwVuwUXvuLIWA6PwktSurwmb7hbRkLRkuVW5Wn1so6YdGJ00TdwBeE7TF9Jol%2FpIZ39GFUWBE5nUlx3W2ZKmaBZlbmPVtsxXc0G0u7Z0Yo2D9gwDOY4mqm1k2KKMuitmpNxya7fSFmEG%2F29TmDxPZjDBegu6IWVHBddhOkLqdJCUrb%2Fl7iBC3e8rdA9TUMNQTdIeIhsAlBtu5ty%2FOfVd4eeWBsEbPIQspxrUzW%2BTcV62DmgdWEP7S3x6Z4sIamsLLaLw%2B12Co%2BAQ4XtKBuBTvYeG37PBLUKTMp46XrI%2BiOVkYYLdMNTJZ44u9lDj7ccpD6rpK2VhhS6ikr9dj7vUjFDIdP0lWUHovo1uHnOr%2F1cu6Ij1RCVZX6F6X8ddodHLuVJEFl0VMjTE0fAoFIPKtRFkf%2FToYghuJMGfGJm0%2Bj5OWo%2FlI45gCkN8bFKcr1tj67GuAzZrYj%2BA89rxtyN5Ia7V658AQTCrn%2F%2FIBjqkAV8CgDwFICarEKHmwyH%2FDYFD73yyv5pePOj%2By8%2FcMQ7SoVhHPA7MCitzM7OLxnfnUjQ%2FxhEeSIsvqQ5N9lghUbq4tEMyeocgitb3rCsd9NqvBngyNhWgt5%2F%2FHYLXXnZVIzPkN8RtXbuHWJ22pCzH4nnLzA%2FqFcvmjK0%2Bo2NyDfuWSZkOWopGUQJWi8MOav%2BJSwtBnzvCoP3EcfuNR4DlhX7UiCR1&X-Amz-Signature=bb1f2f96ec94629b9937bac33a6c0085c4548b55bd1ddad749bdebd688859a2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

