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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25LHOPY%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD0Q1awPXzj0XXunp8c99VM2iLdp6Cp8%2BSycN57Jt8AKwIhAIIhNPxJHb7Go8N90Ock1EG%2FzNzcKmKYwNgf%2FlRmIE3NKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxihgaDnZ0gIw7FQRoq3AN5Apn%2Bufpn0BqQUi2aC%2BcCDpGtQrV82cUcU%2B5iantzHIV7AA49DsahvpNFVKcX51YAJF5BXJmMCO%2F%2Fpyf8GarHHDyKsd7YlflsllOhbI0Iy16LEQM6xMAKNV49mRBVPIKlbE8xiy9J6Rvza9ErwIU7utpy1YHST%2FVOeukiZiQ0kWfMNhnLbsu8hrVb2dwUyD3nstP5rE4uoclwPpHO1qJcQTUNO%2FF8PS0UQToDi94S70eYOXCjJzI4GpXUr40bbkkJB6oIoGnm%2FG5BqfWuKFE3%2FldV2p%2FW%2B%2B3XPY8P0w7UR%2FnQSGeCMS0uT1i8DNosvXTysHQmk61vdrYdxce9RRQkuJlGbridG%2B5oVsBZGg9HXu%2F0i5NJ4dagM%2BMcfp78wnrVIblUwct6vVZ25kYKIZtbZhgtuqOSNMG9yxYq2NspI4jffrsqMjbXDsf3PWN3rtfaOe%2B4jmC9vJAHNNDcIU0SxV%2BOaoRXhCsPGsL%2FeWQma3k0DI%2BSD8VSZ6Pf%2F4uyhkovb3F%2BBPS9zH5UYZ86R7F577YfsHxb2dyPlx2yEUMXM7p3E2kE4ZtMuq77k6WxYNpFOGzefSpI6l5qrRzvHwkItQPEPSSmfzqxg8KurgwZWct6%2BJh7xTXMG8sBnTCR7MDPBjqkAczC2xVjKOQal3EQBceXL83QDZz0HGG%2ByO8BfWmmuLrAtjcNwJo6weETL6hC5aUfPOaXFIciLtVVOp6ls1y4Ti5gqJVM2DDWh5%2FPGOuN3q6K7%2B0cdnL5dlh2rBcJgh3baWcTWlP2kitViLR1%2BeZAP3VBwat9mpuKfKFJSETDz57rkPwNK10Jd2K8NMTlTOC0bqYzUSpXsIW1Sj%2FN%2FcAVYKFUfD0t&X-Amz-Signature=2839327f9fe4e1d158b0a500d8f8773449d3bf4bc6c87692ff0eed3af50aabcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25LHOPY%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD0Q1awPXzj0XXunp8c99VM2iLdp6Cp8%2BSycN57Jt8AKwIhAIIhNPxJHb7Go8N90Ock1EG%2FzNzcKmKYwNgf%2FlRmIE3NKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxihgaDnZ0gIw7FQRoq3AN5Apn%2Bufpn0BqQUi2aC%2BcCDpGtQrV82cUcU%2B5iantzHIV7AA49DsahvpNFVKcX51YAJF5BXJmMCO%2F%2Fpyf8GarHHDyKsd7YlflsllOhbI0Iy16LEQM6xMAKNV49mRBVPIKlbE8xiy9J6Rvza9ErwIU7utpy1YHST%2FVOeukiZiQ0kWfMNhnLbsu8hrVb2dwUyD3nstP5rE4uoclwPpHO1qJcQTUNO%2FF8PS0UQToDi94S70eYOXCjJzI4GpXUr40bbkkJB6oIoGnm%2FG5BqfWuKFE3%2FldV2p%2FW%2B%2B3XPY8P0w7UR%2FnQSGeCMS0uT1i8DNosvXTysHQmk61vdrYdxce9RRQkuJlGbridG%2B5oVsBZGg9HXu%2F0i5NJ4dagM%2BMcfp78wnrVIblUwct6vVZ25kYKIZtbZhgtuqOSNMG9yxYq2NspI4jffrsqMjbXDsf3PWN3rtfaOe%2B4jmC9vJAHNNDcIU0SxV%2BOaoRXhCsPGsL%2FeWQma3k0DI%2BSD8VSZ6Pf%2F4uyhkovb3F%2BBPS9zH5UYZ86R7F577YfsHxb2dyPlx2yEUMXM7p3E2kE4ZtMuq77k6WxYNpFOGzefSpI6l5qrRzvHwkItQPEPSSmfzqxg8KurgwZWct6%2BJh7xTXMG8sBnTCR7MDPBjqkAczC2xVjKOQal3EQBceXL83QDZz0HGG%2ByO8BfWmmuLrAtjcNwJo6weETL6hC5aUfPOaXFIciLtVVOp6ls1y4Ti5gqJVM2DDWh5%2FPGOuN3q6K7%2B0cdnL5dlh2rBcJgh3baWcTWlP2kitViLR1%2BeZAP3VBwat9mpuKfKFJSETDz57rkPwNK10Jd2K8NMTlTOC0bqYzUSpXsIW1Sj%2FN%2FcAVYKFUfD0t&X-Amz-Signature=697a9c5ea0c46c5ca9c025fb7ae21e6229dc50f6084a5071bf1f8b05297f8401&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R25LHOPY%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T043526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQD0Q1awPXzj0XXunp8c99VM2iLdp6Cp8%2BSycN57Jt8AKwIhAIIhNPxJHb7Go8N90Ock1EG%2FzNzcKmKYwNgf%2FlRmIE3NKogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxihgaDnZ0gIw7FQRoq3AN5Apn%2Bufpn0BqQUi2aC%2BcCDpGtQrV82cUcU%2B5iantzHIV7AA49DsahvpNFVKcX51YAJF5BXJmMCO%2F%2Fpyf8GarHHDyKsd7YlflsllOhbI0Iy16LEQM6xMAKNV49mRBVPIKlbE8xiy9J6Rvza9ErwIU7utpy1YHST%2FVOeukiZiQ0kWfMNhnLbsu8hrVb2dwUyD3nstP5rE4uoclwPpHO1qJcQTUNO%2FF8PS0UQToDi94S70eYOXCjJzI4GpXUr40bbkkJB6oIoGnm%2FG5BqfWuKFE3%2FldV2p%2FW%2B%2B3XPY8P0w7UR%2FnQSGeCMS0uT1i8DNosvXTysHQmk61vdrYdxce9RRQkuJlGbridG%2B5oVsBZGg9HXu%2F0i5NJ4dagM%2BMcfp78wnrVIblUwct6vVZ25kYKIZtbZhgtuqOSNMG9yxYq2NspI4jffrsqMjbXDsf3PWN3rtfaOe%2B4jmC9vJAHNNDcIU0SxV%2BOaoRXhCsPGsL%2FeWQma3k0DI%2BSD8VSZ6Pf%2F4uyhkovb3F%2BBPS9zH5UYZ86R7F577YfsHxb2dyPlx2yEUMXM7p3E2kE4ZtMuq77k6WxYNpFOGzefSpI6l5qrRzvHwkItQPEPSSmfzqxg8KurgwZWct6%2BJh7xTXMG8sBnTCR7MDPBjqkAczC2xVjKOQal3EQBceXL83QDZz0HGG%2ByO8BfWmmuLrAtjcNwJo6weETL6hC5aUfPOaXFIciLtVVOp6ls1y4Ti5gqJVM2DDWh5%2FPGOuN3q6K7%2B0cdnL5dlh2rBcJgh3baWcTWlP2kitViLR1%2BeZAP3VBwat9mpuKfKFJSETDz57rkPwNK10Jd2K8NMTlTOC0bqYzUSpXsIW1Sj%2FN%2FcAVYKFUfD0t&X-Amz-Signature=7489ed0c6fcb78f0985b14e6e8b963b51df232d91faa0b5749aec10f744a0756&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

