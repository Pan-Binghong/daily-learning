---
title: 基于Pytorch架构手撕Transformer
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-06-19T03:45:00.000Z'
draft: false
categories:
- AI
---

深入学习Tranformer模型结构, 本来依赖GPT4o, 自己快复现完了, 结果在封装Decoder层的时候, 发生了mask维度匹配不对的问题, 查了很多资料最终还是没解决, 后期再搞吧.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5976f44e-a761-4511-a4fc-db008f73023d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=714fc5a07b871b114b2d61ecaae9344db6cb1c8a47ee9b5fb222b58d207253fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## Transformer 的背景

- 什么是Transformer ?
- Transformer是谁提出的 ?
- Transformer解决了什么问题 ?
- Transformer核心组件有哪些 ?
---

## 注意力机制

- 核心公式 :
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/7ccda5e2-2427-4a14-a91e-cd3a1ad7fc58/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=bb56c453ac59cdc52dae5950ac8d50c82d65f5b6f1e954407d3e83d11323fea7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cb861907-c901-48ad-8055-a0b41d47106a/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=7e61c299f6cff87e3da8672778ec45fd14b3eec216b101702f9937329e7d89e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/2c6924da-ad53-4f28-b2c4-a2f769c588f2/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=47ae841d07b1289af77291a7fcea23dff9b2f51ab28f995fd0c2301c87731d99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 论文原图 :
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38c27c70-67d5-4420-bae3-bfb9ec5c7f30/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=47b1cd40240f8bfe1794907407300e56e9ca2ea8f0fcde1624678dfa8b3c6652&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### Scaled Dot-product Attention

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/90a969cd-6a3b-4923-bfd0-b511f94fd56d/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=ca7ab1627545cbb24e0abb5fbef6be6318526676a3fa701e0b6c8528c7441d69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 代码实现 :
### 代码整合(Scaled Dot-product Attention)

```python
import torch  # 导入PyTorch库
import torch.nn.functional as F  # 导入PyTorch的nn.functional模块，包含了许多神经网络操作的函数
from math import sqrt  # 导入math库中的sqrt函数，用于计算平方根

# 定义Scaled Dot-product Attention函数
def scaled_dot_product_attention(query, key, value, query_mask=None, key_mask=None, mask=None):
    # 获取查询（query）的最后一个维度大小，即键（key）的维度
    dim_k = query.size(-1)
    
    # 计算查询和键的点积，并缩放，得到未归一化的注意力分数
    scores = torch.bmm(query, key.transpose(1, 2)) / sqrt(dim_k)
    
    # 如果提供了查询掩码（query_mask）和键掩码（key_mask），则计算掩码矩阵
    if query_mask is not None and key_mask is not None:
        mask = torch.bmm(query_mask.unsqueeze(-1), key_mask.unsqueeze(1))
    else:
        # 如果没有提供掩码，则使用之前传入的掩码（如果有的话）
        mask = mask
    
    # 如果存在掩码，则将分数矩阵中与掩码对应位置为0的分数替换为负无穷
    # 这样在应用softmax时，这些位置的权重会接近于0
    if mask is not None:
        scores = scores.masked_fill(mask == 0, -float("inf"))
    
    # 使用softmax函数对分数进行归一化，得到注意力权重
    weights = F.softmax(scores, dim=-1)
    
    # 计算加权后的输出，即将注意力权重与值（value）相乘
    # 这里的输出是经过注意力加权后的值向量，用于下游任务
    return torch.bmm(weights, value)
```

### Multi-head Attention

- Multi-head Attention作用 :
首先通过线性映射将 Q,K,V 序列映射到特征空间，每一组线性投影后的向量表示称为一个头 (head)，然后在每组映射后的序列上再应用 Scaled Dot-product Attention, 最后将每个头的向量拼接.
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/ab37c920-8ea8-4dd4-b3a6-655932f8727c/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRFJGJB5%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsApvpifCdQIuH5gHSKUwM%2B81ZojBg7TE37dEtSh0oUQIgHQ0u1MjNd7ycscSYB1xAGVGHLSDg6hgSSscbMKYQ4ZsqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGsrD%2F%2Br2bRB5zN9oircA6qJ3VbmEyvqm8Omu5%2FIDaPTqoEx8IkIhY7c5GZ7Nh646V9fn8TaLAUopVuR6Z17vkLBXMswrRQhENjKZFhVhAF0riZ8nSU86qlzHcaYDsD2gsTSjUQtYF5iI9bcnXc3RKKnrPgU%2BkXX3%2BRh4MpehYfZWCF%2BYPvcVugXkaLriF1GeClQGkIUDCpjyFTl2NIB28UV1eZbsuNmXzoFPwMVKzye39I4%2B2vrybJV7TJulBW0tzhPQoCPH82zWMaRhBEZRE%2Fr5lrXmijuCfKsR2uxWhHk5T2CqMxLT3Q6vQJnBzCiQvQ%2FzNV9WyRJVsPp7OQiBYmgUG1poag8VIBfa9kYz9bOU1VTTSsSEiuFLmn5s9MizCu7B%2F3GUuLayu3zl3sit3XDbMt8vYWr1fy2Jot7wx6lKuQPFf0Wsp74r2kRyHtGmsSWPE8AYKlc1V0ggn6As4MU6iSSCOVSkUi2Y9qfO4M5Jax9c6Vi%2BXYGtORpmiHHxws6HrfUDQd3zTHm06I7uOQywBLBCLWp7GqCDXGNwGOkh598PjG4M3mw%2BjtSbd6Tb5D1M9fTDJM0nceo6lqvjNM4v%2Fmd38vEftUzhWvPxkAkm1Vy%2FgRH80OfqRpVApGCCDepmzFiLNvtnWMYMI2jrMgGOqUBYd54oG8hHl2wbMIxowp8j7MOnqx4rBCUKEpSghRLqjpZxOQgm55j%2FyJsVGrqSUK364QXtG1%2FU2eDEZ1K%2BJGOOZEh7YWccBjPwAWZ%2BDrsosBY318pGCbMXnuLPQ9syNQ95pAO027iAhgL%2FJW34r6Xz5fXZwUeXaueyUtkPt5AMlQQnnPoCD%2FxovMBpaWTwcqu%2FxoDBWnt9qVMra3hZVcMGcHlAeAm&X-Amz-Signature=b955db76a3ac923133aea57638a8d619caf4fd668fe0f19452bed3616dc33413&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 代码整合(Multi-head Attention)

