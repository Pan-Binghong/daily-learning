---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TOCSAAZ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsvdHMMyloIODNWRJNQi7GaK5w2CdYo%2F2kIp29zp%2FcXAIgcgI%2BR6kLEKbZHUWrhPTrWNy5uHui59mRIQc%2FT3Biimgq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDNMllV%2F8Qd26RdMsdircA30I0M76QUwTduQoK1KhK0gn1cOaAEWJ72lz8twe8gvlpWLg7aJlC2yvIBnxlQ5i0YkREudVT1qzIF3Mla91J%2Fi2QIyHb2NeH6M84tUvs3Nmj5svLlcKbXaL5P5SR91%2ByyEhQnx156DCkd70cr0D7szZjLGSjSCHS%2FktDzhiJYBejFsRHlTLU34FtnCN2aQxDN48jK2lwn54x8%2F7tpJQNejmYuJFSbfptjeLWt6HADERitWwkTDq%2BpJPKTTtfkF0bJBwAsyFCZjbrtJ17%2F0cHJ3nrFHvQeyv7UR5tfUyiAA6fu0g0wlGCL13avYLs%2BuKQ1npBUV%2B2YoLA6z2BYSlYIXOLDAPvnnRvBdJt2azo2HHY3WaJ0%2Fbxw2%2BWVOJxFACXxPaVlxAMOwXRy2IftBag%2Bo2991gaJpCX7IQNzgihQs68aKDsNRjPo5cU1QqSCo76%2BH71g7mitVQ%2B%2Fx9ZLVunsDMw9TxkbRZ7FQGPs9YdGAINVdyJxOkFdiToBvGelqEiTV3Hy1PIZunCw8RaTFy2d4V5gvHODnXn4eCwWR8gzyY7fmiRDG%2BpLb9SvuBCgqlkMv0173OCTAZQ9%2FJevn5E0FkMCFZLn1oob7m7Q9HpO9TC9dPDYz2DGTDNIWMMKKW5csGOqUB81kcPmV0A0%2Bd7T5By4sWI8B8UMJSqNzMifErDPEJiF0osqCFhCPLDK4tC0ohoY4V0PG77Hsa%2FOKMYznl8tNxIL7PXWsTAGp53PlERwFS5vH8xk6A8vkK4dMwu3sq%2FYpkzuPueRBumHIVlIjkpPRySTBcHHVQfoq4KV7QZs7N75rAJ0Z5Jaj7PM1bBWAbjP8u%2BQjS8zhhNrIvk00gNrZvK2kaMebq&X-Amz-Signature=8b6f998817ecce68046e6c77f146f7a2a0f57f95bd379aeb1534986e097ddd46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 下载模型

- 方法一(手动下载):
- 方法二(huggingface-cli):
---

### 安装推理/训练框架(Swift)

- 源码安装
---

### 数据处理

