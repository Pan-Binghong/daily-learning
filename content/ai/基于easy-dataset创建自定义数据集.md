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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6IX46EA%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCY7T2ToWiEAHgmiTpOr5KhM0hYqGU8EvR4dJ4xj8sE2wIgaBMX8XYb9aLVXySjXZk5HUro0PgmZrfdYpSYJ7UoG0Uq%2FwMITRAAGgw2Mzc0MjMxODM4MDUiDKc3uj7Fq4ghekySiyrcA1ESHt%2B9C5dsJ61ICDOnG8Kn5quZLwUQq43dyaFownL3ffOK4BUJCTOb0rk%2BIkT0%2BdRruWNawwfjqCso%2BXuNUkxUYhS6MwMys2oKoNxbQw5RyHWiw2VU9ioohXiy75oyoF4O5S4lkHi7DVNDWuA4Mi7nDZ4ZeBSwCovsLA9UoW8WhzGJDDg5Qq29xavo3lEK1M54V7Ow5lCHD5V%2FXIt7soSmZ2JOnR0OiYZJ0BvvYL7GD0dbZVo1FlFE81qam%2BpYvGnlDkrTcvjrE454sHAXORLjl%2Bn3wOzAoJiRSUft9tp9tUBYS%2FWWha5%2Fg6dGpyI5VgKAwc%2B5NFkjQt7D4FiRgvRkXeIaT0eTXGvVkDW%2FJJeYNzJYenrS5mmxtszwSkBgCiEDJ4By6KiUEEAY9b7w2t65ntG0a84y5CvNKbx%2FXJvqaolDtqFEx2aLjzyqCJIyp7SGAMi1txEZNGLXiLn%2FbiDdsLwcf%2BhBygMqrDocmudu86gdaple2daJyXn%2FxCXJNS9KvqwrehNfygHNdfdLlj4%2BQ7dggpB8eamhac28SDBmOEPZLtPRhxoekmkrrBzc4aCcw%2BN8ZAp%2BZCBiC%2FTpgEkiFSD5sBXSAaMVaz7Xf%2B6HsEj2uwGHoXowp3S%2BMMygss4GOqUBGceCyB0UO8VWsoce939U0HyZ6JZsCShJZBdRnFCMG33F0eFHSq%2Bp3A6%2Fp2O1coXmfubSnOcJCY2VoOkFJ6Q2ISb%2F0myPLPmus%2BNUM%2F7ltZW3YxmkHQwjAqQi6AQKA8oBVuVfz1ibrn7%2BHrPoLKuOBv2Btx2wKqsIiitvSLr1YyeodfcHkt4QomkxKdAsU3949Gm9nKiQSgwFq7AWwcBhHSmWT9Va&X-Amz-Signature=a5a2637fe48323ba60663c2f3037a0cbdf916694e2fede49c15c4e5e8ba8b1cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