- 代码实现 :
- 验证代码
---

## 前馈神经网络

### The Feed-Forward Layer

没啥好写的, 就是普通的全连接 + 激活函数

```python
from torch import nn

# 定义FeedForward类，继承自nn.Module
class FeedForward(nn.Module):
    # 初始化函数
    def __init__(self, config):
        super().__init__()  # 调用基类的初始化方法
        # 定义第一个线性层，将输入的隐藏状态映射到中间维度
        self.linear_1 = nn.Linear(config.hidden_size, config.intermediate_size)
        # 定义第二个线性层，将中间维度的表示映射回原始的隐藏状态维度
        self.linear_2 = nn.Linear(config.intermediate_size, config.hidden_size)
        # 定义GELU激活函数
        self.gelu = nn.GELU()
        # 定义Dropout层，用于防止过拟合
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    # 前向传播函数
    def forward(self, x):
        # 应用第一个线性层
        x = self.linear_1(x)
        # 应用GELU激活函数
        x = self.gelu(x)
        # 应用第二个线性层
        x = self.linear_2(x)
        # 应用Dropout
        x = self.dropout(x)
        # 返回最终的输出
        return x
```

与上面构建的注意力机制串联测试 :

```python
feed_forward = FeedForward(config)
ff_outputs = feed_forward(attn_output)
print(ff_outputs.size()) #torch.Size([1, 2, 768])

```

---

## 层归一化 & 残差连接

- 层归一化模块需要包含在残差模块内, 主要作用为 : 将输入的一批向量, 每一个都做标准化处理, 处理为 : 均值为零, 且有单位方差
- 残差连接主要作用为 : 是通过直接将输入绕过中间层的计算，帮助模型更容易训练深层网络，避免梯度消失问题并促进信息流动
### Transformer Encoder Layer

```python
from torch import nn

# 定义TransformerEncoderLayer类，继承自nn.Module
class TransformerEncoderLayer(nn.Module):
    # 初始化函数
    def __init__(self, config):
        super().__init__()  # 调用基类的初始化方法
        # 定义第一个层归一化，用于注意力机制之前
        self.layer_norm_1 = nn.LayerNorm(config.hidden_size)
        # 定义第二个层归一化，用于前馈网络之前
        self.layer_norm_2 = nn.LayerNorm(config.hidden_size)
        # 定义多头注意力机制
        self.attention = MultiHeadAttention(config)
        # 定义前馈神经网络
        self.feed_forward = FeedForward(config)

    # 前向传播函数
    def forward(self, x, mask=None):
        # 应用第一个层归一化
        hidden_state = self.layer_norm_1(x)
        # 应用注意力机制，并将结果与输入进行残差连接
        # 注意力机制的输出将与输入x相加，得到更新后的x
        x = x + self.attention(hidden_state, hidden_state, hidden_state, mask=mask)
        # 应用第二个层归一化
        # 注意这里的self.layer_norm_2(x)实际上是对更新后的x进行归一化
        hidden_state = self.layer_norm_2(x)
        # 应用前馈网络，并将结果与更新后的x进行残差连接
        x = x + self.feed_forward(hidden_state)
        # 返回最终的输出x
        return x
```

代码验证 :

```python
encoder_layer = TransformerEncoderLayer(config)
print(inputs_embeds.shape)
print(encoder_layer(inputs_embeds).size())
#torch.Size([1, 5, 768])
#torch.Size([1, 5, 768])
```

---

## 绝对位置编码

注意力机制无法捕获词语之间的位置信息，因此 Transformer 模型还使用 Positional Embeddings 添加了词语的位置信息。

```python
from torch import nn, LongTensor, arange

# 定义Embeddings类，继承自nn.Module
class Embeddings(nn.Module):
    # 初始化函数
    def __init__(self, config):
        super().__init__()  # 调用基类的初始化方法
        # 定义词嵌入层，将词ID映射到词向量
        self.token_embeddings = nn.Embedding(config.vocab_size, config.hidden_size)
        # 定义位置嵌入层，为序列中的每个位置生成一个唯一的位置向量
        self.position_embeddings = nn.Embedding(config.max_position_embeddings, config.hidden_size)
        # 定义层归一化，用于稳定训练过程
        self.layer_norm = nn.LayerNorm(config.hidden_size, eps=1e-12)
        # 定义Dropout层，用于防止过拟合
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    # 前向传播函数
    def forward(self, input_ids):
        # 根据输入序列的长度创建位置ID
        seq_length = input_ids.size(1)  # 获取序列长度
        position_ids = torch.arange(seq_length, dtype=torch.long).unsqueeze(0)  # 创建位置ID序列
        # 创建词嵌入和位置嵌入
        token_embeddings = self.token_embeddings(input_ids)  # 通过词嵌入层获取词嵌入
        position_embeddings = self.position_embeddings(position_ids)  # 通过位置嵌入层获取位置嵌入
        # 将词嵌入和位置嵌入相加，得到最终的嵌入表示
        embeddings = token_embeddings + position_embeddings
        # 应用层归一化
        embeddings = self.layer_norm(embeddings)
        # 应用Dropout
        embeddings = self.dropout(embeddings)
        # 返回最终的嵌入表示
        return embeddings

# 创建Embeddings层的实例，并使用config配置
embedding_layer = Embeddings(config)

# 使用embedding_layer处理输入的词ID，并打印输出的大小
# 这里假设inputs.input_ids是之前通过tokenizer得到的词ID序列
print(embedding_layer(inputs.input_ids).size()) #torch.Size([1, 5, 768])
```

