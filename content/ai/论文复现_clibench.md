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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/0e35fb09-3f6a-41ca-81d8-654a4d034f3e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJAFSNG7%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBJo5ejrRbwdUIQEIaiOOQ2EM7usr03ivnxN5FZ%2FSd7tAiEA13oK0Fu2fJ6VJVqYJlH9jOr04xm6wP1i3qSA93QjQegq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKf09O%2FM9hwvvl33NyrcAwMGRRlju5OSUIv6aT0CvC1fjDgorjYEMMkozEPrjIjVjRyCkCUgfeBUkoR2O1yi6Vhfs3LmI4UIvc6UXSz5vCzhggW70LOFyFgNIg75ELhmExGQzGak5n%2FYdzwdCzZ0%2F%2BGXhBj0AbGnTVKvVwI9H0D5k8ZWJjZPaeQWXo5tZ5qJ%2Bi3CV6DipvSNoFgjCv9nXEaN6L0Q0eYlKEvsN7e%2FHZLI7y62yCvwa1AVABwuORO0754H6qW0hVuncf0ORBNAX1L2Kq1H1o14dJN33LK3uPM5ZgEHcoPJgE7RBKfvPXX6ancPPgQyJmQ7ve7KLCpZLipcyi00aUztgjb%2Fv%2BIbO1DAkeLGe8o%2FL40FGgNk5TMmQ%2F9PetlFRfZHAFEIuFCXRzS4VFBzYBgA7L%2BZqvPOJ7Qc5uxk9m7zjx8rJqqwy4fhiJr6NiX6qfK5MhwFuLcg%2FCt0st1wlWgjFOpkYKRIv1fZX6brqWe98dxnv9AuuAI6n9S5zW2YsUvzLQwTig0cSaZFe10wyqi6Ficovc0FS8hPNz86SDie8vsmrZwwSDafqROkyq5zhKfNE1qIWLowo5%2BBylJAYOUw4EhKy6L5PKFQE%2BbFpxxvyJZiupZWwUGvBTDIe6wPGh9cwN6kMKOwmckGOqUBBGUbIiGKS8m1JUDmrgquzUpzWcoBnLG7OpB4ZsBWjNd0vSYyKvIPUNLAKot4HpFUbxGj0sk56SZqB4GchiJ9uOJg6936CnchpQks5Ogo%2BZUOjVr25wXEZ7ZIGD%2BfBn5wT1fQOzqts2zAw2lGOO5hsmSIyqfXbvoKYTBDov1Iv3hKObulO1xk4koepfFzbs7jVmysxBJt8IGgpa6mH%2Blw2WO%2FESbd&X-Amz-Signature=abeae619f5727d430a2e0cf584b1cd0a26555e94d4a9325ab6b2cd6184b7cdd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 论文简介

将人工智能（AI），特别是大型语言模型（ LLMs ）集成到临床诊断过程中，为提高医疗保健的效率和可及性提供了巨大的潜力。虽然LLMs在医学领域显示出了一些前景，但它们在临床诊断中的应用仍未得到充分探索，特别是在现实世界的临床实践中，需要做出高度复杂的、针对患者的决策。目前该领域LLMs的评估范围往往较窄，侧重于特定疾病或专业并采用简化的诊断任务。为了弥补这一差距，我们引入了 CliBench，这是一种根据 MIMIC IV 数据集开发的新型基准，可以对LLMs的临床诊断能力进行全面而现实的评估。该基准不仅涵盖各个专业的各种医疗案例的诊断，还包含具有临床意义的任务：治疗程序识别、实验室测试安排和药物处方。在结构化输出本体的支持下，CliBench 能够进行精确的多粒度评估，让您深入了解LLM在所需粒度的各种临床任务上的能力。我们对领先的LLMs进行零样本评估，以评估他们在临床决策方面的熟练程度。我们的初步结果揭示了当前LLMs在临床环境中的潜力和局限性，为LLM驱动的医疗保健的未来进步提供了宝贵的见解。

### 核心目的

本论文旨在探讨如何将大型语言模型（LLMs）应用于临床诊断过程中，以提高医疗保健的效率和可访问性。然而，目前在真实临床实践中，LLMs在临床诊断中的应用仍未得到充分探索。

### 实验思路

本论文提出了一个名为CliBench的基准测试，它涵盖了来自不同专业的各种医疗病例的诊断，并包括治疗程序识别、实验室测试订购和药物处方等具有临床意义的任务。通过结构化输出本体支持，CliBench可以进行精确的多粒度评估，从而深入了解LLMs在不同临床任务上的能力。

### 实验结果

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5dfd9515-7800-4530-878e-f83eb1330acc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJAFSNG7%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBJo5ejrRbwdUIQEIaiOOQ2EM7usr03ivnxN5FZ%2FSd7tAiEA13oK0Fu2fJ6VJVqYJlH9jOr04xm6wP1i3qSA93QjQegq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDKf09O%2FM9hwvvl33NyrcAwMGRRlju5OSUIv6aT0CvC1fjDgorjYEMMkozEPrjIjVjRyCkCUgfeBUkoR2O1yi6Vhfs3LmI4UIvc6UXSz5vCzhggW70LOFyFgNIg75ELhmExGQzGak5n%2FYdzwdCzZ0%2F%2BGXhBj0AbGnTVKvVwI9H0D5k8ZWJjZPaeQWXo5tZ5qJ%2Bi3CV6DipvSNoFgjCv9nXEaN6L0Q0eYlKEvsN7e%2FHZLI7y62yCvwa1AVABwuORO0754H6qW0hVuncf0ORBNAX1L2Kq1H1o14dJN33LK3uPM5ZgEHcoPJgE7RBKfvPXX6ancPPgQyJmQ7ve7KLCpZLipcyi00aUztgjb%2Fv%2BIbO1DAkeLGe8o%2FL40FGgNk5TMmQ%2F9PetlFRfZHAFEIuFCXRzS4VFBzYBgA7L%2BZqvPOJ7Qc5uxk9m7zjx8rJqqwy4fhiJr6NiX6qfK5MhwFuLcg%2FCt0st1wlWgjFOpkYKRIv1fZX6brqWe98dxnv9AuuAI6n9S5zW2YsUvzLQwTig0cSaZFe10wyqi6Ficovc0FS8hPNz86SDie8vsmrZwwSDafqROkyq5zhKfNE1qIWLowo5%2BBylJAYOUw4EhKy6L5PKFQE%2BbFpxxvyJZiupZWwUGvBTDIe6wPGh9cwN6kMKOwmckGOqUBBGUbIiGKS8m1JUDmrgquzUpzWcoBnLG7OpB4ZsBWjNd0vSYyKvIPUNLAKot4HpFUbxGj0sk56SZqB4GchiJ9uOJg6936CnchpQks5Ogo%2BZUOjVr25wXEZ7ZIGD%2BfBn5wT1fQOzqts2zAw2lGOO5hsmSIyqfXbvoKYTBDov1Iv3hKObulO1xk4koepfFzbs7jVmysxBJt8IGgpa6mH%2Blw2WO%2FESbd&X-Amz-Signature=945a2707c8f428e1f144481ac8237a7957f6e84728605d85280e97a9a69b978f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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







