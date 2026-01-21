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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHBOUVWV%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1JQ9Am0WImXQ67uvsbd3gL0czU1lE0uxpNM8Ly7%2FbdQIgdSDH7t4ZbJmMLSuFbnsjQniIT2lXVuTUXjvvryL3r80qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFbsghHhyH%2FD9FiRQCrcA8euk5P9jXMnv4njkwB5m9GNiNdjiF%2Bc60JjNrvx42J%2FT7ckEEz5wtyTtBlZfdIcG04wtMo0v17LStKLGVEj5ZTS9lwsNMIerIEdlvzZRttaK0hqb7zEgVDlQ%2FDxgXv9JHH5F5TMIHkg8rE%2BqKsYhBw6uzq4VgTrWEwX0Xrkvd7aHCAeRlq%2Fltg6JSoCo3awemYjedRXy7wCQ6crImAKKvEP67orkEwiXxBQN%2BgNOb8J4Qoz%2FDs0tqbT6a3Aj5DOFMnqSdhYZHlPbIdgF2%2BHZa%2Foo6uwl8j6uoB%2FFpHAaAuSxBIaCrBotXTGek9wfSyX%2BnKX7X2o5N1gWBOegHCzFIlbz09lGF%2F0aHFIlJkK9lEciEBFKLzTHUnjDZnTEtDIuxMbqP6qhgze2I8XPgN7UtBtD15W4%2Fbz2ATJnsBy3%2BNHFLryoHnQVbvLMmGmFEbPqzd4bJZXp%2BIMichieStsOCVgbpSGbvA%2F7twwY6rzykPlNmAeOHBO66MluCv82RZaA9AXy9oQpEHeVeFeJCnIal5Qhw9t8IoH9pXk3%2FUYXyQJSwwgJpk1s3cvPiRXH3FdsuM6Cppw6FvTQCarEDU4ZRn4wddV6Sk%2BqGtygKUWg8WarHMzH7be31AviDkkMPrZwMsGOqUBFkCjGcDopj3%2FydNeH1qBeegEDuPJk%2BisuqKCT1zZn0f2QfbdEa6NSYAYWX92CfFQ48sxUHh0wXXDwqXXbtq5X%2Bcx4x8iz995AyYaHjKg%2F0M0n0lQaXarts69Buz8IvGWSK4vPlXjXFNdxi7FkHgBZgmjkmSNHwjvc77YCNzHnkCb7fsEZGE2dB9VQgqtSBvFLAFFw4AqzRtYS6AW5JOs4fAGuRZb&X-Amz-Signature=aa99ce4737af53e658411ca0dd2897ee79a397628bac4d81c27562417ad62ea3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHBOUVWV%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1JQ9Am0WImXQ67uvsbd3gL0czU1lE0uxpNM8Ly7%2FbdQIgdSDH7t4ZbJmMLSuFbnsjQniIT2lXVuTUXjvvryL3r80qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFbsghHhyH%2FD9FiRQCrcA8euk5P9jXMnv4njkwB5m9GNiNdjiF%2Bc60JjNrvx42J%2FT7ckEEz5wtyTtBlZfdIcG04wtMo0v17LStKLGVEj5ZTS9lwsNMIerIEdlvzZRttaK0hqb7zEgVDlQ%2FDxgXv9JHH5F5TMIHkg8rE%2BqKsYhBw6uzq4VgTrWEwX0Xrkvd7aHCAeRlq%2Fltg6JSoCo3awemYjedRXy7wCQ6crImAKKvEP67orkEwiXxBQN%2BgNOb8J4Qoz%2FDs0tqbT6a3Aj5DOFMnqSdhYZHlPbIdgF2%2BHZa%2Foo6uwl8j6uoB%2FFpHAaAuSxBIaCrBotXTGek9wfSyX%2BnKX7X2o5N1gWBOegHCzFIlbz09lGF%2F0aHFIlJkK9lEciEBFKLzTHUnjDZnTEtDIuxMbqP6qhgze2I8XPgN7UtBtD15W4%2Fbz2ATJnsBy3%2BNHFLryoHnQVbvLMmGmFEbPqzd4bJZXp%2BIMichieStsOCVgbpSGbvA%2F7twwY6rzykPlNmAeOHBO66MluCv82RZaA9AXy9oQpEHeVeFeJCnIal5Qhw9t8IoH9pXk3%2FUYXyQJSwwgJpk1s3cvPiRXH3FdsuM6Cppw6FvTQCarEDU4ZRn4wddV6Sk%2BqGtygKUWg8WarHMzH7be31AviDkkMPrZwMsGOqUBFkCjGcDopj3%2FydNeH1qBeegEDuPJk%2BisuqKCT1zZn0f2QfbdEa6NSYAYWX92CfFQ48sxUHh0wXXDwqXXbtq5X%2Bcx4x8iz995AyYaHjKg%2F0M0n0lQaXarts69Buz8IvGWSK4vPlXjXFNdxi7FkHgBZgmjkmSNHwjvc77YCNzHnkCb7fsEZGE2dB9VQgqtSBvFLAFFw4AqzRtYS6AW5JOs4fAGuRZb&X-Amz-Signature=8de144c72603c8637f0c854095a99355a83e7bcd3e30e7ea5eca7f80d9dd88e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHBOUVWV%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1JQ9Am0WImXQ67uvsbd3gL0czU1lE0uxpNM8Ly7%2FbdQIgdSDH7t4ZbJmMLSuFbnsjQniIT2lXVuTUXjvvryL3r80qiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFbsghHhyH%2FD9FiRQCrcA8euk5P9jXMnv4njkwB5m9GNiNdjiF%2Bc60JjNrvx42J%2FT7ckEEz5wtyTtBlZfdIcG04wtMo0v17LStKLGVEj5ZTS9lwsNMIerIEdlvzZRttaK0hqb7zEgVDlQ%2FDxgXv9JHH5F5TMIHkg8rE%2BqKsYhBw6uzq4VgTrWEwX0Xrkvd7aHCAeRlq%2Fltg6JSoCo3awemYjedRXy7wCQ6crImAKKvEP67orkEwiXxBQN%2BgNOb8J4Qoz%2FDs0tqbT6a3Aj5DOFMnqSdhYZHlPbIdgF2%2BHZa%2Foo6uwl8j6uoB%2FFpHAaAuSxBIaCrBotXTGek9wfSyX%2BnKX7X2o5N1gWBOegHCzFIlbz09lGF%2F0aHFIlJkK9lEciEBFKLzTHUnjDZnTEtDIuxMbqP6qhgze2I8XPgN7UtBtD15W4%2Fbz2ATJnsBy3%2BNHFLryoHnQVbvLMmGmFEbPqzd4bJZXp%2BIMichieStsOCVgbpSGbvA%2F7twwY6rzykPlNmAeOHBO66MluCv82RZaA9AXy9oQpEHeVeFeJCnIal5Qhw9t8IoH9pXk3%2FUYXyQJSwwgJpk1s3cvPiRXH3FdsuM6Cppw6FvTQCarEDU4ZRn4wddV6Sk%2BqGtygKUWg8WarHMzH7be31AviDkkMPrZwMsGOqUBFkCjGcDopj3%2FydNeH1qBeegEDuPJk%2BisuqKCT1zZn0f2QfbdEa6NSYAYWX92CfFQ48sxUHh0wXXDwqXXbtq5X%2Bcx4x8iz995AyYaHjKg%2F0M0n0lQaXarts69Buz8IvGWSK4vPlXjXFNdxi7FkHgBZgmjkmSNHwjvc77YCNzHnkCb7fsEZGE2dB9VQgqtSBvFLAFFw4AqzRtYS6AW5JOs4fAGuRZb&X-Amz-Signature=496098236ba6c7d65849511d8a205512893d139a3aec6260a2ba2b53c8b2f10b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