### Transformer Encoder

```python
from torch import nn

# 定义TransformerEncoder类，继承自nn.Module
class TransformerEncoder(nn.Module):
    # 初始化函数
    def __init__(self, config):
        super().__init__()  # 调用基类的初始化方法
        # 创建嵌入层实例，用于将输入的词ID转换为嵌入向量
        self.embeddings = Embeddings(config)
        # 创建一个包含多个Transformer编码器层的列表
        # num_hidden_layers表示编码器中隐藏层的数量
        self.layers = nn.ModuleList([TransformerEncoderLayer(config) for _ in range(config.num_hidden_layers)])

    # 前向传播函数
    def forward(self, x, mask=None):
        # 首先通过嵌入层处理输入x
        x = self.embeddings(x)
        # 然后依次通过每个编码器层
        for layer in self.layers:
            # 将当前层的输出作为下一层的输入，并传递掩码（如果有的话）
            x = layer(x, mask=mask)
        # 返回最终的编码器输出
        return x
```

测试代码 :

```python
encoder = TransformerEncoder(config)
print(encoder(inputs.input_ids).size())  #torch.Size([1, 5, 768])
```

## 完整代码

```python
import torch
from torch import nn
import torch.nn.functional as F
from math import sqrt

class AttentionHead(nn.Module):
    def __init__(self, embed_dim, head_dim):
        super().__init__()
        self.q = nn.Linear(embed_dim, head_dim)
        self.k = nn.Linear(embed_dim, head_dim)
        self.v = nn.Linear(embed_dim, head_dim)

    def forward(self, query, key, value, mask=None):
        query, key, value = self.q(query), self.k(key), self.v(value)
        scores = torch.bmm(query, key.transpose(1, 2)) / sqrt(query.size(-1))
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -float("inf"))
        weights = F.softmax(scores, dim=-1)
        return torch.bmm(weights, value)

class MultiHeadAttention(nn.Module):
    def __init__(self, config):
        super().__init__()
        embed_dim = config.hidden_size
        num_heads = config.num_attention_heads
        head_dim = embed_dim // num_heads
        self.heads = nn.ModuleList(
            [AttentionHead(embed_dim, head_dim) for _ in range(num_heads)]
        )
        self.output_linear = nn.Linear(embed_dim, embed_dim)

    def forward(self, query, key, value, mask=None, query_mask=None, key_mask=None):
        if query_mask is not None and key_mask is not None:
            mask = torch.bmm(query_mask.unsqueeze(-1), key_mask.unsqueeze(1))
        x = torch.cat([h(query, key, value, mask) for h in self.heads], dim=-1)
        x = self.output_linear(x)
        return x

class FeedForward(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.linear_1 = nn.Linear(config.hidden_size, config.intermediate_size)
        self.linear_2 = nn.Linear(config.intermediate_size, config.hidden_size)
        self.gelu = nn.GELU()
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

    def forward(self, x):
        x = self.linear_1(x)
        x = self.gelu(x)
        x = self.linear_2(x)
        x = self.dropout(x)
        return x

class TransformerEncoderLayer(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.layer_norm_1 = nn.LayerNorm(config.hidden_size)
        self.layer_norm_2 = nn.LayerNorm(config.hidden_size)
        self.attention = MultiHeadAttention(config)
        self.feed_forward = FeedForward(config)

    def forward(self, x, mask=None):
        # Apply layer normalization and then copy input into query, key, value
        hidden_state = self.layer_norm_1(x)
        # Apply attention with a skip connection
        x = x + self.attention(hidden_state, hidden_state, hidden_state, mask=mask)
        # Apply feed-forward layer with a skip connection
        x = x + self.feed_forward(self.layer_norm_2(x))
        return x

class Embeddings(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.token_embeddings = nn.Embedding(config.vocab_size,
                                             config.hidden_size)
        self.position_embeddings = nn.Embedding(config.max_position_embeddings,
                                                config.hidden_size)
        self.layer_norm = nn.LayerNorm(config.hidden_size, eps=1e-12)
        self.dropout = nn.Dropout()

    def forward(self, input_ids):
        # Create position IDs for input sequence
        seq_length = input_ids.size(1)
        position_ids = torch.arange(seq_length, dtype=torch.long).unsqueeze(0)
        # Create token and position embeddings
        token_embeddings = self.token_embeddings(input_ids)
        position_embeddings = self.position_embeddings(position_ids)
        # Combine token and position embeddings
        embeddings = token_embeddings + position_embeddings
        embeddings = self.layer_norm(embeddings)
        embeddings = self.dropout(embeddings)
        return embeddings

class TransformerEncoder(nn.Module):
    def __init__(self, config):
        super().__init__()
        self.embeddings = Embeddings(config)
        self.layers = nn.ModuleList(
            [TransformerEncoderLayer(config) for _ in range(config.num_hidden_layers)]
        )

    def forward(self, x, mask=None):
        x = self.embeddings(x)
        for layer in self.layers:
            x = layer(x, mask)
        return x

if __name__ == '__main__':
    from transformers import AutoConfig
    from transformers import AutoTokenizer

    model_ckpt = "bert-base-uncased"\
    cache_dir = './pretrained_model'\
    tokenizer = AutoTokenizer.from_pretrained(model_ckpt, cache_dir=cache_dir)
    config = AutoConfig.from_pretrained(model_ckpt)

    text = "hello world"
    inputs = tokenizer(text, return_tensors="pt", add_special_tokens=False)

    encoder = TransformerEncoder(config)
    print(encoder(inputs.input_ids).size())
```

