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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RVVOM6M%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC73TOlLF4pLyWXUBvNRFGy%2BXQEhdH0jAdsk2JyFThowAIgGbKjY1TSRnL4JH4uqpFvNqxC%2Ftn0FQTa%2BA1SSABzFJgqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDObTC9oDdIxYPurJ6CrcA%2FHbmNEgUuwvXEzy6%2BbwBuvr13w5yfdFBSns2eDQzAgoUQaUwZh64NifU3Ft%2BNYYwprDkMd%2BgNqS2XzQY8J2pyG%2BDyuIuNo6y%2FREFl46o2S5few1Mit7k46zmXZ7AEEAEcI7wuVpIGSmyCITIZ6CqI%2FzIG39HVBkqvjnhZ23GfcvsnB0%2FdeZNovoEfQ2rBabZWHRbsRw9aP%2BHn8EakTWnQu2301DqV4lvZGNtxhStViBZKkZnfXOlmanlOBOei%2FUJalFB3mJR%2FMwDxQUjU51iV3JUqbiFCkLDb7ukV7e5ELYSsS84AJY2zlZVr6CYnzjbj%2BP6qZmN3Yh9OBo2OS3FXyXoA4uwkNR%2BNWsf2VzqOsaehu45B5mOxcltw9qlVV8E90pLCs%2BNQpcFGo2%2B5Iq1cAO62s0M8Pr56MzHhiZbJplTFUioME7Ud67HnvbHPkOe30oYOHfxPhwXGxwsq7ra9GLQt3VhzPWlhggr4XoUOp%2F3%2BK6G8YFbG60JHgx3ZZ0Y80MfgJVwnWDsONvfofwlT3ARZzRDiP2N0UF%2B%2BOim5AP1N903XMBvyqsDwtqQSLxSEznxPDU1EpFQ%2FKKwYGBs8jDeidFwAb8bYNXh6pMt9rQ6tean3ehd8LkICpjMLmVsMgGOqUBxfkOSF3zXG6idvt6aUMgUH1l7TgwqkuqsDS4QvDcl%2FDngcAB%2FE3WVeiBQnFG8CY5nDkQAdstEAhi8GhAxDegWtsJsz9x2tmEewLaIDlgN8hEeD6hFLIbHFzt8Erni3CDUwVUZEFDu%2FLAfThKFCSQ3EtmcK3jVjgLOiCFQ4E0EP5NHIZig4SlS0MX2lFfRDnMxxiTjaNKVP%2BDf125SvBkuYPDTB0m&X-Amz-Signature=325ca9d05fd06d86cd4aaa896495dbb17081f682d57cb02dd3a38292b65012ec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

