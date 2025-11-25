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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOC2YHN%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAIy6%2B2biBnwWmkyNaqWzF91bQIDommCNyDeW003%2FIb3AiEA47ltZsLmSfC9yySDcZYOY5JFoUIECbHEKkUeJc79zxQq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJMvHKQBvvbB%2F45fgyrcA%2BI%2FmzJTopYRAAor%2BuZpx5zX9pcgUcje2SaHmWFKqJdcL%2BT62eYY%2B%2F%2FFAMc%2B7vPuWl1kc9%2BLOOw%2F%2BOzPllsL2EOaFBcT5NE7kR%2Fi%2BbJw%2Bfxz1sngKFsDVSv7uAJr3Z4W5YlS%2BY1%2BDfO8GML6pIoA2PxHEA6nvGM4Q2YRxZVlq8YGE1Fj5T%2F28qUnGxjsx%2FGobBdyrYoWDfYfmOOjJL6hZIVWQ7zpL%2FKxBMRYhtceusdUbpqwP5aJsLrM%2BBeRcRqr5RzxiTHd6fmCXTNyNF%2FXQkcYseztomF4vczDmANYnSnI3kmZgsJMwqvR6r7mUxvnlzeAeJbJJV%2F%2BTLgxoS%2FlD3pIScGrIp4cCK9O76WaKrc%2BRFmX67nlPPOQZpN0WG3fnuVotCsQfzUkw4avCCbTlY1tzXMyAo5MQUKcuGYRCKV6KAJAIFhvbR3bH4gi7Zn1V%2F6zpnaFUuyvn3syxImL%2FWU1ycUzCb46RUJbKrGYnWbudOpuBE0tPyFBIBoHtpvPB6XdeWagDk%2FIeVU4RsOUVHP2h%2FKltZVYOglSI9LKp5rWp%2BkcRRU%2BIX4DsH%2FZuuxxx1%2F5m5kYps2GSUvPSjen0cWwuX%2F%2BywfngnPJImd046AwDgQKFowhI75jfHb5MPmslMkGOqUBvsDF04uHAoN9AO6vylRpLTa9IZdB0q3W2mM8e810YoiFfQXO2sow7UvGj3GQx%2FEzA%2BTI5gPfJxblVqOEGcOIG8NuALvcihMTqVZUDUX6Jw1vsQxW6OrviMqpN5x9tfUtwqE7K8KQM5Zc7YpzY86F6G7IlwhJ5dfkkf8vnVr4jZTVc9vYdbMBcnVaIQGMZ7xQF6ze%2BLvjzd%2FoCczn1e7qRkwIuKwo&X-Amz-Signature=9a0f8dcefb14d5d4b13656c9d720c0a91e05683c5af1260c6ae368c8f29786d2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOC2YHN%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAIy6%2B2biBnwWmkyNaqWzF91bQIDommCNyDeW003%2FIb3AiEA47ltZsLmSfC9yySDcZYOY5JFoUIECbHEKkUeJc79zxQq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJMvHKQBvvbB%2F45fgyrcA%2BI%2FmzJTopYRAAor%2BuZpx5zX9pcgUcje2SaHmWFKqJdcL%2BT62eYY%2B%2F%2FFAMc%2B7vPuWl1kc9%2BLOOw%2F%2BOzPllsL2EOaFBcT5NE7kR%2Fi%2BbJw%2Bfxz1sngKFsDVSv7uAJr3Z4W5YlS%2BY1%2BDfO8GML6pIoA2PxHEA6nvGM4Q2YRxZVlq8YGE1Fj5T%2F28qUnGxjsx%2FGobBdyrYoWDfYfmOOjJL6hZIVWQ7zpL%2FKxBMRYhtceusdUbpqwP5aJsLrM%2BBeRcRqr5RzxiTHd6fmCXTNyNF%2FXQkcYseztomF4vczDmANYnSnI3kmZgsJMwqvR6r7mUxvnlzeAeJbJJV%2F%2BTLgxoS%2FlD3pIScGrIp4cCK9O76WaKrc%2BRFmX67nlPPOQZpN0WG3fnuVotCsQfzUkw4avCCbTlY1tzXMyAo5MQUKcuGYRCKV6KAJAIFhvbR3bH4gi7Zn1V%2F6zpnaFUuyvn3syxImL%2FWU1ycUzCb46RUJbKrGYnWbudOpuBE0tPyFBIBoHtpvPB6XdeWagDk%2FIeVU4RsOUVHP2h%2FKltZVYOglSI9LKp5rWp%2BkcRRU%2BIX4DsH%2FZuuxxx1%2F5m5kYps2GSUvPSjen0cWwuX%2F%2BywfngnPJImd046AwDgQKFowhI75jfHb5MPmslMkGOqUBvsDF04uHAoN9AO6vylRpLTa9IZdB0q3W2mM8e810YoiFfQXO2sow7UvGj3GQx%2FEzA%2BTI5gPfJxblVqOEGcOIG8NuALvcihMTqVZUDUX6Jw1vsQxW6OrviMqpN5x9tfUtwqE7K8KQM5Zc7YpzY86F6G7IlwhJ5dfkkf8vnVr4jZTVc9vYdbMBcnVaIQGMZ7xQF6ze%2BLvjzd%2FoCczn1e7qRkwIuKwo&X-Amz-Signature=973c52a0dc0b286b7e3976e0027f8aa995ade318ef0be852645ddb3d9e1dc970&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFOC2YHN%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAIy6%2B2biBnwWmkyNaqWzF91bQIDommCNyDeW003%2FIb3AiEA47ltZsLmSfC9yySDcZYOY5JFoUIECbHEKkUeJc79zxQq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDJMvHKQBvvbB%2F45fgyrcA%2BI%2FmzJTopYRAAor%2BuZpx5zX9pcgUcje2SaHmWFKqJdcL%2BT62eYY%2B%2F%2FFAMc%2B7vPuWl1kc9%2BLOOw%2F%2BOzPllsL2EOaFBcT5NE7kR%2Fi%2BbJw%2Bfxz1sngKFsDVSv7uAJr3Z4W5YlS%2BY1%2BDfO8GML6pIoA2PxHEA6nvGM4Q2YRxZVlq8YGE1Fj5T%2F28qUnGxjsx%2FGobBdyrYoWDfYfmOOjJL6hZIVWQ7zpL%2FKxBMRYhtceusdUbpqwP5aJsLrM%2BBeRcRqr5RzxiTHd6fmCXTNyNF%2FXQkcYseztomF4vczDmANYnSnI3kmZgsJMwqvR6r7mUxvnlzeAeJbJJV%2F%2BTLgxoS%2FlD3pIScGrIp4cCK9O76WaKrc%2BRFmX67nlPPOQZpN0WG3fnuVotCsQfzUkw4avCCbTlY1tzXMyAo5MQUKcuGYRCKV6KAJAIFhvbR3bH4gi7Zn1V%2F6zpnaFUuyvn3syxImL%2FWU1ycUzCb46RUJbKrGYnWbudOpuBE0tPyFBIBoHtpvPB6XdeWagDk%2FIeVU4RsOUVHP2h%2FKltZVYOglSI9LKp5rWp%2BkcRRU%2BIX4DsH%2FZuuxxx1%2F5m5kYps2GSUvPSjen0cWwuX%2F%2BywfngnPJImd046AwDgQKFowhI75jfHb5MPmslMkGOqUBvsDF04uHAoN9AO6vylRpLTa9IZdB0q3W2mM8e810YoiFfQXO2sow7UvGj3GQx%2FEzA%2BTI5gPfJxblVqOEGcOIG8NuALvcihMTqVZUDUX6Jw1vsQxW6OrviMqpN5x9tfUtwqE7K8KQM5Zc7YpzY86F6G7IlwhJ5dfkkf8vnVr4jZTVc9vYdbMBcnVaIQGMZ7xQF6ze%2BLvjzd%2FoCczn1e7qRkwIuKwo&X-Amz-Signature=b8031f7b0025cb8170e1ae43d05b047955ee5492e45fb84f33f19773db2de6d0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

