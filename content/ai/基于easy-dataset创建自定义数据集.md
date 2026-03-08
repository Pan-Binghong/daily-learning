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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GX6EHNN%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDRylGMiNY0V6NCtT5mX6CVpJSQadBxzex%2Ft7ZoMnHObwIhAI8yoVayKYL%2FF62PCMnttc2cZQlZCggAJ1kztp3a1rYxKv8DCAwQABoMNjM3NDIzMTgzODA1IgymmKA5H7DxJxT0Fogq3AO2qmcWvCvYDSIRDs9XMvLtNmGmG39x6f7L8fUzqUhpGKCYkWahOc13HU9mHnAkUHjYjoadzHSVQQVvrV6Tnzh5dbz6BxGK8STGiH8CsF4Utqgq4RCJ5V9T%2B2OXS44N5V%2BIzGa4EnBIb0HnQ9SkRkI44xUiW9wT8Asvmv222cGopIxzR%2BGB83jTUM7pYyte8sQnl2N68RQ7RFVWPh8ykuqzd4SzyqBv33KR7Dpqg7M4gpLRfgSJ%2BCaL790dZAHNS5naUf2oBqGNIoz34WSSQmCiLXFeD805DTjDgOIJwSkscbgvv8s6eQT6L8LtsXvcOyYe9UCRNHEZzqnTU41OSVZ%2FIYk4ZTdq%2FGUsngDGekWEjBcf%2BbXrDkNPKFj7zlN70rHjUnfiPJ8GSOkl0figsMcyj6aTaxLwp%2FMMRh8dnyLr9rEd06XHtUI5QQRaGt8ktr9TFzFY53sOewme3PgxoGb8qhjblceSOVayvmutbDbYhdolY%2B5BCvaqOELmfR%2B1m4LR0W8%2BAvIDoV%2BdZ0BOrtzP10oyQftuUdijPCSRqRUEYy%2Bo18bTuW2ddI03vP1ZvZ3wV6DgFxyOI4C9UufhTMPigHrsgtAVSZtbm612jy840R6QNEfAZhFukCNx4DD0wrPNBjqkAdASEH%2BFYZBwOzi3wCHU8oZ827V4iI03Pvw%2F%2F71naGMcLP3YdY7VHXQ4KMEHc6Z0rY1FEHaE0EXvOuKaVS8aIBZoq0%2Fjk26T5vnwwEpeUSGdx7ah3p7ZW0mo7CIhA8kPUEtO9TRCPKscLMuyr8%2Fl70YS10aTLdWCclUCMYUnKZ%2FJ%2B1uKYIEsJ%2BU%2FqJj16QXLLTBDk7YovBg1iztB0OFsa1KHcSTp&X-Amz-Signature=dbfcf44d76d215d349144b433322a73cb308779a0cb7e2e621e66ec0571e0462&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

