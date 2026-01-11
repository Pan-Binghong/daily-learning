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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZBF4OCY%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGA8lRKoZeMEn%2BnA0cJYWsNnYlZuGulL4cnwyt7A2Z7fAiB6AM4UgDF0Gg3d5PG1NOAyYCtiUMvzrD1qKg1JBG5%2F1iqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyzjnzDbEwMthJfSKKtwDOP0fwkDgGQ2Ml%2Bo3ZZBsui7kvi7SbwvpKYaUe%2BwiG36FD62BoF%2FtrLw6zhfZAIjXaKw%2FbUck%2BXLeRUyNfxmKmDFnr8y%2F5bSIl7WNj4afMoQQAgy7o%2BEOe%2FdNTvGG%2F%2F4zFF5cLaEVC3Hs0gizPiSDlgqVfe2c2ka6ePlvNk2Yplrhi9G5sC9p9TNvXCw2kUSpKa6w%2BU%2F0v4JYPOiENJSid11Mckrjq7wLrOzhL%2B7ISe1KWJXYVFH%2FSVOt0AS%2BIH8Rj1bL7zdUdHr2gOtsPm3iRRDH4v4xkJp5Y6NTyb%2FSePDozW6T57tYQ8BZ1PaI%2B0IBkbQP9PSzW2cqj5DQtnckzaIRz6iX75Bs8zvXzTv04qDrKzbQ8OfxKZzM3h7dZsLPuckMI2DTDYgrhq2WNtEzerDNyt0V7lANi93z5JjEHXt2%2F8fQrh8Uh9tTrfkmN7IjDWd15HwSthyi%2F1XmI74tbsmH8eFdKHxQOwFTbjO6urY%2FHI5AB9508huYajSL6C5Vf4PgOZLbgc3f%2BolhnGiX%2BUNgdqiBVssILtFjq%2FCqNm%2B54fCQejmT8kmv03%2BqqDo5QgDqdBT6bgY46PpBcE3ojM1VHOqxaRhOBMaGWWcdmrTIzFYY4O%2BHIF7z2UEw9PiLywY6pgGaxjLBaFkK9Xj8nUPX4OnjulrFjvZSNaYcfSNCOQaHEWWrjfKAjCevc%2Bq4oKQEinhvMIq4h5rsKCQ1qPY4vfp8WfKAkJuSKVo2x9OSMTx9a57Iux1QbOewmS1D9Ril6ep8GU4l3YbxAt9f%2F15XJ%2BvdNlwHOy2NAIQAMlaoBsGwoJPuDnKY6DCddm8hFqIzLv8xJgKuwYy84sduGBFiclh9rvkbOu5T&X-Amz-Signature=63163043a8b5d28541e56902d856c205de7545c3e5337bb50fc47bda2fb5e41b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZBF4OCY%2F20260111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260111T030946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIGA8lRKoZeMEn%2BnA0cJYWsNnYlZuGulL4cnwyt7A2Z7fAiB6AM4UgDF0Gg3d5PG1NOAyYCtiUMvzrD1qKg1JBG5%2F1iqIBAjL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyzjnzDbEwMthJfSKKtwDOP0fwkDgGQ2Ml%2Bo3ZZBsui7kvi7SbwvpKYaUe%2BwiG36FD62BoF%2FtrLw6zhfZAIjXaKw%2FbUck%2BXLeRUyNfxmKmDFnr8y%2F5bSIl7WNj4afMoQQAgy7o%2BEOe%2FdNTvGG%2F%2F4zFF5cLaEVC3Hs0gizPiSDlgqVfe2c2ka6ePlvNk2Yplrhi9G5sC9p9TNvXCw2kUSpKa6w%2BU%2F0v4JYPOiENJSid11Mckrjq7wLrOzhL%2B7ISe1KWJXYVFH%2FSVOt0AS%2BIH8Rj1bL7zdUdHr2gOtsPm3iRRDH4v4xkJp5Y6NTyb%2FSePDozW6T57tYQ8BZ1PaI%2B0IBkbQP9PSzW2cqj5DQtnckzaIRz6iX75Bs8zvXzTv04qDrKzbQ8OfxKZzM3h7dZsLPuckMI2DTDYgrhq2WNtEzerDNyt0V7lANi93z5JjEHXt2%2F8fQrh8Uh9tTrfkmN7IjDWd15HwSthyi%2F1XmI74tbsmH8eFdKHxQOwFTbjO6urY%2FHI5AB9508huYajSL6C5Vf4PgOZLbgc3f%2BolhnGiX%2BUNgdqiBVssILtFjq%2FCqNm%2B54fCQejmT8kmv03%2BqqDo5QgDqdBT6bgY46PpBcE3ojM1VHOqxaRhOBMaGWWcdmrTIzFYY4O%2BHIF7z2UEw9PiLywY6pgGaxjLBaFkK9Xj8nUPX4OnjulrFjvZSNaYcfSNCOQaHEWWrjfKAjCevc%2Bq4oKQEinhvMIq4h5rsKCQ1qPY4vfp8WfKAkJuSKVo2x9OSMTx9a57Iux1QbOewmS1D9Ril6ep8GU4l3YbxAt9f%2F15XJ%2BvdNlwHOy2NAIQAMlaoBsGwoJPuDnKY6DCddm8hFqIzLv8xJgKuwYy84sduGBFiclh9rvkbOu5T&X-Amz-Signature=d56f10362ceeec883314c05211734de969b777d2f05587e9267baedb11b80da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







