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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGNQXHPH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxS%2Bub03FXg8WpmuHIh3v4rTHor4F8pVIJ7%2F9vM2MRNAiAGx9mxP1my%2BC78HU6MhxdXBK2lOcs6rIVpvqy65jfL9Sr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMzSQtqCajwX9nKw%2B6KtwDkDEwz702cA4O66U0qCieWmXOcdV7pw49vU69MZ0bW6RStIaXmJXwpfSgX7bC6F1D4JCXMM2fjVHjnNZztodySoXCM%2FgLnEZZ9oBy7Wb4WrcMBX7jM4ngSwmizTpYQBc7YLHBbOqPy0OFBN9C8ZCN1azuFW2U05fnBWUtHBPYWoEKnATrlNxGfxwQkFo0CR7Yy4GSd4doYJYl5Zfmz16uAyCqAyLU8x3a%2Flsj0rfZh%2FX4Ycn4b3wLzubhJPjlQlsBgsvvWbe7mExhZ%2FS8O%2FA9hhVczFr51NYxwvUFgWdLZqlmTB5dseJxksnfyowqmcdsKz8veS%2FUFfSuXyTfI9w6B2VDrzM8kbRI%2BHGm%2FlIDiDm5mcKwXMQ5Wxhp7ZtQLPEs779uQdGJUBG4NtI%2FXHnmP4TVk86PLbwuuaC1VURBXMbxal9lyc6dVtilKvbFVkTxk%2FoUD1DrFfGQn%2BPhNaDDnK%2FfUDbZPjW7G9as36jRVh%2Bg7KiROP%2BGtq0%2F%2BOq7roW2RoW7DIAjElKyksRa8Xk%2Bq42e9ViQQ7KGCFvjRjXz2%2FHh%2F6oziTvm2bRF%2FmXBbpWRlBx3OaAA6zEDOS3fWS%2BPodUJVibdhSh9uFpN9mb667sY17iSw2MAkpKqdwUw9uS8zgY6pgFizW%2FdNKgQaGrn3hVYFg23BdrkLTSymiRs%2FQbKJrkati8%2FIZnQDMxD0jRofktk9VYCB1K6hM8fD0xZ9vRl1BdfocUGIG8%2Fa6n%2FAhdcHgWIVGBpORrfYAjHCskigdv5oUlzOGeEGaYnFCXCLSoBwboShqW5fIKRSeNNMIZAv3fcjnOLUMpdnXPGsUat5KlMEl1T5sux56WyGMDPahKMVntd5Kxy3wID&X-Amz-Signature=c0cc64fa0999962f822ecd3c3e3526c662e7493c61362c403f3f3ce7a9d1a30d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGNQXHPH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxS%2Bub03FXg8WpmuHIh3v4rTHor4F8pVIJ7%2F9vM2MRNAiAGx9mxP1my%2BC78HU6MhxdXBK2lOcs6rIVpvqy65jfL9Sr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMzSQtqCajwX9nKw%2B6KtwDkDEwz702cA4O66U0qCieWmXOcdV7pw49vU69MZ0bW6RStIaXmJXwpfSgX7bC6F1D4JCXMM2fjVHjnNZztodySoXCM%2FgLnEZZ9oBy7Wb4WrcMBX7jM4ngSwmizTpYQBc7YLHBbOqPy0OFBN9C8ZCN1azuFW2U05fnBWUtHBPYWoEKnATrlNxGfxwQkFo0CR7Yy4GSd4doYJYl5Zfmz16uAyCqAyLU8x3a%2Flsj0rfZh%2FX4Ycn4b3wLzubhJPjlQlsBgsvvWbe7mExhZ%2FS8O%2FA9hhVczFr51NYxwvUFgWdLZqlmTB5dseJxksnfyowqmcdsKz8veS%2FUFfSuXyTfI9w6B2VDrzM8kbRI%2BHGm%2FlIDiDm5mcKwXMQ5Wxhp7ZtQLPEs779uQdGJUBG4NtI%2FXHnmP4TVk86PLbwuuaC1VURBXMbxal9lyc6dVtilKvbFVkTxk%2FoUD1DrFfGQn%2BPhNaDDnK%2FfUDbZPjW7G9as36jRVh%2Bg7KiROP%2BGtq0%2F%2BOq7roW2RoW7DIAjElKyksRa8Xk%2Bq42e9ViQQ7KGCFvjRjXz2%2FHh%2F6oziTvm2bRF%2FmXBbpWRlBx3OaAA6zEDOS3fWS%2BPodUJVibdhSh9uFpN9mb667sY17iSw2MAkpKqdwUw9uS8zgY6pgFizW%2FdNKgQaGrn3hVYFg23BdrkLTSymiRs%2FQbKJrkati8%2FIZnQDMxD0jRofktk9VYCB1K6hM8fD0xZ9vRl1BdfocUGIG8%2Fa6n%2FAhdcHgWIVGBpORrfYAjHCskigdv5oUlzOGeEGaYnFCXCLSoBwboShqW5fIKRSeNNMIZAv3fcjnOLUMpdnXPGsUat5KlMEl1T5sux56WyGMDPahKMVntd5Kxy3wID&X-Amz-Signature=259b17497fa178e0cbfc83c773b05b44d4d4a70b5685fed1e404aa26b612e1e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGNQXHPH%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034649Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDxS%2Bub03FXg8WpmuHIh3v4rTHor4F8pVIJ7%2F9vM2MRNAiAGx9mxP1my%2BC78HU6MhxdXBK2lOcs6rIVpvqy65jfL9Sr%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMzSQtqCajwX9nKw%2B6KtwDkDEwz702cA4O66U0qCieWmXOcdV7pw49vU69MZ0bW6RStIaXmJXwpfSgX7bC6F1D4JCXMM2fjVHjnNZztodySoXCM%2FgLnEZZ9oBy7Wb4WrcMBX7jM4ngSwmizTpYQBc7YLHBbOqPy0OFBN9C8ZCN1azuFW2U05fnBWUtHBPYWoEKnATrlNxGfxwQkFo0CR7Yy4GSd4doYJYl5Zfmz16uAyCqAyLU8x3a%2Flsj0rfZh%2FX4Ycn4b3wLzubhJPjlQlsBgsvvWbe7mExhZ%2FS8O%2FA9hhVczFr51NYxwvUFgWdLZqlmTB5dseJxksnfyowqmcdsKz8veS%2FUFfSuXyTfI9w6B2VDrzM8kbRI%2BHGm%2FlIDiDm5mcKwXMQ5Wxhp7ZtQLPEs779uQdGJUBG4NtI%2FXHnmP4TVk86PLbwuuaC1VURBXMbxal9lyc6dVtilKvbFVkTxk%2FoUD1DrFfGQn%2BPhNaDDnK%2FfUDbZPjW7G9as36jRVh%2Bg7KiROP%2BGtq0%2F%2BOq7roW2RoW7DIAjElKyksRa8Xk%2Bq42e9ViQQ7KGCFvjRjXz2%2FHh%2F6oziTvm2bRF%2FmXBbpWRlBx3OaAA6zEDOS3fWS%2BPodUJVibdhSh9uFpN9mb667sY17iSw2MAkpKqdwUw9uS8zgY6pgFizW%2FdNKgQaGrn3hVYFg23BdrkLTSymiRs%2FQbKJrkati8%2FIZnQDMxD0jRofktk9VYCB1K6hM8fD0xZ9vRl1BdfocUGIG8%2Fa6n%2FAhdcHgWIVGBpORrfYAjHCskigdv5oUlzOGeEGaYnFCXCLSoBwboShqW5fIKRSeNNMIZAv3fcjnOLUMpdnXPGsUat5KlMEl1T5sux56WyGMDPahKMVntd5Kxy3wID&X-Amz-Signature=f91f33405c45620776d000692ad73b01798ed4650d7229196f1f54982d67afbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