---

> [!IMPORTANT]

## 绝对位置编码

使用Pytorch实现Transformer中的绝对位置编码底层代码

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Positional_Encoding.py
@Time    :   2024/09/26 11:23:36
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   Transformer中的绝对位置编码底层代码实现
'''
import torch
import torch.nn as nn
import math
from transformers import BertTokenizer
import os

file_path = os.path.abspath(__file__)

dir = os.path.dirname(file_path)

os.chdir(dir)

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, max_len=5000):
        ''''
        :param d_model: 模型的维度
        :param max_len: 序列的最大长度
        '''
        super(PositionalEncoding, self).__init__()

        # 创建一个形状为 (max_len, d_model) 的矩阵, 用于存储位置编码
        pe = torch.zeros(max_len, d_model)

        # 创建一个形状为 (max_len, 1) 的矩阵, 用于存储位置信息, 保存索引值 e.g.[0, 1, 2, ... , max_len-1]
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)

        # 这段代码计算位置编码中的两个频率。具体来说，它生成一个从0到d_model（不包括d_model）的偶数序列，
        # 然后将这些偶数转换为浮点数，并乘以一个常数因子 (-math.log(10000.0) / d_model)。
        # 这个常数因子是通过对10000取自然对数并除以d_model得到的。
        # 最后，通过torch.exp函数计算这些值的指数，得到最终的div_term。
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

        # 应用正弦函数 得到偶数索引位置编码
        pe[:, 0::2] = torch.sin(position * div_term)

        # 应用余弦函数 得到奇数索引位置编码
        pe[:, 1::2] = torch.cos(position * div_term)

        # 增加一个 batch 维度, 使其能够与输入一起使用
        pe = pe.unsqueeze(0)

        # 将位置编码矩阵注册为一个参数, 并将其添加到模型参数列表中
        self.register_buffer('pe', pe)

    def forward(self, x):
        ''''
        :param x: 输入的序列张量, shape为: <batch_size, seq_len, d_model>
        :return: 输出的序列张量, shape为: <batch_size, seq_len, d_model>
        '''
        x = x + self.pe[:, :x.size(1), :]
        return x
    
if __name__ == '__main__':
    # 初始化参数
    d_model = 512
    max_len = 2048

    # 初始化位置编码
    pos_encoder = PositionalEncoding(d_model, max_len)

    # 初始化 tokenizer (这里以 Bert 为例)
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', cache_dir='./cache')

    # 使用输入"hello world"
    input_text = "hello world"
    input_ids = torch.tensor([tokenizer.encode(input_text, add_special_tokens=True)])

    # 创建一个形状为 (1, seq_len, d_model) 的零矩阵
    x = torch.zeros(1, input_ids.size(1), d_model)

    # 应用位置编码
    output = pos_encoder(x)

    print("Input Text:", input_text)
    print("Input IDs Shape:", input_ids.shape)
    print("Output Shape:", output.shape)
    print("Output:", output)
```

以上案例为 : 当输入hello world, 经过编码后输出其对应的信息

```shell
Input Text: hello world
Input IDs Shape: torch.Size([1, 4])
Output Shape: torch.Size([1, 4, 512])
Output: tensor([[[ 0.0000e+00,  1.0000e+00,  0.0000e+00,  ...,  1.0000e+00,
           0.0000e+00,  1.0000e+00],
         [ 8.4147e-01,  5.4030e-01,  8.2186e-01,  ...,  1.0000e+00,
           1.0366e-04,  1.0000e+00],
         [ 9.0930e-01, -4.1615e-01,  9.3641e-01,  ...,  1.0000e+00,
           2.0733e-04,  1.0000e+00],
         [ 1.4112e-01, -9.8999e-01,  2.4509e-01,  ...,  1.0000e+00,
           3.1099e-04,  1.0000e+00]]])
```

---

## 多头注意力机制

使用Pytorch实现多头注意力机制的底层代码, 含例子.

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   MultiHeadAttention.py
@Time    :   2024/09/27 09:50:43
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''
import os
import torch
import torch.nn as nn
from transformers import BertTokenizer

# 获取当前文件的绝对路径
file_path = os.path.abspath(__file__)

# 获取当前文件所在的目录路径
dir = os.path.dirname(file_path)

# 将当前工作目录更改为当前文件所在的目录
os.chdir(dir)

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        '''
        初始化多头注意力机制
        :param embed_size: 输入嵌入向量的维度
        :param num_heads: 多头注意力机制的头数
        '''
        super(MultiHeadAttention, self).__init__()

        assert embed_size % heads == 0, "嵌入维度必须能被头数整除"

        self.embed_size = embed_size
        self.heads = heads
        # 每个头的维度
        self.heads_dim = embed_size // heads

        self.value = nn.Linear(self.heads_dim, self.heads_dim, bias=False)
        self.key = nn.Linear(self.heads_dim, self.heads_dim, bias=False)
        self.query = nn.Linear(self.heads_dim, self.heads_dim, bias=False)

        self.fc_out = nn.Linear(heads * self.heads_dim, embed_size)
    
    def forward(self, query, keys, values, mask):
        N = query.shape[0]
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]

        # 将输入的数据划分为多个头, 先调整shape为 (N, value_len, heads, heads_dim)
        values = values.reshape(N, value_len, self.heads, self.heads_dim)
        keys = keys.reshape(N, key_len, self.heads, self.heads_dim)
        query = query.reshape(N, query_len, self.heads, self.heads_dim)

        # 初始化Q, K, V矩阵
        values = self.value(values)
        keys = self.key(keys)
        query = self.query(query)

        # 计算注意力分数
        # 这行代码使用爱因斯坦求和约定（Einstein Summation Convention）来计算注意力分数。
        # 具体来说，它通过矩阵乘法计算query和keys之间的点积，然后将其重塑为所需的形状。
        # 
        # 参数解释：
        # - "nqhd,nkhd->nhqk" 是爱因斯坦求和约定的字符串表示。
        #   - "n" 表示批次大小（batch size）。
        #   - "q" 表示查询序列的长度（query length）。
        #   - "h" 表示注意力头数（number of heads）。
        #   - "d" 表示每个头的维度（dimension per head）。
        #   - "k" 表示键序列的长度（key length）。
        # 
        # 具体操作：
        # - query 的形状为 (N, query_len, heads, heads_dim)。
        # - keys 的形状为 (N, key_len, heads, heads_dim)。
        # - 通过 torch.einsum 计算 query 和 keys 的点积，结果的形状为 (N, heads, query_len, key_len)。
        # 
        # 计算过程：
        # - 对于每个批次（n），每个头（h），计算 query 和 keys 的点积，得到一个形状为 (query_len, key_len) 的矩阵。
        # - 最终结果是一个形状为 (N, heads, query_len, key_len) 的张量，表示每个查询和每个键之间的注意力分数。
        energy = torch.einsum("nqhd,nkhd->nhqk", [query, keys])

        # 应用注意力机制
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float('-1e20'))

        attention = torch.softmax(energy / (self.embed_size ** (1/2)), dim=3)

        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
            N, query_len, self.heads * self.heads_dim
        )

        out = self.fc_out(out)

        return out

if __name__ == '__main__':


    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', cache_dir='./cache')

    input_text = "Hello world!"

    # 初始化随机keys,values, query

    tokens = tokenizer.tokenize(input_text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    token_ids = torch.tensor([token_ids]).long()

    batch_size,seq_length = token_ids.shape
    embed_size =512
    heads = 8

    values = torch.rand(batch_size, seq_length, embed_size)
    keys = torch.rand(batch_size, seq_length, embed_size)
    query = torch.rand(batch_size, seq_length, embed_size)
    mask = None

    attention = MultiHeadAttention(embed_size, heads)
    out = attention(query, keys, values, mask)

    print(f"Tokens: {tokens}")
    print(f"Token IDs: {token_ids}")
    print(out.shape)
    print(f"Multi-head Attention Output: \n{out}")
```

运行以上代码后输出 :

```python
Tokens: ['hello', 'world', '!']
Token IDs: tensor([[7592, 2088,  999]])
torch.Size([1, 3, 512])
Multi-head Attention Output:
tensor([[[-0.0855, -0.2076,  0.0354,  ...,  0.1631, -0.0024, -0.1372],
         [-0.0852, -0.2079,  0.0366,  ...,  0.1636, -0.0025, -0.1374],
         [-0.0860, -0.2076,  0.0364,  ...,  0.1644, -0.0018, -0.1361]]],
       grad_fn=<ViewBackward0>)
```

---

## 前馈神经网络

就是一个简单的全连接层…没啥好说的, 看代码 :

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   FeedForwardNetwork.py
@Time    :   2024/09/27 14:46:48
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''
import os
import torch
import torch.nn as nn
from transformers import BertTokenizer

file_path = os.path.abspath(__file__)
dir = os.path.dirname(file_path)
os.chdir(dir)

class FeedForwardNetwork(nn.Module):
    def __init__(self, d_model, hidden_size, dropout=0.1):
        '''
        :param d_model:输入的特征维度大小
        :param hidden_size:隐藏层大小
        :param dropout:dropout概率
        '''
        super(FeedForwardNetwork, self).__init__()

        self.liner1 = nn.Linear(d_model, hidden_size)
        self.relu = nn.ReLU()
        self.liner2 = nn.Linear(hidden_size, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        '''
        :param x:输入的特征
        :return:输出的特征
        '''
        x = self.liner1(x)
        x = self.relu(x)
        x = self.liner2(x)
        x = self.dropout(x)
        return x

if __name__ == '__main__':
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',cache_dir='./cache')
    input_text = "Hello world"
    tokens = tokenizer.tokenize(input_text)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)
    token_ids = torch.tensor([token_ids]).long()

    d_model = token_ids.shape[1]
    hidden_size = 256

    ff_netword = FeedForwardNetwork(d_model, hidden_size)

    output = ff_netword(token_ids.float())
    print(f'Input tokens: \n{tokens}')
    print(f'Input token_ids: \n{token_ids}')
    print(f'Output from FeedForwardNetwork: \n{output}')
    print(f'Output shape: \n{output.shape}')
```

输出结果 :

```python
Input tokens:
['hello', 'world']
Input token_ids:
tensor([[7592, 2088]])
Output from FeedForwardNetwork:
tensor([[2332.0767, 1194.7576]], grad_fn=<MulBackward0>)
Output shape:
torch.Size([1, 2])
```

#  层归一化 & 残差连接

---

Layer Normalization

---

代码如下 :

---




```javascript
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LayerNormalization.py
@Time    :   2024/09/27 15:17:48
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''
import torch
import torch.nn as nn

class LayerNormalization(nn.Module):
    def __init__(self, features, eps=1e-6):
        '''
        初始化层归一化模块
        :param features: 特征维度大小
        :param eps: 防止除零的小常数
        '''
        super(LayerNormalization, self).__init__()  # 调用父类nn.Module的初始化方法
        self.eps = eps  # 设置防止除零的小常数
        self.gain = nn.Parameter(torch.ones(features))  # 初始化增益参数，形状为(features,)，初始值为1
        self.bias = nn.Parameter(torch.zeros(features))  # 初始化偏置参数，形状为(features,)，初始值为0

    def forward(self, x):
        '''
        前向传播函数
        :param x: 输入张量，形状为(batch_size, seq_len, features)
        :return: 归一化后的输出张量
        '''
        mean = x.mean(-1, keepdim=True)  # 计算输入张量在最后一个维度上的均值，保持维度
        std = x.std(-1, keepdim=True)  # 计算输入张量在最后一个维度上的标准差，保持维度
        return self.gain * (x - mean) / (std + self.eps) + self.bias  # 应用层归一化公式并返回结果
    

if __name__ == "__main__":
    batch_size = 1
    seq_len = 2048
    features = 4096

    # 创建一个简单的输入张量
    x = torch.randn(batch_size, seq_len, features)  # 随机初始化输入张量
    # 初始化层归一化层
    ln = LayerNormalization(features)

    # 应用层归一化
    normalized_x = ln(x)

    # 打印原始和归一化后的张量
    print("原始输入张量:")
    print(x)
    print("\n归一化后的输出张量:")
    print(normalized_x)
    print("\n归一化后的维度:")
    print(normalized_x.shape)
```



---

输出 :

---

```javascript
原始输入张量:
tensor([[[ 0.7926,  0.9379,  0.9247,  ..., -0.8849,  0.4262, -0.1126],
         [-1.0093, -0.3612, -0.7135,  ...,  1.7116, -0.1164,  0.8453],
         [ 1.1906, -0.3223,  0.3553,  ..., -0.0293,  0.6014,  0.3705],
         ...,
         [-0.3714, -0.1437,  1.2062,  ..., -0.7603, -1.2689, -0.4045],
         [-0.6838, -0.5469,  0.2328,  ..., -0.4500, -1.1035, -0.2005],
         [ 0.4267, -0.5163,  1.1316,  ..., -0.1339, -0.4004,  0.2841]]])

归一化后的输出张量:
tensor([[[ 0.7959,  0.9418,  0.9285,  ..., -0.8873,  0.4283, -0.1123],
         [-0.9919, -0.3548, -0.7011,  ...,  1.6830, -0.1141,  0.8314],
         [ 1.2045, -0.3012,  0.3732,  ..., -0.0096,  0.6181,  0.3883],
         ...,
         [-0.3827, -0.1589,  1.1681,  ..., -0.7650, -1.2649, -0.4152],
         [-0.7084, -0.5709,  0.2130,  ..., -0.4735, -1.1304, -0.2226],
         [ 0.3982, -0.5383,  1.0983,  ..., -0.1585, -0.4232,  0.2567]]],
       grad_fn=<AddBackward0>)

归一化后的维度:
torch.Size([1, 2048, 4096])
```

---

### Residual Connections

残差连接代码实现 :

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ResidualConnection.py
@Time    :   2024/09/27 15:33:49
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''
import torch
import torch.nn as nn
from LayerNormalization import LayerNormalization


class ResidualConnection(nn.Module):
    def __init__(self, size, dropout):
        super(ResidualConnection, self).__init__()  # 正确调用父类构造函数
        self.norm = LayerNormalization(size)  # 在父类构造函数之后设置属性
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x, sublayer):
        return x + self.dropout(sublayer(self.norm(x)))

if __name__ == '__main__':
    
    size = 512
    dropout = 0.1
    
    residual_module = ResidualConnection(size, dropout)

    x = torch.rand(32, 10, size)
    sublayer = nn.Linear(size, size)

    output = residual_module(x, sublayer)
    print(f'output shape: \n{output.shape}')
    print(f'out: \n{output}')
```

输出内容 :

```python
output shape:
torch.Size([32, 10, 512])
out:
tensor([[[ 0.3520,  0.6030, -0.2354,  ...,  0.8682, -0.3730,  0.1524],
         [ 1.4186,  0.5724,  0.2079,  ...,  0.4792,  1.2186,  0.6546],
         [ 1.0631,  1.0479,  0.4523,  ...,  1.4115,  1.5870,  0.7165],
         ...,
         [ 0.0567,  2.4177,  1.6159,  ..., -0.5791,  0.4186,  0.6306],
         [ 1.9228,  0.8467,  0.7399,  ..., -0.5388, -0.1463,  1.1880],
         [ 0.1197,  0.0182,  0.2941,  ...,  0.5807,  0.3925, -0.4700]],

        [[ 0.3333,  0.8267,  0.3082,  ...,  1.3075,  0.2646,  0.4092],
         [ 0.7507,  0.9554,  0.2910,  ...,  1.1357,  0.4684,  0.4244],
         [ 0.6514,  0.2003, -0.3597,  ...,  0.3598,  0.4869, -0.1992],
         ...,
         [-0.0030,  1.0668,  0.3075,  ...,  0.5691,  0.2380, -0.1247],
         [ 0.9135,  0.4341,  0.0337,  ...,  0.3597, -0.7784,  0.8458],
         [-0.1205,  0.6370,  1.0110,  ...,  0.0136,  0.6965,  0.2374]],

        [[ 1.7201,  0.9184,  1.4459,  ...,  0.6506, -0.4328,  0.4222],
         [ 0.1091, -0.7816,  0.0389,  ...,  0.4128,  0.5077,  1.2345],
         [ 0.3344,  0.5098,  0.1903,  ...,  0.4348,  0.1655,  1.0356],
         ...,
         [ 0.6577,  1.0894,  0.3509,  ...,  0.9495, -0.3284,  0.8220],
         [-0.3985,  1.0728,  1.2246,  ...,  0.6893,  0.3443,  0.4279],
         [ 0.2423,  0.0113,  1.3485,  ..., -0.2677, -0.0577,  0.4010]],

        ...,

        [[ 1.4007,  1.3420,  0.1977,  ...,  0.8533,  0.1814,  0.2697],
         [ 0.6700,  0.2914,  0.7087,  ...,  0.4371, -0.6651, -0.3476],
         [ 1.7371, -0.3646, -0.7164,  ..., -0.2941,  1.5312,  0.1496],
         ...,
         [ 1.4492,  1.6843,  0.4061,  ...,  0.2602,  0.3412,  0.9145],
         [ 0.5208,  0.7262,  1.1507,  ...,  1.6124,  0.1670, -0.7637],
         [ 0.6195,  1.8701,  0.6011,  ...,  0.7136,  0.1405,  0.7195]],

        [[ 1.2362,  0.3252,  1.5944,  ..., -0.6239, -0.5983,  0.0794],
         [ 1.1429, -0.8601,  0.6993,  ...,  0.1767, -0.7440,  0.6210],
         [ 0.1337, -0.8456, -0.4567,  ...,  1.0074,  0.6997, -0.7483],
         ...,
         [-0.2421,  0.8441,  1.1355,  ...,  1.2241,  0.0689, -0.8084],
         [ 0.1203, -0.1496, -0.3044,  ...,  0.2365,  1.0541,  0.5421],
         [ 0.7855,  0.0565,  0.9192,  ...,  0.8071, -0.9707,  1.3335]],

        [[ 0.6022,  1.4715,  0.2470,  ..., -0.0782, -0.6734,  0.8383],
         [ 0.8088,  0.3382,  0.6812,  ...,  1.1501,  1.0537,  0.5442],
         [-0.0593,  1.7771,  0.0580,  ..., -0.0578,  0.7382,  1.2158],
         ...,
         [ 1.1114,  0.3564,  0.8435,  ...,  0.1796,  1.2682,  0.5146],
         [ 1.0304,  1.2170,  0.8374,  ...,  2.2357,  0.2286,  0.3899],
         [ 0.5022,  0.3711,  0.2397,  ...,  0.9505,  0.3877, -0.2048]]],
       grad_fn=<AddBackward0>)
```

## 编码器

### Encoder Layer

编码器层由之前构建的多头注意力机制, 前馈神经网络, 残差模块, 层归一化组合构成

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   EncoderLayer.py
@Time    :   2024/09/27 16:51:01
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   多头注意力机制、前馈神经网络、位置编码、残差连接和层归一化结合起来，\n
                   构建一个 Encoder Layer。Encoder Layer 是 Transformer 编码器的基本组成单位。
'''

