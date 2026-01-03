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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXYCRVKA%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCICdVMFcMIh4lSqWUGrkLUoOc4xG3IGpjDJwZ4DHivUrFAiEAkJEekWW%2FT7yoOvzZq1aGyykrn3Ab%2FgwSFikiC6IjHnIq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDGtQr7K4rfSpDbXiUCrcA3aqKhh6aitWLbPWQeXjAYjHWsoPvfppaXKdUsrp0BsNS5sbDesh%2FVZdBxln%2ByP5s1TCqRAHJnBgy%2FB3Pgq0GlVIBfJ16UhE7yIm0JUqQDuY75NQs6BHHMDuxT2qrakaJ%2BAJIQoh75GqKS%2Bp3XB4CWamaQoHL8E8u1RP6z8fOFy6b9oZ7ZOEMyobmqry%2BPn5D51c95NZsMY6NQDPlTGxV%2F9p9M9qT%2BWj9cC8LOojIfl7oFqvycmWdr3UZnPnx088ZPPJCavQqhAqfw0XAbzOBvpQ9fNk83DCmzscPZUY%2Bm7W40O%2BlQzhvwOuNLES8cOC49GEgoe5BQdZMpWRdg7gAzb6%2FLf8i1HO5UhxUhoNUIj3WeN8uKh8GzY4AirnegC6p3GTayIVfQCTuEH6pbv%2BlSAg7zVId5953Fx58lCzWQ89DYJdIi%2F67TnXB%2BBJQoclbc1yskR8CZSO2rtcrpL6glGDhkfbYy%2BHbssNxDDpNWQRLtb2QFfw37fHcYYH2azSjxofkBAEUSBklg4F1FieoqwYIZ5JFYFUQdMpAdiX%2BVQjBZPSf%2Fz%2FaYqd79Z8rx%2FVeCVORWsVKC1vMrj3d9w7DwdJuY3eWAJImasyn7Vqbrr%2BBnqoQ2c5inMvWwfKMND04coGOqUBKpsdv%2B%2Ft4eVuqU025Rg8GAYSrgGhGdtOV%2Fzn%2F%2BawwK00RWZ7wlyQvwbZvPSAwh9etXS2ne2Uz2tIoGPS5CVIbW7ZChxkEl4QRR21FLpUc6TPNH5uAz4vV%2Bh9F8luqvoINY6Lxgv5Oa121Owq%2FQM2q1gon%2BorQmcZMb9hGI7L4HkfAKdPdVJmddRPakGBBwEZ2iZI5pxZKKPhHVHXB3sUca6hjp02&X-Amz-Signature=2c0f6b8947590a6591a7adc37e67927b0af0156681add4bfc6b5c8526f5451ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXYCRVKA%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCICdVMFcMIh4lSqWUGrkLUoOc4xG3IGpjDJwZ4DHivUrFAiEAkJEekWW%2FT7yoOvzZq1aGyykrn3Ab%2FgwSFikiC6IjHnIq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDGtQr7K4rfSpDbXiUCrcA3aqKhh6aitWLbPWQeXjAYjHWsoPvfppaXKdUsrp0BsNS5sbDesh%2FVZdBxln%2ByP5s1TCqRAHJnBgy%2FB3Pgq0GlVIBfJ16UhE7yIm0JUqQDuY75NQs6BHHMDuxT2qrakaJ%2BAJIQoh75GqKS%2Bp3XB4CWamaQoHL8E8u1RP6z8fOFy6b9oZ7ZOEMyobmqry%2BPn5D51c95NZsMY6NQDPlTGxV%2F9p9M9qT%2BWj9cC8LOojIfl7oFqvycmWdr3UZnPnx088ZPPJCavQqhAqfw0XAbzOBvpQ9fNk83DCmzscPZUY%2Bm7W40O%2BlQzhvwOuNLES8cOC49GEgoe5BQdZMpWRdg7gAzb6%2FLf8i1HO5UhxUhoNUIj3WeN8uKh8GzY4AirnegC6p3GTayIVfQCTuEH6pbv%2BlSAg7zVId5953Fx58lCzWQ89DYJdIi%2F67TnXB%2BBJQoclbc1yskR8CZSO2rtcrpL6glGDhkfbYy%2BHbssNxDDpNWQRLtb2QFfw37fHcYYH2azSjxofkBAEUSBklg4F1FieoqwYIZ5JFYFUQdMpAdiX%2BVQjBZPSf%2Fz%2FaYqd79Z8rx%2FVeCVORWsVKC1vMrj3d9w7DwdJuY3eWAJImasyn7Vqbrr%2BBnqoQ2c5inMvWwfKMND04coGOqUBKpsdv%2B%2Ft4eVuqU025Rg8GAYSrgGhGdtOV%2Fzn%2F%2BawwK00RWZ7wlyQvwbZvPSAwh9etXS2ne2Uz2tIoGPS5CVIbW7ZChxkEl4QRR21FLpUc6TPNH5uAz4vV%2Bh9F8luqvoINY6Lxgv5Oa121Owq%2FQM2q1gon%2BorQmcZMb9hGI7L4HkfAKdPdVJmddRPakGBBwEZ2iZI5pxZKKPhHVHXB3sUca6hjp02&X-Amz-Signature=b7e1677c0e334299124312769bbafae31a0a9fdb1aeb044b0959a1ac1332a738&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXYCRVKA%2F20260103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260103T025108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCICdVMFcMIh4lSqWUGrkLUoOc4xG3IGpjDJwZ4DHivUrFAiEAkJEekWW%2FT7yoOvzZq1aGyykrn3Ab%2FgwSFikiC6IjHnIq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDGtQr7K4rfSpDbXiUCrcA3aqKhh6aitWLbPWQeXjAYjHWsoPvfppaXKdUsrp0BsNS5sbDesh%2FVZdBxln%2ByP5s1TCqRAHJnBgy%2FB3Pgq0GlVIBfJ16UhE7yIm0JUqQDuY75NQs6BHHMDuxT2qrakaJ%2BAJIQoh75GqKS%2Bp3XB4CWamaQoHL8E8u1RP6z8fOFy6b9oZ7ZOEMyobmqry%2BPn5D51c95NZsMY6NQDPlTGxV%2F9p9M9qT%2BWj9cC8LOojIfl7oFqvycmWdr3UZnPnx088ZPPJCavQqhAqfw0XAbzOBvpQ9fNk83DCmzscPZUY%2Bm7W40O%2BlQzhvwOuNLES8cOC49GEgoe5BQdZMpWRdg7gAzb6%2FLf8i1HO5UhxUhoNUIj3WeN8uKh8GzY4AirnegC6p3GTayIVfQCTuEH6pbv%2BlSAg7zVId5953Fx58lCzWQ89DYJdIi%2F67TnXB%2BBJQoclbc1yskR8CZSO2rtcrpL6glGDhkfbYy%2BHbssNxDDpNWQRLtb2QFfw37fHcYYH2azSjxofkBAEUSBklg4F1FieoqwYIZ5JFYFUQdMpAdiX%2BVQjBZPSf%2Fz%2FaYqd79Z8rx%2FVeCVORWsVKC1vMrj3d9w7DwdJuY3eWAJImasyn7Vqbrr%2BBnqoQ2c5inMvWwfKMND04coGOqUBKpsdv%2B%2Ft4eVuqU025Rg8GAYSrgGhGdtOV%2Fzn%2F%2BawwK00RWZ7wlyQvwbZvPSAwh9etXS2ne2Uz2tIoGPS5CVIbW7ZChxkEl4QRR21FLpUc6TPNH5uAz4vV%2Bh9F8luqvoINY6Lxgv5Oa121Owq%2FQM2q1gon%2BorQmcZMb9hGI7L4HkfAKdPdVJmddRPakGBBwEZ2iZI5pxZKKPhHVHXB3sUca6hjp02&X-Amz-Signature=798353fe97073deb082df2b71d9e28485deffcfb30d3d17f804975052c95d11b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

