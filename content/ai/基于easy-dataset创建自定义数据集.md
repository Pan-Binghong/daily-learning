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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2ND7TXY%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQCI3Hf1Fg6wbGgXn5ZaSOuiGPSbbjxjY7xNaE067F9MRwIgTIdLp57%2FQd2OCAaDGFew3fu1mSyq3EgQk%2FoG3QC5WnYq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKDkvUVT9nBUAmCR%2FCrcAwvp0KgzBYe9WkehwnkHrMayc7mLv8iBW10ConHPbFIqe%2BlzqYS7GYslzjHLW8xG1HrSEt2tCaWr0hfInfToCqF8Tf7%2FVApgiKsfkoBENA8kIDBopMYkh5UOCstbXNFlgtE8JJZBKG4uvQ37cp0obaICBG1N5jLzEy8FxtserjE4Rb6wjxm7%2F4ZHuMlj%2FubMo6bux%2BCek8FBSOpaAvRho5KlNYl9R%2BCiodvkrPwp%2FIlZKFBTlCPJ%2Fd7tarY%2B0qSSC2jHJtcF5%2BtdNITIFJPRDnUSq389wxWXaD3L%2B6ygefmc01U3tqerF9Cd5TX8NMCerFVD4ebWyWvzeDHaOMn5S6WyTQ51aJQzltEFZMKQWnZIGmlRHbFgp5QMpJPg3QfzuP7hUsi%2BAGl4qfd9vIJclCKduf29rF4CmItkG29iV2N589o0l3vYC7EAttnyS7ppRKovDVNwF0JN3S60v77tHLcC%2B7DyJOdmiaKwhJlbJE6wke1UCNjbFskcVUk%2FmLMRoql36hl%2B8xhQS8vqiXKEtCvKxWUSReAv%2FXWLcjA5x4GNgkNXmRSdRCtsjhkRPDy8iIOeyUrrYZbGvn77L9ET4q4NQZ94Bk%2BdMBRaEEJYGZX6BBI5qckMGKe2778TMPr068oGOqUBarm7etKBFRBopXvcdZpe0lBcGKykWgxZZGRGtB0Oh3%2B3tN5R7TSCDZJmGjpL9lZElrqHPhXO5ZANP4YlJUqIDNACri6%2F%2FyUAapJ80OlPVDlL7j3aaRDnIwQDwVu1Br%2FaILRvNKpfgN7Vx3u5eKF3DkygphxZ6J2DPhCm4soD%2BSK8ER1lXkyfWy32v3e%2BHXIITVHdCR12OB562fJYbgJGFYns%2FIAh&X-Amz-Signature=dd07aa3d1d80626813a2b6f587dc9b8db0e7cc0589cf6f762f89dd49ae68c295&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

