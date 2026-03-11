---
title: 论文复现_CliBench
date: '2024-11-13T02:07:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- Paper
categories:
- AI
---

> 💡 对大型语言模型在诊断、手术、实验室测试订单和处方等临床决策中的多方面评估。

## 文章介绍

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654BCNJCT%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDMM6htLdI7K0ufOpjNC%2BxsBAyQ7kmZMM%2BAYn78CLHswAiBBPldcEthJvCHvq8qX%2BokmEFeYwphHKrckI0zb7fqGsSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMyOLzhjFoK0HIOwezKtwDJv2v5s73Xoo4Y56S3g334mSliEMZgQON1fnZiNHiBn9pi1%2BetEyaXtYwW8zBiwu8SI0g9dwoKg3V8CZZ%2Fyvl4M789nTg%2FDgAcZIsQBEdv65%2B4dwy1RirO1gYtqswfO16pHX%2FgOqQq6b8pI3Qvf%2F8HVmI1uC8NE1plniCpMDMiIEP%2BckhIsLPlkjftuP8vb13CF9UgQwnNjNCpQHdYk280V9SHyf4hhqb2BIqTeaOhqYw1r19uweykNyiNHQynU4Ax8w2W6Y2%2Bc8ZZeKTRSAQEt51yJrpAy0tqhbOSKdNk5VyP9Zq56QiSlnzpZcW90OmeNUAgo0nPcUBALEDRdFMilJjlgdf1ZGxY8oW04hDKQ7lTxi6n%2BKVtG1hSemSn72AD%2BU3vG6G1MbZv%2BSEV%2F1bqs2GljP%2F4ENsuJVt3wal6%2FDPb5OSER6ZMQ%2BH6vS2a4ndidfmf5pyz6mQym2FfR2mzs54saY1b7tYSVpkx7LkkJyiSrKzmVxZnPAaZtGwmWMN4NFNHOBx6XCRrCPOvumdB58aomhWfFyTGIwgJjTIvUW9A9lo2Dg4GADwZ1vcUKq8A%2BSamQzo3FJRZIZsCQYwdhWZ%2F5pLcsF8Gs3RRtSHKE5b4%2FI3uD5FdwoUw60wusDDzQY6pgGFbFGlaVFYB447x%2FdKt5rPhpxPmZ24czeoC8L2ZgZ3A7hfUDcaaRHk4F2AC94FxY9SBg6JgfsUS%2FS%2B4AvuW7DjiOHxhSvWGWmMSqzPn%2F7K92yqdI%2BWUTXvyGDWYYZM%2FfaI8sW6hf6C8MoKS3nCLp9DXZERX8myblczzUd7EppEDNmcpMh9mfFVM2k9qW38Mrb96OZK%2BhPy%2F5PWq73KkMRUkg4%2FfixK&X-Amz-Signature=0cae22625d7dfdf77f3db3ae57de120709c088d2ba9ccab6bd25a179f2c3a4fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654BCNJCT%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T032742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDMM6htLdI7K0ufOpjNC%2BxsBAyQ7kmZMM%2BAYn78CLHswAiBBPldcEthJvCHvq8qX%2BokmEFeYwphHKrckI0zb7fqGsSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMyOLzhjFoK0HIOwezKtwDJv2v5s73Xoo4Y56S3g334mSliEMZgQON1fnZiNHiBn9pi1%2BetEyaXtYwW8zBiwu8SI0g9dwoKg3V8CZZ%2Fyvl4M789nTg%2FDgAcZIsQBEdv65%2B4dwy1RirO1gYtqswfO16pHX%2FgOqQq6b8pI3Qvf%2F8HVmI1uC8NE1plniCpMDMiIEP%2BckhIsLPlkjftuP8vb13CF9UgQwnNjNCpQHdYk280V9SHyf4hhqb2BIqTeaOhqYw1r19uweykNyiNHQynU4Ax8w2W6Y2%2Bc8ZZeKTRSAQEt51yJrpAy0tqhbOSKdNk5VyP9Zq56QiSlnzpZcW90OmeNUAgo0nPcUBALEDRdFMilJjlgdf1ZGxY8oW04hDKQ7lTxi6n%2BKVtG1hSemSn72AD%2BU3vG6G1MbZv%2BSEV%2F1bqs2GljP%2F4ENsuJVt3wal6%2FDPb5OSER6ZMQ%2BH6vS2a4ndidfmf5pyz6mQym2FfR2mzs54saY1b7tYSVpkx7LkkJyiSrKzmVxZnPAaZtGwmWMN4NFNHOBx6XCRrCPOvumdB58aomhWfFyTGIwgJjTIvUW9A9lo2Dg4GADwZ1vcUKq8A%2BSamQzo3FJRZIZsCQYwdhWZ%2F5pLcsF8Gs3RRtSHKE5b4%2FI3uD5FdwoUw60wusDDzQY6pgGFbFGlaVFYB447x%2FdKt5rPhpxPmZ24czeoC8L2ZgZ3A7hfUDcaaRHk4F2AC94FxY9SBg6JgfsUS%2FS%2B4AvuW7DjiOHxhSvWGWmMSqzPn%2F7K92yqdI%2BWUTXvyGDWYYZM%2FfaI8sW6hf6C8MoKS3nCLp9DXZERX8myblczzUd7EppEDNmcpMh9mfFVM2k9qW38Mrb96OZK%2BhPy%2F5PWq73KkMRUkg4%2FfixK&X-Amz-Signature=2125f2a4ef371af047b27bf123a288608b4e7829697db3a7612a16348567e6f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 复现流程

### 下载数据

- 数据申请
- 下载 NDC 代码元数据并将ndc_metadata.json放在code_sys/NDC目录下。
### 安装环境依赖

### 运行实验

- 数据处理
- 生成输出
- 计算分数


---

### References

> https://github.com/CliBench/CliBench







