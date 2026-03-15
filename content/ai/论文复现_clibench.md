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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMSOQTWC%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLUb7pw6b8sqb%2FM4guPIWPX%2FMzNmoR6p9rr6E7pPvNXwIhALk86wMyitib3GOq07gpR8%2BGDPonqXRsytI44d6VKPQIKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIB7f269Vz%2BRDFcc4q3AMWJR0iHr42vxSJp%2FI2v535dDx7W937dbcdUXP4ECqqG7XCL%2F3avsf1a%2BA9kxVqr%2BGYoI3MXcSoTnCWhn9esKjaBknmFieM2umhj6ZSPV%2FA5LDD9UF0izpiAZ7MnyV%2FUTuPX9NR1a5WIuS%2FkribO2Jqzu7SUlN9el1bRBDVrsjSub5GtAdE%2FUq1avhgc2AlczmZxwX%2F5QXX3RlXftZVHhqAhF%2FsF9VYMIsHG8Q0nETBeMmkX4SZWgguocpPVBgWlqBdwVjxbPqrXCZB4iQdkr2QroxSS1uBc2aXZGKTfWW7N5uCxaEuPI2K5epcbmovTMbEBoU%2Bb128I8H16kgtvlEyehpI4YseKhxB5M66%2BrVPqDIxyGZrga8pqYum2%2Bqsv1MPpRXSgdTV6LhFIx%2Fy%2BkCUptZFadVX0wsk8AG%2FG7LJfATJhSiFOxkdlg6SfGmLQjWH26Vzs0Ff2BDjNgdbPoLzAK71jFyvRmu3GbvkDzJyUR6a8IGbkXn1085yqpdHF9T4RqeIUqSy3mBOXLl4B81AC2d5bhXXMxtAQDJp5XbOoHQ%2BYCfBppqMkIxrywsABtowngrSThbWdU5gQY3JwbYd46647QXpDIbM9LIjiApoaKs97tJ2zk0UyVTg3TDHkNjNBjqkAfbndcf7eYelFYYKgclZK92Ek5UsQ8KFF0UfOLilJCIeqy3WmGkOZjtPo767O2EQpQcEXYRgvbSiViDH2DubpstbyI2x45Jy1HeHQmsxj6QpTrM9R2S%2Be8RmfpAey8e1TNRtAoVEivELXTzhx32EaXdxYuSMhCFUfsKoALKTGQDpXvZ207COU3nOJidIDnOPT3JM9sadOJYevciV1RwKPanGPO%2Fz&X-Amz-Signature=15ecedb85856ead2ae90504387f4c19da916fc23117b8a664312bb7ffff63b55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMSOQTWC%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDLUb7pw6b8sqb%2FM4guPIWPX%2FMzNmoR6p9rr6E7pPvNXwIhALk86wMyitib3GOq07gpR8%2BGDPonqXRsytI44d6VKPQIKogECLL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzIB7f269Vz%2BRDFcc4q3AMWJR0iHr42vxSJp%2FI2v535dDx7W937dbcdUXP4ECqqG7XCL%2F3avsf1a%2BA9kxVqr%2BGYoI3MXcSoTnCWhn9esKjaBknmFieM2umhj6ZSPV%2FA5LDD9UF0izpiAZ7MnyV%2FUTuPX9NR1a5WIuS%2FkribO2Jqzu7SUlN9el1bRBDVrsjSub5GtAdE%2FUq1avhgc2AlczmZxwX%2F5QXX3RlXftZVHhqAhF%2FsF9VYMIsHG8Q0nETBeMmkX4SZWgguocpPVBgWlqBdwVjxbPqrXCZB4iQdkr2QroxSS1uBc2aXZGKTfWW7N5uCxaEuPI2K5epcbmovTMbEBoU%2Bb128I8H16kgtvlEyehpI4YseKhxB5M66%2BrVPqDIxyGZrga8pqYum2%2Bqsv1MPpRXSgdTV6LhFIx%2Fy%2BkCUptZFadVX0wsk8AG%2FG7LJfATJhSiFOxkdlg6SfGmLQjWH26Vzs0Ff2BDjNgdbPoLzAK71jFyvRmu3GbvkDzJyUR6a8IGbkXn1085yqpdHF9T4RqeIUqSy3mBOXLl4B81AC2d5bhXXMxtAQDJp5XbOoHQ%2BYCfBppqMkIxrywsABtowngrSThbWdU5gQY3JwbYd46647QXpDIbM9LIjiApoaKs97tJ2zk0UyVTg3TDHkNjNBjqkAfbndcf7eYelFYYKgclZK92Ek5UsQ8KFF0UfOLilJCIeqy3WmGkOZjtPo767O2EQpQcEXYRgvbSiViDH2DubpstbyI2x45Jy1HeHQmsxj6QpTrM9R2S%2Be8RmfpAey8e1TNRtAoVEivELXTzhx32EaXdxYuSMhCFUfsKoALKTGQDpXvZ207COU3nOJidIDnOPT3JM9sadOJYevciV1RwKPanGPO%2Fz&X-Amz-Signature=a291b5ae5ec2e459c69cc8fed3c3ff7a614a1cd4e8bdb1f6e7846069a935abc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







