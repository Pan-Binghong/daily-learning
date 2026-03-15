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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=2b7e26b1fc9fe9e7ef9039cc040acdd2416178910a62fa0d4831dfb933276bd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=30bdb1fa491d6b6325532f2327a4676fdddf3f4b2f74ea5c224553caa0b13dbd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656CP2OKS%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTJ5XaMg6yTStH1d8bBE5LWV4wbKiLCeviwNC4oKCdAiEAs0fmA2GhO8oZgCMfuRzQ33ZMhcx3Jk%2Fx%2FWQo21Y5RrsqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2BQ6RZ6xe8cyFfhcyrcA%2BFPHU67UZGak6WWg2dmfGUeGaGVpXvjYmsjGs278AaUCIznl%2FlGfHlyHIOQRhYtGd6YfeYTaPo0Gv3wQzawxkTC%2F1KsVaBqs2Ro4dCJbA77js9JdOauQh8saMetZSQQvte3ED%2FCbsyAOPxYO6qpJDRzbw5noo8K1u6An%2BxRmhgJcHzQnbuKexZDSs2Aic7LDydaMqiyBQgqYTXKMXAwkLGKVK1qB7ZdoS4LPX7d1EWJmNz6Y8Kaj5u1yoHpezaNpy8zEUVlAXBoipCZWJM9oO%2BAvfJrqmAoaSbI1Jf0zbwe2nYUIzox7Sn6XTEOKL0Ce5PNyXG6vYPjlpviAdWRhOAdrOzX%2FIkQ1n8M020%2FYBjNo%2Bwu21K8s4u4VaI8dR%2BSYhP6XH1BicppFFx2WNOttAjlrVK2aH0sOEwdfpXeOeGU9h%2BJL9akcUCZADLSdzmw42VsF48PN5AjzNQ3vfINlyq9jIzVEBpB1CQC6NLrjCsJ8nZNC%2B3Ur4ieh%2Fmetr%2FH0Bv6%2BuyBnBe8GjMb1H5BE7Kj9HVZ8HayhxsV0f5z6fqHXHuNU4Tb0DcgG3QeMUNe8GvX%2B4uxlfsOk8%2Frh6DZZ1lJNIqcWOheqstmW5ARiSeD9bKbxTWEzJWw%2FwMRMKSQ2M0GOqUBuVxjgPeLUhLgK4avUXLmuu5ZomrprOz3BL90gJGEdk4bM2SryzaDoHLvP4vQ1hISNyA9VXP2molB57uF8l66F3IiQ6%2BymIEEPaJHU4GEqTgcGObMcIWn1eIKoB185KKjxpDdTu6lungZFwFXcxYKBAoG0a%2FRTA0vvpFMfg3QDNGG7LK5f3utzzSLrHyRWvQdyg%2FvtzltkuRTt3N8PdbzP2xLS%2FNJ&X-Amz-Signature=a68f8f58d9c2cf7c0e40f9f02fff0af687e73d33e5a62fb0d80dc300d1eeb5eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

