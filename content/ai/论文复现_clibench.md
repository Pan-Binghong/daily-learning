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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMYD6LJ%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQD%2FQep4REykvNzl9HMZZT2m3MGYnZk3bYrGxV7qFDB2TwIhAOq8reSxFmAFnijq9tjGs21GGY9LH9o44DazLwKlVUO7Kv8DCAEQABoMNjM3NDIzMTgzODA1IgyHk3usF%2BCTPVAivhIq3AO5H8HeakeLut3m7zl0WmNf26s0RBDQfAI3lw2K9N3mtreuQ5xbP8bKkpYF3qGK9jG9xjeQMvQ210%2BG%2Bw0wUO7W1G7i2ygdw4NPvR4nb1L0gsHxepdbzWp6dH2CaSK9DFh6yE9QXnS6D8npB8zIj%2F%2FAsdktM0oa0v%2B0deXFimQtPSdc3jeVOfqgkMLNkDh4M2jGha7SWCD653m2LB4n2vpxYQVLhVEPRKbm8Ad7ZGy8G5hU5B4OO9%2BPjV1EmIUVR%2FWubomCadOLA1RpUnW2lT1OoP34%2BGdcVi518pz5ycbxjDWlP6qqRRusLq0S3br3Bfljp66ZNtWl5p4LwdsEDkvp8MhTYfpWbEpdKR%2FZbaEP4MSUDwTxkU0sWy5pj8ygoZZ4q%2B9WRu1qzpB2SFz10TLqPuRnkAEBTJco6GyZSf%2BnjDZFYn7O2rFE2LULlCbhawhUZHaB3L3IEGDPPDIWD9hnBK0aWar8e7fOATv9OUvG0tX%2B57xpT%2FE50KFEYMZkGqnjcSjFWTtXBLVEW49SSB66JBX%2FhHFNoYR3lczLwl8gsgjC%2FAFfDaEEsBh8nOTIdIW7Z3mTLMxwY%2BVem34%2BEDDjM1jKuOwa65AYqaC7mycSXdbL0%2BrrpRD5OK7WVTC8g%2FnMBjqkAcd42p4k0a4zqIFAFRYFlvHPWE0ZjzEf6p6FqYLzgA%2B61mJ22ck6ttaUiHKpiFK%2BY3sz%2F2ynGF2UoqwQDw2t35YTXTH%2FWkNODXszaWz6WyVkD%2Fk2BORkwptUfiIBlWTjqfyHyVK3CDt3yRpF2ZQ92Gnv7M2sFR630kRo8WouFciRHYdT1N01nGWIuyJ0qjRTFcDyMFqEQ0KY0Vd91gpY5aZA%2F153&X-Amz-Signature=199f2665f926b14acafc287aa1c9aa6b22a28aa000bc35593e15d4133037f88c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGMYD6LJ%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQD%2FQep4REykvNzl9HMZZT2m3MGYnZk3bYrGxV7qFDB2TwIhAOq8reSxFmAFnijq9tjGs21GGY9LH9o44DazLwKlVUO7Kv8DCAEQABoMNjM3NDIzMTgzODA1IgyHk3usF%2BCTPVAivhIq3AO5H8HeakeLut3m7zl0WmNf26s0RBDQfAI3lw2K9N3mtreuQ5xbP8bKkpYF3qGK9jG9xjeQMvQ210%2BG%2Bw0wUO7W1G7i2ygdw4NPvR4nb1L0gsHxepdbzWp6dH2CaSK9DFh6yE9QXnS6D8npB8zIj%2F%2FAsdktM0oa0v%2B0deXFimQtPSdc3jeVOfqgkMLNkDh4M2jGha7SWCD653m2LB4n2vpxYQVLhVEPRKbm8Ad7ZGy8G5hU5B4OO9%2BPjV1EmIUVR%2FWubomCadOLA1RpUnW2lT1OoP34%2BGdcVi518pz5ycbxjDWlP6qqRRusLq0S3br3Bfljp66ZNtWl5p4LwdsEDkvp8MhTYfpWbEpdKR%2FZbaEP4MSUDwTxkU0sWy5pj8ygoZZ4q%2B9WRu1qzpB2SFz10TLqPuRnkAEBTJco6GyZSf%2BnjDZFYn7O2rFE2LULlCbhawhUZHaB3L3IEGDPPDIWD9hnBK0aWar8e7fOATv9OUvG0tX%2B57xpT%2FE50KFEYMZkGqnjcSjFWTtXBLVEW49SSB66JBX%2FhHFNoYR3lczLwl8gsgjC%2FAFfDaEEsBh8nOTIdIW7Z3mTLMxwY%2BVem34%2BEDDjM1jKuOwa65AYqaC7mycSXdbL0%2BrrpRD5OK7WVTC8g%2FnMBjqkAcd42p4k0a4zqIFAFRYFlvHPWE0ZjzEf6p6FqYLzgA%2B61mJ22ck6ttaUiHKpiFK%2BY3sz%2F2ynGF2UoqwQDw2t35YTXTH%2FWkNODXszaWz6WyVkD%2Fk2BORkwptUfiIBlWTjqfyHyVK3CDt3yRpF2ZQ92Gnv7M2sFR630kRo8WouFciRHYdT1N01nGWIuyJ0qjRTFcDyMFqEQ0KY0Vd91gpY5aZA%2F153&X-Amz-Signature=d68cf7fca16ecf1ebbaa048ac314b35e941a8fa18eb9c70e3f2d4723bb78795c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







