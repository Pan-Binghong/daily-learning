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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EP4PIL%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIM746fk7tslpUFoMLwG5YhdgROq2CNMf7OJ7v2ZJOgAiBMmoq9EO8MXheGH%2Fo%2B%2B%2BKHugC%2Bth4ge7FoD97i8tYNfyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0oMrUrrH1qj8Hn3KtwDmlD%2Boh9ZaMPjhllIq3NmQpjRZxTd4TPffeSC%2FouCPV%2BoEsIx2WxlooVWaZkgqupuR1jlxDlumnmeoUwscFjT6kvdPYnGsvld7BheIJ6NExflVMhFohih%2Bvip7gsf241VNNM47v%2B4FgvBZEYrRxdN7NEkcdf4GaZ42pEgBK2JPej04TMrmA3P2KC7h4GqYrAcOA6WyV9cfbh82u1Ozo7Zshd64i6GwiqMizrcqd%2FUgqg%2By%2FIyuPcjbmWxFkak9iklqaqZue3r0O5CMjZTFa%2FZ205qErcmE9L8pV8HvahJFR9Xp%2FL0pnWDv4qb8oFiHH7OJpVeUmJraAYk84Y7zk%2FSJdd8GI5j2uazP1jju42iyVgnaR8vjn8uIG5W2PxeXzf8RiViLkw4Gi2g6j1pE5%2FgML54rZSuQZdo0V%2FZpcsgdlZeCNYvVUy5mIZrRLbNg%2F7dFPwS5SuS7wokI1w3MjNxdD381hNkTjgAbIMo706iMOBYTNgRG5bpMbucUZhJzCXgncqJSHS47WxRLP8Xga6biksSM7h6PTp9ZQTDnp0b6jkMY6qjPKCZnd80lYPOnMRaFkBRKpC3XOTE2OkOJLbQsVkTxbc729dmAsn1%2FLgCmqh6pQXCisTWPipNev0w%2BN72zgY6pgH%2BVWKOMzjB1OAwFRJh3%2F2YJVWPKcwZMmlkuh%2BJ284NChasP2Tb7XAOiHitv9rQUO1Q%2FvOWOynTaoZQi%2Be2h2qL69KYQTxM%2BWuayHF%2Bat6SZX5VcvlfmbBiz92xicD7TrCoMt4btLasGgiAHxFMr5l1OIpRLE5QD%2Fk6R6I9uqPV1X83Kj%2B4yxMOAs52kYkwYfgh%2BUyaksg7h22YS1mAIAAGBV9UXluS&X-Amz-Signature=580470f5d2d775cf314f84d90973d846d5815183fd5824f311188592c4ead092&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EP4PIL%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHIM746fk7tslpUFoMLwG5YhdgROq2CNMf7OJ7v2ZJOgAiBMmoq9EO8MXheGH%2Fo%2B%2B%2BKHugC%2Bth4ge7FoD97i8tYNfyqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMz0oMrUrrH1qj8Hn3KtwDmlD%2Boh9ZaMPjhllIq3NmQpjRZxTd4TPffeSC%2FouCPV%2BoEsIx2WxlooVWaZkgqupuR1jlxDlumnmeoUwscFjT6kvdPYnGsvld7BheIJ6NExflVMhFohih%2Bvip7gsf241VNNM47v%2B4FgvBZEYrRxdN7NEkcdf4GaZ42pEgBK2JPej04TMrmA3P2KC7h4GqYrAcOA6WyV9cfbh82u1Ozo7Zshd64i6GwiqMizrcqd%2FUgqg%2By%2FIyuPcjbmWxFkak9iklqaqZue3r0O5CMjZTFa%2FZ205qErcmE9L8pV8HvahJFR9Xp%2FL0pnWDv4qb8oFiHH7OJpVeUmJraAYk84Y7zk%2FSJdd8GI5j2uazP1jju42iyVgnaR8vjn8uIG5W2PxeXzf8RiViLkw4Gi2g6j1pE5%2FgML54rZSuQZdo0V%2FZpcsgdlZeCNYvVUy5mIZrRLbNg%2F7dFPwS5SuS7wokI1w3MjNxdD381hNkTjgAbIMo706iMOBYTNgRG5bpMbucUZhJzCXgncqJSHS47WxRLP8Xga6biksSM7h6PTp9ZQTDnp0b6jkMY6qjPKCZnd80lYPOnMRaFkBRKpC3XOTE2OkOJLbQsVkTxbc729dmAsn1%2FLgCmqh6pQXCisTWPipNev0w%2BN72zgY6pgH%2BVWKOMzjB1OAwFRJh3%2F2YJVWPKcwZMmlkuh%2BJ284NChasP2Tb7XAOiHitv9rQUO1Q%2FvOWOynTaoZQi%2Be2h2qL69KYQTxM%2BWuayHF%2Bat6SZX5VcvlfmbBiz92xicD7TrCoMt4btLasGgiAHxFMr5l1OIpRLE5QD%2Fk6R6I9uqPV1X83Kj%2B4yxMOAs52kYkwYfgh%2BUyaksg7h22YS1mAIAAGBV9UXluS&X-Amz-Signature=38e5e666e2a239c7ebd761e251e9ee9ac9bddcd664e8790f93596cace59bab70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







