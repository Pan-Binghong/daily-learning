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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QBXNMPA%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwEkhxc0fzF3heAgHnLL%2BVnPUJBOzY6GZ0JSkhok6dqQIhAIIEDdHs%2FyM1bAwqIuOcIea14fFfjIqqYw76CcFJjZapKv8DCGwQABoMNjM3NDIzMTgzODA1IgwlpRgY6XqoJUrmBOcq3AOUBD1yOHv4dW40X7nEp60lS1Si8vUA6ytVWEYzvj3q%2BTI3kl3ZUgBq5QBGuUP6ZBbT%2FcfOTVxPktTT5E5cyIVCR88%2FHb1u4Tg5gTMC1NzNFcdEVjrER4O%2FPznfwNEDSOWsrYKR7yCN5JShVYqHfxaaVJb9y4RBdMbE%2BTUAJA0W8Hn7BzQTQXPj7Z%2BQp5D5BbGlXZR1%2FCGe4zmsIq83t34cAmqSN6voJGfamn4aWDe1xKQpjUqqwDpoqoiJu2MasQLxe0QjODtM3Nh5YibKaI8QqiPLNsjgeGGUZIVKdj8M6og5y7IhY7CFTzdhu%2B500BVO30by2iFQI0MPWfUjDJZ9QVTQOruI4HDSmMsFFzPnwK28IXcituMioV3%2BI91yFC7mhS0Mmd9mz%2Bbp3ekrR%2F1MDl%2Fssu50NjqLWHvHXeQOzUpMwxgLjHAXRqsPzqVPerBGZjINYnusy2l482dBWGSD8ahwa3JYM%2B5r8uTdyIWANs%2BSTduprzd71TmB9nJyTzl%2Bg4iqW6VfGsRJcQ8DmTAGEgVdCGkVmWzmXNkvtWVA4GuJpqj57XMs7OW6%2BMOjTbr6BQ5rgt%2BNIPKNKQqmA9kLAzVSLgUqUxL7nIgk1fBcc0k7zkTEmlIVoYNkmTCLj%2FfKBjqkAY66gmN9K78NNBpK0CYcu8JkPMlDGNW65pYjbkxkkahEUFwIh3KcHSexZDyVTbjLsxwajNpZhH3aTeliZYUEyG2KJZzVsh%2Fisb%2FYQu3asaSM0DTqYSQd%2FSLuPZfvgjcJ2E4L7BjPraxDvMNtbRcljeFZtJw7%2BkmyRmcxf9g%2B3CXrZrRYTI52vcoTrxlRGLdVb32aMVqqdYMjbMLYER51nvpDOOdd&X-Amz-Signature=02c8bd4fe0eb7a423b9b37c6c98a51c91a66b01bc30d66e02bc4ca8f3843dc44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

