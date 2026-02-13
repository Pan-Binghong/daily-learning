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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667D3QPVUF%2F20260213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260213T034147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDni2fqAIdSpbvDFIsYIkPUMDzc0VzTYwnGhObMx39AgAIhAPpXU7trSdnxMZKVi16glNc72jVR3kVmEW57MLvlpxHwKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzb%2BSRzae0oZFFqFBQq3AMLJhlLG4YtS%2BXr%2BUSxNxTCLGFLscKjte%2BuEtwwSyIamiE%2BYVBeQRb8RmYLgKuRVaJA03uVkvULf3zKECF80IFkYGdwUijHuIeGSir2cqZXVyRkWRIKrabtuXklq0WJ7C3zLB6lGaFKNAkBCtDsff6BVZfQwBDTP6TC45E2sNUfQI0owu6MlGCABQ36%2Bw19VzwVpOZ5SDpdltnp3rbcpLAtp%2BaSwMS5eI0c9a6cnRI5yR3jB06VjXjtFPTxTvS0FvWJd6YzcSdFr8Om%2BMNGC%2F2t3eJnrnUfQs0GP%2BdqWzEEjPjP3blBALscBl6RWTRfcwV3DJi9bUkSAtA29LDs8pbhvZ4UUORKPhLzTMMEao0v%2BkD8J2b2ZbT5HZmSvYT%2BvcJL14U3afIR4rIJpKLp04hf7JVs3VrWCLzy0qFeLF%2BmVPQYYOVqONBF15ONGZfRDUugs0zo5TgS6uK%2FPVvoRvCvdE6EHHkqj4qWHhEe6YicFL67xjALoIRZbk1gf%2FUUatPCJ8UXegfm2hguNju46%2FR3mHWr4l3WY5CD2SkBlR2IeAP6qIu1j74YHq1iXgwi%2FNIH0i94tSAJAk4uWj%2BHnx5w0rowETF%2BIPqZa1BhLIXeoH%2FMs9MnGr95WmrPHjCRk7rMBjqkAVX%2FvegWENozeQ2V47%2F7173nlmfZU8VByu1P5%2B9mc5HA9wfhxdcQKttTHzf3ZDnHBFTyMU%2BdKbRUtduoScqC5ecGHmQOco9iGH8hI6yAWLHdeNjgKYSzndVudMhDhtT05LQ0lOWpcYjRFOTfQYJSBcQGrQ6IT7EnF%2Fn%2FYV5hMcvsQZkAKtZS%2FqdTQqomohTGJwTys6KnxAzxKRRjee5e0%2B5YmnyA&X-Amz-Signature=e0cea60362bcc4601a1eca0a4c7ee02946794d7772d091f4b5300697ee770bb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