- 使用自己的数据, 需要最终处理为jsonl格式, 考虑到数据保密, 在此不展示真实数据.
- 数据集格式可以自定义为以下几种格式 :
- 处理为train.jsonl的最终截图：
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TOCSAAZ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsvdHMMyloIODNWRJNQi7GaK5w2CdYo%2F2kIp29zp%2FcXAIgcgI%2BR6kLEKbZHUWrhPTrWNy5uHui59mRIQc%2FT3Biimgq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDNMllV%2F8Qd26RdMsdircA30I0M76QUwTduQoK1KhK0gn1cOaAEWJ72lz8twe8gvlpWLg7aJlC2yvIBnxlQ5i0YkREudVT1qzIF3Mla91J%2Fi2QIyHb2NeH6M84tUvs3Nmj5svLlcKbXaL5P5SR91%2ByyEhQnx156DCkd70cr0D7szZjLGSjSCHS%2FktDzhiJYBejFsRHlTLU34FtnCN2aQxDN48jK2lwn54x8%2F7tpJQNejmYuJFSbfptjeLWt6HADERitWwkTDq%2BpJPKTTtfkF0bJBwAsyFCZjbrtJ17%2F0cHJ3nrFHvQeyv7UR5tfUyiAA6fu0g0wlGCL13avYLs%2BuKQ1npBUV%2B2YoLA6z2BYSlYIXOLDAPvnnRvBdJt2azo2HHY3WaJ0%2Fbxw2%2BWVOJxFACXxPaVlxAMOwXRy2IftBag%2Bo2991gaJpCX7IQNzgihQs68aKDsNRjPo5cU1QqSCo76%2BH71g7mitVQ%2B%2Fx9ZLVunsDMw9TxkbRZ7FQGPs9YdGAINVdyJxOkFdiToBvGelqEiTV3Hy1PIZunCw8RaTFy2d4V5gvHODnXn4eCwWR8gzyY7fmiRDG%2BpLb9SvuBCgqlkMv0173OCTAZQ9%2FJevn5E0FkMCFZLn1oob7m7Q9HpO9TC9dPDYz2DGTDNIWMMKKW5csGOqUB81kcPmV0A0%2Bd7T5By4sWI8B8UMJSqNzMifErDPEJiF0osqCFhCPLDK4tC0ohoY4V0PG77Hsa%2FOKMYznl8tNxIL7PXWsTAGp53PlERwFS5vH8xk6A8vkK4dMwu3sq%2FYpkzuPueRBumHIVlIjkpPRySTBcHHVQfoq4KV7QZs7N75rAJ0Z5Jaj7PM1bBWAbjP8u%2BQjS8zhhNrIvk00gNrZvK2kaMebq&X-Amz-Signature=44b73495b93fe5271a1ad4a2b7eaa105f36d3733fa1ec49c41e41982fc8a27e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TOCSAAZ%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsvdHMMyloIODNWRJNQi7GaK5w2CdYo%2F2kIp29zp%2FcXAIgcgI%2BR6kLEKbZHUWrhPTrWNy5uHui59mRIQc%2FT3Biimgq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDNMllV%2F8Qd26RdMsdircA30I0M76QUwTduQoK1KhK0gn1cOaAEWJ72lz8twe8gvlpWLg7aJlC2yvIBnxlQ5i0YkREudVT1qzIF3Mla91J%2Fi2QIyHb2NeH6M84tUvs3Nmj5svLlcKbXaL5P5SR91%2ByyEhQnx156DCkd70cr0D7szZjLGSjSCHS%2FktDzhiJYBejFsRHlTLU34FtnCN2aQxDN48jK2lwn54x8%2F7tpJQNejmYuJFSbfptjeLWt6HADERitWwkTDq%2BpJPKTTtfkF0bJBwAsyFCZjbrtJ17%2F0cHJ3nrFHvQeyv7UR5tfUyiAA6fu0g0wlGCL13avYLs%2BuKQ1npBUV%2B2YoLA6z2BYSlYIXOLDAPvnnRvBdJt2azo2HHY3WaJ0%2Fbxw2%2BWVOJxFACXxPaVlxAMOwXRy2IftBag%2Bo2991gaJpCX7IQNzgihQs68aKDsNRjPo5cU1QqSCo76%2BH71g7mitVQ%2B%2Fx9ZLVunsDMw9TxkbRZ7FQGPs9YdGAINVdyJxOkFdiToBvGelqEiTV3Hy1PIZunCw8RaTFy2d4V5gvHODnXn4eCwWR8gzyY7fmiRDG%2BpLb9SvuBCgqlkMv0173OCTAZQ9%2FJevn5E0FkMCFZLn1oob7m7Q9HpO9TC9dPDYz2DGTDNIWMMKKW5csGOqUB81kcPmV0A0%2Bd7T5By4sWI8B8UMJSqNzMifErDPEJiF0osqCFhCPLDK4tC0ohoY4V0PG77Hsa%2FOKMYznl8tNxIL7PXWsTAGp53PlERwFS5vH8xk6A8vkK4dMwu3sq%2FYpkzuPueRBumHIVlIjkpPRySTBcHHVQfoq4KV7QZs7N75rAJ0Z5Jaj7PM1bBWAbjP8u%2BQjS8zhhNrIvk00gNrZvK2kaMebq&X-Amz-Signature=313d012778b8eafe88aeab8717bcf93112d3ea56a66391ac3269956311840f2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 合并权重+推理

- 运行推理命令
- ckpt_dir 微调后的模型权重地址
---

### 效果演示

> 根据上一步合并, 已经得到了新的模型权重, 位置在/你的服务器地址/root/autodl-tmp/.autodl/output/minicpm-v-v2_6-chat/v0-xxx/checkpoint-xxx-merged

- 使用Swift的web-ui推理演示
- 使用Swift的cli推理演示
- 使用MiniCPM代码库的web-ui推理演示
- 使用Python代码推理演示
> reference

