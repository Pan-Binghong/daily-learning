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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BLTPB7%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmbdFe2OfARA83i5ikJ9NA%2FoyYtHHl9C6c6BRtJkfv1AiBM1WSGy33Vj6w2Uqjtfr6ADRomI0axGkwB4g1vYT%2FwMCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFnGDV%2BrooZ1xgwwIKtwDq6XsrVBMtOqRD%2BEbo1n2W1Tbfgpdp0UHj8iXHj3jwkQcjs6kcQW7RbczbR25I%2BrOOvpkhQivc46TvmPOUThzRXbP5Yg24JT%2BArmPA2C4iope0iQ8FVJJRbBz3ZvApXiAP5ue8nAVFPoUzdWVY2gFqmgyO333jbswDpmTaq232fAYXRvwYJld4EEByoYwEXEVa0gFV2CUXDypFfqLwWm8MB3UsPGAF4AnunzT%2BE1sSosnKRjSpo69TIuX79IiJQ4P62NGUSktrqS4%2FHn8Opu4vnWVBFpmK5BbwHvALpS20nRs6Wksx02HWsvrDA4KzZZ75w4kyI%2BM30fHq87wniWTOK0epUOmtK1O0o7tB0X3N7Zng6OPpd4bNe6q%2BaTuTVJhdrzINdrtFQ37bwtz3Dq0kF0C5%2B%2F3C0VQm%2Bh6qOz0BeZr6ptVsVP7u2B62bjUDTQYC3nBj9yug1ZRcc61n8epiHaPhFqtcaZAH1r8UZAjaWDGzlFdnOYZojFRao%2BnZm94Ihm2wpI8utoSP8iZ0d0qDpbI6Ra0wOrwsuQbEfDUs3Fo%2BY6sILD5eUcMAjTV4UX4aafS7VgP4%2BAtH5YjSow4CUHBzoxiMbZZA7NPBxtaZlDaMgReeqSyCdSP9JUw7oHTzQY6pgGYD5HbWFVyJmSsumnsgZGSeJFEu4c2l0RwWitvQryXqcIH7jB%2Byek2YeIGpDWYV9HUm%2F5G03nPOInBmWLSWCcgHH3AHLis2TZBSVa%2BW4RIyOu801AKQFGCsByMb83%2B%2Fci53Q2R7PPQGrPud3FMeoTBsnIEeW9EEPy8F%2B63THkzaJnlvd8d17ubMt87mqUncdhLBIDMj3Q1b3SztxfRwIGFTRNcQGB2&X-Amz-Signature=ca364b9bd3e4decbe22d99dc27babc4e95fbc324d7cb10b3acae67902d832995&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W4BLTPB7%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGmbdFe2OfARA83i5ikJ9NA%2FoyYtHHl9C6c6BRtJkfv1AiBM1WSGy33Vj6w2Uqjtfr6ADRomI0axGkwB4g1vYT%2FwMCqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFnGDV%2BrooZ1xgwwIKtwDq6XsrVBMtOqRD%2BEbo1n2W1Tbfgpdp0UHj8iXHj3jwkQcjs6kcQW7RbczbR25I%2BrOOvpkhQivc46TvmPOUThzRXbP5Yg24JT%2BArmPA2C4iope0iQ8FVJJRbBz3ZvApXiAP5ue8nAVFPoUzdWVY2gFqmgyO333jbswDpmTaq232fAYXRvwYJld4EEByoYwEXEVa0gFV2CUXDypFfqLwWm8MB3UsPGAF4AnunzT%2BE1sSosnKRjSpo69TIuX79IiJQ4P62NGUSktrqS4%2FHn8Opu4vnWVBFpmK5BbwHvALpS20nRs6Wksx02HWsvrDA4KzZZ75w4kyI%2BM30fHq87wniWTOK0epUOmtK1O0o7tB0X3N7Zng6OPpd4bNe6q%2BaTuTVJhdrzINdrtFQ37bwtz3Dq0kF0C5%2B%2F3C0VQm%2Bh6qOz0BeZr6ptVsVP7u2B62bjUDTQYC3nBj9yug1ZRcc61n8epiHaPhFqtcaZAH1r8UZAjaWDGzlFdnOYZojFRao%2BnZm94Ihm2wpI8utoSP8iZ0d0qDpbI6Ra0wOrwsuQbEfDUs3Fo%2BY6sILD5eUcMAjTV4UX4aafS7VgP4%2BAtH5YjSow4CUHBzoxiMbZZA7NPBxtaZlDaMgReeqSyCdSP9JUw7oHTzQY6pgGYD5HbWFVyJmSsumnsgZGSeJFEu4c2l0RwWitvQryXqcIH7jB%2Byek2YeIGpDWYV9HUm%2F5G03nPOInBmWLSWCcgHH3AHLis2TZBSVa%2BW4RIyOu801AKQFGCsByMb83%2B%2Fci53Q2R7PPQGrPud3FMeoTBsnIEeW9EEPy8F%2B63THkzaJnlvd8d17ubMt87mqUncdhLBIDMj3Q1b3SztxfRwIGFTRNcQGB2&X-Amz-Signature=99e19756a9a27b4070a3a56867457b2649fc988ba9eccedcb15d72faa2896c36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







