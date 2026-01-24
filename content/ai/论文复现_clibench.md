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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEVKPRQ%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQDnuj8oaWUuHciFKGXRK%2BnL8dKp%2B33Be5NZupPlcNVMtgIgcU7z2duzK3CzaMl2WtNsPS28hMcPiKFgKv4AVLgyppkq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDACJuPyk9%2BIAazQ4IircA00RhSB2RCHXhaqUG3dqdtHKmdOncB28vJWAOKdLnRh7o2yB0NJf6GzWctAoH6SNSfmciW0nN4Kyp51Zibi5YiDy0awKAHcSBK7cg31jKHCspmuUZc4eE2OnlpZ%2Fl%2Fn%2FtD84BVmyNfPyuHE0H65Mi4OXiqi0apZpsuvYQgZmW49L4630gaXtPB2ckcszLqsywT2pUPLxyoC5V8p8tTK1nxTsjeT4wjsAmc4TXgfj3KpN7i90xQt3n8a4FqnrsN7nAQTIAYLXSRaDj%2FCQWL%2Fq65NbHpi7O%2FUwh%2FBi78kpLRCfEswwnirMMxovOV3yMEvLftPBVkLC30ZXBwg4dK%2BuWTCcrTILwrCKc8x1gqoeIT9D8FotO%2BrlIutsuaJeWf6Ko3gKj8lrxIxSX9JVDrqsLTVO%2B25YZqnyXv6ZF4y3BkUfTMI9Zu9w1RNKmK79jJdFiLChZ498p%2FlLXBd7tF4JjINzM1xndhv1%2FtslOxF4MZIEsf4C%2BVT5%2Fupa9VrcCieL%2Fr%2BK2FDYmeVAG9JQgM3FzxcQd5ciGGGI8sb1yen4lBd64j%2BC%2BnLWkImXYQZykjspRl0Brz4Vj3rWAXpdNWYJ5yrJMiwc%2Fsf0fwjm9Rzf%2BVYvW%2F8aWhecm1gYbU8XMPvO0MsGOqUB0CxUVh7bR9eGFsE15sOkj32Ish3Z2H%2F4T3skPx1nJQAm4sDbZupisFjPxVUrjMkpsTUfHqpmHZA0GBAaKVUBOK5zSoImdnQARnP%2FWuegwMt7nVzg1OZg8yYthuOVNFp8uIoYTDBXTMbgsPAHv2MUKsfQnQvt2vTrNhovLy2aTpuWJqoey4T7t1b71gViZYyaD8EBGVSf4TUzSAn%2FXoCcVq9aB%2F%2F9&X-Amz-Signature=8eb335274b6df66e1c40bb702759efebf21cf01e1f14ffae9d977a02b928504f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQEVKPRQ%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQDnuj8oaWUuHciFKGXRK%2BnL8dKp%2B33Be5NZupPlcNVMtgIgcU7z2duzK3CzaMl2WtNsPS28hMcPiKFgKv4AVLgyppkq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDACJuPyk9%2BIAazQ4IircA00RhSB2RCHXhaqUG3dqdtHKmdOncB28vJWAOKdLnRh7o2yB0NJf6GzWctAoH6SNSfmciW0nN4Kyp51Zibi5YiDy0awKAHcSBK7cg31jKHCspmuUZc4eE2OnlpZ%2Fl%2Fn%2FtD84BVmyNfPyuHE0H65Mi4OXiqi0apZpsuvYQgZmW49L4630gaXtPB2ckcszLqsywT2pUPLxyoC5V8p8tTK1nxTsjeT4wjsAmc4TXgfj3KpN7i90xQt3n8a4FqnrsN7nAQTIAYLXSRaDj%2FCQWL%2Fq65NbHpi7O%2FUwh%2FBi78kpLRCfEswwnirMMxovOV3yMEvLftPBVkLC30ZXBwg4dK%2BuWTCcrTILwrCKc8x1gqoeIT9D8FotO%2BrlIutsuaJeWf6Ko3gKj8lrxIxSX9JVDrqsLTVO%2B25YZqnyXv6ZF4y3BkUfTMI9Zu9w1RNKmK79jJdFiLChZ498p%2FlLXBd7tF4JjINzM1xndhv1%2FtslOxF4MZIEsf4C%2BVT5%2Fupa9VrcCieL%2Fr%2BK2FDYmeVAG9JQgM3FzxcQd5ciGGGI8sb1yen4lBd64j%2BC%2BnLWkImXYQZykjspRl0Brz4Vj3rWAXpdNWYJ5yrJMiwc%2Fsf0fwjm9Rzf%2BVYvW%2F8aWhecm1gYbU8XMPvO0MsGOqUB0CxUVh7bR9eGFsE15sOkj32Ish3Z2H%2F4T3skPx1nJQAm4sDbZupisFjPxVUrjMkpsTUfHqpmHZA0GBAaKVUBOK5zSoImdnQARnP%2FWuegwMt7nVzg1OZg8yYthuOVNFp8uIoYTDBXTMbgsPAHv2MUKsfQnQvt2vTrNhovLy2aTpuWJqoey4T7t1b71gViZYyaD8EBGVSf4TUzSAn%2FXoCcVq9aB%2F%2F9&X-Amz-Signature=19ed191ccb5e881edc5f8acd396044cd5a5d97bd45af226dd3a6d52f741de69d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







