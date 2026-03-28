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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PYCAVPX%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034009Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQDnU2dHuc9lL3v0RiVKDeWDxmfBEGF6K11ouQVmpM1fzQIgATN3jl3dhn3LOW%2B7tF0NL4RO8%2FnL1P1RaE1uJuG%2B%2BO8qiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCbvVEytsNknPF4KOSrcA7XICTYCPKTvpnb1pzpXXoGjMOXgQ8vABuJoyHgw0WcxdR5wBthZ3QkyOUyWRx72y%2FznNB%2BCjaalhit50aOPJIdvUtsMLOfhz%2FWkl8Pbooo8ClcAxjufXwlixEs3XA5T3PjtUaQ0coPLQtv4L1ywa5031BAMc0OxFDHh21mbBJ%2Bow86am1T%2FXh4dxxwKstICf2dm72vUg2BXK%2F85I82eOYB%2FYoU5%2BsmtF%2BWOgUTJbO96O7ZNlfDxjNSt3x69%2F2TD73aWxwKXsTbMABiy0aeprTpt1xR6NdSrOtk8kSo1vwY05cjFUNDI57AIUQPmHORggBBL1sIEZOjDSJMAByuWRu9fVodugNDDdQjQc3%2FF65y5C8ShEMNo%2BdETs%2BdWXW2YI10lzRV6z3iUfTz4YgnQfKWCGEYItEO8NfKIXZ4kGFIR4eoCGOSGmUv8mSd6ic9z%2BU04Lp%2BWFc%2F7aYR%2B%2BXS15ZOTajd3hD8GRapmNcuMJHTlgnGOncPTOXMEQm3aFpx1htJHqMWoStbZX52PWnN69EHda8%2B7oMK9kmy%2B9eueD%2F%2BQOSODfBD0rOzGP29B5CTagm82Pr1wGlwDdJSu%2BYWfOJWnn0ZLHFQrR2uiHLIHlDq2OxnFkU29IFlMP1L9MMX%2BnM4GOqUByNsOXMp%2Bi0Gh%2Bcg6Mzyv8mEwKsN2OatlEtyvC5p4yrU%2FDnIHsPpYD9lAbwyn3d6g6WxA0s1ldkFdsCpTljVtFAe9ItGGLLnElVZThAsg5pKyWm26c175FOcE7Rb1aNQtNDJap4I829IKgD%2BqLW%2B3sg3U%2B5QTf2Vb266uhAYAf0bf%2FmnDtRXNSbNaD%2B2FTnX6EWCFV%2Fghm9Wtkq5t2Rl%2FciBM%2BvCD&X-Amz-Signature=26e42884e04c53361277d195e696faca3beb88715f5a5cbcd682632d1dff5674&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

