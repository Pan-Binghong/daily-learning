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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO6GZW3V%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIBOzDer513RtVF92hslZOvyex%2BOGEnBzxcmFPnhf9LT1AiEAhNaobBlFmQtX4eA6mEOZKYofp7AvbTpPjnZ%2FfktoYw8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDElOg2kJBgP5%2FUnQWyrcA0s%2FFCOSeAigNADEB5aPGiA4yEzrOoDcZsApQ0zgZZbrjCt65E9Va4rOuGeSilFKFRa1%2F6z%2Bs%2FfgHUzmOsQF1smHBZjAdxximtKhPA4WyvxL4aZJE4ESiJLhYHqXOJ%2BT3MqAzF%2FlWRJIBJTDAa3%2ByWIp5vB%2FgfCnEEKRxk8XOrW9D9ycbj95JDvGWKJEzxR1dypu6qBe%2BTRVQDvTsvV5PX%2FNPEYf4cizMYYCfnwp7w1dHQAHMwPi7fAnzyUGHkwzOLcQAUHhKcdOXZpBoqZOLsOJAdTBiPCMyrFJ8B9ijWIOqEMbnwUG5tm5Tjwb8aosUjD86XGX4B8sLhbdlaJOKej1WOEtNgcn3T7szFznMbMeH8KLTv5JFc%2FvSj056yvwpzZU620S5Z124e4ny%2FPr5CXvY%2BHL6fNp5ufZmH1dJbR5el5qHHs3XYOLlANWWu1jOTVdM0Z1Y2JfEzRqpZm2D5LFletHhnuaodARfczvHlLQUHLNLERDajpr7k2ACjFxxuJJt7vLpzHld58oGXVnPq2hqIlGB2l%2B4xroxPI%2Ftz%2Fu3jS9FA6BbB1EjYlgZU9g5Ldirpfh59K6JDGWCXbF8oKfEwdn5uYXTo%2B3bjlre3JiWttogp%2FC0OizoHPbMJPI7c0GOqUB8vL1uAVSXxbdmWB9Irb1Wn%2B8iyj%2FlrlT%2B4s%2FZgNdqly%2FLhxZMsVBOmkVSL1mAn%2B%2FgZOXDwx2Pu1d3L68R7V5AHZK7QbsYb9Wm72fHiQ%2B8vQcPJ%2BYpmykG1CzOMedy3g9cdAapnUk2X5QZrOUHpZerP%2F%2B77K%2FaKD7aT4Bp1ZTPL4uqiGVhkgrWdzlpqBMzWl54l1Fc3IO6ic7Hv83nNwEZ4xGnkQz&X-Amz-Signature=0e68fe5c5c0dd9455890667a5570def757fd6906f758dc64adfbd0f134c01583&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TO6GZW3V%2F20260319%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260319T034149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIBOzDer513RtVF92hslZOvyex%2BOGEnBzxcmFPnhf9LT1AiEAhNaobBlFmQtX4eA6mEOZKYofp7AvbTpPjnZ%2FfktoYw8q%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDElOg2kJBgP5%2FUnQWyrcA0s%2FFCOSeAigNADEB5aPGiA4yEzrOoDcZsApQ0zgZZbrjCt65E9Va4rOuGeSilFKFRa1%2F6z%2Bs%2FfgHUzmOsQF1smHBZjAdxximtKhPA4WyvxL4aZJE4ESiJLhYHqXOJ%2BT3MqAzF%2FlWRJIBJTDAa3%2ByWIp5vB%2FgfCnEEKRxk8XOrW9D9ycbj95JDvGWKJEzxR1dypu6qBe%2BTRVQDvTsvV5PX%2FNPEYf4cizMYYCfnwp7w1dHQAHMwPi7fAnzyUGHkwzOLcQAUHhKcdOXZpBoqZOLsOJAdTBiPCMyrFJ8B9ijWIOqEMbnwUG5tm5Tjwb8aosUjD86XGX4B8sLhbdlaJOKej1WOEtNgcn3T7szFznMbMeH8KLTv5JFc%2FvSj056yvwpzZU620S5Z124e4ny%2FPr5CXvY%2BHL6fNp5ufZmH1dJbR5el5qHHs3XYOLlANWWu1jOTVdM0Z1Y2JfEzRqpZm2D5LFletHhnuaodARfczvHlLQUHLNLERDajpr7k2ACjFxxuJJt7vLpzHld58oGXVnPq2hqIlGB2l%2B4xroxPI%2Ftz%2Fu3jS9FA6BbB1EjYlgZU9g5Ldirpfh59K6JDGWCXbF8oKfEwdn5uYXTo%2B3bjlre3JiWttogp%2FC0OizoHPbMJPI7c0GOqUB8vL1uAVSXxbdmWB9Irb1Wn%2B8iyj%2FlrlT%2B4s%2FZgNdqly%2FLhxZMsVBOmkVSL1mAn%2B%2FgZOXDwx2Pu1d3L68R7V5AHZK7QbsYb9Wm72fHiQ%2B8vQcPJ%2BYpmykG1CzOMedy3g9cdAapnUk2X5QZrOUHpZerP%2F%2B77K%2FaKD7aT4Bp1ZTPL4uqiGVhkgrWdzlpqBMzWl54l1Fc3IO6ic7Hv83nNwEZ4xGnkQz&X-Amz-Signature=e0312fb8ef659cd2bf79fc97705da450fa098796c3997abf58de095918f231b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







