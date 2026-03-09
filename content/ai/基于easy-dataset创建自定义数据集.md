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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RMNEFXZ%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIDcAYgRaikPGt8nXP1uufSpFdzw8F3tUSmnHssYfAY6JAiAyiDlu8zn7z6KdlhBx4zVbrkNvxaG8iIdOvmUDRODM3ir%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMkihCMg%2FGqAOebD0aKtwDLaP3S0FrWjU8tNjye03uo4ihszB2GGVIR74Qa8KA3BRWuueAjB904W0G%2FRJhlP3blKQbNw6myGYXwPHCkh3zlYvrJSVqFmMkkbY5qCOrKfDsyS96DkFbCm5gQyb5lPq4BftwmG8UpDN%2Bg%2FCFvagDJYiz5ZhJOJMOCykjsRQ%2BOR%2FB4NnCP01Fz%2BcsG1s66DSzlwaPu8u9Tta9VgNwTvaNrmazqv3GC3t6zMN4h%2F6JX963A0eBqIV%2BJiRxa3Uy8d0mSfP%2BahF0PkBkrq77hlMiq7k0s2FEGYGa5FC41ZgOteD%2F5JEFuZ%2By6bnBk0fLR1i6EMV9SaR9Gm2EKzzwL56r5u37zQyxBuEUBVr21cKwBsXmdduFXF41t19dZeURbvTSYHXssQF2imoxgitS7yNl5j3M1PeynGQNTh07yMXoUUiq00zlSuviWWrpIdRmw3O4x8dfyPRDDegbCPoTlDw0vAeKETWiE%2B5UJp8MU7Z44qVANZHIILIDDENrN%2FwnPmYdyUqjqx1zpJHdVC1ZnzRhQ7toNLm8BQlEMyZwoJ%2B3pXwaX8s4i2mtDakkvxVR4hcr8ai9Z0AkzE3UvBxg0a9c%2BAW8kpyd4fTwBdbx2QW38MYJQKDIn92cLIy6GFUw5%2Fy4zQY6pgGTdS%2FPc6iykoucmf9MPL47H%2FQT7LIThCs2wjSNZpfKAqqZN29SIg3FCIqajj%2Bo7fUYSHATUPRlbaSMUF79p%2B%2Fqb01weWhsJF3DTUPFswQNN6PZs3fg0dCD439nIBI%2BUrupfG9nQyJ7wyYPu24julPflXHqjG%2FY9rF4PQuuzMF%2FUEn0KxdfCwDfj5JrSm06WkoQ4F%2BsiES5fInqH13JbiqNjR1GPJav&X-Amz-Signature=f3b268fc6a4472fa82c5e0efec8a3dc1f27c6646ffa33d125bf3259d30831a7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

