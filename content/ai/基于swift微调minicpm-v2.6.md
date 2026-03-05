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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHC2O2ZP%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8MW%2BF6iMrn1yO7oCb4Mupf7RLGglfspGPrtRtZ0mT9wIgMIlbs9P3r003EQ4x6oFSiueqWWZu9j1E1xdICyjmZEYqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJHjg2YdwWZ6lodSircAwqV6ctlnMU0ysQpC19YsVzytU6kB4v5x1Gte7Mw5XPGiVyC2duT6CJNF5IhbpccGo5qNMJm6LwCRdrh7Z4Ctsto1aXW4MPhVFEQ75m7WGyeV0Y3QA8wAydnQ68L6%2BQHy8sP3T%2Fz0sVoM6ks7OxZQcmXybFkw4Rjj4RTkdOzRBQabS0ooooFm6NhGmbGq2aF1z2l8%2BDQqV8WI%2BrDOZFyxuejF5sbDUoee0yDGQ%2B2C1W15y0doOd42ApN2AD0R5OSUHZH1OnwNcS1OC7Va7YcIhSKytONZxdC2ysRaZpSrCiAno638d9%2FJABOrtNdb6c4gMKMGVCXy2mv9DOA2U1U2XCimyNezXgOLVKA9l8XsB8t1Am0MZsSuo2xhSXuDK5LlZi6EPeRpGbF57nWpdXAH%2B2%2BXwOFgRhL6McjL6ey9c%2BXqzoHTqRJ2dvKA%2FZvMsVqrFPkxGgwfWfkRSAl4n2VR%2FtnLDSX0GQywzJyEz%2BYOgxrv9JaJLBmsh0upXOm2DOdEh7EpNMYIJ68p%2FZ%2Byp7W%2BxoPyXFIbW8BnT3AKeUOYX6QlANeP7uU86lWrAgWn00v%2BcN6O6jdJAAG0ZqoKINZ%2FGMOYs6p79%2BhyHNiKsWM88MN4TJ2XtEcqWEw5bYSMNnfo80GOqUBKbH9tw05ki3K%2BO7Kn5JE2KibuW%2B8a%2FiHSgYwem2NNtaeDqGv81AWqQks1Tvfhs5J%2FnjE97tb%2BiT1n5tgdp7DslhWDWZm8S3RfTCwvUGJ68mTmQpBxqbIPIGzbLjkv%2BWMuLUeSzEiTgNh1dWlXaUb6utU52t3MqatXvTWy%2FG4SJyJLrRrWGZ%2BfmQhOhNQTS8lEDmdnYruNxukG57XQdP%2FVydg3m8O&X-Amz-Signature=67073b1dee7c4d59c83b405674306c23d5da899a0c0d76f18df7179a515335ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHC2O2ZP%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8MW%2BF6iMrn1yO7oCb4Mupf7RLGglfspGPrtRtZ0mT9wIgMIlbs9P3r003EQ4x6oFSiueqWWZu9j1E1xdICyjmZEYqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJHjg2YdwWZ6lodSircAwqV6ctlnMU0ysQpC19YsVzytU6kB4v5x1Gte7Mw5XPGiVyC2duT6CJNF5IhbpccGo5qNMJm6LwCRdrh7Z4Ctsto1aXW4MPhVFEQ75m7WGyeV0Y3QA8wAydnQ68L6%2BQHy8sP3T%2Fz0sVoM6ks7OxZQcmXybFkw4Rjj4RTkdOzRBQabS0ooooFm6NhGmbGq2aF1z2l8%2BDQqV8WI%2BrDOZFyxuejF5sbDUoee0yDGQ%2B2C1W15y0doOd42ApN2AD0R5OSUHZH1OnwNcS1OC7Va7YcIhSKytONZxdC2ysRaZpSrCiAno638d9%2FJABOrtNdb6c4gMKMGVCXy2mv9DOA2U1U2XCimyNezXgOLVKA9l8XsB8t1Am0MZsSuo2xhSXuDK5LlZi6EPeRpGbF57nWpdXAH%2B2%2BXwOFgRhL6McjL6ey9c%2BXqzoHTqRJ2dvKA%2FZvMsVqrFPkxGgwfWfkRSAl4n2VR%2FtnLDSX0GQywzJyEz%2BYOgxrv9JaJLBmsh0upXOm2DOdEh7EpNMYIJ68p%2FZ%2Byp7W%2BxoPyXFIbW8BnT3AKeUOYX6QlANeP7uU86lWrAgWn00v%2BcN6O6jdJAAG0ZqoKINZ%2FGMOYs6p79%2BhyHNiKsWM88MN4TJ2XtEcqWEw5bYSMNnfo80GOqUBKbH9tw05ki3K%2BO7Kn5JE2KibuW%2B8a%2FiHSgYwem2NNtaeDqGv81AWqQks1Tvfhs5J%2FnjE97tb%2BiT1n5tgdp7DslhWDWZm8S3RfTCwvUGJ68mTmQpBxqbIPIGzbLjkv%2BWMuLUeSzEiTgNh1dWlXaUb6utU52t3MqatXvTWy%2FG4SJyJLrRrWGZ%2BfmQhOhNQTS8lEDmdnYruNxukG57XQdP%2FVydg3m8O&X-Amz-Signature=2ad53e0a67f32de024b9c115919c9f773492b2174d93591772f836689ebba78b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHC2O2ZP%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8MW%2BF6iMrn1yO7oCb4Mupf7RLGglfspGPrtRtZ0mT9wIgMIlbs9P3r003EQ4x6oFSiueqWWZu9j1E1xdICyjmZEYqiAQIxP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJHjg2YdwWZ6lodSircAwqV6ctlnMU0ysQpC19YsVzytU6kB4v5x1Gte7Mw5XPGiVyC2duT6CJNF5IhbpccGo5qNMJm6LwCRdrh7Z4Ctsto1aXW4MPhVFEQ75m7WGyeV0Y3QA8wAydnQ68L6%2BQHy8sP3T%2Fz0sVoM6ks7OxZQcmXybFkw4Rjj4RTkdOzRBQabS0ooooFm6NhGmbGq2aF1z2l8%2BDQqV8WI%2BrDOZFyxuejF5sbDUoee0yDGQ%2B2C1W15y0doOd42ApN2AD0R5OSUHZH1OnwNcS1OC7Va7YcIhSKytONZxdC2ysRaZpSrCiAno638d9%2FJABOrtNdb6c4gMKMGVCXy2mv9DOA2U1U2XCimyNezXgOLVKA9l8XsB8t1Am0MZsSuo2xhSXuDK5LlZi6EPeRpGbF57nWpdXAH%2B2%2BXwOFgRhL6McjL6ey9c%2BXqzoHTqRJ2dvKA%2FZvMsVqrFPkxGgwfWfkRSAl4n2VR%2FtnLDSX0GQywzJyEz%2BYOgxrv9JaJLBmsh0upXOm2DOdEh7EpNMYIJ68p%2FZ%2Byp7W%2BxoPyXFIbW8BnT3AKeUOYX6QlANeP7uU86lWrAgWn00v%2BcN6O6jdJAAG0ZqoKINZ%2FGMOYs6p79%2BhyHNiKsWM88MN4TJ2XtEcqWEw5bYSMNnfo80GOqUBKbH9tw05ki3K%2BO7Kn5JE2KibuW%2B8a%2FiHSgYwem2NNtaeDqGv81AWqQks1Tvfhs5J%2FnjE97tb%2BiT1n5tgdp7DslhWDWZm8S3RfTCwvUGJ68mTmQpBxqbIPIGzbLjkv%2BWMuLUeSzEiTgNh1dWlXaUb6utU52t3MqatXvTWy%2FG4SJyJLrRrWGZ%2BfmQhOhNQTS8lEDmdnYruNxukG57XQdP%2FVydg3m8O&X-Amz-Signature=ca7f4e0e49e4bd372df87b2396f166a65390cba6b88b3098913a232570e7697c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

