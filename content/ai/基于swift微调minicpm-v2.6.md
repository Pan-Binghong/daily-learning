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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J7UPR6T%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcKzSkUXGuMd%2FHZ2cXSBLCvgCb1Nlp%2B7G9%2FWTmWcKNYAiEApeRBpdyIeqxrpul66GZhKWHmL7arvSrzSW7wZRQp8AEqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP9QTuSqKQnfJkg27SrcAwKQNrV%2FIEagBnx8sE9cUjehp%2FOF1qTqd5JEnmGwOiWzyMDv86q0yhFl39rQhRdSiv2sZtzN6VjeUBmk18yrUpJUK8VQlq2W0peEEyuacBUM0lam4yh865AbHjbUFh1DskPvXx5DygdoUC%2FiWJR7tnj7Pe0u82Y08eps8TXHBa5UwXbfihuFeNlGtDplAvvywglYFSCShTnYd8PHYKa%2FMWBNJwgjaf68QeWI9ILy2cjdakIXc4wSAeQPx7dbf4VgKV8iC18mpssOMaxIjVwjU%2Bj%2Bd9Y1kyfEObhaiUGMffPzozEryrjDL3wK68g%2Bp7lYDKEzozPEz1AJSfNPHbwZro3bhzFqeCLUjWTHHeIKgrgeQySzJD%2BB1rGcyaxDuXTaDVF1p9n43wy%2FJHPmzKE9fugp5WQ0oyyiq6%2BOfw3F%2FnMAgO9ciVtCRV8ZgOuMzIPCQLGu%2BnkjM%2BvTnbvMhqdOGse4VgANq0%2FoO0nDgCDe4%2FzSLEuHmSAjWbZzDktt2k2gz2ijVPeOUCNl%2BLd%2FR3V85IvX2AClzk7otNCISId1x0%2BF2tMI1YCSTdxsLcCZmGZVkCl7U%2FzkwJxtZzrI92LPsbRpRKa2TkmByzOBj9J0SyCw4LH00UN49sz%2BQerNMI31h84GOqUBbKwqR9ZU6XSNTanZ6hsDbn0%2FT1f8yIPqXxMH93g5UkIz2UxGvu4%2BE6RFDumd2KlzemWogLkNjJjGVaMdNKTx9QzVQRwHhGy7Rca%2Bld29%2BtJFog92N6EMTosThCvyxCloZ5Oohuj3PQ08ffYmVl%2BKQMYK8LtztTGqIfA%2FCU2uAFnuqJZNY7PU5xwXsOyGHLTJX0E%2FmsoRTedstBEEokuwaRP0%2B6Rj&X-Amz-Signature=b771d82785fb908e8f8c5f9652f665990e298108806d2cbc541a06a6700ee519&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J7UPR6T%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcKzSkUXGuMd%2FHZ2cXSBLCvgCb1Nlp%2B7G9%2FWTmWcKNYAiEApeRBpdyIeqxrpul66GZhKWHmL7arvSrzSW7wZRQp8AEqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP9QTuSqKQnfJkg27SrcAwKQNrV%2FIEagBnx8sE9cUjehp%2FOF1qTqd5JEnmGwOiWzyMDv86q0yhFl39rQhRdSiv2sZtzN6VjeUBmk18yrUpJUK8VQlq2W0peEEyuacBUM0lam4yh865AbHjbUFh1DskPvXx5DygdoUC%2FiWJR7tnj7Pe0u82Y08eps8TXHBa5UwXbfihuFeNlGtDplAvvywglYFSCShTnYd8PHYKa%2FMWBNJwgjaf68QeWI9ILy2cjdakIXc4wSAeQPx7dbf4VgKV8iC18mpssOMaxIjVwjU%2Bj%2Bd9Y1kyfEObhaiUGMffPzozEryrjDL3wK68g%2Bp7lYDKEzozPEz1AJSfNPHbwZro3bhzFqeCLUjWTHHeIKgrgeQySzJD%2BB1rGcyaxDuXTaDVF1p9n43wy%2FJHPmzKE9fugp5WQ0oyyiq6%2BOfw3F%2FnMAgO9ciVtCRV8ZgOuMzIPCQLGu%2BnkjM%2BvTnbvMhqdOGse4VgANq0%2FoO0nDgCDe4%2FzSLEuHmSAjWbZzDktt2k2gz2ijVPeOUCNl%2BLd%2FR3V85IvX2AClzk7otNCISId1x0%2BF2tMI1YCSTdxsLcCZmGZVkCl7U%2FzkwJxtZzrI92LPsbRpRKa2TkmByzOBj9J0SyCw4LH00UN49sz%2BQerNMI31h84GOqUBbKwqR9ZU6XSNTanZ6hsDbn0%2FT1f8yIPqXxMH93g5UkIz2UxGvu4%2BE6RFDumd2KlzemWogLkNjJjGVaMdNKTx9QzVQRwHhGy7Rca%2Bld29%2BtJFog92N6EMTosThCvyxCloZ5Oohuj3PQ08ffYmVl%2BKQMYK8LtztTGqIfA%2FCU2uAFnuqJZNY7PU5xwXsOyGHLTJX0E%2FmsoRTedstBEEokuwaRP0%2B6Rj&X-Amz-Signature=10c3d7b466dd41627441891028f5cb11e8d43ee50d06ecbfd9181119a8100232&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J7UPR6T%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcKzSkUXGuMd%2FHZ2cXSBLCvgCb1Nlp%2B7G9%2FWTmWcKNYAiEApeRBpdyIeqxrpul66GZhKWHmL7arvSrzSW7wZRQp8AEqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP9QTuSqKQnfJkg27SrcAwKQNrV%2FIEagBnx8sE9cUjehp%2FOF1qTqd5JEnmGwOiWzyMDv86q0yhFl39rQhRdSiv2sZtzN6VjeUBmk18yrUpJUK8VQlq2W0peEEyuacBUM0lam4yh865AbHjbUFh1DskPvXx5DygdoUC%2FiWJR7tnj7Pe0u82Y08eps8TXHBa5UwXbfihuFeNlGtDplAvvywglYFSCShTnYd8PHYKa%2FMWBNJwgjaf68QeWI9ILy2cjdakIXc4wSAeQPx7dbf4VgKV8iC18mpssOMaxIjVwjU%2Bj%2Bd9Y1kyfEObhaiUGMffPzozEryrjDL3wK68g%2Bp7lYDKEzozPEz1AJSfNPHbwZro3bhzFqeCLUjWTHHeIKgrgeQySzJD%2BB1rGcyaxDuXTaDVF1p9n43wy%2FJHPmzKE9fugp5WQ0oyyiq6%2BOfw3F%2FnMAgO9ciVtCRV8ZgOuMzIPCQLGu%2BnkjM%2BvTnbvMhqdOGse4VgANq0%2FoO0nDgCDe4%2FzSLEuHmSAjWbZzDktt2k2gz2ijVPeOUCNl%2BLd%2FR3V85IvX2AClzk7otNCISId1x0%2BF2tMI1YCSTdxsLcCZmGZVkCl7U%2FzkwJxtZzrI92LPsbRpRKa2TkmByzOBj9J0SyCw4LH00UN49sz%2BQerNMI31h84GOqUBbKwqR9ZU6XSNTanZ6hsDbn0%2FT1f8yIPqXxMH93g5UkIz2UxGvu4%2BE6RFDumd2KlzemWogLkNjJjGVaMdNKTx9QzVQRwHhGy7Rca%2Bld29%2BtJFog92N6EMTosThCvyxCloZ5Oohuj3PQ08ffYmVl%2BKQMYK8LtztTGqIfA%2FCU2uAFnuqJZNY7PU5xwXsOyGHLTJX0E%2FmsoRTedstBEEokuwaRP0%2B6Rj&X-Amz-Signature=7bf3d10c99d05c5710ad63295d7c2d9ba7b6915f869eed29c3f644698db82070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

