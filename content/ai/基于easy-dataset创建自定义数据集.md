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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQKXQPRD%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC3eza5w1a3FnWIXcQB6dkY1xqruugeaxLKwehQRSytbAiEA74f5NXoRd8O4LZxBo8NB%2B1jPBOwFm0ym%2BCzK8HF%2F%2B7wq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDI%2F1wYPVacyslO%2BcFCrcA2sAL9JOECZGGF5BG18hi4QJ%2BMSKnGVTurJ%2Bv2EWI90YMV%2FzFx8HzXIZX1btK0xeErmjKiMV0Nvs9D0NJP%2B1gh7x9%2Fc9qBjFB74ZT3MCnVXW58wwCNVnIU%2BkqpNnwu%2FohFFmaMyKu1SsGenB4jVS4%2FXJvUSSibwWxJLZIO9Tj64cgASlO76%2BpMKJpD750VZi2eYHl%2FaSMUb%2FHTIbLeCAJ%2BGXr16siShOP0%2BKzS9oxfyB6roPgRPrc3CZnhvGP02oabO5v79TWzvrA9FvfhRVDnEbywNaspwIsHjnZpkk5kgPAWXob9uw9Ivu26INLSdeGfA3eWQawoIlUGT8EqhDJ0L6frrUBQhhpEA5fnAhRHJCD6wgwJsecqyzOGw3iC5bonQNPnTbiXrmS4T0uHAOELY73polSTKLebbI8OI0r8F69m1THrKicHOcxg%2BMb1d4N8vboDuc48AHt7VAFoz1%2ButM0XgRBRNHGnnL9o4rIho%2BV1AhpTY7tD07XFpF%2FuROD%2B3jzaNzJ6F90fh%2BceGL2HtzIQ%2Bw3Fx%2FZGY5qLL8qKold0EfDdltjhj11SEeKU%2FqNxUJR369dV8o9iHRWS9%2FEQpLuksj21s%2Fxwfpw9c8AxaHGxGP6jvWJW6szWUbMLuulMkGOqUBhMfT%2FY1WHCO2DAVqS7NsOVeq3WRNLmTSsQO%2FjeXP%2FSkyXIjdV0MnomUxrYqsjCXPUHNXOrLjfN3lvJPOip6nyyN741fPTd9tpXJpg1Ug%2FQJdCQBzAhFK0%2B0%2FTtDfYseC3gV6FxzCXiKtI271aQs8wsyShFEqRmA2eL5MWBI7oT24eVEMzAZvmylQhYJFueJjFprFOMrWaITjAUqTfV50o%2Fkc7gq9&X-Amz-Signature=37e7176883f1f451f527634777180f5303c9108743cffbd78d59d2f07aa326b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

