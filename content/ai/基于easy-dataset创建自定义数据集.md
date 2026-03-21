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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBSY43JM%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIEZ2vFu78kSDpv8y9ib%2FrHyYIbAOWXZPcACJm2JQbOnEAiEA7o8mYAZQ5KIptSNPOzPPPel4rrSaKXQ28BLIJyqRHUgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDCeuDaq4MtrYwC63FyrcA0Fk1kgjoAIlR5PNv6d1XxE3%2BsT2bgXH3cUfqDExy55Q5cteWKivivUEpnOtk6dxXO5nxCA%2B4bjkaVNuqVSy4H7OdllfERYYIC1USPOVX%2B8JKdQY4391s0B%2FHqeUrPNzq3WhlwEQX6ox9EsV%2FQ5gWWoFtGv3NAHcFSqAGV%2F0l2NPAxvZW%2F0bw0ibNh%2Bn2aALsgziW6cuSMgb7Ot3S%2FfCv0oiNuRXWwtv%2FFk01OtFkgNlSXOLoyPynlvroUeyv4haWxB%2ByHNl4qLHH64hZCrwP4dzmSg%2FccX81Tly85dYaXpuSw4yGXQgL%2Fd1xRgpwdtADXMnPqV55jyj%2BHQ0OkyiTq%2FKANkFjinFMgrBdYqhylOMwxXAmvBDcVNFluvFYFT3Do1NVdzkigSMZ%2F1YiZQ50bRTiJdXn936Ll%2FffP2kTtaw56qXzOircaduT%2F1oSAbP9AXoRhHsRdaNQrl3OF%2FR67RIbCgLJTnBl55D5WXiH%2FJ3LboocZAjwPAiRUlQW6ldBrLAbyMsBkM4rDHSv9qvqE3RDKuuebI1lo491BQed6boYvVvley6LIQURph6Q%2FBXvQeYiu%2BkbQxQNsP2uxZTqCOsuliOwBET7PWTZ4n%2F1bZWoWwKnP5QNqQ7hgr%2FMI%2BP%2BM0GOqUBIxW02tl0%2ByvrwD974aQTddr7OMJ8k1MK2luYnEBEtlH9o72%2FvAXBvM5q7j3NZn%2FslPt2sutUqVjOHNe8WP6asYnp0ceQAGFGCCCfhxhX3fwPVzIvOolbVMgv3MZYyfrKa4xVDlxh40swQvjlqzL3RATWKpPundg1K9LQnAO1Xu6pLceBn8FX42nlJhpxvmpb4sIODCDqbYaA%2FJMdxyG8f2wSaR4F&X-Amz-Signature=21b45b33fb0a4d7fc9d5fa476dd36a13ee1d211d1e8fa36af662f1d2b6680a6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

