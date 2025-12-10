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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644SVYA66%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCWS1QSw%2B%2FB%2Fkxdopy1i4idFM2XpXbCjoFYN%2FGvfM90XAIgBH76G2eBnZsoQ%2FuaZMS8JjkwHpfp%2BaTGnvc%2FB0Lhk4gqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcfF1TCH7j07U6vgyrcA%2BLSbQ9gcjeNf%2BFUxzelO54lXdc5Vddc3%2FmApSMCyhGdzVSxPtPuNPt5vnJG%2FDGgfUaDpQsqhxdSoJugLpzYgS8KXAzr4DtAZeb5cSMwP%2Fda3zJ4MJWUsrccqAn%2BuT4J1x0fFB7gzOkhL0MM%2Bt%2BBXjAv8mBiRx0lDnf2j3X74zA4%2BvYy1HrLRY8ZqmVL%2Fh3i1r5v5naFjbtZVdt6AxYCtKpqAP2mXSPi2iUwh07HXK7D8FHFGILHOlXYeL9v3%2BlRy3ea6l%2BefwfO%2BVdmwacW8uQTuD3PXda6u8TfuIkbP7zwhaOr2t107UKJzaCNBYw6ECSXChNsLy350Ij%2Fzh1BVBlwcOCmU1%2BVGMLBz3KSZhtAQR3mzSvZLFVEtt8cFMQWQxEv1bBb0uAk7Gltvtu4uxG1uQHBKjODbfFOBdvwk9xZ9IZzO%2BL%2F8V8A8%2B9FTESJ9KMJiE6vbuCCE00WVjkHRu%2FRXnrJtKJzVylElNQfWyru5x2oZSkQtq3IDq3MFnrK9DoaplRf6wV%2FDxXsZTok89RfYswgLsrQRWIOjK7qEbq0JCiluIvc55jek66uC7oYRbNaHZJA8uKIVvIEHcljPQIdCbkOarEaHCUcUO4qHEnS5AZpt7tT2rYRZI%2BGMO6%2F48kGOqUBVpcD95OxFl8ot02ykQ%2FYzOMUVYJt6BwTApqgZrxFH0xHj905GJVzFgyfho%2FnBXbRdSHP%2FLBj%2F3NSS86noPLuhbEC2e8kbGRGjLT6jjfttp50iE6nA8vv25thSBMSmaWG02tTiY1te7QBm3MjdzgS1yb5AhPJUpd0SkjHSQnK4h8dcaGrBtrheepxNKwqQ%2BXbOKpu%2F8mKdqdmh%2BRC446GeyaBfuRi&X-Amz-Signature=a74afb4ca30a860d887725bc87e1dd890d80c3a3efd7faa4bdbb7538c5808ca1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644SVYA66%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCWS1QSw%2B%2FB%2Fkxdopy1i4idFM2XpXbCjoFYN%2FGvfM90XAIgBH76G2eBnZsoQ%2FuaZMS8JjkwHpfp%2BaTGnvc%2FB0Lhk4gqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcfF1TCH7j07U6vgyrcA%2BLSbQ9gcjeNf%2BFUxzelO54lXdc5Vddc3%2FmApSMCyhGdzVSxPtPuNPt5vnJG%2FDGgfUaDpQsqhxdSoJugLpzYgS8KXAzr4DtAZeb5cSMwP%2Fda3zJ4MJWUsrccqAn%2BuT4J1x0fFB7gzOkhL0MM%2Bt%2BBXjAv8mBiRx0lDnf2j3X74zA4%2BvYy1HrLRY8ZqmVL%2Fh3i1r5v5naFjbtZVdt6AxYCtKpqAP2mXSPi2iUwh07HXK7D8FHFGILHOlXYeL9v3%2BlRy3ea6l%2BefwfO%2BVdmwacW8uQTuD3PXda6u8TfuIkbP7zwhaOr2t107UKJzaCNBYw6ECSXChNsLy350Ij%2Fzh1BVBlwcOCmU1%2BVGMLBz3KSZhtAQR3mzSvZLFVEtt8cFMQWQxEv1bBb0uAk7Gltvtu4uxG1uQHBKjODbfFOBdvwk9xZ9IZzO%2BL%2F8V8A8%2B9FTESJ9KMJiE6vbuCCE00WVjkHRu%2FRXnrJtKJzVylElNQfWyru5x2oZSkQtq3IDq3MFnrK9DoaplRf6wV%2FDxXsZTok89RfYswgLsrQRWIOjK7qEbq0JCiluIvc55jek66uC7oYRbNaHZJA8uKIVvIEHcljPQIdCbkOarEaHCUcUO4qHEnS5AZpt7tT2rYRZI%2BGMO6%2F48kGOqUBVpcD95OxFl8ot02ykQ%2FYzOMUVYJt6BwTApqgZrxFH0xHj905GJVzFgyfho%2FnBXbRdSHP%2FLBj%2F3NSS86noPLuhbEC2e8kbGRGjLT6jjfttp50iE6nA8vv25thSBMSmaWG02tTiY1te7QBm3MjdzgS1yb5AhPJUpd0SkjHSQnK4h8dcaGrBtrheepxNKwqQ%2BXbOKpu%2F8mKdqdmh%2BRC446GeyaBfuRi&X-Amz-Signature=eab8e937bd23ce80914c43f9ecd13cd4be37bd27d48085fac0d07624a25bd625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46644SVYA66%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025240Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCWS1QSw%2B%2FB%2Fkxdopy1i4idFM2XpXbCjoFYN%2FGvfM90XAIgBH76G2eBnZsoQ%2FuaZMS8JjkwHpfp%2BaTGnvc%2FB0Lhk4gqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPcfF1TCH7j07U6vgyrcA%2BLSbQ9gcjeNf%2BFUxzelO54lXdc5Vddc3%2FmApSMCyhGdzVSxPtPuNPt5vnJG%2FDGgfUaDpQsqhxdSoJugLpzYgS8KXAzr4DtAZeb5cSMwP%2Fda3zJ4MJWUsrccqAn%2BuT4J1x0fFB7gzOkhL0MM%2Bt%2BBXjAv8mBiRx0lDnf2j3X74zA4%2BvYy1HrLRY8ZqmVL%2Fh3i1r5v5naFjbtZVdt6AxYCtKpqAP2mXSPi2iUwh07HXK7D8FHFGILHOlXYeL9v3%2BlRy3ea6l%2BefwfO%2BVdmwacW8uQTuD3PXda6u8TfuIkbP7zwhaOr2t107UKJzaCNBYw6ECSXChNsLy350Ij%2Fzh1BVBlwcOCmU1%2BVGMLBz3KSZhtAQR3mzSvZLFVEtt8cFMQWQxEv1bBb0uAk7Gltvtu4uxG1uQHBKjODbfFOBdvwk9xZ9IZzO%2BL%2F8V8A8%2B9FTESJ9KMJiE6vbuCCE00WVjkHRu%2FRXnrJtKJzVylElNQfWyru5x2oZSkQtq3IDq3MFnrK9DoaplRf6wV%2FDxXsZTok89RfYswgLsrQRWIOjK7qEbq0JCiluIvc55jek66uC7oYRbNaHZJA8uKIVvIEHcljPQIdCbkOarEaHCUcUO4qHEnS5AZpt7tT2rYRZI%2BGMO6%2F48kGOqUBVpcD95OxFl8ot02ykQ%2FYzOMUVYJt6BwTApqgZrxFH0xHj905GJVzFgyfho%2FnBXbRdSHP%2FLBj%2F3NSS86noPLuhbEC2e8kbGRGjLT6jjfttp50iE6nA8vv25thSBMSmaWG02tTiY1te7QBm3MjdzgS1yb5AhPJUpd0SkjHSQnK4h8dcaGrBtrheepxNKwqQ%2BXbOKpu%2F8mKdqdmh%2BRC446GeyaBfuRi&X-Amz-Signature=c9dfdea581a05b8edc52c584f1862c0e6cc6fbed799895377afe00e5dc86b345&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

