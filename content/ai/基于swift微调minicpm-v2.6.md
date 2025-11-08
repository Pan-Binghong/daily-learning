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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVT5PXZ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCvxCY4wY3eXuMDa6SYoTPY7MHH9YTnV0hn66iaxMufDQIhAKJ2dd0%2B7IUQr3lSSiFJr%2Bmw1Krvnm1nKfjRdCDdJagTKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzym29P26n%2BzvPVXSMq3ANFvWaX3V6C%2Bul1vrqahOHar4%2BAgOiEoKAYHACWvY3MSoGFiHurVyIMNbVlkcCtJ1v8PiK3wcyiSsGvEG%2FKnR5HmwLpxXd%2Fk6tk7bmqZSmPwycG4QQxmvRAJVGC%2FyxCcH%2BHNLwoa6JwfVMh0p4mS8rDJPLW7MbxMN7PSBNLxUGO1%2FYCnZ8WW0IdNGTAEFmXxSzF%2FQwqaKCCxCURH2bwgEAcSfDfPB39U9SK%2F13yitbofLLexfjiqia%2Fo7wZJdnBjDuowCPjfsMEDQD%2F6oi66FI5IYdxG6zCwSkHRXlZZmsOg6VGymxaYZGFJlRJ0ytyfF8VFTzGyY4VnumN3Endd%2FjXBR3tv8DXtAoy800vcmRTd%2BV%2Bbwdd84vOU%2BOv%2FaAOSLrazu7nwJ55w2ohQDLwxyDzfpYwcGtvrDh%2FxQURhypWnNVdH2OxNUU134FvWdeEp6LQ99bBZAK1%2Bk6lFWZRiWicWFrYs7yVBBpBRwzJpUv7byMGTQJXtxhKxyupuiqzAkFbr8kkWjVbCq7nI1tVWTOIzdq%2Bumh2jbEip%2BhSvcLq73TSYOrNcG8YP%2BWd67RLDq2Qa4lvMsiCDER913nQJ%2Bq76RYDehnX4wASNkaYNXbTh8nKUITmzEgQLtahzjC30LrIBjqkAcZCjM2gMFylKZ%2FZb%2FiNOxdruelFPty3nLrrwNV09S%2FTT4hf2AfShKbwTxUn%2FpalQlUhpfkDgIjfCHLVDPv1pZydVaVP9mClUNbD0eVyO5xZf7LBriTGrPIJ301WBbymWoDqmfZi%2B3lDGC7W5idwgQK3D2GmhbWZ%2B%2FHjOPvUHbhoBz6fS0r1HbT%2FIkiyGO%2FiljRn4IfXlR54W3m7M08NbngM2zCw&X-Amz-Signature=6859fcf04a68b68aefb3c35490a79acb03e74c00e0953026071ccffc988668b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVT5PXZ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCvxCY4wY3eXuMDa6SYoTPY7MHH9YTnV0hn66iaxMufDQIhAKJ2dd0%2B7IUQr3lSSiFJr%2Bmw1Krvnm1nKfjRdCDdJagTKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzym29P26n%2BzvPVXSMq3ANFvWaX3V6C%2Bul1vrqahOHar4%2BAgOiEoKAYHACWvY3MSoGFiHurVyIMNbVlkcCtJ1v8PiK3wcyiSsGvEG%2FKnR5HmwLpxXd%2Fk6tk7bmqZSmPwycG4QQxmvRAJVGC%2FyxCcH%2BHNLwoa6JwfVMh0p4mS8rDJPLW7MbxMN7PSBNLxUGO1%2FYCnZ8WW0IdNGTAEFmXxSzF%2FQwqaKCCxCURH2bwgEAcSfDfPB39U9SK%2F13yitbofLLexfjiqia%2Fo7wZJdnBjDuowCPjfsMEDQD%2F6oi66FI5IYdxG6zCwSkHRXlZZmsOg6VGymxaYZGFJlRJ0ytyfF8VFTzGyY4VnumN3Endd%2FjXBR3tv8DXtAoy800vcmRTd%2BV%2Bbwdd84vOU%2BOv%2FaAOSLrazu7nwJ55w2ohQDLwxyDzfpYwcGtvrDh%2FxQURhypWnNVdH2OxNUU134FvWdeEp6LQ99bBZAK1%2Bk6lFWZRiWicWFrYs7yVBBpBRwzJpUv7byMGTQJXtxhKxyupuiqzAkFbr8kkWjVbCq7nI1tVWTOIzdq%2Bumh2jbEip%2BhSvcLq73TSYOrNcG8YP%2BWd67RLDq2Qa4lvMsiCDER913nQJ%2Bq76RYDehnX4wASNkaYNXbTh8nKUITmzEgQLtahzjC30LrIBjqkAcZCjM2gMFylKZ%2FZb%2FiNOxdruelFPty3nLrrwNV09S%2FTT4hf2AfShKbwTxUn%2FpalQlUhpfkDgIjfCHLVDPv1pZydVaVP9mClUNbD0eVyO5xZf7LBriTGrPIJ301WBbymWoDqmfZi%2B3lDGC7W5idwgQK3D2GmhbWZ%2B%2FHjOPvUHbhoBz6fS0r1HbT%2FIkiyGO%2FiljRn4IfXlR54W3m7M08NbngM2zCw&X-Amz-Signature=524b4e128aeafaa20dbac3d8a804cc370b930a2c1c11e28b0343cb42670afebe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCVT5PXZ%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCvxCY4wY3eXuMDa6SYoTPY7MHH9YTnV0hn66iaxMufDQIhAKJ2dd0%2B7IUQr3lSSiFJr%2Bmw1Krvnm1nKfjRdCDdJagTKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzym29P26n%2BzvPVXSMq3ANFvWaX3V6C%2Bul1vrqahOHar4%2BAgOiEoKAYHACWvY3MSoGFiHurVyIMNbVlkcCtJ1v8PiK3wcyiSsGvEG%2FKnR5HmwLpxXd%2Fk6tk7bmqZSmPwycG4QQxmvRAJVGC%2FyxCcH%2BHNLwoa6JwfVMh0p4mS8rDJPLW7MbxMN7PSBNLxUGO1%2FYCnZ8WW0IdNGTAEFmXxSzF%2FQwqaKCCxCURH2bwgEAcSfDfPB39U9SK%2F13yitbofLLexfjiqia%2Fo7wZJdnBjDuowCPjfsMEDQD%2F6oi66FI5IYdxG6zCwSkHRXlZZmsOg6VGymxaYZGFJlRJ0ytyfF8VFTzGyY4VnumN3Endd%2FjXBR3tv8DXtAoy800vcmRTd%2BV%2Bbwdd84vOU%2BOv%2FaAOSLrazu7nwJ55w2ohQDLwxyDzfpYwcGtvrDh%2FxQURhypWnNVdH2OxNUU134FvWdeEp6LQ99bBZAK1%2Bk6lFWZRiWicWFrYs7yVBBpBRwzJpUv7byMGTQJXtxhKxyupuiqzAkFbr8kkWjVbCq7nI1tVWTOIzdq%2Bumh2jbEip%2BhSvcLq73TSYOrNcG8YP%2BWd67RLDq2Qa4lvMsiCDER913nQJ%2Bq76RYDehnX4wASNkaYNXbTh8nKUITmzEgQLtahzjC30LrIBjqkAcZCjM2gMFylKZ%2FZb%2FiNOxdruelFPty3nLrrwNV09S%2FTT4hf2AfShKbwTxUn%2FpalQlUhpfkDgIjfCHLVDPv1pZydVaVP9mClUNbD0eVyO5xZf7LBriTGrPIJ301WBbymWoDqmfZi%2B3lDGC7W5idwgQK3D2GmhbWZ%2B%2FHjOPvUHbhoBz6fS0r1HbT%2FIkiyGO%2FiljRn4IfXlR54W3m7M08NbngM2zCw&X-Amz-Signature=933b34bfecd30dd5129f2c467a3cd5ab9941edfb6e717934487e2a6ba284b9e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

