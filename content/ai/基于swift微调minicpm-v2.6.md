---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GD7ES5T%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCU%2FdoGHFIu9YaAJwIx2XBO%2Fev0hKtXOHA%2BR0TZIHoiIwIhAPbDiYsL3Pi2JGeaAUTIAir99qabYRchlG6EY8GIyPrdKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxczeIoAh%2FkzuqR1%2FYq3AOqynGs%2BsUuHl0Od0WOA9PmH25ScuHc2o7DouWlvoh1cr%2FjNVdn6wkt%2BysG7bddEJd3AdnaUvy7mNzVROn6QqVN8PzB%2F%2B4O%2FNISvMwzKjJYsj9Hwnhn9A3WwuLtjMQw1cxfxaevne%2BlaMKs%2FiLPQCWY1hYInEXbTN%2B0y5zorGE57woADfFK7ul%2BEgdbxqJAkDfk8geQ83vpIPBwHLENM3Imc2%2FpH4O22r7AeD%2BkGQ0Epv4iJqV41FNj2f%2Fzyln%2BlL7TZ%2FDTm56VqLiuIFxKS19l0y35LgRGfp8AvbN%2Bv0B6JyLme%2B4l8tKZt6Ay%2FTH7ibovRjx6yC2y7KTOJqxTBY7XKITu2qp3oz1a8a5O5hEj8%2FNTh41lnvN47zVnoU%2FccWYHQScH9U75wsSK9nSYQ2yEIJitZw1zqFTdYGkR3yLHWx1PfasytYn8PDwtVzjt19Hwcc7znb15S1eBMnr%2Btzd12YjztrR8N5VRb186yNgaEB3bBLIw%2BRwqF7UuFS9iSixA%2FT3kHHBSmQr83Gh4AYEF44IcJxLk6k5p9NJWp9IvSC%2BIqktemQAL%2FcrP1n86F4QjrBveMNbMoet%2Blu8lmcsVxB5UPV9%2Bq4d5EdAG8v8ulDGaDrpJDwqfttnGjzCro6zIBjqkATgomQPqk3xfaledphGs7RTISWQq8hqtKqGdixanLNx4VGDgPijdtzkAt3v8vzyGDIsZ6Ar%2FyT1SOUYLUSqswjdUnmtkeffEfyjNqg5HTvipjM62uzcGY%2FlKynSUEs%2B3JJHYtKQ4B%2FzOHZJYgFyE7H3688cD5SG%2BTWWOwo8uw5DZnriMKcMjqpKhzSwirp3AdD6qJDmL2dj55ykp2IM%2B1S%2FLHKEF&X-Amz-Signature=521d82d2bffeca9709a2a8fb1bc4ed34a1993a6a91c1e228a7de4c97555b2496&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GD7ES5T%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCU%2FdoGHFIu9YaAJwIx2XBO%2Fev0hKtXOHA%2BR0TZIHoiIwIhAPbDiYsL3Pi2JGeaAUTIAir99qabYRchlG6EY8GIyPrdKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxczeIoAh%2FkzuqR1%2FYq3AOqynGs%2BsUuHl0Od0WOA9PmH25ScuHc2o7DouWlvoh1cr%2FjNVdn6wkt%2BysG7bddEJd3AdnaUvy7mNzVROn6QqVN8PzB%2F%2B4O%2FNISvMwzKjJYsj9Hwnhn9A3WwuLtjMQw1cxfxaevne%2BlaMKs%2FiLPQCWY1hYInEXbTN%2B0y5zorGE57woADfFK7ul%2BEgdbxqJAkDfk8geQ83vpIPBwHLENM3Imc2%2FpH4O22r7AeD%2BkGQ0Epv4iJqV41FNj2f%2Fzyln%2BlL7TZ%2FDTm56VqLiuIFxKS19l0y35LgRGfp8AvbN%2Bv0B6JyLme%2B4l8tKZt6Ay%2FTH7ibovRjx6yC2y7KTOJqxTBY7XKITu2qp3oz1a8a5O5hEj8%2FNTh41lnvN47zVnoU%2FccWYHQScH9U75wsSK9nSYQ2yEIJitZw1zqFTdYGkR3yLHWx1PfasytYn8PDwtVzjt19Hwcc7znb15S1eBMnr%2Btzd12YjztrR8N5VRb186yNgaEB3bBLIw%2BRwqF7UuFS9iSixA%2FT3kHHBSmQr83Gh4AYEF44IcJxLk6k5p9NJWp9IvSC%2BIqktemQAL%2FcrP1n86F4QjrBveMNbMoet%2Blu8lmcsVxB5UPV9%2Bq4d5EdAG8v8ulDGaDrpJDwqfttnGjzCro6zIBjqkATgomQPqk3xfaledphGs7RTISWQq8hqtKqGdixanLNx4VGDgPijdtzkAt3v8vzyGDIsZ6Ar%2FyT1SOUYLUSqswjdUnmtkeffEfyjNqg5HTvipjM62uzcGY%2FlKynSUEs%2B3JJHYtKQ4B%2FzOHZJYgFyE7H3688cD5SG%2BTWWOwo8uw5DZnriMKcMjqpKhzSwirp3AdD6qJDmL2dj55ykp2IM%2B1S%2FLHKEF&X-Amz-Signature=859b187bcead89651c61a36b74f8048db8759537424351052308e319b43a41ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GD7ES5T%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCU%2FdoGHFIu9YaAJwIx2XBO%2Fev0hKtXOHA%2BR0TZIHoiIwIhAPbDiYsL3Pi2JGeaAUTIAir99qabYRchlG6EY8GIyPrdKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxczeIoAh%2FkzuqR1%2FYq3AOqynGs%2BsUuHl0Od0WOA9PmH25ScuHc2o7DouWlvoh1cr%2FjNVdn6wkt%2BysG7bddEJd3AdnaUvy7mNzVROn6QqVN8PzB%2F%2B4O%2FNISvMwzKjJYsj9Hwnhn9A3WwuLtjMQw1cxfxaevne%2BlaMKs%2FiLPQCWY1hYInEXbTN%2B0y5zorGE57woADfFK7ul%2BEgdbxqJAkDfk8geQ83vpIPBwHLENM3Imc2%2FpH4O22r7AeD%2BkGQ0Epv4iJqV41FNj2f%2Fzyln%2BlL7TZ%2FDTm56VqLiuIFxKS19l0y35LgRGfp8AvbN%2Bv0B6JyLme%2B4l8tKZt6Ay%2FTH7ibovRjx6yC2y7KTOJqxTBY7XKITu2qp3oz1a8a5O5hEj8%2FNTh41lnvN47zVnoU%2FccWYHQScH9U75wsSK9nSYQ2yEIJitZw1zqFTdYGkR3yLHWx1PfasytYn8PDwtVzjt19Hwcc7znb15S1eBMnr%2Btzd12YjztrR8N5VRb186yNgaEB3bBLIw%2BRwqF7UuFS9iSixA%2FT3kHHBSmQr83Gh4AYEF44IcJxLk6k5p9NJWp9IvSC%2BIqktemQAL%2FcrP1n86F4QjrBveMNbMoet%2Blu8lmcsVxB5UPV9%2Bq4d5EdAG8v8ulDGaDrpJDwqfttnGjzCro6zIBjqkATgomQPqk3xfaledphGs7RTISWQq8hqtKqGdixanLNx4VGDgPijdtzkAt3v8vzyGDIsZ6Ar%2FyT1SOUYLUSqswjdUnmtkeffEfyjNqg5HTvipjM62uzcGY%2FlKynSUEs%2B3JJHYtKQ4B%2FzOHZJYgFyE7H3688cD5SG%2BTWWOwo8uw5DZnriMKcMjqpKhzSwirp3AdD6qJDmL2dj55ykp2IM%2B1S%2FLHKEF&X-Amz-Signature=8805cf3f087dc391e25d94a6d12d8ef0ba0767a9fe5ad1d3bd14945033942dd9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

