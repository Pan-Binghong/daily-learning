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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMY5A7M%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7uWrQuFDt9ba1f0psCvj61KfJ%2F%2FmJjRlEay4ULKym3AIgRWsF6pNmeKy1TQwPlAdzk9u7sIwHrhBAo0JofEjJIQ0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDII8c4xZ%2BPiISRUYFCrcAzXdY2%2B3GhH8XHgi8KbcFFTINQpR6kZTiWVELp3EhGmLm0iGdPC8s23alCmdxp2raZkfcc1s5zIoNQ77WBZcRXyxaYhpeFVmnhYIGGESdKrcvPiYpcKJIKQjMPXtXnUiifLmw6qvGTb4Nz4SWIPesrGLwHZKxOwxizMRBgyAV95TGPq3EC1HLNkkzCMIAXOEmesIBnNMkQn10IJsLkz92C6%2FMGtIM3h9m6UGFLLOr4oVknE08Nf%2BWC7o%2FC0F61a0eMaebpy6O5mj2LK0%2FmAUXliVwXSic9d1LDjQ0MWHeckYgXc6SrV3ji6qr%2BhbxM%2BeE8VYA7EWOBRtpk6D1z1SumuO9VmaIpzPqRHFsTBVmcVy5KjI0A9h31hYFX7zX7ejq0dFOdmu5HKe45llgBxSl%2FBCYIA8Kq3IZ510Ul79lguHyLIJjHWdAZCdjvHV1bje9CCrjwVKo8sJp73ejwWoeqCwGu1y%2F73nfKqD%2FPSCgnG5wH1ZYJcK%2F4rKNRq4jXeIqzgw1Iwt%2FOvroV5zaFlCVIJoCv91ZYJwzmAAHquzd%2B0QuS%2BaN%2BDPKJU0e0q6%2FQ5WsBmRKcmhcyQqEw%2Bz1xR39EEV5EYfKNzUiGIhgQqyaFTn%2FszQoxG%2FhDmdARxDMKXyr8gGOqUB%2B355rDplmf5%2BD8XBR5DWPAcCdGSXbkf9xwLrL0XwX3P0KE141QOUadLddWv49QbMrZY9ZCdjRc3CeQ1LWrRA%2FfjvljgBasFlS%2BPGcNAKsLH9XpBcCtKP%2FpI2TcZVhgYgRt5pvk0MJHASxG4KANGxH53dYVatpCRl9HpgbdPMoid%2FhoxNBwPd3s4fd1Vy5xVXPvSDLW6AcJ6oKKiOhNjedSYhDzhA&X-Amz-Signature=3fc86bc79d4582083f5b955a7df33ca6a4d75fc0fbd0b3042649928ef3b4f485&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMY5A7M%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7uWrQuFDt9ba1f0psCvj61KfJ%2F%2FmJjRlEay4ULKym3AIgRWsF6pNmeKy1TQwPlAdzk9u7sIwHrhBAo0JofEjJIQ0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDII8c4xZ%2BPiISRUYFCrcAzXdY2%2B3GhH8XHgi8KbcFFTINQpR6kZTiWVELp3EhGmLm0iGdPC8s23alCmdxp2raZkfcc1s5zIoNQ77WBZcRXyxaYhpeFVmnhYIGGESdKrcvPiYpcKJIKQjMPXtXnUiifLmw6qvGTb4Nz4SWIPesrGLwHZKxOwxizMRBgyAV95TGPq3EC1HLNkkzCMIAXOEmesIBnNMkQn10IJsLkz92C6%2FMGtIM3h9m6UGFLLOr4oVknE08Nf%2BWC7o%2FC0F61a0eMaebpy6O5mj2LK0%2FmAUXliVwXSic9d1LDjQ0MWHeckYgXc6SrV3ji6qr%2BhbxM%2BeE8VYA7EWOBRtpk6D1z1SumuO9VmaIpzPqRHFsTBVmcVy5KjI0A9h31hYFX7zX7ejq0dFOdmu5HKe45llgBxSl%2FBCYIA8Kq3IZ510Ul79lguHyLIJjHWdAZCdjvHV1bje9CCrjwVKo8sJp73ejwWoeqCwGu1y%2F73nfKqD%2FPSCgnG5wH1ZYJcK%2F4rKNRq4jXeIqzgw1Iwt%2FOvroV5zaFlCVIJoCv91ZYJwzmAAHquzd%2B0QuS%2BaN%2BDPKJU0e0q6%2FQ5WsBmRKcmhcyQqEw%2Bz1xR39EEV5EYfKNzUiGIhgQqyaFTn%2FszQoxG%2FhDmdARxDMKXyr8gGOqUB%2B355rDplmf5%2BD8XBR5DWPAcCdGSXbkf9xwLrL0XwX3P0KE141QOUadLddWv49QbMrZY9ZCdjRc3CeQ1LWrRA%2FfjvljgBasFlS%2BPGcNAKsLH9XpBcCtKP%2FpI2TcZVhgYgRt5pvk0MJHASxG4KANGxH53dYVatpCRl9HpgbdPMoid%2FhoxNBwPd3s4fd1Vy5xVXPvSDLW6AcJ6oKKiOhNjedSYhDzhA&X-Amz-Signature=8a8b123431d52739b0d4d69183bad4c1b1f18aec0c923984b2fb77318266cda6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XOMY5A7M%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD7uWrQuFDt9ba1f0psCvj61KfJ%2F%2FmJjRlEay4ULKym3AIgRWsF6pNmeKy1TQwPlAdzk9u7sIwHrhBAo0JofEjJIQ0qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDII8c4xZ%2BPiISRUYFCrcAzXdY2%2B3GhH8XHgi8KbcFFTINQpR6kZTiWVELp3EhGmLm0iGdPC8s23alCmdxp2raZkfcc1s5zIoNQ77WBZcRXyxaYhpeFVmnhYIGGESdKrcvPiYpcKJIKQjMPXtXnUiifLmw6qvGTb4Nz4SWIPesrGLwHZKxOwxizMRBgyAV95TGPq3EC1HLNkkzCMIAXOEmesIBnNMkQn10IJsLkz92C6%2FMGtIM3h9m6UGFLLOr4oVknE08Nf%2BWC7o%2FC0F61a0eMaebpy6O5mj2LK0%2FmAUXliVwXSic9d1LDjQ0MWHeckYgXc6SrV3ji6qr%2BhbxM%2BeE8VYA7EWOBRtpk6D1z1SumuO9VmaIpzPqRHFsTBVmcVy5KjI0A9h31hYFX7zX7ejq0dFOdmu5HKe45llgBxSl%2FBCYIA8Kq3IZ510Ul79lguHyLIJjHWdAZCdjvHV1bje9CCrjwVKo8sJp73ejwWoeqCwGu1y%2F73nfKqD%2FPSCgnG5wH1ZYJcK%2F4rKNRq4jXeIqzgw1Iwt%2FOvroV5zaFlCVIJoCv91ZYJwzmAAHquzd%2B0QuS%2BaN%2BDPKJU0e0q6%2FQ5WsBmRKcmhcyQqEw%2Bz1xR39EEV5EYfKNzUiGIhgQqyaFTn%2FszQoxG%2FhDmdARxDMKXyr8gGOqUB%2B355rDplmf5%2BD8XBR5DWPAcCdGSXbkf9xwLrL0XwX3P0KE141QOUadLddWv49QbMrZY9ZCdjRc3CeQ1LWrRA%2FfjvljgBasFlS%2BPGcNAKsLH9XpBcCtKP%2FpI2TcZVhgYgRt5pvk0MJHASxG4KANGxH53dYVatpCRl9HpgbdPMoid%2FhoxNBwPd3s4fd1Vy5xVXPvSDLW6AcJ6oKKiOhNjedSYhDzhA&X-Amz-Signature=b7c0ec62119b6d2ca8e4e142e49c0ce89b0cf454f62fbaeb7e1201fd7ae056eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

