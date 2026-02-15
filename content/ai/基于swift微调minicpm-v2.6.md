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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R6AXYS6%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQD9DEap4QxSylmYas%2FpW296FSOjFaAxI2V7p2WX8IYhgwIhAPJ29M%2FCZmrFbTYi7a1y7Ccy3xz9a0L8obP8dd%2BM4bHKKv8DCBEQABoMNjM3NDIzMTgzODA1IgzOlrpVHUkLvg7NhEsq3AMM2vLqvnv4ZcC4ET0qJR2cgpNqBiExgVkLtI7G0CFiy2I%2FRZbqV04rLVgWPUDUCXQInxg5Rnglsy3LvwBliMUE5l%2F3X%2B%2Bi2VGquwvBtRYRNqc6uXlF%2FW4KucT5HW%2BFO%2FwhtmUyLTBJyuGHR2gV2snGwOenRRaLmDpUDaXswjmR56siFsJqyMps43xnleNowzDspF26Qk85MxTDRmccM2wrYD%2BvfKeKFU3nu%2FL345ZvHF7B2PxFmDCLr3aCaAMU3jaada6Bqyvy9pPl%2BvBKzXKZuYPpz2L1hpY3Ga5Cdsxi%2BZ90Fa7qM3s0FCOpRvCuUatnQaCGVJ2HcwL0bnzBLSTbVW2LLR%2BFH7tJJSUjdCpH1ogcPveQmqbEwJFWsa%2BtSrZOp93SbcccOletq%2BWEgYg0kh%2FUiss9X3Brb9S9PI87BLiWcSJmAV%2BK8vjx%2FWVKqiKOL782e1eJr%2Bw5%2F%2FRJitvMe2kKNV7TW%2Blck2EKlRzAE0wPfrSTEcPsBcrImBFzn0EHXdrOtby5XYpb5Zan%2F29W7ZRx13LOFl4diL4l%2FGRfGD7qH9CJncSZi3UGiVtdyUxor2x44XJ1kSaf63q8QWpm1xWSE9S%2FilXMaizTjgzYVeq0w4i6Wr2wgCsf6zDpncTMBjqkAeXDqO41e0lqBqayM0Bx%2Br0irvZpGwndyx8%2FuZa7aUzD9dOWNA7VC%2BAQCs8TcCkCEdVYhhnjVGcmKdrMeoWl0G6O%2FlegJ9AdIvJMTHEbKS33648llRrLw8boFhbmwURmt3qF1RE%2BPq7QFkDmKJDx0ICGFIEdx3KHO8FZhyVQ5g%2F0BreyhBqCu7ZF59RGok%2Bz%2FCbmg8wg%2Fbq8PJoWJj7d1iVQ63L7&X-Amz-Signature=890481fb5a0abb749d926e75c00fae3c65889651b81fbb08488f606c5e5d4992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R6AXYS6%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQD9DEap4QxSylmYas%2FpW296FSOjFaAxI2V7p2WX8IYhgwIhAPJ29M%2FCZmrFbTYi7a1y7Ccy3xz9a0L8obP8dd%2BM4bHKKv8DCBEQABoMNjM3NDIzMTgzODA1IgzOlrpVHUkLvg7NhEsq3AMM2vLqvnv4ZcC4ET0qJR2cgpNqBiExgVkLtI7G0CFiy2I%2FRZbqV04rLVgWPUDUCXQInxg5Rnglsy3LvwBliMUE5l%2F3X%2B%2Bi2VGquwvBtRYRNqc6uXlF%2FW4KucT5HW%2BFO%2FwhtmUyLTBJyuGHR2gV2snGwOenRRaLmDpUDaXswjmR56siFsJqyMps43xnleNowzDspF26Qk85MxTDRmccM2wrYD%2BvfKeKFU3nu%2FL345ZvHF7B2PxFmDCLr3aCaAMU3jaada6Bqyvy9pPl%2BvBKzXKZuYPpz2L1hpY3Ga5Cdsxi%2BZ90Fa7qM3s0FCOpRvCuUatnQaCGVJ2HcwL0bnzBLSTbVW2LLR%2BFH7tJJSUjdCpH1ogcPveQmqbEwJFWsa%2BtSrZOp93SbcccOletq%2BWEgYg0kh%2FUiss9X3Brb9S9PI87BLiWcSJmAV%2BK8vjx%2FWVKqiKOL782e1eJr%2Bw5%2F%2FRJitvMe2kKNV7TW%2Blck2EKlRzAE0wPfrSTEcPsBcrImBFzn0EHXdrOtby5XYpb5Zan%2F29W7ZRx13LOFl4diL4l%2FGRfGD7qH9CJncSZi3UGiVtdyUxor2x44XJ1kSaf63q8QWpm1xWSE9S%2FilXMaizTjgzYVeq0w4i6Wr2wgCsf6zDpncTMBjqkAeXDqO41e0lqBqayM0Bx%2Br0irvZpGwndyx8%2FuZa7aUzD9dOWNA7VC%2BAQCs8TcCkCEdVYhhnjVGcmKdrMeoWl0G6O%2FlegJ9AdIvJMTHEbKS33648llRrLw8boFhbmwURmt3qF1RE%2BPq7QFkDmKJDx0ICGFIEdx3KHO8FZhyVQ5g%2F0BreyhBqCu7ZF59RGok%2Bz%2FCbmg8wg%2Fbq8PJoWJj7d1iVQ63L7&X-Amz-Signature=15bb1cd0a1bb13b3d985e96bb3ebbf05d60bcb2ec6f783504c0337bbdc28e237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667R6AXYS6%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJIMEYCIQD9DEap4QxSylmYas%2FpW296FSOjFaAxI2V7p2WX8IYhgwIhAPJ29M%2FCZmrFbTYi7a1y7Ccy3xz9a0L8obP8dd%2BM4bHKKv8DCBEQABoMNjM3NDIzMTgzODA1IgzOlrpVHUkLvg7NhEsq3AMM2vLqvnv4ZcC4ET0qJR2cgpNqBiExgVkLtI7G0CFiy2I%2FRZbqV04rLVgWPUDUCXQInxg5Rnglsy3LvwBliMUE5l%2F3X%2B%2Bi2VGquwvBtRYRNqc6uXlF%2FW4KucT5HW%2BFO%2FwhtmUyLTBJyuGHR2gV2snGwOenRRaLmDpUDaXswjmR56siFsJqyMps43xnleNowzDspF26Qk85MxTDRmccM2wrYD%2BvfKeKFU3nu%2FL345ZvHF7B2PxFmDCLr3aCaAMU3jaada6Bqyvy9pPl%2BvBKzXKZuYPpz2L1hpY3Ga5Cdsxi%2BZ90Fa7qM3s0FCOpRvCuUatnQaCGVJ2HcwL0bnzBLSTbVW2LLR%2BFH7tJJSUjdCpH1ogcPveQmqbEwJFWsa%2BtSrZOp93SbcccOletq%2BWEgYg0kh%2FUiss9X3Brb9S9PI87BLiWcSJmAV%2BK8vjx%2FWVKqiKOL782e1eJr%2Bw5%2F%2FRJitvMe2kKNV7TW%2Blck2EKlRzAE0wPfrSTEcPsBcrImBFzn0EHXdrOtby5XYpb5Zan%2F29W7ZRx13LOFl4diL4l%2FGRfGD7qH9CJncSZi3UGiVtdyUxor2x44XJ1kSaf63q8QWpm1xWSE9S%2FilXMaizTjgzYVeq0w4i6Wr2wgCsf6zDpncTMBjqkAeXDqO41e0lqBqayM0Bx%2Br0irvZpGwndyx8%2FuZa7aUzD9dOWNA7VC%2BAQCs8TcCkCEdVYhhnjVGcmKdrMeoWl0G6O%2FlegJ9AdIvJMTHEbKS33648llRrLw8boFhbmwURmt3qF1RE%2BPq7QFkDmKJDx0ICGFIEdx3KHO8FZhyVQ5g%2F0BreyhBqCu7ZF59RGok%2Bz%2FCbmg8wg%2Fbq8PJoWJj7d1iVQ63L7&X-Amz-Signature=1b9ab4752246bd3bc37155569d6185adadb6a43c07e145f4f8308dfa5b5688c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

