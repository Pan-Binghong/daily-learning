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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XABUU43O%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQCkF4yglhtBJx85KEho%2FAZ%2F6dyy3F1fc7hPqEXfocSuwAIhAIihl9r8%2FceACas3Z0eWhUN4bWTwQBHgzTjiJRE2vdGUKv8DCAIQABoMNjM3NDIzMTgzODA1IgxbOZ857dK8LD3Iarkq3ANd0vyh4Q4boDDCMfRQcZEXRB0XO50ooHEK6Lj1qJI3pR%2B6vxuu50qRW3Y4Su8WUJyaMju3gBPjx5rKq53%2FDJl%2BIVJHMk1Dla518zmmG0PFuTN%2FBZvYKFdn%2FVIr7LRgOkOAYmL772YjPF5xoNMQhxxpcoZv33VVrjLH8nS3SgiIVy5bmOkdudA31zdJB%2BtPcOW8ab22JNdoJzBvrOmu%2FY0iad3kLAYDQRMCGv5O6BM3QMcR3KSlNzq5j%2FRgWJKkcICTsbJx7wjdHHaxzchpX7DsbYa9AQWcbHIXweIS7xYDlPYu2h%2BuEkH1x5lC%2ByjXMnGeII6OnAoivtwwIMZAR1tlS6q85glWSiGgL9JEm%2BVKPTKl6txWdF1AKtpq6sLCtUOSCblvABSzIvB2A%2FGql%2F9xs%2BSf3RXfU4JTwgZQ6H4hhQM0pqceavIkhzHzCzxnRrO%2B55MyZN8L8RHE6DOP%2FgcmXFNZ9Ddqxq9FRhryZfY56TZluEFyHijkwIrnoJXCq0QQ%2Bjq%2Brk%2FI8kR3y7qI%2Bt4qawymt3bW04vMZy0tOzvSy75bKdlZwp9w9Jn2LsbAFoeZIsPw5zUS4vmxWKzhblpemEX5KS5JijvJfzAkEpL9JnxtG8dM9EBxeatMKzDzg%2FnMBjqkAVg5StZdwJTP03HpxEunGOpyO%2Fqvah7WLnhIwthrLQXE9QaJD4T8Y%2Fp0fIC97w4S2jmu2L8e5N5rqPqW%2FoyinwC1QjioK9a%2Bvc5f8%2BLlmXRFDwE8d8h%2BOXOHapwllafOBPM129isIP8K%2BFKBtGFObuxjFs0WSD0rYTKfIF79aazftBQzMU8OAFDMr3YFXFwFGIuz6axg%2BShQ5%2B%2F9nY3hVS695buN&X-Amz-Signature=a5dd03adbee59bf11923d65ec75bbbef39050e3b59376b70a4d610f0ccd103c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

