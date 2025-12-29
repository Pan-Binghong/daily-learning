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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4JK7GGS%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXzyuvpwqHKn%2BCQ3vxluSqsIC9FfZU2KsxDEUT14IYsgIhAO34EoOpK7g5C9rj0S4ga9HF2H7N%2B82OPo4fkcmLNF0zKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgo9YpACSDsY7GGzgq3AOaO6XaY1XxgEOSw6B1TJFjdeOCdS1OqF4mmi2rBU2t10QckssYnTcyJELeylRyvCjAlNfLVB985FPBh%2BQ8IS9fFKc6tyourHulb1JsZOZLu3R%2FcuhPoUXsB1mWsbV5xnXFT5%2BFGf%2FEqsPaFpIeAXjpT1bQjDBWX4%2FFCLGzjRj2OhOSa1qlWLyQzQxr0ATEC8n8EVwgti9ACRENbvPQX2if%2FEDp04Hszxti4vlkUkAn6YH1KktZwgQDqlMzjDzwpWL%2BrtS5imhEmjQvpz%2FzcJ9EUPyYG24Fzx%2BIejBxZE7awCu0u6TJ27H2DVIeAdEZjl4%2B64uKixIAVDUQa46OdVU7oxiqRpw80K2h62p968wGqDMBG0SKBb6kaWyjh6kpDbfvxM4jl1Y54dRQSj57qm4BjTmc1wt2jVAbod%2B6j5rDT6bzYse4QW5fYoNAG1JR4JbdnevUTJcS1r%2BQ3Xg9lHA1oqL0D3RW4gT2PP2ROP1sT6QY6CXiXogPLe09I%2FiCRY6JP3f8qV%2BLOn8j0iOv%2BkNG68%2Bf96axeXTWl1mM0xeU2BFxURwsoaqzsNsBYy%2BWX5JgUuIns95VjvMogvk%2BmSUFZLO%2Bj2lDWklDg2wieSG0DSDQGG%2Bom9FbeP6byDClnMfKBjqkAYvhEEKzE0XS9BLC%2F9OkFXYNpJwTc9%2BicffiH6NV57BEQABWq0kfqY5wj%2FMXxAxy7IxSuFFzt8kwYhBTzZslylih2iBayDDcWc%2BYd2kRnJIL4C60Y%2BkmdTz%2Fb8%2BQztP%2Br3IpqjpDzZYJanCQyXpCW5jTvzQ6r2lCQXyFn1j%2F%2BqfGKOGhKaWdChNoYUu1%2FgYchzQjT%2FvuqXjsdD0UX0oGyl5aRpqG&X-Amz-Signature=ff7d844c097945c90b6b25c08295326b1cd8042f51bd5e77134dc95a8b49b0e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4JK7GGS%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXzyuvpwqHKn%2BCQ3vxluSqsIC9FfZU2KsxDEUT14IYsgIhAO34EoOpK7g5C9rj0S4ga9HF2H7N%2B82OPo4fkcmLNF0zKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgo9YpACSDsY7GGzgq3AOaO6XaY1XxgEOSw6B1TJFjdeOCdS1OqF4mmi2rBU2t10QckssYnTcyJELeylRyvCjAlNfLVB985FPBh%2BQ8IS9fFKc6tyourHulb1JsZOZLu3R%2FcuhPoUXsB1mWsbV5xnXFT5%2BFGf%2FEqsPaFpIeAXjpT1bQjDBWX4%2FFCLGzjRj2OhOSa1qlWLyQzQxr0ATEC8n8EVwgti9ACRENbvPQX2if%2FEDp04Hszxti4vlkUkAn6YH1KktZwgQDqlMzjDzwpWL%2BrtS5imhEmjQvpz%2FzcJ9EUPyYG24Fzx%2BIejBxZE7awCu0u6TJ27H2DVIeAdEZjl4%2B64uKixIAVDUQa46OdVU7oxiqRpw80K2h62p968wGqDMBG0SKBb6kaWyjh6kpDbfvxM4jl1Y54dRQSj57qm4BjTmc1wt2jVAbod%2B6j5rDT6bzYse4QW5fYoNAG1JR4JbdnevUTJcS1r%2BQ3Xg9lHA1oqL0D3RW4gT2PP2ROP1sT6QY6CXiXogPLe09I%2FiCRY6JP3f8qV%2BLOn8j0iOv%2BkNG68%2Bf96axeXTWl1mM0xeU2BFxURwsoaqzsNsBYy%2BWX5JgUuIns95VjvMogvk%2BmSUFZLO%2Bj2lDWklDg2wieSG0DSDQGG%2Bom9FbeP6byDClnMfKBjqkAYvhEEKzE0XS9BLC%2F9OkFXYNpJwTc9%2BicffiH6NV57BEQABWq0kfqY5wj%2FMXxAxy7IxSuFFzt8kwYhBTzZslylih2iBayDDcWc%2BYd2kRnJIL4C60Y%2BkmdTz%2Fb8%2BQztP%2Br3IpqjpDzZYJanCQyXpCW5jTvzQ6r2lCQXyFn1j%2F%2BqfGKOGhKaWdChNoYUu1%2FgYchzQjT%2FvuqXjsdD0UX0oGyl5aRpqG&X-Amz-Signature=ff5ac82e3d33a129e45851861bf8d42ba298897058810fffa181153840d9b0ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4JK7GGS%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDXzyuvpwqHKn%2BCQ3vxluSqsIC9FfZU2KsxDEUT14IYsgIhAO34EoOpK7g5C9rj0S4ga9HF2H7N%2B82OPo4fkcmLNF0zKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwgo9YpACSDsY7GGzgq3AOaO6XaY1XxgEOSw6B1TJFjdeOCdS1OqF4mmi2rBU2t10QckssYnTcyJELeylRyvCjAlNfLVB985FPBh%2BQ8IS9fFKc6tyourHulb1JsZOZLu3R%2FcuhPoUXsB1mWsbV5xnXFT5%2BFGf%2FEqsPaFpIeAXjpT1bQjDBWX4%2FFCLGzjRj2OhOSa1qlWLyQzQxr0ATEC8n8EVwgti9ACRENbvPQX2if%2FEDp04Hszxti4vlkUkAn6YH1KktZwgQDqlMzjDzwpWL%2BrtS5imhEmjQvpz%2FzcJ9EUPyYG24Fzx%2BIejBxZE7awCu0u6TJ27H2DVIeAdEZjl4%2B64uKixIAVDUQa46OdVU7oxiqRpw80K2h62p968wGqDMBG0SKBb6kaWyjh6kpDbfvxM4jl1Y54dRQSj57qm4BjTmc1wt2jVAbod%2B6j5rDT6bzYse4QW5fYoNAG1JR4JbdnevUTJcS1r%2BQ3Xg9lHA1oqL0D3RW4gT2PP2ROP1sT6QY6CXiXogPLe09I%2FiCRY6JP3f8qV%2BLOn8j0iOv%2BkNG68%2Bf96axeXTWl1mM0xeU2BFxURwsoaqzsNsBYy%2BWX5JgUuIns95VjvMogvk%2BmSUFZLO%2Bj2lDWklDg2wieSG0DSDQGG%2Bom9FbeP6byDClnMfKBjqkAYvhEEKzE0XS9BLC%2F9OkFXYNpJwTc9%2BicffiH6NV57BEQABWq0kfqY5wj%2FMXxAxy7IxSuFFzt8kwYhBTzZslylih2iBayDDcWc%2BYd2kRnJIL4C60Y%2BkmdTz%2Fb8%2BQztP%2Br3IpqjpDzZYJanCQyXpCW5jTvzQ6r2lCQXyFn1j%2F%2BqfGKOGhKaWdChNoYUu1%2FgYchzQjT%2FvuqXjsdD0UX0oGyl5aRpqG&X-Amz-Signature=2705c0c0135be63ea8f4fabeef60e7c7b9583091398fe8dfe47dba4aa6faa9c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

