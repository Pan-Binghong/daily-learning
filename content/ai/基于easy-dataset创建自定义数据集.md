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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X574LUIR%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T034007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5dvoN%2FaqhDWd6S5%2FuDdZawVkngvLwAnOVch171KGeRAIhAIzoQM7J2sYp07Af6VpXVUgeG6iwTOQuq50pcywWT6VjKv8DCFoQABoMNjM3NDIzMTgzODA1IgyLbgIMYD44cYtPG4Aq3ANEhB4olBzocHMUdHhCA6kyFxGbGHEJRYKTuoC1gzloFiDRRqsU3qdNer%2FLSnZZHWIDaOHkLT2OCKk%2Bdbur8ygKMdZcHMxuh46%2BsCM8QUFrHXSvi0xdjtgkNtHU48TYKn3cLXKf8O0XXd59mS%2Fp68u36AbWHDJfazsORUYdj6iKjD9Rd2qmkgS1FGyiJfj2pNYSMgopCGHPFDovNIV1x0V7BKABtiOBpgkCT0tWTwCowVcfK6arcfbyqwUAVoRvnxW8JeAdq8jI7gp7%2B%2BIVy0toTCyYqr6b2pYR57Rij%2FJcBNurvALIB492cNwEbmjlhnG4w%2FUPegOz%2F7ttFLIDaVZ3VhQ5Kw1mNmAZ4aHU%2FnEUDVChOrJAISD3KEPqMZsQJA07mXB0fTvJzd8cNaPiB%2F0nsBgVh9ieoLMHRQ1%2FGzqIK4Gfg58WR6WtjIF7T4gWCZ0l7tR%2FCFl1d%2FSLDxBhkJqmq4W4E2WNC%2FYlyQP5095e%2F0oESbagbWcy6lUOlAj%2FgzW%2BxgzI8ZZ%2FGsZMN6vupIWhqlRfePhHRd0DXd2tF6Q97NhkvXjrOHH6R%2BnyGtxKUcn7PaV4gXWOXqRT5uyQw8rYaR6WyTKh5SYpwhT1qpp7CZW7bLz%2BGK%2Fk2idunDCHn9TMBjqkAaah%2BpiZzWjkQnuKwgcwV8NsmKiiqVlHl51NL3oKn3C3snQNL3Bg7v4wsUyuuo0obvbd3oRQJMvGj4zhHsZHEMP%2B%2B85d97bThXK4fGntYqlDbfQFZ9dJAH2yfI8vSb4MbSl7n5KPYU11ZeN3Woafpgmygjr2w2ZDtXkihV8%2BuaKOBTIRQH4D09rJKJkktM4RcqyXWiYv%2FD1Gamg%2BojYY07dcfy5d&X-Amz-Signature=72ba675cb12f82f855a89af39d024c08c9db8a5144592ba9370effc16c981b62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

