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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DAUQH4L%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVshJ41Jkz6RqlqTwM%2BDdwt3lH%2BX2WdXu7SHnsKvKjSAIgIoV0qbItZGqf%2BSXXvl4srLUXthn8qEoicW0mFA%2F5ZsEq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDPvSzloCOEeqxX89PyrcA7xnu9Us141a9HzTLb%2F4%2FrDN%2BxZvVSyM1tApho2Pg2lWOtOMMImk0zBZqpvD%2FkKA0YL4gpIZfIBLWf6BWKA3cd7eNqESwkskoay15sNtSRcm7zK%2B71UYMnuKzSyKVfzaErOC4uzF1fVi%2FlQVpE6O%2FhcWUhwyMFsSTM3VGVMY54rq0LqblM6SUEzihfJfltDnK1rNF0SSD0FXCxGfNon1NMvBq1I1iTaH6Xv4LimT1DQgf%2FrrfUV%2FeqsJ42FbpWl%2BK6X7gcocT1mXezGN5D89j0L1Wf6RntzXNSFX1GLK9KnPRT0P7vbA%2BIOmtvgFnJuyFX1Zwk%2FNWKLU68J7hnmFtybR3Bfyk7qMhmVOEGRhFj%2FJGR%2FhlZ2Xl2uGl3BlnhwG12PB9uK1nL1AsjS%2BcsAMIhJ6hRMv%2Bp54Krbok2%2BQvpg5j0Gx8UYaLHvd08L4stnKYKsmlfVeWSit99PcFSvKWmKshiaVOJRT%2FjHWV%2Fj9ieyPXq7TTaUxVrY%2FJFiBakS4IFyoXHY5F%2Bx1kFrG1MatSE4G111IXtO%2BxVNpuQ90RtUEHgfOyJo4JIhQtbVfdze6QInwUIOBdJLbmT0botbqi%2B2cyY9VwQXTEnZ4AnpNUdfwtz0NPhe7Fo2ZflHcMPzDmswGOqUBKJHBHMFQKL4Jqf4qrY1hCMUq6s%2Fq490fEWueAwJWZL1hY4pE0Q4JYSpdHqj%2B0z%2B8yODRZPt5mmJSnDRhHj0LWeNQL8ygU%2BoIpjh73wf3aV8O7RlIwt7B06mP6clcqywkIKq%2BNACNHGtmth2sdoTXwm%2FinCoiVOfUqo3OAK52D%2B3dwP1Y3R3SQ6JjprXhOzvE54pu7a2kZyOW7srKL6EyY58w6MBe&X-Amz-Signature=9357cc548ab75c1e008c0e7240ea19801b2c396a5cbb6cf4964ab8e124b790dc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