import torch
import torch.nn as nn
from MultiHeadAttention import MultiHeadAttention
from FeedForwardNetwork import FeedForwardNetwork
from LayerNormalization import LayerNormalization #在残差连接模块中完成
from ResidualConnection import ResidualConnection

class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, hidden_size, dropout=0.1):
        super(EncoderLayer, self).__init__()
        self.d_model = d_model
        self.self_attn = MultiHeadAttention(d_model, num_heads)
        self.pos_ffn = FeedForwardNetwork(d_model, hidden_size, dropout)
        self.residual = nn.ModuleList([
            ResidualConnection(d_model, dropout),
            ResidualConnection(d_model, dropout)
        ])
    
    def forward(self, x, mask=None):
        x = self.residual[0](x, lambda x: self.self_attn(x, x, x, mask))
        x = self.residual[1](x, self.pos_ffn)
        return x
    
# 示例
if __name__ == "__main__":
    # 示例输入
    d_model = 512
    num_heads = 8
    hidden_size = 2048
    dropout = 0.1
    batch_size = 32
    seq_len = 10

    encoder_layer = EncoderLayer(d_model, num_heads, hidden_size, dropout)
    input_tensor = torch.randn(batch_size, seq_len, d_model)
    mask = torch.ones(batch_size, 1,seq_len, seq_len)

    # 前向传播
    output_tensor = encoder_layer(input_tensor, mask)

    # 输出结果
    print("Input shape:", input_tensor.shape)
    print("Output shape:", output_tensor.shape)
