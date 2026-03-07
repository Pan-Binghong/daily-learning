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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKKPSTVF%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDqjl%2FcwraAJYfcmljVPDrktfA3yZTfmEBhr0naksfmpgIhAJLDy%2FSBTkb2KCWZWCKOWiQGKeXu8h%2FEcrggF3cIviDgKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz54wC5MhjztREI6V8q3ANd3bTyXEKVYfAgjQaMxC82MUt2xpFnKq%2BObwn2yCqcv%2BTewMdHsQuUypXB0bCLcNxFJhxv%2FkUE12JXvfYwugnC%2BxtgG2kPQ9hZ8%2BN%2BXZFF5VbCkIuGjYjRxY8t%2F%2BmJNymy2dqTs5XF6RvuizMhzl8%2BuTv%2FCl6lIf6DopKXXWAui0ghb97CWPtuzsDt4k4Hwt%2F%2BIe69%2BAwpu1ptFIUNG8KtEHgAihWsr%2Bvl86bRxhq8m3bRSv57yqTebykeQhDjR6a0mp40O9w1BHab4dwOXagI4tkMZOFIU4JHDXvwUIgNoYNC%2FlqctdIAlG0zyfmSo9lBJ5xKFIgMvbAvzgE6Y%2B8D%2F93W6%2BXWlnrbR7E9W3BAshyhTevwkeDj7n1EcaD%2Buq1ef33CPcwX5nsI%2B6yI7q5RIlk9VUn4Zvvl2padaGUg%2FJHHwiVP44eQRNYEJoMnvMONlD9UNx29i%2BRtviITe2G9dSagwJCBUFgmqTRufxEYFUK2Uf618vu0MkWWor175PXg3igo%2BsbJ%2BEQ9KTFhevsXnwHnZTxMU%2FeP2vu6KbWE7XURJrATTvR8iIPZrBsAKkc%2BrX9icjCvy7tKqdBSQsdoK2Qs4J9jDrdIzCbSinMpeLa63qv6VXbr%2BhTWeDDZlK7NBjqkAa8uZQ0r0JM5znraXJkhGbU7ck3ffziCHBRd7zrHnebi8XyKcqjdnSegp8wDRMz1VevfMhwD7qtkobAK7bJGewyFHsStzoHXoHVmpm5fn4sE1BTgOTAEBAW2dZ1f5gchlsTKOZe%2BlmdUe6pj6yEj2RrUB4ToVRCX0XOyX%2FIh4IuaWMJGq9gFB5uD6QOxQhLSfvSLwX4e0Yd5FUklzxlilKrfyxgR&X-Amz-Signature=b9cfebc6203e26a182c50a29eb10d782187094f6bcfccd2441da4ad047733daa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKKPSTVF%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDqjl%2FcwraAJYfcmljVPDrktfA3yZTfmEBhr0naksfmpgIhAJLDy%2FSBTkb2KCWZWCKOWiQGKeXu8h%2FEcrggF3cIviDgKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz54wC5MhjztREI6V8q3ANd3bTyXEKVYfAgjQaMxC82MUt2xpFnKq%2BObwn2yCqcv%2BTewMdHsQuUypXB0bCLcNxFJhxv%2FkUE12JXvfYwugnC%2BxtgG2kPQ9hZ8%2BN%2BXZFF5VbCkIuGjYjRxY8t%2F%2BmJNymy2dqTs5XF6RvuizMhzl8%2BuTv%2FCl6lIf6DopKXXWAui0ghb97CWPtuzsDt4k4Hwt%2F%2BIe69%2BAwpu1ptFIUNG8KtEHgAihWsr%2Bvl86bRxhq8m3bRSv57yqTebykeQhDjR6a0mp40O9w1BHab4dwOXagI4tkMZOFIU4JHDXvwUIgNoYNC%2FlqctdIAlG0zyfmSo9lBJ5xKFIgMvbAvzgE6Y%2B8D%2F93W6%2BXWlnrbR7E9W3BAshyhTevwkeDj7n1EcaD%2Buq1ef33CPcwX5nsI%2B6yI7q5RIlk9VUn4Zvvl2padaGUg%2FJHHwiVP44eQRNYEJoMnvMONlD9UNx29i%2BRtviITe2G9dSagwJCBUFgmqTRufxEYFUK2Uf618vu0MkWWor175PXg3igo%2BsbJ%2BEQ9KTFhevsXnwHnZTxMU%2FeP2vu6KbWE7XURJrATTvR8iIPZrBsAKkc%2BrX9icjCvy7tKqdBSQsdoK2Qs4J9jDrdIzCbSinMpeLa63qv6VXbr%2BhTWeDDZlK7NBjqkAa8uZQ0r0JM5znraXJkhGbU7ck3ffziCHBRd7zrHnebi8XyKcqjdnSegp8wDRMz1VevfMhwD7qtkobAK7bJGewyFHsStzoHXoHVmpm5fn4sE1BTgOTAEBAW2dZ1f5gchlsTKOZe%2BlmdUe6pj6yEj2RrUB4ToVRCX0XOyX%2FIh4IuaWMJGq9gFB5uD6QOxQhLSfvSLwX4e0Yd5FUklzxlilKrfyxgR&X-Amz-Signature=f58b2e0c983996bc55518aa4c0c372050902fdec6234ca395f7bad78411fa36c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKKPSTVF%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJIMEYCIQDqjl%2FcwraAJYfcmljVPDrktfA3yZTfmEBhr0naksfmpgIhAJLDy%2FSBTkb2KCWZWCKOWiQGKeXu8h%2FEcrggF3cIviDgKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz54wC5MhjztREI6V8q3ANd3bTyXEKVYfAgjQaMxC82MUt2xpFnKq%2BObwn2yCqcv%2BTewMdHsQuUypXB0bCLcNxFJhxv%2FkUE12JXvfYwugnC%2BxtgG2kPQ9hZ8%2BN%2BXZFF5VbCkIuGjYjRxY8t%2F%2BmJNymy2dqTs5XF6RvuizMhzl8%2BuTv%2FCl6lIf6DopKXXWAui0ghb97CWPtuzsDt4k4Hwt%2F%2BIe69%2BAwpu1ptFIUNG8KtEHgAihWsr%2Bvl86bRxhq8m3bRSv57yqTebykeQhDjR6a0mp40O9w1BHab4dwOXagI4tkMZOFIU4JHDXvwUIgNoYNC%2FlqctdIAlG0zyfmSo9lBJ5xKFIgMvbAvzgE6Y%2B8D%2F93W6%2BXWlnrbR7E9W3BAshyhTevwkeDj7n1EcaD%2Buq1ef33CPcwX5nsI%2B6yI7q5RIlk9VUn4Zvvl2padaGUg%2FJHHwiVP44eQRNYEJoMnvMONlD9UNx29i%2BRtviITe2G9dSagwJCBUFgmqTRufxEYFUK2Uf618vu0MkWWor175PXg3igo%2BsbJ%2BEQ9KTFhevsXnwHnZTxMU%2FeP2vu6KbWE7XURJrATTvR8iIPZrBsAKkc%2BrX9icjCvy7tKqdBSQsdoK2Qs4J9jDrdIzCbSinMpeLa63qv6VXbr%2BhTWeDDZlK7NBjqkAa8uZQ0r0JM5znraXJkhGbU7ck3ffziCHBRd7zrHnebi8XyKcqjdnSegp8wDRMz1VevfMhwD7qtkobAK7bJGewyFHsStzoHXoHVmpm5fn4sE1BTgOTAEBAW2dZ1f5gchlsTKOZe%2BlmdUe6pj6yEj2RrUB4ToVRCX0XOyX%2FIh4IuaWMJGq9gFB5uD6QOxQhLSfvSLwX4e0Yd5FUklzxlilKrfyxgR&X-Amz-Signature=951594220180972a16e5d1ea8dc96494481ac7e7c8942695302390246309fea4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

