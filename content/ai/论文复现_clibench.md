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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5TASZDT%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDcfGDVV%2BgkkVFisVhvB5uChWVGKRjZCj2oxDeCpRyS3gIhAOyNqtES3lDUqupDX0cm6FZmLYfCTap0xDxtQi9wH0OzKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiBDAyEAL%2FhFVGPwoq3AOIcaanXHv7Bqxdmpt2BVesy0fv9FYDzj7lMiiNJpjV15SOX8PPyO2jtO%2BLGapgCw0XBppyxTfALRZC8yJMJCdZf5M0lS7et7X6M30HL9GgIUV5%2BvuPQzrlC37cJ6TtrCFtdSIgZfjf8lzkHYwCbmm6BUMQ3MvQmaPpnwK6qV4%2FJP97LKA7Ok7Agwrhwseqc%2F%2F5wqx0AfW0Tx8L2oqDQeqvP0xP3BE%2FbpwTFKlmMshNDR7r2FwDglP27Rqb%2F1%2BkZd%2FW4Qr%2FlWge7nwcMVo2lQr2vdjpTXCQvYFdOmzPd95WNMUk%2F9anGxmQR4ecuiMFquiKovX%2FsOzSwRooA%2FT4fgh2Z5NhZCd34M5mXMg9GKgA%2BpW8pDuRB%2FinwQ1s2nkKYqupAtKurJiwMOxfIg%2ByD3f0OWhythLKkeUWIfBv4mFG76wn39VDGyGfyjA7FmBaoDYMhAL5mA1RjUiq%2FA40hJFOEZ3RgBKYnF6jarRI86tchcVCFGQWDJlezMNSKD5%2BJgV9%2F%2BNmI%2F5L2%2FhamL83ZrIeybMI0M3d3HRZp7WMpwuZVMDGE2qvghEiTZQTQHIsqTUE12exGb2Ad7Lq8a5P4HFNFbjzdI2yIcbO96dAldkwBJydjXCu5pqNnoxlUjDFtujJBjqkAWw6LTSeTna79%2FrmHNuDsGS0O81KxlwW7hHTfuhXKhj8L9voL3wQw3Bvdkolihd9vai0sHFJ%2FojAHZxzXwpBIYEbpNQk0RwNl4k5ewdpIZrOSswsBq%2BKCohKwy2IvZxRLnb6ko46lIiiUIWIXdAeXbDFA0n3yHkxnkB4uWZA0M3UDHZePMBbHcHxvK0bk0aw3TJAnihZihh3%2FVpKxIFl4WWmUi5t&X-Amz-Signature=60132bbc12cbd1c120d5f6808f7b1a60452df8a70d1fb99788a33cf767bf27f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5TASZDT%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQDcfGDVV%2BgkkVFisVhvB5uChWVGKRjZCj2oxDeCpRyS3gIhAOyNqtES3lDUqupDX0cm6FZmLYfCTap0xDxtQi9wH0OzKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxiBDAyEAL%2FhFVGPwoq3AOIcaanXHv7Bqxdmpt2BVesy0fv9FYDzj7lMiiNJpjV15SOX8PPyO2jtO%2BLGapgCw0XBppyxTfALRZC8yJMJCdZf5M0lS7et7X6M30HL9GgIUV5%2BvuPQzrlC37cJ6TtrCFtdSIgZfjf8lzkHYwCbmm6BUMQ3MvQmaPpnwK6qV4%2FJP97LKA7Ok7Agwrhwseqc%2F%2F5wqx0AfW0Tx8L2oqDQeqvP0xP3BE%2FbpwTFKlmMshNDR7r2FwDglP27Rqb%2F1%2BkZd%2FW4Qr%2FlWge7nwcMVo2lQr2vdjpTXCQvYFdOmzPd95WNMUk%2F9anGxmQR4ecuiMFquiKovX%2FsOzSwRooA%2FT4fgh2Z5NhZCd34M5mXMg9GKgA%2BpW8pDuRB%2FinwQ1s2nkKYqupAtKurJiwMOxfIg%2ByD3f0OWhythLKkeUWIfBv4mFG76wn39VDGyGfyjA7FmBaoDYMhAL5mA1RjUiq%2FA40hJFOEZ3RgBKYnF6jarRI86tchcVCFGQWDJlezMNSKD5%2BJgV9%2F%2BNmI%2F5L2%2FhamL83ZrIeybMI0M3d3HRZp7WMpwuZVMDGE2qvghEiTZQTQHIsqTUE12exGb2Ad7Lq8a5P4HFNFbjzdI2yIcbO96dAldkwBJydjXCu5pqNnoxlUjDFtujJBjqkAWw6LTSeTna79%2FrmHNuDsGS0O81KxlwW7hHTfuhXKhj8L9voL3wQw3Bvdkolihd9vai0sHFJ%2FojAHZxzXwpBIYEbpNQk0RwNl4k5ewdpIZrOSswsBq%2BKCohKwy2IvZxRLnb6ko46lIiiUIWIXdAeXbDFA0n3yHkxnkB4uWZA0M3UDHZePMBbHcHxvK0bk0aw3TJAnihZihh3%2FVpKxIFl4WWmUi5t&X-Amz-Signature=e12f9344905b4ad199169ac9e22d13f001ba1fb4ad791ed63ddd68b8ae5a2ab6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