```

输出结果为 :

```python
Input shape: torch.Size([32, 10, 512])
Output shape: torch.Size([32, 10, 512])
```

### Encoder

Encoder由n个Encoder_Lyaer组成, 详细代码如下 :

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Encoder.py
@Time    :   2024/09/29 08:39:15
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   
'''
import os
import sys
import torch
import torch.nn as nn
from EncoderLayer import EncoderLayer
from LayerNormalization import LayerNormalization

class Encoder(nn.Module):
    def __init__(self, encoder_layer, num_layers):
        super(Encoder, self).__init__()
        self.encoder_layer = nn.ModuleList([
            encoder_layer for _ in range(num_layers)
        ])
        self.norm = LayerNormalization(encoder_layer.d_model)

    def forward(self, src, mask=None):
        for layer in self.encoder_layer:
            src = layer(src, mask)
        return self.norm(src)
    
if __name__ == '__main__':
    d_model = 512
    num_heades = 8
    hidden_size = 2048
    droupout = 0.1
    num_layers = 6

    encoder_layer = EncoderLayer(d_model, num_heades, hidden_size, droupout)
    encoder = Encoder(encoder_layer, num_layers)

    src = torch.rand(32, 10 , d_model)

    output = encoder(src)

    print(output.shape)
```

输出结果为 :

