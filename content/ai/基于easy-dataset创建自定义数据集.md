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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGCUQKSD%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC9GHVscATJZqpP7cEsDk6LHzIk6ShisnKNlCO4NQOmLAiEAhbUCskifRpVejnSFCZJlClZDSyM%2B2o8sYubrmDbf%2Br8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDN3goESFtiw0cDJIGyrcA45ROgJRUqsKZDuwgddVXXzfxpiJ0qtxeEJS934R8pCmZusQlkmjPEUE0YsOgW9Fn5lV591cq22%2BYV1dtvwA2o5qJra1BwBDy2dIwxkV9xodU4ke%2FOSzFb3U8RiLGuDy9RcmD0tJ7ZNLbP9KNhuLrNwF0PFVWBzXlqXF7SO%2Fm1N%2FjtHz8i9DvzngLoBzA%2BFCFlUJuKwQnfReCGZRPdQYAMmLMPS2Jes4s%2Fd749TI22QNyZ%2FOFyIH5MJMMGWiHucJl%2FXXoYUW1bcxCOTOBKQrCisPGmLMC5U7eoh1IX2UkcUmygxz24U%2FVAiG9Z5FJxnAIJG6F2tNj6YZnnlDJtRxln9E30mTCEx%2FHTAoPDXf%2BQC2aaSXrP1yPZbWk0q7DMXCk%2BHWMxdUqqeUjY79PUvJyTg2%2BIKYLUie%2BcLnISwVD%2Fx%2BP5NyWzIWcS51nUy68TVa0c3ClqWsPChkJ4ktStQgA%2B8yn%2Bx3IEJ%2BfKfbb9%2BM5Z3zT%2By8BQZP2zSb9Rcf2jlrkFg%2Fq7lcjYkCvQKfPme6BMHfhWGiK5usAszBOaZdY32rC7Oq7klwVRGFAS19FXLknk8ALkq1sVOItohiNS9hdcaGnzxy6Wdh6cxpuqGos%2Fq7RYYs4LOG0sg45keSMJndjskGOqUBWrpWFW59iZpub2piVydCEHGxq9faVgz8YuOtVL49xxK99kKBH1CA2tcHGHZF%2FpJ2C9LhBpgJve6H8JYbPgtoY55%2Bz1ONxMDqXISfdGSXtScRd%2FKZ63MNIbOD1kAbij4AtQsFc4G58OmGE4t%2BEcKQp7DCHZJX%2B5fGZN22clA4ZlsVv7Nd5cr%2BGkhy03uR4tZUpiImwoGJgrq97lvglr3AUatR0LPz&X-Amz-Signature=58134f04f17c31c6a638b49afcd3a49227f1fc3615567a9845d77e651cf3f3a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

