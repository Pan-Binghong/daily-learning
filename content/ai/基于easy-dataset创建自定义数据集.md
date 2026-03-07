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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIMEKDF5%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQCFwvMT7bEv8Soroy2E%2FExMOPCbS1gU0JwG0Ju03Q69%2FAIhAIt7kV0VqXZ21AI5%2F3oivt1AK8SYaImAilkWj1qo%2FzNjKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzzmOkEIdCsIez8l2Uq3APDaD8doqDr3m8yJsLYGDiFX%2B%2BjnaCetf5vpq50cKIL1l89C9PL3OWM51W7d75EYsa2%2FdoJXCEAVaYl8RK0kmcclQnyZjRpD0Hs5yww9ZPRYeMsk%2Fl2GB2cGRV4Te%2B9E8ZMLCVPzt9uDOZTLbYFPhHDa9y7gZBz4dAQyd%2F3X9J1vtxax7ho3cwE539dTgK26YfJF1Mw6K02WYXaALaebC%2FWM3xH4YUHdXM8bO2fb59q2uc7zJj2ROC7rPG44jEzGkxlqzPpWodLpSv%2FfAiYSHpbTAUZWkCxWjmu4b0RGUTDBoRa0ys7CYPIPkTY6mS7TdvkSWb5MTPGthjAVGKQ3oKL4vZp60Yvq6VgmvYY%2BySdkj9UhGUdpnvoIe91W31nrIs4NS6f%2BD78hxXeLt1NaLPWO001MNWymPSLdOJBxbwUoAM%2FZymZCB4STNHHrcNe0XUQIdvQd2OCtR2mNXcU4ddNt8uCcv3vBhYAGUQ8CypB3W7nrvSMYwzPmGV9f0PzU799PhF%2FUvo9iX%2Bm0j8znIG2A2cVYHPwwqpvetIkxlEhPIUwiI186jxuiQD6NbJh69Rnrfub2j34SlGekwLtDwxna8%2BShK%2BkK5A%2FmC0PuP8ygRxDrH1mgCw1r9fycDDRk67NBjqkAUbXLu7H9p5a%2FYRJolweSFuEDnvq8sGxZHPZQvUlJq1w22ScTxCxR5%2FfriXY%2BoQa%2F%2B72EWjFoB3EY7MEIWaXrc7ZkFfbdsY%2FryCk24wUZ30KtHAXxYOifiRHePWWmRxK2qaBzxrlxTbQ7oPq8zlWPhCJfy3dTELdUc%2B%2FMKCG1WVJM1cELQFmqiTvnR2TTzTmMo9Fw3frQwedNR%2Buh9MR0NqHFZWO&X-Amz-Signature=094ddaf79b7935f16ab51c08fce7d7c29aff287e0ff7491ed33252d87ce3c1b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

