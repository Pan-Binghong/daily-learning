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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U73FQ2LZ%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCeQIXGJ0dnrWyU%2F9jgBzZe9glG04vrAiFvJwm72mqd5wIhAJl23hPW2VyYtgTvDMB4EuInaADJtYbYyT3MX9vsoeMtKv8DCAkQABoMNjM3NDIzMTgzODA1IgyESEo30i8HEOChfgkq3AN2QGVrYyoyDa5VbyBnzO5fWqB%2BmM5WZ8ZmxkZ0zK0bGjOb%2BdvB0DsKbqhHbj84Mhg8ifKHhQk27ddx2AtCm11TOAZq6bFqlq21uJ1rXEZFz55XC6aLfH%2FzH6x2NJ%2FFmiLUv1MWNgOQy5kAOFQVX7w2r356bx9iUQ9V8eSRBem9sySCTiuu0l63lJtHilaoW7QQXE19oaXDp5X716mXKr4XUc2fr07IcCoL38nBBCwDGdxpQhsfbE8%2FsJwaViBCt0G5Gz4tW7Ymyym8piqAIqDXlwCkPMF8DFHLyTZpEFG1zItYQ%2BmICf6wqHFBWZ6nLvZOtVXeCGFvVHphsGLQX4vOIbeaAgYHuOlJmr%2FtDNrEtz%2Bpft3GxWS8KtQPwIXK3SX%2BaodjKT883Hyb61j88wdoIkYIufx%2FWzcTtNvPhpp7JB%2BCzK2%2BEpP0xnOy3dAO2LPYfCGVi0F%2FoMdQeWoOTAJ50t8oUL77i%2Bp33QPeY8d0K3EwUwgdv0EyZkVkzDgDGxgsw%2FcH1aiR9TTp8EGQGSLxVi%2BQXBuqrft8PEeU8hos9fVB9zEcV3taDb1wzq%2Fv6UY94Z9XHohigyTtsbsDrTMecdCWk0zQs93MxXYIr2DtiFVnAfvOAPp6t3RHBTDU3rjJBjqkAYPEC42sC0YEn4%2Fk6hfWlMRx6njd%2FYzQflXCSngDUiop450eeAkx%2FRmCyW%2Fcq2tMnO3pL75aLMzehMY1nZuNULfZqCZ%2Fy9xnQiRktLD3U6s%2Bh8qWP8SA%2BSqn9CSbbbLp%2FmQmz4jErs3QAhBzKefMJqOqbyd6nx8W4sENn878nnL0l5ynP9kc0L3wXPAhZwzsdT3yhAXFjcd5q7CHd0usM2YCRdl1&X-Amz-Signature=28f83d384a4cab0f97faffd103d013afa9d80469a662ffd0625c3515a0753bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U73FQ2LZ%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQCeQIXGJ0dnrWyU%2F9jgBzZe9glG04vrAiFvJwm72mqd5wIhAJl23hPW2VyYtgTvDMB4EuInaADJtYbYyT3MX9vsoeMtKv8DCAkQABoMNjM3NDIzMTgzODA1IgyESEo30i8HEOChfgkq3AN2QGVrYyoyDa5VbyBnzO5fWqB%2BmM5WZ8ZmxkZ0zK0bGjOb%2BdvB0DsKbqhHbj84Mhg8ifKHhQk27ddx2AtCm11TOAZq6bFqlq21uJ1rXEZFz55XC6aLfH%2FzH6x2NJ%2FFmiLUv1MWNgOQy5kAOFQVX7w2r356bx9iUQ9V8eSRBem9sySCTiuu0l63lJtHilaoW7QQXE19oaXDp5X716mXKr4XUc2fr07IcCoL38nBBCwDGdxpQhsfbE8%2FsJwaViBCt0G5Gz4tW7Ymyym8piqAIqDXlwCkPMF8DFHLyTZpEFG1zItYQ%2BmICf6wqHFBWZ6nLvZOtVXeCGFvVHphsGLQX4vOIbeaAgYHuOlJmr%2FtDNrEtz%2Bpft3GxWS8KtQPwIXK3SX%2BaodjKT883Hyb61j88wdoIkYIufx%2FWzcTtNvPhpp7JB%2BCzK2%2BEpP0xnOy3dAO2LPYfCGVi0F%2FoMdQeWoOTAJ50t8oUL77i%2Bp33QPeY8d0K3EwUwgdv0EyZkVkzDgDGxgsw%2FcH1aiR9TTp8EGQGSLxVi%2BQXBuqrft8PEeU8hos9fVB9zEcV3taDb1wzq%2Fv6UY94Z9XHohigyTtsbsDrTMecdCWk0zQs93MxXYIr2DtiFVnAfvOAPp6t3RHBTDU3rjJBjqkAYPEC42sC0YEn4%2Fk6hfWlMRx6njd%2FYzQflXCSngDUiop450eeAkx%2FRmCyW%2Fcq2tMnO3pL75aLMzehMY1nZuNULfZqCZ%2Fy9xnQiRktLD3U6s%2Bh8qWP8SA%2BSqn9CSbbbLp%2FmQmz4jErs3QAhBzKefMJqOqbyd6nx8W4sENn878nnL0l5ynP9kc0L3wXPAhZwzsdT3yhAXFjcd5q7CHd0usM2YCRdl1&X-Amz-Signature=a88f165857289d39ec0c0bbf70ec3321d40fcea8ef49e145900340b52218f665&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







