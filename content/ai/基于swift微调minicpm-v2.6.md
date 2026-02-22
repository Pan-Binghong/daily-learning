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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUEZN4EV%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAniLe%2FCjGOYvouoVsm6GHtif95YLgHw79hRe9x3eKimAiAE3%2FtTH3WzC%2Bz7VC%2Bs7B8tk%2F8hefm5kbF8UpV0QAIYICqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjnbs3ZG1ENsD0nCgKtwDQSm6sFiZ8mqvulHyp5xBnBdrMiNSZoX%2BRIJw3v6BsOX3IblX4weXc7h2Ain5drlbxDnFQYHMfKMtRg7Ijdu9wU2zaHaMKUmEp7zknGtbiU1noEhVV6Cnu1FRdhhjWO0bQDrfm5DBVkeaaHuNm%2F9StESto9Cyaq5wkgC9aarVhbMOOTgqKLbuASbCcql%2BggEZiVMrnnxM3src%2Fvuwu7j9iz9KAR3Ilvltig1FCmXV2qv6uRmX0fVq%2BTS8K5zsJYC%2BzwvFiKHorQhSJ8ZVeJgIMpmI3HtFKprnh4xshepWnBIkSy1JSzUjnz0XYrUpr6RMVzZZ5K48IsUyS8Lw1vdXjTB3Fhm2QMlVR4sdqiJm%2BiB7ObZBp3BrrAuR3XUdHm5pbY4MZEXPNOyyhI3FY9jEEO9he9hO0BXREXo%2Bbf3xS2DLgtM7Rus2HY4JB4pV3TIfdb%2BVX3P5TtWRIGXeCULew%2FhtJGZI6F5ECm1bQUwYfRSx6%2BWYoOYg4GXaHkncvb8s3FYALbSC6BKIpIu%2BqgwygKaKcAgWjw7%2BpuuRoAGaMfu5Y6nPvR5lXfHWTeeKqqa3KaUqUPc50PuA5ZDoeoXx%2F1iy%2FDLYhPB9EIZDONUQgFdIpiAX%2FLAvSApvfBcw7czpzAY6pgEbB0NR3aErPSt7KXPl3kWBiF%2FGPNzXi7RlHnjHu0WqxrbNNZFzueXIETgARUppyR2eSmV9pyeclPW%2F4KnOGjRJZY4hM9d3VAOQg2UVSJXp1Fd5STvTVs79UDe0yM9e3ujMIK0ZGP7ZpvJnyawHJaJbl%2FbM3dXsD3tkTtDAuUgACecN%2BpocigHPQIcda%2FS2BqCCX6wYA0LZeGtmMULVDtsw8Qp3B43z&X-Amz-Signature=b98f1428670ae8d7e95422b62045785efe1f9af6b093bc38607e6776b7761c44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUEZN4EV%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAniLe%2FCjGOYvouoVsm6GHtif95YLgHw79hRe9x3eKimAiAE3%2FtTH3WzC%2Bz7VC%2Bs7B8tk%2F8hefm5kbF8UpV0QAIYICqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjnbs3ZG1ENsD0nCgKtwDQSm6sFiZ8mqvulHyp5xBnBdrMiNSZoX%2BRIJw3v6BsOX3IblX4weXc7h2Ain5drlbxDnFQYHMfKMtRg7Ijdu9wU2zaHaMKUmEp7zknGtbiU1noEhVV6Cnu1FRdhhjWO0bQDrfm5DBVkeaaHuNm%2F9StESto9Cyaq5wkgC9aarVhbMOOTgqKLbuASbCcql%2BggEZiVMrnnxM3src%2Fvuwu7j9iz9KAR3Ilvltig1FCmXV2qv6uRmX0fVq%2BTS8K5zsJYC%2BzwvFiKHorQhSJ8ZVeJgIMpmI3HtFKprnh4xshepWnBIkSy1JSzUjnz0XYrUpr6RMVzZZ5K48IsUyS8Lw1vdXjTB3Fhm2QMlVR4sdqiJm%2BiB7ObZBp3BrrAuR3XUdHm5pbY4MZEXPNOyyhI3FY9jEEO9he9hO0BXREXo%2Bbf3xS2DLgtM7Rus2HY4JB4pV3TIfdb%2BVX3P5TtWRIGXeCULew%2FhtJGZI6F5ECm1bQUwYfRSx6%2BWYoOYg4GXaHkncvb8s3FYALbSC6BKIpIu%2BqgwygKaKcAgWjw7%2BpuuRoAGaMfu5Y6nPvR5lXfHWTeeKqqa3KaUqUPc50PuA5ZDoeoXx%2F1iy%2FDLYhPB9EIZDONUQgFdIpiAX%2FLAvSApvfBcw7czpzAY6pgEbB0NR3aErPSt7KXPl3kWBiF%2FGPNzXi7RlHnjHu0WqxrbNNZFzueXIETgARUppyR2eSmV9pyeclPW%2F4KnOGjRJZY4hM9d3VAOQg2UVSJXp1Fd5STvTVs79UDe0yM9e3ujMIK0ZGP7ZpvJnyawHJaJbl%2FbM3dXsD3tkTtDAuUgACecN%2BpocigHPQIcda%2FS2BqCCX6wYA0LZeGtmMULVDtsw8Qp3B43z&X-Amz-Signature=69266ba8e1fff80e27880199b293a3084fd88f8cebc9dee9c98a023d919a74ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUEZN4EV%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033740Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAniLe%2FCjGOYvouoVsm6GHtif95YLgHw79hRe9x3eKimAiAE3%2FtTH3WzC%2Bz7VC%2Bs7B8tk%2F8hefm5kbF8UpV0QAIYICqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjnbs3ZG1ENsD0nCgKtwDQSm6sFiZ8mqvulHyp5xBnBdrMiNSZoX%2BRIJw3v6BsOX3IblX4weXc7h2Ain5drlbxDnFQYHMfKMtRg7Ijdu9wU2zaHaMKUmEp7zknGtbiU1noEhVV6Cnu1FRdhhjWO0bQDrfm5DBVkeaaHuNm%2F9StESto9Cyaq5wkgC9aarVhbMOOTgqKLbuASbCcql%2BggEZiVMrnnxM3src%2Fvuwu7j9iz9KAR3Ilvltig1FCmXV2qv6uRmX0fVq%2BTS8K5zsJYC%2BzwvFiKHorQhSJ8ZVeJgIMpmI3HtFKprnh4xshepWnBIkSy1JSzUjnz0XYrUpr6RMVzZZ5K48IsUyS8Lw1vdXjTB3Fhm2QMlVR4sdqiJm%2BiB7ObZBp3BrrAuR3XUdHm5pbY4MZEXPNOyyhI3FY9jEEO9he9hO0BXREXo%2Bbf3xS2DLgtM7Rus2HY4JB4pV3TIfdb%2BVX3P5TtWRIGXeCULew%2FhtJGZI6F5ECm1bQUwYfRSx6%2BWYoOYg4GXaHkncvb8s3FYALbSC6BKIpIu%2BqgwygKaKcAgWjw7%2BpuuRoAGaMfu5Y6nPvR5lXfHWTeeKqqa3KaUqUPc50PuA5ZDoeoXx%2F1iy%2FDLYhPB9EIZDONUQgFdIpiAX%2FLAvSApvfBcw7czpzAY6pgEbB0NR3aErPSt7KXPl3kWBiF%2FGPNzXi7RlHnjHu0WqxrbNNZFzueXIETgARUppyR2eSmV9pyeclPW%2F4KnOGjRJZY4hM9d3VAOQg2UVSJXp1Fd5STvTVs79UDe0yM9e3ujMIK0ZGP7ZpvJnyawHJaJbl%2FbM3dXsD3tkTtDAuUgACecN%2BpocigHPQIcda%2FS2BqCCX6wYA0LZeGtmMULVDtsw8Qp3B43z&X-Amz-Signature=4ec21d801ce5ae9fbee788aed817a85fd93f9a0ff6d79b208433e3f4d5e43759&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

