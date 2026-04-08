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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAW3B3KT%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIBYUS6FlLCpqKY14XCcQJCxprAOmb0Nd3zV5KSZXMzcmAiA3i%2Fbl%2FTVWzk70NlrkSWkz04%2Fe%2FE8B2mQvkxOCgqvikiqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhjA4aYQ2eBg5UKx7KtwDG%2BVos7yiY%2B70Id7KUfD142ywv9GBm73Yvrm11%2Fq9plDQa6gCJkwxUGwJqjb8vNkLbHAEU2rrqHuxlLBut%2Bsw1f3o2dUcIwVn%2BJahpHHGo5KM392a8EI7flfZmcojJ9%2BSFqAgRk3SKTx7YbK%2FVXluaQ6yI%2B2Iqpc63NCtThQ4QKB8h6hoDT%2BMpCyW1aJOVb52B5YK9SEDXDlO%2B8hBsyukGxuJMrnOstuRIxYSBAh46BYxy880olXO1s82tAr7825O1QOI7cYhu2c5QfRXf3v5eXB8l3Y%2B6licXkMeIx%2ByDDI713rhefuP0ubeb%2B5xasB8rPrTFFm8j0jFfhnbT495xhXDWWNBivX0LTMPUU6uJHG6iiRAw9hfTbYRhpCxV7cMuTTtgaGnPGe1KQPgSFa9ma8nrYIVz9MpUmV3lALoK7OrWVM2FPES%2BTYiIAKk9P%2Fzei5%2Fk8y%2BkkqRBuu21G%2BgSs42l2O1RLgaCg0qfOHrpc%2BtN5r1P5%2BtIPW%2BPGtpzmo4NOQw2k%2F1kE%2FnZTY59cHGvOTPUTHy%2FFiQJHIS6NrGIXjX3tELxMPwOpnYnAteVMi0WkFZm3hM4fVbj0I%2BI4NMV7lZhPEg27xCwS7mJRGhRTs24K11YMz3HgzcyM0wuYjXzgY6pgHrA9P0mpKpQICNvpA9H%2FLt9erRvIqCtzPMDyYA1sw5f585m1wf1FzSUXwPfahAWKDZpI5rhYl%2BlSMSqVHii9RfldKlkUwsDVr7qDXjUfncfrowyB5AkaqX3gmwVLkeKu9rMbRKbEw1PCADVSI0ut8qktASTjz2zeI1dC61yYRu12V7QDzEfqeUGuQA%2BqRYbqUIE3sfk%2BzTxXLaqI%2FZdZai1kZTsGkJ&X-Amz-Signature=dc7e0101a54934310584626a68e23c7348a8e5f76d7f5f2c22bb950cb4487a75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

