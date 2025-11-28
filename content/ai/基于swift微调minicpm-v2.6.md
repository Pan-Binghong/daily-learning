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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T3URZ5%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHdfeQo1Dg55Kym2PZd4tXiCHuKWx6tOltNhZBvjq7F2AiA92sWwKZJObWJz4lB2gue7SQmrb4aumEZY57K69tkMFSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTjHffNth7VMzQ8DKtwDk3%2Bkdi0lhNwSb1wYvuybtbAj4novxx%2BnpiJ703TuNQtU6nAKF%2FjqP5wzJXputwmSUViTJyTCHtvkTy6VsPmwlNb2jgExtLiowxtzYB6L%2BO0B3ztiKaT7TfzPqOYWODSOHiC57TB7120Xn9nE%2BKkLXaqNbrtcXxyDMGMtsO2xwGVI%2Ff%2B5ahvkokUwUSKC6DVVNGMGaJxLatW1AredPar7iihJd68N0dCukxnC37LNNV605EpSXBdccJgekt3mK%2F4KnCf6ntTAfrdiOhMWxLWgNwWv%2FFJk%2BW9slIF%2FwULmVEI%2FlAqrsmB8vtLZwXXREIE5GGQf7BC2HOMF9%2FUtQ3vdh5iWOZW4hf5q4ZT8Lef7ew%2FCHiv1ZLVEJOhZ8Wv8berJAfpTpvYZ%2FLyLMUivd8XCYqAqJIHXcAcZJI8dB%2FVamOnANKvAfIx5wT6f%2B2OidbwR00VzZYSUp1alOvQLll1n09acf8mA9XAWTOBcVfocbotCcC0%2FeklAK1gCpC9mtxvISnjbg62%2BBAnLfveiFTCmWJHC8DW6VMWKhXEA01zUnv5rM6FGwtfOUvNFE82QuFHOcpRZHZ7zURi7Aq9DdzTTJq3VeoZ%2B%2ByD16MRrh3Tbl7UWxKFk9aMmITHlhNwwsvWjyQY6pgEfj85SUd%2BSawgEgpmTvxJxH4LOUSfEV24b%2Fb%2BypSCm30Va9wI5uE4%2BRYuxvg9v9JPYjABf7OpwN%2BxE9wIIyvqKWw9PbYg7SC8NZIUpbON%2BDsCJ9IJ3004tr7VyWJ38o3SK2JBi9D%2FMlGuFJcy%2FPsBSCYNXQ867occyNz9H%2B73TeaXYkugGPplPXPo%2B68AJRMlGMwcSAa137kWIKiUobOZIAVoHKP6d&X-Amz-Signature=5bb7ed099cd8fdde235b34fda67a470009253077ce87983e8e3b538d84f5f07b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T3URZ5%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHdfeQo1Dg55Kym2PZd4tXiCHuKWx6tOltNhZBvjq7F2AiA92sWwKZJObWJz4lB2gue7SQmrb4aumEZY57K69tkMFSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTjHffNth7VMzQ8DKtwDk3%2Bkdi0lhNwSb1wYvuybtbAj4novxx%2BnpiJ703TuNQtU6nAKF%2FjqP5wzJXputwmSUViTJyTCHtvkTy6VsPmwlNb2jgExtLiowxtzYB6L%2BO0B3ztiKaT7TfzPqOYWODSOHiC57TB7120Xn9nE%2BKkLXaqNbrtcXxyDMGMtsO2xwGVI%2Ff%2B5ahvkokUwUSKC6DVVNGMGaJxLatW1AredPar7iihJd68N0dCukxnC37LNNV605EpSXBdccJgekt3mK%2F4KnCf6ntTAfrdiOhMWxLWgNwWv%2FFJk%2BW9slIF%2FwULmVEI%2FlAqrsmB8vtLZwXXREIE5GGQf7BC2HOMF9%2FUtQ3vdh5iWOZW4hf5q4ZT8Lef7ew%2FCHiv1ZLVEJOhZ8Wv8berJAfpTpvYZ%2FLyLMUivd8XCYqAqJIHXcAcZJI8dB%2FVamOnANKvAfIx5wT6f%2B2OidbwR00VzZYSUp1alOvQLll1n09acf8mA9XAWTOBcVfocbotCcC0%2FeklAK1gCpC9mtxvISnjbg62%2BBAnLfveiFTCmWJHC8DW6VMWKhXEA01zUnv5rM6FGwtfOUvNFE82QuFHOcpRZHZ7zURi7Aq9DdzTTJq3VeoZ%2B%2ByD16MRrh3Tbl7UWxKFk9aMmITHlhNwwsvWjyQY6pgEfj85SUd%2BSawgEgpmTvxJxH4LOUSfEV24b%2Fb%2BypSCm30Va9wI5uE4%2BRYuxvg9v9JPYjABf7OpwN%2BxE9wIIyvqKWw9PbYg7SC8NZIUpbON%2BDsCJ9IJ3004tr7VyWJ38o3SK2JBi9D%2FMlGuFJcy%2FPsBSCYNXQ867occyNz9H%2B73TeaXYkugGPplPXPo%2B68AJRMlGMwcSAa137kWIKiUobOZIAVoHKP6d&X-Amz-Signature=bc47a67f875866024473f282aece22070bb6d789bdffc2412a87627973137b68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7T3URZ5%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHdfeQo1Dg55Kym2PZd4tXiCHuKWx6tOltNhZBvjq7F2AiA92sWwKZJObWJz4lB2gue7SQmrb4aumEZY57K69tkMFSqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwTjHffNth7VMzQ8DKtwDk3%2Bkdi0lhNwSb1wYvuybtbAj4novxx%2BnpiJ703TuNQtU6nAKF%2FjqP5wzJXputwmSUViTJyTCHtvkTy6VsPmwlNb2jgExtLiowxtzYB6L%2BO0B3ztiKaT7TfzPqOYWODSOHiC57TB7120Xn9nE%2BKkLXaqNbrtcXxyDMGMtsO2xwGVI%2Ff%2B5ahvkokUwUSKC6DVVNGMGaJxLatW1AredPar7iihJd68N0dCukxnC37LNNV605EpSXBdccJgekt3mK%2F4KnCf6ntTAfrdiOhMWxLWgNwWv%2FFJk%2BW9slIF%2FwULmVEI%2FlAqrsmB8vtLZwXXREIE5GGQf7BC2HOMF9%2FUtQ3vdh5iWOZW4hf5q4ZT8Lef7ew%2FCHiv1ZLVEJOhZ8Wv8berJAfpTpvYZ%2FLyLMUivd8XCYqAqJIHXcAcZJI8dB%2FVamOnANKvAfIx5wT6f%2B2OidbwR00VzZYSUp1alOvQLll1n09acf8mA9XAWTOBcVfocbotCcC0%2FeklAK1gCpC9mtxvISnjbg62%2BBAnLfveiFTCmWJHC8DW6VMWKhXEA01zUnv5rM6FGwtfOUvNFE82QuFHOcpRZHZ7zURi7Aq9DdzTTJq3VeoZ%2B%2ByD16MRrh3Tbl7UWxKFk9aMmITHlhNwwsvWjyQY6pgEfj85SUd%2BSawgEgpmTvxJxH4LOUSfEV24b%2Fb%2BypSCm30Va9wI5uE4%2BRYuxvg9v9JPYjABf7OpwN%2BxE9wIIyvqKWw9PbYg7SC8NZIUpbON%2BDsCJ9IJ3004tr7VyWJ38o3SK2JBi9D%2FMlGuFJcy%2FPsBSCYNXQ867occyNz9H%2B73TeaXYkugGPplPXPo%2B68AJRMlGMwcSAa137kWIKiUobOZIAVoHKP6d&X-Amz-Signature=fab210b47dcd2e42e411f06a61d665d2a417fb4e89292cb1c6653233b628aab1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

