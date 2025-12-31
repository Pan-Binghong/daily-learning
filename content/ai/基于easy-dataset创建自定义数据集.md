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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BKXWRB6%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB4%2BKPyL1vnXKcm%2FH7%2BtRq7f8uIqM4zwVgfS5xPWPqacAiBObaVeW5BRkpQTVo6HzKFc%2FI36SuJ4wLmv445U4l9lnyqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF%2F7BXiBdbmhzo2HUKtwD%2BE%2FHyjWLWulLPt8cc77CvREUuygfmmaout1orYl7sxr%2FVmuRI0l3BhthtBFe3iEtDQJqAmgNmoYJxvTh38dIJnMwjCC0fW8ZJdS9SNxr809ZQL1y3ip0raCWg9FRInFVOSdFSmjhkd9yUrmgiYpls%2F9TV5ap5DXehoglRIa2iRT2Ubxw9dSuzCgy2W101A8v4xBhJuymnLTRDUsRouko11D1tUuN7rj%2F4rTDP0ukmmdS03Y9KF97fL1tCS%2FY6QYzHKlblBBv4hT4iJtcafo1%2BwZkhVD6REe9J80R2dDn%2FS6ISrOxE6eVvRi9DGYaIakEXdTt87aadVZ1nKeo9DzFhs5gFyXE%2BFA43F4Eitqufeo5MK9QTfDAVOPn5AEUSv0d4%2FNGglSMH6cdo9aHzQOcuCASpoYXPb4rHER%2BCpXIrQMbJcBMr4P74UGE3hwRwTJZ0eiKfjNthSvFhEjSIi1u0HKchqs4CEY3axTjA18rVVGRR2UexqoiAL%2FgFW%2B5b3telvRJdjk%2BEXh0w2Yo1m8D4cbmWUUaCLAOur%2BVoK799HrblK0wJ7EyOkhlvODwpEuOf3H0I6YwKS8GqnoZHTxuJ7%2FOx0YI4KGLg%2FdkTXAnxQTdUTVklPEfAEVXbL8wnvHRygY6pgHHATH4x0gYrXk7J3zthoNJMBKURJhVHheq0dj%2FBxlj0%2BEsYPssWlZxwCLoK7KGxS1SLAJ62DHpynB6LzP6BDYXLZ0ycAK5jvB6vJkA3GSCl239ayCUlr7oH15iapSKbY7uqBIjLkA%2FPef3PdhtH57wznWWfoQPsx%2FCXV7e38Y8eWfdI7HTvmiRsavN5erXC%2FC5vW5BVOphrPiE7i2C120tN5bKYo06&X-Amz-Signature=4f4bf76e83f9b703f8edc7bf0c770655927bb9ded40f1d0653f984448f085095&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

