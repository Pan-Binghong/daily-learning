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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZZWMUEV%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T031012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDJ5sJhWR%2F5BnGlHaL%2Fzjdf9kZZrmUJPJoBnPiA4wa%2FqQIhALYOvbaSKm8iVPY6cKGtpejWOla8P%2FIgblQhrJErw37nKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi4LjtChS67mBj2BYq3ANyw1ThWx%2FTHTu%2B44w%2FZ0Eg%2Fbw%2B9a%2Fm1FJPZwVxJG2yOsYC%2F9MsJ4It3bMMe8SYmcOORlKGlxF0y%2BZ3bsq7N5BczEiVVKLj0Pcu3PuNwMhZcuTxveTFyzVcijxDIZrvBJd2zqYfAGvnhUGDlEkmGWDk54xVJe1CTbEx%2FnZsAty5x9qaDnY02mG6lqLHNf4oge5z99T7B%2BZfUdwbPtalQFvn7%2BOxnUvxMJ3KBMUXLwSOVodezeSfp%2FvycukK%2FQhpAZYjOrfWO7l015eWEy%2F%2FPTofTq0D50fGD3w4l6Q%2BfjiplpU6YLDGw3xHVaz1AkYIOBJIhhKkR1s81ngQshJHwKCE7c8agt7sRbVr%2FOsNfBuM0uW1IlEDwSnmKeIKNp2W3mHpsnA3EWcgRIKhy3pSoES53gEIBj13eOXjzzi0O0EUi9C2zdeGEfkUbPDFX5omukRHElnZhd3OX1qZ8q6VXIDUyyD4ZE3uJ2uj6bG13fpnZWilpMps1PUCa7QIzZVZLM%2BAHcEG%2FoWddFa89LXCQV%2FBPWdkqCnd%2F0bl7TKTsqqZZseKe7O%2FcctwDgdu8y7IlJfkbA4lpmPEKt0BUDNsCKj6Z1suzBhhBwn2Eabosfs03BSbLdZCyrtjdZwAQDD6%2FIvLBjqkAdhNupmfowi6Xgh6XQ16G2%2F1i8vnNdToQqtH8GNprYQscQN6Nl3LoLygmLtgixrwTsn05ZD06SQ9XqiFnw98bOVFWvongOEXUG0P1WKHruTdbuTg1t28pdu1mpUu5Xx0amdKEZ1W5Y8SiAFGQf8cjqKWNPrrr7MkiVaNbugX1eGRtC%2FK0LgRhzAjsksUIa80EI%2BxhecXpDmpUWlGz%2BM%2FrTsdJhEF&X-Amz-Signature=69c73219294a36fd7632da543602a7323d1d75c00f86237ca37b88edc61694d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

