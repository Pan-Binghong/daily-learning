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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WGLLDI%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICMM4%2FE5Or5a9nHeik4aG0qO0WBdS4vQ5OfIhRWUAiWgAiByOpB2YhhRKRecCAzOZOuyiw02kzpt0cg1hX%2F%2BZ9XI1yqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOgruVjIOydflpv2xKtwDz1qLXM46ze8vwPfe3mBWSEK7kusJ4k1BuC1y4CWQ7UIbKMM0Afp%2FFoWNmUoD0jh8VUUDx5j%2B18PGreoElIlI4hV0bSiiiue0T6pLRZFVRmcwFFWtdpf0Mi2g8iLn%2FwjCfOt1DPhSVOM3ie%2Fv1eaVTGuH4EUGW%2FQH995rjZlKM32uS8hbY%2FfnGesJupNk6AaI0RSQepT9IzzBujmHa65vAA%2ByDdwIRKWDvBuIey08arPXS%2BKGHYpN%2B7RD3W6sCa7aMe4ROgmSSpFGlZfxXYZuk%2FrN%2BK3bEDspjEIXUuwKU4Wss2vvCi%2FnilbnQyJ2Y955rmnJeCW5s3Ye9sJRHblOvOJoWWRxr2tw1pghrt1v3cwKh1yc99ZnyznUOtkG%2Bi2VNdRq4dV%2BQlhl75tvQ6bV9LUqWFyhioFSqcyP1AEdlgZFWVl1PjCf%2FnY2JaHhhtDkEvyWiegq3Uu110y%2FwwzvxiIXT%2BeTikZjvZKYFse%2F5Vd%2FdcMAIx89zae1KgF3CAF2UT%2BQyfXEBkWT4znBNK8cW%2FDJD9IzhWIIqt7FOQMd9YHV6cu7t8e3JYNUcgYAACPQP6DmcwBTwFcX7zOdtU9SKxJjiIYzMKqW1seL7qDe4%2FHXR1dGCdSfo0EL2acwvZ3HzgY6pgF1P6%2BwyB23Id0LRHlHtqshmuosOhnmhnEY6hqKMEBRfsF56H64CRDJzg4CBD7GWLYd7gpHZB6cd%2FUUMYWLRP7j2lGp8%2BAJWOcSZaE7Bx7e6%2BsGt5QgWacrdoJvFCt6Vw4yk9ZLPyPNTLoLR3L%2FJvxzCtlXLE3T79GEcrymQw%2FHF%2B7a636JzXC7t5prEYEbX6tS83u%2BlZ9xVFq6lTYiASFuKY%2FqKOT3&X-Amz-Signature=d63be40a4f49e42c5e55f21954e13fc5036eec8ee9903af179f20a3a029d2f74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WGLLDI%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICMM4%2FE5Or5a9nHeik4aG0qO0WBdS4vQ5OfIhRWUAiWgAiByOpB2YhhRKRecCAzOZOuyiw02kzpt0cg1hX%2F%2BZ9XI1yqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOgruVjIOydflpv2xKtwDz1qLXM46ze8vwPfe3mBWSEK7kusJ4k1BuC1y4CWQ7UIbKMM0Afp%2FFoWNmUoD0jh8VUUDx5j%2B18PGreoElIlI4hV0bSiiiue0T6pLRZFVRmcwFFWtdpf0Mi2g8iLn%2FwjCfOt1DPhSVOM3ie%2Fv1eaVTGuH4EUGW%2FQH995rjZlKM32uS8hbY%2FfnGesJupNk6AaI0RSQepT9IzzBujmHa65vAA%2ByDdwIRKWDvBuIey08arPXS%2BKGHYpN%2B7RD3W6sCa7aMe4ROgmSSpFGlZfxXYZuk%2FrN%2BK3bEDspjEIXUuwKU4Wss2vvCi%2FnilbnQyJ2Y955rmnJeCW5s3Ye9sJRHblOvOJoWWRxr2tw1pghrt1v3cwKh1yc99ZnyznUOtkG%2Bi2VNdRq4dV%2BQlhl75tvQ6bV9LUqWFyhioFSqcyP1AEdlgZFWVl1PjCf%2FnY2JaHhhtDkEvyWiegq3Uu110y%2FwwzvxiIXT%2BeTikZjvZKYFse%2F5Vd%2FdcMAIx89zae1KgF3CAF2UT%2BQyfXEBkWT4znBNK8cW%2FDJD9IzhWIIqt7FOQMd9YHV6cu7t8e3JYNUcgYAACPQP6DmcwBTwFcX7zOdtU9SKxJjiIYzMKqW1seL7qDe4%2FHXR1dGCdSfo0EL2acwvZ3HzgY6pgF1P6%2BwyB23Id0LRHlHtqshmuosOhnmhnEY6hqKMEBRfsF56H64CRDJzg4CBD7GWLYd7gpHZB6cd%2FUUMYWLRP7j2lGp8%2BAJWOcSZaE7Bx7e6%2BsGt5QgWacrdoJvFCt6Vw4yk9ZLPyPNTLoLR3L%2FJvxzCtlXLE3T79GEcrymQw%2FHF%2B7a636JzXC7t5prEYEbX6tS83u%2BlZ9xVFq6lTYiASFuKY%2FqKOT3&X-Amz-Signature=d3b0d6c0d584b79bd52b9af461d09cd66a07b5444af629b0c0cd8ef557299681&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637WGLLDI%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICMM4%2FE5Or5a9nHeik4aG0qO0WBdS4vQ5OfIhRWUAiWgAiByOpB2YhhRKRecCAzOZOuyiw02kzpt0cg1hX%2F%2BZ9XI1yqIBAis%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOgruVjIOydflpv2xKtwDz1qLXM46ze8vwPfe3mBWSEK7kusJ4k1BuC1y4CWQ7UIbKMM0Afp%2FFoWNmUoD0jh8VUUDx5j%2B18PGreoElIlI4hV0bSiiiue0T6pLRZFVRmcwFFWtdpf0Mi2g8iLn%2FwjCfOt1DPhSVOM3ie%2Fv1eaVTGuH4EUGW%2FQH995rjZlKM32uS8hbY%2FfnGesJupNk6AaI0RSQepT9IzzBujmHa65vAA%2ByDdwIRKWDvBuIey08arPXS%2BKGHYpN%2B7RD3W6sCa7aMe4ROgmSSpFGlZfxXYZuk%2FrN%2BK3bEDspjEIXUuwKU4Wss2vvCi%2FnilbnQyJ2Y955rmnJeCW5s3Ye9sJRHblOvOJoWWRxr2tw1pghrt1v3cwKh1yc99ZnyznUOtkG%2Bi2VNdRq4dV%2BQlhl75tvQ6bV9LUqWFyhioFSqcyP1AEdlgZFWVl1PjCf%2FnY2JaHhhtDkEvyWiegq3Uu110y%2FwwzvxiIXT%2BeTikZjvZKYFse%2F5Vd%2FdcMAIx89zae1KgF3CAF2UT%2BQyfXEBkWT4znBNK8cW%2FDJD9IzhWIIqt7FOQMd9YHV6cu7t8e3JYNUcgYAACPQP6DmcwBTwFcX7zOdtU9SKxJjiIYzMKqW1seL7qDe4%2FHXR1dGCdSfo0EL2acwvZ3HzgY6pgF1P6%2BwyB23Id0LRHlHtqshmuosOhnmhnEY6hqKMEBRfsF56H64CRDJzg4CBD7GWLYd7gpHZB6cd%2FUUMYWLRP7j2lGp8%2BAJWOcSZaE7Bx7e6%2BsGt5QgWacrdoJvFCt6Vw4yk9ZLPyPNTLoLR3L%2FJvxzCtlXLE3T79GEcrymQw%2FHF%2B7a636JzXC7t5prEYEbX6tS83u%2BlZ9xVFq6lTYiASFuKY%2FqKOT3&X-Amz-Signature=14969e62c09836e77def65cd1928c568dc37e8d3513361176271c5017544d854&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

