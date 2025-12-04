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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OAG66I6%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQCoulEKsY8fPMEIHojVT2M0QWvfHDiNZh1%2FVmWc8wnKTAIgB%2F3Vn0YWfZRr3HIYu3w7ohf1GracPXrblM1afBV8JUwq%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDNBfCu6a5Z7MvEnWhircA9PpVcap8DXWShN9xj9TKV245sh9JEMCJ%2BlIqt%2B%2BTs2Tvn%2BMHxZyaLkmC1rcIQZKcjMSCgjh%2Ft5GhgQM%2FJfodZQPsW5iaMB2qwP%2BAKpL4Ll7z7P6rThQut2kJTpJQTZcvvrOVd1E22nBZZtnV4%2Bup%2BthSPwsd%2F%2BzeegLvCnIe19lOUFWPcr%2FhyPZDC2Iu9nH5HJuUCWzCJDJi%2BMnR8unXAa%2Fj%2BrryTgURLXnoCXxnr9wKQSXTcxI4kKspJKuLj%2BNA72cyvvGd3ZCmg0n%2B1N1GNZBTGP60TuKVTgyGOmrZGmHkrOugNLqzyH2VCezOOsZTI7OhkTRiiKNB6b7dLXX4saWrIzNU7mMFpk%2B1dHBcCCvSeRXVy48g695zwSOFrR48A%2BJWYCsSyt27KlqzxF%2B0x5gERpZYXPfbMhsm3rqg3ukNNPtIUfnlsg0UHkAY6YPIgIwSwjqY9aQ6XrLJkqSztSj0nfZapWvgXg2XguRr7nlFU1yxz9mlkjAh3DC6bNkfWVdOas22wRaLHcHiLJX4VxSl%2Bt4xfnDL9kNkFZDh04zka4Z%2F7gLWY4yd3zIzO7EiCVKCr%2FZhwc0s4kAWrEyBtbq2%2Bvkni3%2BfQLxXKzBbS9VkHXBEZIsYYtrkwocMI7Vw8kGOqUB60QHKiJk8NKbaeJkxKS7epPK3ZB70c9itG3HP5R4y2nyA0dWREa%2FmIHZVqSDvbuJxxncxoqFijk7ZTDvlZ1FGR8j9VqG11zFBtofC1UVEf8Zef09PcO9ou1%2FeTZSvf87qh1X86UXqYZcKvPFnN%2F33r63lHoSZYg5%2Fh7yuM%2FAbjR6ji9Muhl%2BtqhO%2Beo1gaYx0l5KbXeeO7AO6SlBX1%2FYOdNNGOxB&X-Amz-Signature=bed78ed980855ea48ffffd3496834f3cebb88ed03c122f335f7b08f5e01f81d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

