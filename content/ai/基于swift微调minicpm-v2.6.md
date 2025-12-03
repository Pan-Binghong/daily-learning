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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAQTJVBI%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICXBChcsNwJ0pY0Yjl7h1kUAfvYvHYMPh%2FIBEZS3FEF6AiEA7QCqBEE69AVh8HVw7H8QTbdEXvkBIibhpV9hJyk0ouUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDLUa0q%2F%2BjklwKLsgHyrcA5484sqGUkDWaFx23396Fhhhu%2BccoMOZM7bLofoIvlloYyBNeFtZD%2Fq8MP8fIb%2F9KDMhoedLNuZjhKEVHBEN0Ru6W35R2yrb%2BtCxNGWJl2wyQY2eJFtrWaZNDP9vpDx9fiXkwQmc6UZ7jllGCAo9j1d4%2BihFnk7GAFA3J7o6BRAw9Lhaxu%2B3KnlXAtP6C%2Bc29cEMSomRAv901YXNJJV8%2F2%2BvxSMAAC5BfkWE%2B3rz%2Fm6HMSYN9r%2FAc%2BMCL9abYRGlDexcesdrN4WSjiTrFKEyk6GnWGysSKyLMaQRj571rwkowK3tXLpnbXzLwojDguPMG0mz7VuKD%2BbruM3xTXyfut2xzH3SWvwww6FiHA8OPv8j3YHUjMs%2BTBpFSNFyWAfzF3gSvkYxw3JKk%2FJoi7qWJtCbO%2FWzb7rdwU0ohaS9qVK3sf2VxKxmOEaGcUrW9L5uDvRHF0itIFZt0OSFkXtqYy901Tio7VwGhAPf%2BXe2gZ124qwkrGFPPl1Nt7Ajs3izrho6YvWKWX76j6NwQbJp%2B%2BSDYK4s1Rx9fSYlt4vrqSb6jgEZlB%2FAqbHMu2Xya8S8Xonn9Q64xolTVupXV07izP8s29lTU9Es7kd43JCfWJvGNsAe74fBmdHRoCRuMNWWvskGOqUBzaw99JP6tYTvfhtPtfZruZ%2BalhfcWYWzvSqo5%2FObnZgTYbXd%2FubPV695%2Bjvr6AqypRCyWsdBWOq42rJgTtQoKZWE9UfRQcOasJdrrnuHGOF8yrg1ydUGl1p5L3tFzUIxoXhRXnWRRMiXprI%2FMz6bNKJgnmLy6dCHVABZILGpOyb%2FvsosdqfyX1s9ixLpnGYMNXaHkiOv2%2B2l6EXVALGPkm8ypZRv&X-Amz-Signature=9319f2ec50164d036146b338c0cfa1a75995853d439b9fb4a17d512c930042f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAQTJVBI%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICXBChcsNwJ0pY0Yjl7h1kUAfvYvHYMPh%2FIBEZS3FEF6AiEA7QCqBEE69AVh8HVw7H8QTbdEXvkBIibhpV9hJyk0ouUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDLUa0q%2F%2BjklwKLsgHyrcA5484sqGUkDWaFx23396Fhhhu%2BccoMOZM7bLofoIvlloYyBNeFtZD%2Fq8MP8fIb%2F9KDMhoedLNuZjhKEVHBEN0Ru6W35R2yrb%2BtCxNGWJl2wyQY2eJFtrWaZNDP9vpDx9fiXkwQmc6UZ7jllGCAo9j1d4%2BihFnk7GAFA3J7o6BRAw9Lhaxu%2B3KnlXAtP6C%2Bc29cEMSomRAv901YXNJJV8%2F2%2BvxSMAAC5BfkWE%2B3rz%2Fm6HMSYN9r%2FAc%2BMCL9abYRGlDexcesdrN4WSjiTrFKEyk6GnWGysSKyLMaQRj571rwkowK3tXLpnbXzLwojDguPMG0mz7VuKD%2BbruM3xTXyfut2xzH3SWvwww6FiHA8OPv8j3YHUjMs%2BTBpFSNFyWAfzF3gSvkYxw3JKk%2FJoi7qWJtCbO%2FWzb7rdwU0ohaS9qVK3sf2VxKxmOEaGcUrW9L5uDvRHF0itIFZt0OSFkXtqYy901Tio7VwGhAPf%2BXe2gZ124qwkrGFPPl1Nt7Ajs3izrho6YvWKWX76j6NwQbJp%2B%2BSDYK4s1Rx9fSYlt4vrqSb6jgEZlB%2FAqbHMu2Xya8S8Xonn9Q64xolTVupXV07izP8s29lTU9Es7kd43JCfWJvGNsAe74fBmdHRoCRuMNWWvskGOqUBzaw99JP6tYTvfhtPtfZruZ%2BalhfcWYWzvSqo5%2FObnZgTYbXd%2FubPV695%2Bjvr6AqypRCyWsdBWOq42rJgTtQoKZWE9UfRQcOasJdrrnuHGOF8yrg1ydUGl1p5L3tFzUIxoXhRXnWRRMiXprI%2FMz6bNKJgnmLy6dCHVABZILGpOyb%2FvsosdqfyX1s9ixLpnGYMNXaHkiOv2%2B2l6EXVALGPkm8ypZRv&X-Amz-Signature=5048f520e5983cab5fea9740fc2376a3425150d5169728deeb1c5f2ce590bc1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAQTJVBI%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCICXBChcsNwJ0pY0Yjl7h1kUAfvYvHYMPh%2FIBEZS3FEF6AiEA7QCqBEE69AVh8HVw7H8QTbdEXvkBIibhpV9hJyk0ouUq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDLUa0q%2F%2BjklwKLsgHyrcA5484sqGUkDWaFx23396Fhhhu%2BccoMOZM7bLofoIvlloYyBNeFtZD%2Fq8MP8fIb%2F9KDMhoedLNuZjhKEVHBEN0Ru6W35R2yrb%2BtCxNGWJl2wyQY2eJFtrWaZNDP9vpDx9fiXkwQmc6UZ7jllGCAo9j1d4%2BihFnk7GAFA3J7o6BRAw9Lhaxu%2B3KnlXAtP6C%2Bc29cEMSomRAv901YXNJJV8%2F2%2BvxSMAAC5BfkWE%2B3rz%2Fm6HMSYN9r%2FAc%2BMCL9abYRGlDexcesdrN4WSjiTrFKEyk6GnWGysSKyLMaQRj571rwkowK3tXLpnbXzLwojDguPMG0mz7VuKD%2BbruM3xTXyfut2xzH3SWvwww6FiHA8OPv8j3YHUjMs%2BTBpFSNFyWAfzF3gSvkYxw3JKk%2FJoi7qWJtCbO%2FWzb7rdwU0ohaS9qVK3sf2VxKxmOEaGcUrW9L5uDvRHF0itIFZt0OSFkXtqYy901Tio7VwGhAPf%2BXe2gZ124qwkrGFPPl1Nt7Ajs3izrho6YvWKWX76j6NwQbJp%2B%2BSDYK4s1Rx9fSYlt4vrqSb6jgEZlB%2FAqbHMu2Xya8S8Xonn9Q64xolTVupXV07izP8s29lTU9Es7kd43JCfWJvGNsAe74fBmdHRoCRuMNWWvskGOqUBzaw99JP6tYTvfhtPtfZruZ%2BalhfcWYWzvSqo5%2FObnZgTYbXd%2FubPV695%2Bjvr6AqypRCyWsdBWOq42rJgTtQoKZWE9UfRQcOasJdrrnuHGOF8yrg1ydUGl1p5L3tFzUIxoXhRXnWRRMiXprI%2FMz6bNKJgnmLy6dCHVABZILGpOyb%2FvsosdqfyX1s9ixLpnGYMNXaHkiOv2%2B2l6EXVALGPkm8ypZRv&X-Amz-Signature=da3ae2e78449db1d94f28df9df99c41fe1907afd5d7bc7d5c70fc32644dd3924&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

