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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U75NO3WU%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDs85D0yW5oAp9xMexvafaHi%2BHSXGCsDaccsXJjdr%2BmAiEAyBY8zrJO5Jr5VBMbHI7Y4jwB%2FvtXyqn66u44bFKNCAAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpWiXdcqeHCk9iHLCrcA1gcepH1oO8o0vSJWl8FQoRVvBa514XnAHftMVk5ia0rAAW%2BlAQ%2B6JDy98WANLrTz3rGTYkVy6xRHCKMOCtfxvm0YKrcDYM4vOXJ8RnEMY6qhXx5Q9tFmMbXyKkFAntxBxyqOEYKnLAxx9gS%2FPdXgtH%2BwAnn2uABcIskgwbXD06s8l%2B2vTPQ%2BKDdx2km3Y%2FtU%2F8g13dwlOGytyhO8mgaRk2hn%2F7WtYAZMrF9NGTMq35ZB4F33OHGTcpbf8nVfND98nuCEAbjAOHus1mD%2BLcUVSVpmNyYIPzcycvPErovlSZRqL8sFwzCYWu3vfQn2FUnoHNoRvGCvkT5%2FPVuK4SsYxIWwKgUA2KygAHyhOiyJMGPQrRO5XgxhxNXPK79vxuvdYgivgLxocUnWME3O2bfSHQCu2mbG83jlO4jlY5cxYN59wV3EpTnkCTPl07FYBqc4zESL4TVmEsu4srJDXgZ4A0PM1Bgrx0%2FfHiepbss2BUfIQJQoB0khWKGuBG1g7JXA8VIJdZEOcv4IysruXWKgyXTWWMzqLeyosrZCq01jwsxDhN5lubzlZnnUfmXFWQFiGrzIvRjUkd7XRokBcYaaOAjVDfGqJ1XP%2FMDleTPFzCFHNpo7WMIfE4A44h6MJ35hssGOqUBXyGPo4clTzkHcS%2FOpGHr6TdPE6FZGkzbcO5f5VFyDJnK%2FXfAroPmWn2shNiF9OWJ4z8CoY4LN5W6XSGWVpPyZJbjGRhXHBV4qEiUceVAJg7dojvNXU%2Ba0rOK1v3mNigw0D5NFxrVGoFYnBqSY%2Bj4OO%2BdKxS9nsNljQYn1TfRn0hLryO78hs8o3ehF61D5eoSvc0FLh5k7%2F24fTAElCMr4w0O8DSP&X-Amz-Signature=c4bb975e265e186bc492260b484c93926d5e711eb5012183f0c4f1642e704216&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U75NO3WU%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDs85D0yW5oAp9xMexvafaHi%2BHSXGCsDaccsXJjdr%2BmAiEAyBY8zrJO5Jr5VBMbHI7Y4jwB%2FvtXyqn66u44bFKNCAAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpWiXdcqeHCk9iHLCrcA1gcepH1oO8o0vSJWl8FQoRVvBa514XnAHftMVk5ia0rAAW%2BlAQ%2B6JDy98WANLrTz3rGTYkVy6xRHCKMOCtfxvm0YKrcDYM4vOXJ8RnEMY6qhXx5Q9tFmMbXyKkFAntxBxyqOEYKnLAxx9gS%2FPdXgtH%2BwAnn2uABcIskgwbXD06s8l%2B2vTPQ%2BKDdx2km3Y%2FtU%2F8g13dwlOGytyhO8mgaRk2hn%2F7WtYAZMrF9NGTMq35ZB4F33OHGTcpbf8nVfND98nuCEAbjAOHus1mD%2BLcUVSVpmNyYIPzcycvPErovlSZRqL8sFwzCYWu3vfQn2FUnoHNoRvGCvkT5%2FPVuK4SsYxIWwKgUA2KygAHyhOiyJMGPQrRO5XgxhxNXPK79vxuvdYgivgLxocUnWME3O2bfSHQCu2mbG83jlO4jlY5cxYN59wV3EpTnkCTPl07FYBqc4zESL4TVmEsu4srJDXgZ4A0PM1Bgrx0%2FfHiepbss2BUfIQJQoB0khWKGuBG1g7JXA8VIJdZEOcv4IysruXWKgyXTWWMzqLeyosrZCq01jwsxDhN5lubzlZnnUfmXFWQFiGrzIvRjUkd7XRokBcYaaOAjVDfGqJ1XP%2FMDleTPFzCFHNpo7WMIfE4A44h6MJ35hssGOqUBXyGPo4clTzkHcS%2FOpGHr6TdPE6FZGkzbcO5f5VFyDJnK%2FXfAroPmWn2shNiF9OWJ4z8CoY4LN5W6XSGWVpPyZJbjGRhXHBV4qEiUceVAJg7dojvNXU%2Ba0rOK1v3mNigw0D5NFxrVGoFYnBqSY%2Bj4OO%2BdKxS9nsNljQYn1TfRn0hLryO78hs8o3ehF61D5eoSvc0FLh5k7%2F24fTAElCMr4w0O8DSP&X-Amz-Signature=1fea71edc2ab16a77fe459b840992b5f8f434ba09c2d54c004d82db388f0c468&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U75NO3WU%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHDs85D0yW5oAp9xMexvafaHi%2BHSXGCsDaccsXJjdr%2BmAiEAyBY8zrJO5Jr5VBMbHI7Y4jwB%2FvtXyqn66u44bFKNCAAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMpWiXdcqeHCk9iHLCrcA1gcepH1oO8o0vSJWl8FQoRVvBa514XnAHftMVk5ia0rAAW%2BlAQ%2B6JDy98WANLrTz3rGTYkVy6xRHCKMOCtfxvm0YKrcDYM4vOXJ8RnEMY6qhXx5Q9tFmMbXyKkFAntxBxyqOEYKnLAxx9gS%2FPdXgtH%2BwAnn2uABcIskgwbXD06s8l%2B2vTPQ%2BKDdx2km3Y%2FtU%2F8g13dwlOGytyhO8mgaRk2hn%2F7WtYAZMrF9NGTMq35ZB4F33OHGTcpbf8nVfND98nuCEAbjAOHus1mD%2BLcUVSVpmNyYIPzcycvPErovlSZRqL8sFwzCYWu3vfQn2FUnoHNoRvGCvkT5%2FPVuK4SsYxIWwKgUA2KygAHyhOiyJMGPQrRO5XgxhxNXPK79vxuvdYgivgLxocUnWME3O2bfSHQCu2mbG83jlO4jlY5cxYN59wV3EpTnkCTPl07FYBqc4zESL4TVmEsu4srJDXgZ4A0PM1Bgrx0%2FfHiepbss2BUfIQJQoB0khWKGuBG1g7JXA8VIJdZEOcv4IysruXWKgyXTWWMzqLeyosrZCq01jwsxDhN5lubzlZnnUfmXFWQFiGrzIvRjUkd7XRokBcYaaOAjVDfGqJ1XP%2FMDleTPFzCFHNpo7WMIfE4A44h6MJ35hssGOqUBXyGPo4clTzkHcS%2FOpGHr6TdPE6FZGkzbcO5f5VFyDJnK%2FXfAroPmWn2shNiF9OWJ4z8CoY4LN5W6XSGWVpPyZJbjGRhXHBV4qEiUceVAJg7dojvNXU%2Ba0rOK1v3mNigw0D5NFxrVGoFYnBqSY%2Bj4OO%2BdKxS9nsNljQYn1TfRn0hLryO78hs8o3ehF61D5eoSvc0FLh5k7%2F24fTAElCMr4w0O8DSP&X-Amz-Signature=ddc83ef27060f99024b9baa0e1215d336fdc1c103412451743b7686dc4c41237&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

