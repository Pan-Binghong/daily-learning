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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAEOVAI3%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCPHMSE%2Bead2ooauzataAA%2Fj0ppKmTxbcUcho8n%2BpFsnQIhALrRCOYhJ%2BD81TwF5QrSjL2VQLGv2WsravBFPL%2BCYv6JKv8DCCUQABoMNjM3NDIzMTgzODA1Igzs7lxfxYoytm6zBRMq3AOWS3%2BtDdsM36GKk%2FTM%2FowIz0ASXETE4kZeafcRZ0430s9537x7C0VwjBWxE%2BJFafzURcDcxuZtPOfZhjvwnM9HIlPa2ENwaXTC0Ffk5hm7aQhJtr0XLXd7rYLwVw3KSUfbwMt2zx8tYFMZy8e3mSClcDfT1sAY%2FaW7VcIyRNwLO%2FScjTrxnZSysV%2BEp3Bsc4YVxPRBm3%2BFDWLnkRyDcraWk%2B6o2K%2FY%2F6FsZjEukYmoQ8%2BLPLG9BdhKZSARGRZZBFmaYl1VdRMdlmXafXvfCcEwRi8Nm3SJdeqrQvrehJPPE5bcdbnHDUpVC5qMeQrgbYghRpTibToN7hSnbCMDz9wXlw1aQFP91uKzvyuOdWkWPSwUhz1BlUHV7uT4UgWg4ykiwMdAaWntFCpfgI%2FUd8f7pYseu7A6o%2Baj8IeFjhG3E3LMd1nLDkIdrOxPSYvJZ7wuqUfJoJJEC%2BwEnoKSMI5U2IUVS5KuDRKJ0PS9SJH2LImfL0aIOJgEfX9bAbNCfVRZ2d%2FFsy%2FHPKJPMri5XwVqSqlVXf%2BAYnKhPRFGdUbOONAgck%2B2Tc9K%2Fk2wUzhVmAbzRirDfnESROISVMwKUD5%2BgeWL%2FKXDzJge0m7NtpiFWyGRR%2FBnRAUwD8zRejCf%2FbjNBjqkAYZlGIpL8sfHu1b9Pr8iNaybU4H3DG2iP%2FVI6HaPeyrtl554VvLJqOuCgnQShkIQytIRdgCRR4UCuFCFNSmmYPb2JFtWDT1YhM8RMCBms165NLW%2FXpc4q4G0wTaaXEhzFhRG59fT9G3tx1cTvuWDaUZLT5417NFUfwn9HyuRTjE%2Brdg%2BTszTVnrUjaqMfDVAAHJwqJejwWF7muTqt4nn7KT6Il6n&X-Amz-Signature=22cf030bd2b1598f8d97e7e76e19467edcbd118742b0c4ea940be22ce1e587f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAEOVAI3%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCPHMSE%2Bead2ooauzataAA%2Fj0ppKmTxbcUcho8n%2BpFsnQIhALrRCOYhJ%2BD81TwF5QrSjL2VQLGv2WsravBFPL%2BCYv6JKv8DCCUQABoMNjM3NDIzMTgzODA1Igzs7lxfxYoytm6zBRMq3AOWS3%2BtDdsM36GKk%2FTM%2FowIz0ASXETE4kZeafcRZ0430s9537x7C0VwjBWxE%2BJFafzURcDcxuZtPOfZhjvwnM9HIlPa2ENwaXTC0Ffk5hm7aQhJtr0XLXd7rYLwVw3KSUfbwMt2zx8tYFMZy8e3mSClcDfT1sAY%2FaW7VcIyRNwLO%2FScjTrxnZSysV%2BEp3Bsc4YVxPRBm3%2BFDWLnkRyDcraWk%2B6o2K%2FY%2F6FsZjEukYmoQ8%2BLPLG9BdhKZSARGRZZBFmaYl1VdRMdlmXafXvfCcEwRi8Nm3SJdeqrQvrehJPPE5bcdbnHDUpVC5qMeQrgbYghRpTibToN7hSnbCMDz9wXlw1aQFP91uKzvyuOdWkWPSwUhz1BlUHV7uT4UgWg4ykiwMdAaWntFCpfgI%2FUd8f7pYseu7A6o%2Baj8IeFjhG3E3LMd1nLDkIdrOxPSYvJZ7wuqUfJoJJEC%2BwEnoKSMI5U2IUVS5KuDRKJ0PS9SJH2LImfL0aIOJgEfX9bAbNCfVRZ2d%2FFsy%2FHPKJPMri5XwVqSqlVXf%2BAYnKhPRFGdUbOONAgck%2B2Tc9K%2Fk2wUzhVmAbzRirDfnESROISVMwKUD5%2BgeWL%2FKXDzJge0m7NtpiFWyGRR%2FBnRAUwD8zRejCf%2FbjNBjqkAYZlGIpL8sfHu1b9Pr8iNaybU4H3DG2iP%2FVI6HaPeyrtl554VvLJqOuCgnQShkIQytIRdgCRR4UCuFCFNSmmYPb2JFtWDT1YhM8RMCBms165NLW%2FXpc4q4G0wTaaXEhzFhRG59fT9G3tx1cTvuWDaUZLT5417NFUfwn9HyuRTjE%2Brdg%2BTszTVnrUjaqMfDVAAHJwqJejwWF7muTqt4nn7KT6Il6n&X-Amz-Signature=40b7e83954aa7706ce38ed89e8b68f4baaf2a107dfe00567b0b0c28af544d315&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAEOVAI3%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJIMEYCIQCPHMSE%2Bead2ooauzataAA%2Fj0ppKmTxbcUcho8n%2BpFsnQIhALrRCOYhJ%2BD81TwF5QrSjL2VQLGv2WsravBFPL%2BCYv6JKv8DCCUQABoMNjM3NDIzMTgzODA1Igzs7lxfxYoytm6zBRMq3AOWS3%2BtDdsM36GKk%2FTM%2FowIz0ASXETE4kZeafcRZ0430s9537x7C0VwjBWxE%2BJFafzURcDcxuZtPOfZhjvwnM9HIlPa2ENwaXTC0Ffk5hm7aQhJtr0XLXd7rYLwVw3KSUfbwMt2zx8tYFMZy8e3mSClcDfT1sAY%2FaW7VcIyRNwLO%2FScjTrxnZSysV%2BEp3Bsc4YVxPRBm3%2BFDWLnkRyDcraWk%2B6o2K%2FY%2F6FsZjEukYmoQ8%2BLPLG9BdhKZSARGRZZBFmaYl1VdRMdlmXafXvfCcEwRi8Nm3SJdeqrQvrehJPPE5bcdbnHDUpVC5qMeQrgbYghRpTibToN7hSnbCMDz9wXlw1aQFP91uKzvyuOdWkWPSwUhz1BlUHV7uT4UgWg4ykiwMdAaWntFCpfgI%2FUd8f7pYseu7A6o%2Baj8IeFjhG3E3LMd1nLDkIdrOxPSYvJZ7wuqUfJoJJEC%2BwEnoKSMI5U2IUVS5KuDRKJ0PS9SJH2LImfL0aIOJgEfX9bAbNCfVRZ2d%2FFsy%2FHPKJPMri5XwVqSqlVXf%2BAYnKhPRFGdUbOONAgck%2B2Tc9K%2Fk2wUzhVmAbzRirDfnESROISVMwKUD5%2BgeWL%2FKXDzJge0m7NtpiFWyGRR%2FBnRAUwD8zRejCf%2FbjNBjqkAYZlGIpL8sfHu1b9Pr8iNaybU4H3DG2iP%2FVI6HaPeyrtl554VvLJqOuCgnQShkIQytIRdgCRR4UCuFCFNSmmYPb2JFtWDT1YhM8RMCBms165NLW%2FXpc4q4G0wTaaXEhzFhRG59fT9G3tx1cTvuWDaUZLT5417NFUfwn9HyuRTjE%2Brdg%2BTszTVnrUjaqMfDVAAHJwqJejwWF7muTqt4nn7KT6Il6n&X-Amz-Signature=89ba7a0c67a0fdf3102195e90bc53d9baef175a44586c7c62c4799f9ae9455d4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

