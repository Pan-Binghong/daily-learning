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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y47DPCLM%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIDIBRs%2BAdHsaqa4N0pZ0HSsQ0qsnL4nSax1nb%2FTydKUbAiB1G6KvBDZbmkez%2FbGKRDgxboCuig65MzYqwg0cak%2BPjir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMsfOXOmoJOZVKDXAaKtwDeY2tAd4N40v%2FCM7wAv6Q8g4I%2FIZzGjibGu%2BRNeMvJTdM2yC5ZvAXBt0VTeWPiOncJnfyFiZiPzE%2BWJQS1W%2FEGdVqp5KDUIUZkk%2B5l4%2B%2BoXOu34JEGdayWzYbcDkaKbB5xYR%2Fn2F%2Ff%2FlsAK9Ms1bctahorRd9rV%2BqtR4pn6V99IxazYsRtn6uADyQGTCuBRYAi6VpFyKHSO%2BEQbg%2FUlHIX4F%2FbuMSTpvQ2MQS3wwuHbBGf3PrF0UGKb8%2FFZYTa4k34peJhdxuEaZlnjI2n4hYrruzrrUu6LRup39oE4VB4Q23aTDN04rvrhqDI7DswlCSi3NBGwPrnJPHp5Bpup0fo3hvI6Hll7jDjFgpDaIIcgw32UfIzRtRNhsnAKSrpVmxVgHDOJEn94Wb78bYjNTRtoMsXvqT6%2FdQAfEKEWgZZ9u6bYclNUP6fWpGgYdvslcmo%2FlYkXQAHiANZUVQPhcMhnMFf1SaQPGslOFyzUcfkeo4PolGxU8a0PnNJPbVJx5NFKZZguIH7O2BquiCsW3LeGRgoiivkaK0L%2Bx6Hi5FTfTZBRU%2B4smiO%2FJR3Fkg%2FzRAMf6sLM9Mp8YDjag89auGHlnCw%2Bego9sZhXI%2B%2Bi885o31MUbvNESHFmxGOM8wgZG%2BzQY6pgFon3eh%2F4TytL9Rre4bLiwimEQsJg4fr46u1TfB3hE5oP84sOv6YKRz11hOSGmpnSoenuOTdjWo6YQo076g6kRPZri8MeTWOdFW7hXZrz70J0a%2Bhn6MDDvzeVAWw2OnXJ3JtYWR3M7W%2BKXjtAWDblqmQDcqBKfcvBHkjmp3s6%2ByFrE9A7fplAZhlesEo1agAKIuwux%2BzNcz5nWN48CDgUmYsjl5x8i%2F&X-Amz-Signature=b750981bda48ef9d9a053467b8a9308f45181727239fc94fcd968efc1164ce93&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y47DPCLM%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032745Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJGMEQCIDIBRs%2BAdHsaqa4N0pZ0HSsQ0qsnL4nSax1nb%2FTydKUbAiB1G6KvBDZbmkez%2FbGKRDgxboCuig65MzYqwg0cak%2BPjir%2FAwg8EAAaDDYzNzQyMzE4MzgwNSIMsfOXOmoJOZVKDXAaKtwDeY2tAd4N40v%2FCM7wAv6Q8g4I%2FIZzGjibGu%2BRNeMvJTdM2yC5ZvAXBt0VTeWPiOncJnfyFiZiPzE%2BWJQS1W%2FEGdVqp5KDUIUZkk%2B5l4%2B%2BoXOu34JEGdayWzYbcDkaKbB5xYR%2Fn2F%2Ff%2FlsAK9Ms1bctahorRd9rV%2BqtR4pn6V99IxazYsRtn6uADyQGTCuBRYAi6VpFyKHSO%2BEQbg%2FUlHIX4F%2FbuMSTpvQ2MQS3wwuHbBGf3PrF0UGKb8%2FFZYTa4k34peJhdxuEaZlnjI2n4hYrruzrrUu6LRup39oE4VB4Q23aTDN04rvrhqDI7DswlCSi3NBGwPrnJPHp5Bpup0fo3hvI6Hll7jDjFgpDaIIcgw32UfIzRtRNhsnAKSrpVmxVgHDOJEn94Wb78bYjNTRtoMsXvqT6%2FdQAfEKEWgZZ9u6bYclNUP6fWpGgYdvslcmo%2FlYkXQAHiANZUVQPhcMhnMFf1SaQPGslOFyzUcfkeo4PolGxU8a0PnNJPbVJx5NFKZZguIH7O2BquiCsW3LeGRgoiivkaK0L%2Bx6Hi5FTfTZBRU%2B4smiO%2FJR3Fkg%2FzRAMf6sLM9Mp8YDjag89auGHlnCw%2Bego9sZhXI%2B%2Bi885o31MUbvNESHFmxGOM8wgZG%2BzQY6pgFon3eh%2F4TytL9Rre4bLiwimEQsJg4fr46u1TfB3hE5oP84sOv6YKRz11hOSGmpnSoenuOTdjWo6YQo076g6kRPZri8MeTWOdFW7hXZrz70J0a%2Bhn6MDDvzeVAWw2OnXJ3JtYWR3M7W%2BKXjtAWDblqmQDcqBKfcvBHkjmp3s6%2ByFrE9A7fplAZhlesEo1agAKIuwux%2BzNcz5nWN48CDgUmYsjl5x8i%2F&X-Amz-Signature=b30c6d489f37212cae7ac461c262ee64901b75bd3b1d9667dd80e6a982ae4ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







