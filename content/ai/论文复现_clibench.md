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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTJBTR6U%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChSVSxg8gXGdqm6djDOdktxLMv%2BYzGiyhYe%2BJLCMEtWAIhALf0YnVquRpIULmmzBhkXEpJmEH5QPEOXnUTuA2sIyCoKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FGuQTI1ba%2FOo7iKgq3AOl9SNQbgmt3N8AKYFFFDzhHGJ%2FNWyvxm0iUZr6RxTDdohdW3zJl8he81u8EUL6%2BDdhDnTi7CllpKE8KrCWLg95R5xPGXbETbuUT4qOmbqiDFyRHioaLwjniweS3htETX7KPrp5IH7fW%2BRMmH5lvs17gevQv9wuEgUBTT3KIzZwBVFXKQ%2BicBDOkepitVzmWAFdTREYTOhCG7WpkMcW63Jkx78YtEJ3%2FALOXCm%2B9LkYRrB1FuCMyAIFFQIzNyfC4wgH1UBbXOHeQxhIbbGhw7%2BjDTQeBbY9iTIQVMmY39PE5Id70bgiVTk0CycXXU4J%2FPRs1p8dArVbuxpMhU5N6DdV4TWLwHm4Hs7FzvpiNspnNTxPiMvob9vg3IqBZVuAP9hgstF0Agmp%2FuiZaAK2lIRSRQv%2Bsj5DmbGrDGnVmnQIXJLdkN2UFl16ck0TR4mF3n3r%2F50V7AJrzgg4zgA8BlnEoXS700wihEFnG1ByMLQFY2b8VhDRp1PNp8cs2rl1A0UgcruhoXPYOEoDctVdMrAKmx4IS1boWikvZkadTgD%2FVJrm3LJxYoFi4Uw7ol6Aijz3QTG9Mr2ZklzDhh0hWbf1rrFxs2JiUy0%2BCjuE7CnlPLykUezWdVoJdtiJeTCOy5LOBjqkATId91dXUh6YyQHDCTtZopZ95k4XSTCu3wx11PSUeKAAfhXV5SpwafTN6GqKLPMUggUlp49ul0hmfrwyH%2FFYbtQlVe5JB0ukZzNmw0W5Ah%2BOM4%2BzUUPxM3he%2BoRBCw1B8rPF%2FoCpuOaAc5X4NnWQKrlo%2FLJt1Z7iXpswt0%2BTvTV09%2Fz3lUJidFS7%2BEn5RbAQl45RQq%2Bn53yzJOyOHQ%2BET7jO35IE&X-Amz-Signature=29e5de87e91619fe4300427080dd8ab510007f6cebf4a1cca82e6984cb84719c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTJBTR6U%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChSVSxg8gXGdqm6djDOdktxLMv%2BYzGiyhYe%2BJLCMEtWAIhALf0YnVquRpIULmmzBhkXEpJmEH5QPEOXnUTuA2sIyCoKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FGuQTI1ba%2FOo7iKgq3AOl9SNQbgmt3N8AKYFFFDzhHGJ%2FNWyvxm0iUZr6RxTDdohdW3zJl8he81u8EUL6%2BDdhDnTi7CllpKE8KrCWLg95R5xPGXbETbuUT4qOmbqiDFyRHioaLwjniweS3htETX7KPrp5IH7fW%2BRMmH5lvs17gevQv9wuEgUBTT3KIzZwBVFXKQ%2BicBDOkepitVzmWAFdTREYTOhCG7WpkMcW63Jkx78YtEJ3%2FALOXCm%2B9LkYRrB1FuCMyAIFFQIzNyfC4wgH1UBbXOHeQxhIbbGhw7%2BjDTQeBbY9iTIQVMmY39PE5Id70bgiVTk0CycXXU4J%2FPRs1p8dArVbuxpMhU5N6DdV4TWLwHm4Hs7FzvpiNspnNTxPiMvob9vg3IqBZVuAP9hgstF0Agmp%2FuiZaAK2lIRSRQv%2Bsj5DmbGrDGnVmnQIXJLdkN2UFl16ck0TR4mF3n3r%2F50V7AJrzgg4zgA8BlnEoXS700wihEFnG1ByMLQFY2b8VhDRp1PNp8cs2rl1A0UgcruhoXPYOEoDctVdMrAKmx4IS1boWikvZkadTgD%2FVJrm3LJxYoFi4Uw7ol6Aijz3QTG9Mr2ZklzDhh0hWbf1rrFxs2JiUy0%2BCjuE7CnlPLykUezWdVoJdtiJeTCOy5LOBjqkATId91dXUh6YyQHDCTtZopZ95k4XSTCu3wx11PSUeKAAfhXV5SpwafTN6GqKLPMUggUlp49ul0hmfrwyH%2FFYbtQlVe5JB0ukZzNmw0W5Ah%2BOM4%2BzUUPxM3he%2BoRBCw1B8rPF%2FoCpuOaAc5X4NnWQKrlo%2FLJt1Z7iXpswt0%2BTvTV09%2Fz3lUJidFS7%2BEn5RbAQl45RQq%2Bn53yzJOyOHQ%2BET7jO35IE&X-Amz-Signature=847f0026112c8991acf3fe9bd606ff269f2af7b04816f649a61efea178b26c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







