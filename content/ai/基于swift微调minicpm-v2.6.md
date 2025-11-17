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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5UTAEKX%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1SntnT9dSEB6jmcf1uBpepc1A5fN8SkI9dfnFZM1tqAiAV5KWpLBUQBsyHgZkX127kdWp7WFalssgfa5ZRPY1AbSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjax0PMQ9BYQfsDxfKtwDKrD90gqnTgFu7QoKbB6PJHG01%2FVDUT4jrCaM2qHCLdIjLFKs23u8coxH3wp1XPJmjMklZ3mgSK2txEdq9Iths2UQpZNUTOhCSoKpHFPhSvTGzhdO%2Fxl%2BBMa%2FyPRiMdVDxmLC4%2BG2tVAcFEYgydP36L8OOpuE6wSuCbTEkjKDxvVsn2wihJ4%2FbtqIEmq2vdULc%2F6TVYv2Jk6XTs4AzTHq%2FGYy%2FBRfQflv%2BCfDfB61WRsaz6GXmlggqIPNfC9UOzqW%2F5Yb%2BRv3lj0xW03cDbih7PmALTdCCQhy17H%2FUoqFCwsdFLB2ahmT2th5zrXIhWNowJAI2ib4SILYPxhEGY8uRnukI%2Bde9m8ic8TRZq2%2BjKIfezG9ikjF2TlD880%2FI3%2BNETQ4nBUKoWSUaWYLluhgo8vINjewnCo1OGKriWdMUhg1Y9WjA2YI%2FmurY2aOSAosO7BKHhaOXqsh3UUaN0NPcGjaRjqMwD14hwnRXTc8o21uOQe58UijnzmO8rY128Y24RhURwbtFkXZFYN9VtPE3O1lZbBKuduzq7vnc8Nm1mbjBv%2BGqhHTZmhJG2kjiAuVH6LVFb%2FtD3YyWr03EceGyg2uHtqzeBBNHtfiTgn2c8pABLg926456fvqL58wlYfqyAY6pgFY5uTPBN6P4byi9AiYcNBG3LOmsDnDeEYLlhZe4QUrgb9WCEFpCc2%2FmH8SRZf%2BYzWhoKD%2FUCxL4U0rVEKk4SxrASp6HBjwf5fEfYUtpbm3%2FG6lXFR%2B5M8FzykLDvrBcz5nJjNx9bcfaGEvxIGxVaZG4vkQj11ULGZfFRY6aU4Xl9HaCIeJtG6u2lUIqmpJEZAFSiLzUa6bsFmiNisrE9EEI4xxGFIa&X-Amz-Signature=eef43e459dd184eb20874e48e0863414b228861a50e70ce0576e37c40d2d9417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5UTAEKX%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1SntnT9dSEB6jmcf1uBpepc1A5fN8SkI9dfnFZM1tqAiAV5KWpLBUQBsyHgZkX127kdWp7WFalssgfa5ZRPY1AbSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjax0PMQ9BYQfsDxfKtwDKrD90gqnTgFu7QoKbB6PJHG01%2FVDUT4jrCaM2qHCLdIjLFKs23u8coxH3wp1XPJmjMklZ3mgSK2txEdq9Iths2UQpZNUTOhCSoKpHFPhSvTGzhdO%2Fxl%2BBMa%2FyPRiMdVDxmLC4%2BG2tVAcFEYgydP36L8OOpuE6wSuCbTEkjKDxvVsn2wihJ4%2FbtqIEmq2vdULc%2F6TVYv2Jk6XTs4AzTHq%2FGYy%2FBRfQflv%2BCfDfB61WRsaz6GXmlggqIPNfC9UOzqW%2F5Yb%2BRv3lj0xW03cDbih7PmALTdCCQhy17H%2FUoqFCwsdFLB2ahmT2th5zrXIhWNowJAI2ib4SILYPxhEGY8uRnukI%2Bde9m8ic8TRZq2%2BjKIfezG9ikjF2TlD880%2FI3%2BNETQ4nBUKoWSUaWYLluhgo8vINjewnCo1OGKriWdMUhg1Y9WjA2YI%2FmurY2aOSAosO7BKHhaOXqsh3UUaN0NPcGjaRjqMwD14hwnRXTc8o21uOQe58UijnzmO8rY128Y24RhURwbtFkXZFYN9VtPE3O1lZbBKuduzq7vnc8Nm1mbjBv%2BGqhHTZmhJG2kjiAuVH6LVFb%2FtD3YyWr03EceGyg2uHtqzeBBNHtfiTgn2c8pABLg926456fvqL58wlYfqyAY6pgFY5uTPBN6P4byi9AiYcNBG3LOmsDnDeEYLlhZe4QUrgb9WCEFpCc2%2FmH8SRZf%2BYzWhoKD%2FUCxL4U0rVEKk4SxrASp6HBjwf5fEfYUtpbm3%2FG6lXFR%2B5M8FzykLDvrBcz5nJjNx9bcfaGEvxIGxVaZG4vkQj11ULGZfFRY6aU4Xl9HaCIeJtG6u2lUIqmpJEZAFSiLzUa6bsFmiNisrE9EEI4xxGFIa&X-Amz-Signature=4553caa2b21f218230c73c38fec225cf6f8ae06fd9bc200064ef19a5619a8569&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5UTAEKX%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH1SntnT9dSEB6jmcf1uBpepc1A5fN8SkI9dfnFZM1tqAiAV5KWpLBUQBsyHgZkX127kdWp7WFalssgfa5ZRPY1AbSqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjax0PMQ9BYQfsDxfKtwDKrD90gqnTgFu7QoKbB6PJHG01%2FVDUT4jrCaM2qHCLdIjLFKs23u8coxH3wp1XPJmjMklZ3mgSK2txEdq9Iths2UQpZNUTOhCSoKpHFPhSvTGzhdO%2Fxl%2BBMa%2FyPRiMdVDxmLC4%2BG2tVAcFEYgydP36L8OOpuE6wSuCbTEkjKDxvVsn2wihJ4%2FbtqIEmq2vdULc%2F6TVYv2Jk6XTs4AzTHq%2FGYy%2FBRfQflv%2BCfDfB61WRsaz6GXmlggqIPNfC9UOzqW%2F5Yb%2BRv3lj0xW03cDbih7PmALTdCCQhy17H%2FUoqFCwsdFLB2ahmT2th5zrXIhWNowJAI2ib4SILYPxhEGY8uRnukI%2Bde9m8ic8TRZq2%2BjKIfezG9ikjF2TlD880%2FI3%2BNETQ4nBUKoWSUaWYLluhgo8vINjewnCo1OGKriWdMUhg1Y9WjA2YI%2FmurY2aOSAosO7BKHhaOXqsh3UUaN0NPcGjaRjqMwD14hwnRXTc8o21uOQe58UijnzmO8rY128Y24RhURwbtFkXZFYN9VtPE3O1lZbBKuduzq7vnc8Nm1mbjBv%2BGqhHTZmhJG2kjiAuVH6LVFb%2FtD3YyWr03EceGyg2uHtqzeBBNHtfiTgn2c8pABLg926456fvqL58wlYfqyAY6pgFY5uTPBN6P4byi9AiYcNBG3LOmsDnDeEYLlhZe4QUrgb9WCEFpCc2%2FmH8SRZf%2BYzWhoKD%2FUCxL4U0rVEKk4SxrASp6HBjwf5fEfYUtpbm3%2FG6lXFR%2B5M8FzykLDvrBcz5nJjNx9bcfaGEvxIGxVaZG4vkQj11ULGZfFRY6aU4Xl9HaCIeJtG6u2lUIqmpJEZAFSiLzUa6bsFmiNisrE9EEI4xxGFIa&X-Amz-Signature=53b27a2cb91c1632847e13c771ebf4aa43329e0cb736bb02eaef3f323a7afdc2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