```shell
Input shape: torch.Size([32, 10, 512])
Output shape: torch.Size([32, 10, 512])
```

- 32个样本
- 每个样本有10个时间步
- 每个时间步的特征向量有512个维度
---

## 解码器

### Decoder_Layer

编码器与解码器最大的区别就是使用了Mask Multi-Head Attention, 用于防止模型训练过程中”看到”后续的目标词, 由多个解码器层构成, 代码如下 :

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   DecoderLayer.py
@Time    :   2024/09/29 09:34:04
@Author  :   pan binghong 
@Email   :   19909442097@163.com
@description   :   Transformer 解码器与编码器类似，\n
主要区别在于解码器使用了 Masked Multi-Head Attention，\n
用于防止模型在训练过程中“看到”后续的目标词。\n
解码器也是由多个 Decoder Layer 堆叠组成。
'''
import torch
import torch.nn as nn
from MultiHeadAttention import MultiHeadAttention
from FeedForwardNetwork import FeedForwardNetwork
from ResidualConnection import ResidualConnection


class DecoderLayer(nn.Module):
    def __init__(self, d_model, heads, hidden_size, dropout=0.1):
        super(DecoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, heads)
        self.src_attn = MultiHeadAttention(d_model, heads)
        self.feed_forward = FeedForwardNetwork(d_model, hidden_size, dropout)
        self.residuals = nn.ModuleList([
            ResidualConnection(d_model, dropout),
            ResidualConnection(d_model, dropout),            
            ResidualConnection(d_model, dropout)
        ])

    def forward(self, x, memory, src_mask=None, trg_mask=None):
        # 自注意力机制
        x = self.residuals[0](x, lambda x: self.self_attn(x, x, x, trg_mask))
        # 编码器-解码器注意力机制
        x = self.residuals[1](x, lambda x: self.src_attn(x, memory, memory, src_mask))
        # 前馈网络
        return self.residuals[2](x, self.feed_forward)

if __name__ == '__main__':
    embedding_size = 512
    heads = 8
    hidden_size = 2048
    batch_size = 8

    decoder_layer = DecoderLayer(embedding_size, heads, hidden_size)
    print(decoder_layer)
    print(decoder_layer.parameters)

    x = torch.rand(batch_size, 16, embedding_size)
    memory = torch.rand(batch_size, 16, embedding_size)
    src_mask = torch.rand(batch_size, 1, 16)
    trg_mask = torch.rand(batch_size, 16, 16)

    output = decoder_layer(x, memory, src_mask, trg_mask)
    print(output.shape)
```

输出结果如下 :

```python
DecoderLayer(
  (self_attn): MultiHeadAttention(
    (value): Linear(in_features=64, out_features=64, bias=False)
    (key): Linear(in_features=64, out_features=64, bias=False)
    (query): Linear(in_features=64, out_features=64, bias=False)
    (fc_out): Linear(in_features=512, out_features=512, bias=True)
  )
  (src_attn): MultiHeadAttention(
    (value): Linear(in_features=64, out_features=64, bias=False)
    (key): Linear(in_features=64, out_features=64, bias=False)
    (query): Linear(in_features=64, out_features=64, bias=False)
    (fc_out): Linear(in_features=512, out_features=512, bias=True)
  )
  (feed_forward): FeedForwardNetwork(
    (liner1): Linear(in_features=512, out_features=2048, bias=True)
    (relu): ReLU()
    (liner2): Linear(in_features=2048, out_features=512, bias=True)
    (dropout): Dropout(p=0.1, inplace=False)
  )
  (residuals): ModuleList(
    (0-2): 3 x ResidualConnection(
      (norm): LayerNormalization()
      (dropout): Dropout(p=0.1, inplace=False)
    )
  )
)
<bound method Module.parameters of DecoderLayer(
  (self_attn): MultiHeadAttention(
    (value): Linear(in_features=64, out_features=64, bias=False)
    (key): Linear(in_features=64, out_features=64, bias=False)
    (query): Linear(in_features=64, out_features=64, bias=False)
    (fc_out): Linear(in_features=512, out_features=512, bias=True)
  )
  (src_attn): MultiHeadAttention(
    (value): Linear(in_features=64, out_features=64, bias=False)
    (key): Linear(in_features=64, out_features=64, bias=False)
    (query): Linear(in_features=64, out_features=64, bias=False)
    (fc_out): Linear(in_features=512, out_features=512, bias=True)
  )
  (feed_forward): FeedForwardNetwork(
    (liner1): Linear(in_features=512, out_features=2048, bias=True)
    (relu): ReLU()
    (liner2): Linear(in_features=2048, out_features=512, bias=True)
    (dropout): Dropout(p=0.1, inplace=False)
  )
  (residuals): ModuleList(
    (0-2): 3 x ResidualConnection(
      (norm): LayerNormalization()
      (dropout): Dropout(p=0.1, inplace=False)
    )
  )
)>
torch.Size([8, 16, 512])
```

### Decoder

代码报错解决中…

---

> References

