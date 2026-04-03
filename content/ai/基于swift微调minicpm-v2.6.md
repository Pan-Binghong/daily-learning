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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632RHCCAI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdGdC751xry1X8KIesMxijcHsntLem3ugE5EZIJPd%2BMgIhAKhiJjX4otyT4L2wkPhvGNnos5aZicgDnV3phhl9Nh3bKv8DCH8QABoMNjM3NDIzMTgzODA1IgxNVUlx59%2BufrGgN6Uq3AOsspwYYqQ%2B1imQq7keCJRQH9rBvbqEZg1yhM%2F9bGhStbD3Ioc7ubwsm7AFPrx9DOjEyaHp7aU96S7vvesWccaKwXhhAJmxXl4ZRY1Tj4SaR0ksWXX6SBiMUqBGSu1uv4aeOTJ4GynBHTrwLqcqpENlJn2LIxMD3OXKkZ%2BYyhciQeEYzxljyCnZU5QbWob%2Flim6uID6%2FvooU3p2xY%2FjZksERBr8dUp3hj3vn8FA4K46Xsa9ktkLSZZtt37Z4BkLg%2FNMa2J3ReVTC3ilyiMLf2%2FdrpeVmYs3lrR3HovuzckpIhYz%2FKa9d83R3S0z3Fpwx2CSN1JO91%2Ffdw2COul1kmF%2BxQoBmrttSqYnqPuB71FLxCe7meGICzHWTg3wsgDy9RfUPix7t3zMS2D28xEjA6ANacC4td%2BuZD%2BfXASAsEdtsiRW7t23YKk09pPXUxaN57bcTjEef7RIzDYULsRdN9Ao3oWiZjYtx3BJP9SOF4lOdLTP%2BGexxXgBSu8u8eUGIPUV4hrRWOkWRz4SVAxiEjtfH%2Bmy6A4iCAwZZVKjcn6XkVti%2F8sQNySBsIn3lyspY9DfnRobn8lPsq8lZNga0PxwEYxMeku9gLFJ%2FgHQ1vlocerbgHJbsMRokmuMEjDaq73OBjqkAeA5q6tYa%2BVz44a2xWnPaQkUEFTVVhnpWr%2BsmMZi4j4DUJhaizU3pydOgJu%2FoGZnPMYADOXHlOSX3ilmCROnRPWHQuXRtefqAFdX97iaBT%2B3XtJWdnVM83U6Dek%2FBkmMWnjQ%2BwWyPVgium9SqVPPK1WlmpxQreSFjwxf%2BsPae62C4yOWyTZ7OhRIhEbH9ZsOMugy%2FecZmnvQCuzYUQpNH5S4lc0g&X-Amz-Signature=eb739045fa2c30051fc1ac9b6b88ad32a158e2cab2a312e73b4b9807b57b2d89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632RHCCAI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdGdC751xry1X8KIesMxijcHsntLem3ugE5EZIJPd%2BMgIhAKhiJjX4otyT4L2wkPhvGNnos5aZicgDnV3phhl9Nh3bKv8DCH8QABoMNjM3NDIzMTgzODA1IgxNVUlx59%2BufrGgN6Uq3AOsspwYYqQ%2B1imQq7keCJRQH9rBvbqEZg1yhM%2F9bGhStbD3Ioc7ubwsm7AFPrx9DOjEyaHp7aU96S7vvesWccaKwXhhAJmxXl4ZRY1Tj4SaR0ksWXX6SBiMUqBGSu1uv4aeOTJ4GynBHTrwLqcqpENlJn2LIxMD3OXKkZ%2BYyhciQeEYzxljyCnZU5QbWob%2Flim6uID6%2FvooU3p2xY%2FjZksERBr8dUp3hj3vn8FA4K46Xsa9ktkLSZZtt37Z4BkLg%2FNMa2J3ReVTC3ilyiMLf2%2FdrpeVmYs3lrR3HovuzckpIhYz%2FKa9d83R3S0z3Fpwx2CSN1JO91%2Ffdw2COul1kmF%2BxQoBmrttSqYnqPuB71FLxCe7meGICzHWTg3wsgDy9RfUPix7t3zMS2D28xEjA6ANacC4td%2BuZD%2BfXASAsEdtsiRW7t23YKk09pPXUxaN57bcTjEef7RIzDYULsRdN9Ao3oWiZjYtx3BJP9SOF4lOdLTP%2BGexxXgBSu8u8eUGIPUV4hrRWOkWRz4SVAxiEjtfH%2Bmy6A4iCAwZZVKjcn6XkVti%2F8sQNySBsIn3lyspY9DfnRobn8lPsq8lZNga0PxwEYxMeku9gLFJ%2FgHQ1vlocerbgHJbsMRokmuMEjDaq73OBjqkAeA5q6tYa%2BVz44a2xWnPaQkUEFTVVhnpWr%2BsmMZi4j4DUJhaizU3pydOgJu%2FoGZnPMYADOXHlOSX3ilmCROnRPWHQuXRtefqAFdX97iaBT%2B3XtJWdnVM83U6Dek%2FBkmMWnjQ%2BwWyPVgium9SqVPPK1WlmpxQreSFjwxf%2BsPae62C4yOWyTZ7OhRIhEbH9ZsOMugy%2FecZmnvQCuzYUQpNH5S4lc0g&X-Amz-Signature=86f1e3a55a3a425eb99766a760d178763f3a925dbc6fa18cf958bda60bc1de13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632RHCCAI%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdGdC751xry1X8KIesMxijcHsntLem3ugE5EZIJPd%2BMgIhAKhiJjX4otyT4L2wkPhvGNnos5aZicgDnV3phhl9Nh3bKv8DCH8QABoMNjM3NDIzMTgzODA1IgxNVUlx59%2BufrGgN6Uq3AOsspwYYqQ%2B1imQq7keCJRQH9rBvbqEZg1yhM%2F9bGhStbD3Ioc7ubwsm7AFPrx9DOjEyaHp7aU96S7vvesWccaKwXhhAJmxXl4ZRY1Tj4SaR0ksWXX6SBiMUqBGSu1uv4aeOTJ4GynBHTrwLqcqpENlJn2LIxMD3OXKkZ%2BYyhciQeEYzxljyCnZU5QbWob%2Flim6uID6%2FvooU3p2xY%2FjZksERBr8dUp3hj3vn8FA4K46Xsa9ktkLSZZtt37Z4BkLg%2FNMa2J3ReVTC3ilyiMLf2%2FdrpeVmYs3lrR3HovuzckpIhYz%2FKa9d83R3S0z3Fpwx2CSN1JO91%2Ffdw2COul1kmF%2BxQoBmrttSqYnqPuB71FLxCe7meGICzHWTg3wsgDy9RfUPix7t3zMS2D28xEjA6ANacC4td%2BuZD%2BfXASAsEdtsiRW7t23YKk09pPXUxaN57bcTjEef7RIzDYULsRdN9Ao3oWiZjYtx3BJP9SOF4lOdLTP%2BGexxXgBSu8u8eUGIPUV4hrRWOkWRz4SVAxiEjtfH%2Bmy6A4iCAwZZVKjcn6XkVti%2F8sQNySBsIn3lyspY9DfnRobn8lPsq8lZNga0PxwEYxMeku9gLFJ%2FgHQ1vlocerbgHJbsMRokmuMEjDaq73OBjqkAeA5q6tYa%2BVz44a2xWnPaQkUEFTVVhnpWr%2BsmMZi4j4DUJhaizU3pydOgJu%2FoGZnPMYADOXHlOSX3ilmCROnRPWHQuXRtefqAFdX97iaBT%2B3XtJWdnVM83U6Dek%2FBkmMWnjQ%2BwWyPVgium9SqVPPK1WlmpxQreSFjwxf%2BsPae62C4yOWyTZ7OhRIhEbH9ZsOMugy%2FecZmnvQCuzYUQpNH5S4lc0g&X-Amz-Signature=3d640a4a7501dcdb526bd97a902c75d2acbe573c401cc4a8db8633bb7588fa4f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

