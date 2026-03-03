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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX4REEEX%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWq5okcEs%2FGQxgxMdDw7TBsWowpmrdpAxF657jVS5q1AiEA19LgcbOkTDPYAQ%2FoTERexHm9XdF7Ca%2BO0PzxBZkp2ksqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQty9Gnz1mbiKXKQyrcA2O9THdZ%2FhfiDUOELzAuD5i5JklsCm5YCy8MuADbxLW2OZ0ekPn%2B2Lp6%2BLrA%2BiG0HSKM8kmDIwwzKT10rNxGvHtCminoEWZ8Bp5PbIZFjNZ%2FQfiLgel4ei9c2kOUlgsnEtT15w6opMbCEYtSWsOQbFz7iBVIJzVjWm43b1YBH86NT5B3ze7PrOqu1HvOLmPJS9l6%2Bvxu1TkXmA6YA2UClRgud0ZAUyfLrcslp7FU7nODTYEmYeuPB%2FXl79m65YZ%2Foci818qfINipKBKwkqx63Z5%2BaZK1knr6jnhxd%2BJ9UhKVCsVgRlcocYFpCx8%2BV1hG3eO16kArHZ1YshQ5Mp%2BhqHzT7ezdAiIURul87zHglnSbCKEguPlKqBfnvIY6%2BSt%2B8izsSGjSsXsMhefTp4c3tdMMFKngEA28iDLXX57fMgwFgWOht9w1wT0UpeFVpUkwNPa4erBbTTfoqM53L8BIJXmdat%2F9ZYiCacr2pBiMwbABU%2BYmAp4uX8qUoj%2FLODMlSop4HW3%2Bdxci2Cqfj77g7QdUjTfzvYcpknr%2BvPG6Pl%2BQ9waCFULNLN7UowK538XbKprOhSsZN6VlrGqM3bU38UOtzvR8XXgaaUVwMG9yvkJanmFyxZFL6HDoAe6tMIK2mM0GOqUBOCqb1bvCZcDXQimGWsTrUF9MKTBuG9SXne1eURWuP8dZbGpbqRRBgrr6moV4SPW7mGFb6pk%2BBtfhiciO5NhaD8PQ0%2BIwv65%2FarWYAF11vJHchWXU2PSrjncWaGpXc3OD%2BQpFN9BDfcUiTkjDE%2FkDQpAvSmnXZ%2FArIO8kYhz60zo6LrW9RzUILGJ3NMtYG7qu7zye%2BVMafB%2ByJfSt58rgs6am3kM9&X-Amz-Signature=b85c5ae85f91abe5af7d81ce5de4d580eb4242c0f991a32a55fa2a73982a3548&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX4REEEX%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWq5okcEs%2FGQxgxMdDw7TBsWowpmrdpAxF657jVS5q1AiEA19LgcbOkTDPYAQ%2FoTERexHm9XdF7Ca%2BO0PzxBZkp2ksqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQty9Gnz1mbiKXKQyrcA2O9THdZ%2FhfiDUOELzAuD5i5JklsCm5YCy8MuADbxLW2OZ0ekPn%2B2Lp6%2BLrA%2BiG0HSKM8kmDIwwzKT10rNxGvHtCminoEWZ8Bp5PbIZFjNZ%2FQfiLgel4ei9c2kOUlgsnEtT15w6opMbCEYtSWsOQbFz7iBVIJzVjWm43b1YBH86NT5B3ze7PrOqu1HvOLmPJS9l6%2Bvxu1TkXmA6YA2UClRgud0ZAUyfLrcslp7FU7nODTYEmYeuPB%2FXl79m65YZ%2Foci818qfINipKBKwkqx63Z5%2BaZK1knr6jnhxd%2BJ9UhKVCsVgRlcocYFpCx8%2BV1hG3eO16kArHZ1YshQ5Mp%2BhqHzT7ezdAiIURul87zHglnSbCKEguPlKqBfnvIY6%2BSt%2B8izsSGjSsXsMhefTp4c3tdMMFKngEA28iDLXX57fMgwFgWOht9w1wT0UpeFVpUkwNPa4erBbTTfoqM53L8BIJXmdat%2F9ZYiCacr2pBiMwbABU%2BYmAp4uX8qUoj%2FLODMlSop4HW3%2Bdxci2Cqfj77g7QdUjTfzvYcpknr%2BvPG6Pl%2BQ9waCFULNLN7UowK538XbKprOhSsZN6VlrGqM3bU38UOtzvR8XXgaaUVwMG9yvkJanmFyxZFL6HDoAe6tMIK2mM0GOqUBOCqb1bvCZcDXQimGWsTrUF9MKTBuG9SXne1eURWuP8dZbGpbqRRBgrr6moV4SPW7mGFb6pk%2BBtfhiciO5NhaD8PQ0%2BIwv65%2FarWYAF11vJHchWXU2PSrjncWaGpXc3OD%2BQpFN9BDfcUiTkjDE%2FkDQpAvSmnXZ%2FArIO8kYhz60zo6LrW9RzUILGJ3NMtYG7qu7zye%2BVMafB%2ByJfSt58rgs6am3kM9&X-Amz-Signature=8d96f5b34110629ff2c7f255e6b09772c75f5b0db67501749c8280cc4fad4326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX4REEEX%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033515Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWq5okcEs%2FGQxgxMdDw7TBsWowpmrdpAxF657jVS5q1AiEA19LgcbOkTDPYAQ%2FoTERexHm9XdF7Ca%2BO0PzxBZkp2ksqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHQty9Gnz1mbiKXKQyrcA2O9THdZ%2FhfiDUOELzAuD5i5JklsCm5YCy8MuADbxLW2OZ0ekPn%2B2Lp6%2BLrA%2BiG0HSKM8kmDIwwzKT10rNxGvHtCminoEWZ8Bp5PbIZFjNZ%2FQfiLgel4ei9c2kOUlgsnEtT15w6opMbCEYtSWsOQbFz7iBVIJzVjWm43b1YBH86NT5B3ze7PrOqu1HvOLmPJS9l6%2Bvxu1TkXmA6YA2UClRgud0ZAUyfLrcslp7FU7nODTYEmYeuPB%2FXl79m65YZ%2Foci818qfINipKBKwkqx63Z5%2BaZK1knr6jnhxd%2BJ9UhKVCsVgRlcocYFpCx8%2BV1hG3eO16kArHZ1YshQ5Mp%2BhqHzT7ezdAiIURul87zHglnSbCKEguPlKqBfnvIY6%2BSt%2B8izsSGjSsXsMhefTp4c3tdMMFKngEA28iDLXX57fMgwFgWOht9w1wT0UpeFVpUkwNPa4erBbTTfoqM53L8BIJXmdat%2F9ZYiCacr2pBiMwbABU%2BYmAp4uX8qUoj%2FLODMlSop4HW3%2Bdxci2Cqfj77g7QdUjTfzvYcpknr%2BvPG6Pl%2BQ9waCFULNLN7UowK538XbKprOhSsZN6VlrGqM3bU38UOtzvR8XXgaaUVwMG9yvkJanmFyxZFL6HDoAe6tMIK2mM0GOqUBOCqb1bvCZcDXQimGWsTrUF9MKTBuG9SXne1eURWuP8dZbGpbqRRBgrr6moV4SPW7mGFb6pk%2BBtfhiciO5NhaD8PQ0%2BIwv65%2FarWYAF11vJHchWXU2PSrjncWaGpXc3OD%2BQpFN9BDfcUiTkjDE%2FkDQpAvSmnXZ%2FArIO8kYhz60zo6LrW9RzUILGJ3NMtYG7qu7zye%2BVMafB%2ByJfSt58rgs6am3kM9&X-Amz-Signature=19ea58e6e59680fcd72b8c62eddc920ee2ffc2c1eb9d1834d6f346bd06395fb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

