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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z3UKELW%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCZVivD6XJh%2FAF2Z1S5o2Hk4157ieKMurReHcDNDErTQwIgPFvCuHvuU096uNi6kOCMUSP32ldIRUgxUPpin3eSGZ0qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHIt%2FH3wX0eva3LEgSrcAwskmajX%2BGHfj3l0n5DNxGsyZjaKLrX6rI2FS86N4%2FM6eU5Vo6q6vq0rjUCLgM6bsTr2X17Ad4Jq6Pt%2B5NmE%2BI8eJeCLSJjM96FLXIFYYKKbydcNRyEEOGjbz7luXxidmHl130x%2FWtbj%2Be%2Bn01t6NyUfZ%2BJTv%2FZLhrs%2FxvvCllKbsqXAXp7HG2trQaFK8Mq3he%2FOuZp4WLq%2BpRsatDbwE5tnM5rRVH%2FW%2B8jM8rDRJSRzLWZs%2Bx9fhwX10%2B7tYsNerkgdPJKc9157sjs8Kec147q%2FZJOC5zSuyuh4iFvBIurqa%2F4ND9Osj8o6b7ti5tRJbEjG0lsAaBFrfpdk73GokEy77AbKg%2BrqpqytVQeZFjbjaC%2FxEX1jtFGZYdIgCkxpAACg7slH9s0ZvdjY%2FMyE59gUlzecS5bqnW8%2B7H7UXrVy8lPsk2Qq5Qz%2FCR4oNQNHJk%2FfMWUAdHpdr6CFhDh6BR5WK0fTNXNmor0BfmQH9eBDQ3sZ6tORIxAXkmJd76FZ%2FwlOUfjIBfNRqIxDNPmGpI%2BNZaDl3sR2qgOOjSZ%2BXW6ZIcZ67GmaudklG006NH5KyokdMVAxpCx6GfBStOYaDLsqQbJJE13wihYKKlzX4%2F%2FPYRw4ZXdqM4xXqGS9MIaIgMwGOqUBNh%2BMrzZF49nK3HPQEAtm3F4kq04FP4PL7pGnz5KYVFEhDyhSovQ6FuDaF4iSike8PKZAqOWzYoIl8IGjDUN4usfBUyIrZRWjk4Y%2F5ASG%2BMsm%2BlNA%2BNX7Mmv36t90vnA%2BO%2BCxxTujiFi9MzNX%2BlIuCaM%2BHWKtvrOSnf1piHh6B%2BVZWC94hAzFGWw%2B6UC6EupYTxiPDt%2B2TMcwYxp8RW0lUyEx8Yjh&X-Amz-Signature=ff07c2f6ba659297f81e9e2c5a9797db803af9afac4e3722e3394dcf321e0541&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z3UKELW%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCZVivD6XJh%2FAF2Z1S5o2Hk4157ieKMurReHcDNDErTQwIgPFvCuHvuU096uNi6kOCMUSP32ldIRUgxUPpin3eSGZ0qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHIt%2FH3wX0eva3LEgSrcAwskmajX%2BGHfj3l0n5DNxGsyZjaKLrX6rI2FS86N4%2FM6eU5Vo6q6vq0rjUCLgM6bsTr2X17Ad4Jq6Pt%2B5NmE%2BI8eJeCLSJjM96FLXIFYYKKbydcNRyEEOGjbz7luXxidmHl130x%2FWtbj%2Be%2Bn01t6NyUfZ%2BJTv%2FZLhrs%2FxvvCllKbsqXAXp7HG2trQaFK8Mq3he%2FOuZp4WLq%2BpRsatDbwE5tnM5rRVH%2FW%2B8jM8rDRJSRzLWZs%2Bx9fhwX10%2B7tYsNerkgdPJKc9157sjs8Kec147q%2FZJOC5zSuyuh4iFvBIurqa%2F4ND9Osj8o6b7ti5tRJbEjG0lsAaBFrfpdk73GokEy77AbKg%2BrqpqytVQeZFjbjaC%2FxEX1jtFGZYdIgCkxpAACg7slH9s0ZvdjY%2FMyE59gUlzecS5bqnW8%2B7H7UXrVy8lPsk2Qq5Qz%2FCR4oNQNHJk%2FfMWUAdHpdr6CFhDh6BR5WK0fTNXNmor0BfmQH9eBDQ3sZ6tORIxAXkmJd76FZ%2FwlOUfjIBfNRqIxDNPmGpI%2BNZaDl3sR2qgOOjSZ%2BXW6ZIcZ67GmaudklG006NH5KyokdMVAxpCx6GfBStOYaDLsqQbJJE13wihYKKlzX4%2F%2FPYRw4ZXdqM4xXqGS9MIaIgMwGOqUBNh%2BMrzZF49nK3HPQEAtm3F4kq04FP4PL7pGnz5KYVFEhDyhSovQ6FuDaF4iSike8PKZAqOWzYoIl8IGjDUN4usfBUyIrZRWjk4Y%2F5ASG%2BMsm%2BlNA%2BNX7Mmv36t90vnA%2BO%2BCxxTujiFi9MzNX%2BlIuCaM%2BHWKtvrOSnf1piHh6B%2BVZWC94hAzFGWw%2B6UC6EupYTxiPDt%2B2TMcwYxp8RW0lUyEx8Yjh&X-Amz-Signature=2928b0dae02735c5cb1d61d7495fb62227ec12dd50a85f8d74ab55527a0688f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662Z3UKELW%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQCZVivD6XJh%2FAF2Z1S5o2Hk4157ieKMurReHcDNDErTQwIgPFvCuHvuU096uNi6kOCMUSP32ldIRUgxUPpin3eSGZ0qiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHIt%2FH3wX0eva3LEgSrcAwskmajX%2BGHfj3l0n5DNxGsyZjaKLrX6rI2FS86N4%2FM6eU5Vo6q6vq0rjUCLgM6bsTr2X17Ad4Jq6Pt%2B5NmE%2BI8eJeCLSJjM96FLXIFYYKKbydcNRyEEOGjbz7luXxidmHl130x%2FWtbj%2Be%2Bn01t6NyUfZ%2BJTv%2FZLhrs%2FxvvCllKbsqXAXp7HG2trQaFK8Mq3he%2FOuZp4WLq%2BpRsatDbwE5tnM5rRVH%2FW%2B8jM8rDRJSRzLWZs%2Bx9fhwX10%2B7tYsNerkgdPJKc9157sjs8Kec147q%2FZJOC5zSuyuh4iFvBIurqa%2F4ND9Osj8o6b7ti5tRJbEjG0lsAaBFrfpdk73GokEy77AbKg%2BrqpqytVQeZFjbjaC%2FxEX1jtFGZYdIgCkxpAACg7slH9s0ZvdjY%2FMyE59gUlzecS5bqnW8%2B7H7UXrVy8lPsk2Qq5Qz%2FCR4oNQNHJk%2FfMWUAdHpdr6CFhDh6BR5WK0fTNXNmor0BfmQH9eBDQ3sZ6tORIxAXkmJd76FZ%2FwlOUfjIBfNRqIxDNPmGpI%2BNZaDl3sR2qgOOjSZ%2BXW6ZIcZ67GmaudklG006NH5KyokdMVAxpCx6GfBStOYaDLsqQbJJE13wihYKKlzX4%2F%2FPYRw4ZXdqM4xXqGS9MIaIgMwGOqUBNh%2BMrzZF49nK3HPQEAtm3F4kq04FP4PL7pGnz5KYVFEhDyhSovQ6FuDaF4iSike8PKZAqOWzYoIl8IGjDUN4usfBUyIrZRWjk4Y%2F5ASG%2BMsm%2BlNA%2BNX7Mmv36t90vnA%2BO%2BCxxTujiFi9MzNX%2BlIuCaM%2BHWKtvrOSnf1piHh6B%2BVZWC94hAzFGWw%2B6UC6EupYTxiPDt%2B2TMcwYxp8RW0lUyEx8Yjh&X-Amz-Signature=11258d375da9e8f6cf0691ea5c7b77fcc08c6c155a26941576e12fc34a5c3c2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

