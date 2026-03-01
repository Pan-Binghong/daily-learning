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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625N5K6IL%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPwiIujYbzBOxXOEYtjKOp%2FOyG0vS%2FwAcvUWyhEP8SSwIgYc8H%2FUW5w6w3g1ZII96M%2F%2BcfKxPiwK4S5KP%2BMiIGVVMq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMPNI0Czh3ttXIhsCircA4VJvmy5E4ueTrO9wQ1E8sipwk2HSdqcmH%2FKJBtqQi7kimyesgUqm%2Bmtrc%2BtFK0OzH5EFTnIxdvvpkvUgpss8bPv1AMNYAe7WzdBzjKGz2nRcXk6qF6Hz3GNy5cIrCm3h%2BVjV1Zcfv2GlUCvtigHdsz2TKC3SylpxH9e%2FgqWwkmwNjNvAq5A7lfv5zl8q6aA1w6KSU8f%2BpLzmD3IopJQAcvKS%2FOE%2FBLVAYPUgKQIlO7x2%2BDKurm0b1Kf3oR2aFo75ggsSm5TJP5AYz3oeOKWLtBxciATvzHevkD4nwH6C1Ms48jCVuLiM8VZC8fNYEQe%2F9Mq1CKelXnEtMKq8WMPgsE8aq9sje3Al%2FWekcGtsUpyOcY9eByc8N1ahqbSE6CzLixJSPoFpq8Pve8atQLTOlG07C1GGab3NXERz3iWZ11612dIi94XgTvWpFziaQYJuym2zHbcAT2cZIC0qnid2N7JV0BdfIMGwesoDEMAk9mZGzgUBLL55bdGB%2B8cKAt42Q6emEuvo3DNwizUHDhfrtTvttOe7tvVrNMGEo14nhfRCr3l1ak08vMkFYOwfBs0SRJJ1cgjTZ5H2zdBKq%2BoxsdjN3RMr03kVDHIyqPZGHsZTp%2B3MpySVVZsSEtAMP%2FNjs0GOqUB2iXif0XsQeAO1yXWgUBdrdC4qRUv1MRWT6VdjWZ%2FgPFv1cN1%2Boz7DQbH4lw1bOxfHkV%2FNIUZIRzOT95wIpRnoFefenkldF0e0XE4JjjXs4oxmgWrs3ykurEwhJXROWvCWEokFtmAzhxmJHNBEPmQ9QP2n7c9gF9Bg%2BWX4R2SKRXewLNg%2B5NgyVpgWdqfVjyuU%2FSzVpZhACBaAmGy1o9JwPbGWmEw&X-Amz-Signature=0115d9ce879cad958bbf038698e3ec3571bdc2b5ed3f851b65b4b854b22b0ed5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625N5K6IL%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPwiIujYbzBOxXOEYtjKOp%2FOyG0vS%2FwAcvUWyhEP8SSwIgYc8H%2FUW5w6w3g1ZII96M%2F%2BcfKxPiwK4S5KP%2BMiIGVVMq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMPNI0Czh3ttXIhsCircA4VJvmy5E4ueTrO9wQ1E8sipwk2HSdqcmH%2FKJBtqQi7kimyesgUqm%2Bmtrc%2BtFK0OzH5EFTnIxdvvpkvUgpss8bPv1AMNYAe7WzdBzjKGz2nRcXk6qF6Hz3GNy5cIrCm3h%2BVjV1Zcfv2GlUCvtigHdsz2TKC3SylpxH9e%2FgqWwkmwNjNvAq5A7lfv5zl8q6aA1w6KSU8f%2BpLzmD3IopJQAcvKS%2FOE%2FBLVAYPUgKQIlO7x2%2BDKurm0b1Kf3oR2aFo75ggsSm5TJP5AYz3oeOKWLtBxciATvzHevkD4nwH6C1Ms48jCVuLiM8VZC8fNYEQe%2F9Mq1CKelXnEtMKq8WMPgsE8aq9sje3Al%2FWekcGtsUpyOcY9eByc8N1ahqbSE6CzLixJSPoFpq8Pve8atQLTOlG07C1GGab3NXERz3iWZ11612dIi94XgTvWpFziaQYJuym2zHbcAT2cZIC0qnid2N7JV0BdfIMGwesoDEMAk9mZGzgUBLL55bdGB%2B8cKAt42Q6emEuvo3DNwizUHDhfrtTvttOe7tvVrNMGEo14nhfRCr3l1ak08vMkFYOwfBs0SRJJ1cgjTZ5H2zdBKq%2BoxsdjN3RMr03kVDHIyqPZGHsZTp%2B3MpySVVZsSEtAMP%2FNjs0GOqUB2iXif0XsQeAO1yXWgUBdrdC4qRUv1MRWT6VdjWZ%2FgPFv1cN1%2Boz7DQbH4lw1bOxfHkV%2FNIUZIRzOT95wIpRnoFefenkldF0e0XE4JjjXs4oxmgWrs3ykurEwhJXROWvCWEokFtmAzhxmJHNBEPmQ9QP2n7c9gF9Bg%2BWX4R2SKRXewLNg%2B5NgyVpgWdqfVjyuU%2FSzVpZhACBaAmGy1o9JwPbGWmEw&X-Amz-Signature=caf1d72b9ae182e3a3aaaf00035ee63a830824e10e13ea9b3998b79bdba97185&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625N5K6IL%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPwiIujYbzBOxXOEYtjKOp%2FOyG0vS%2FwAcvUWyhEP8SSwIgYc8H%2FUW5w6w3g1ZII96M%2F%2BcfKxPiwK4S5KP%2BMiIGVVMq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDMPNI0Czh3ttXIhsCircA4VJvmy5E4ueTrO9wQ1E8sipwk2HSdqcmH%2FKJBtqQi7kimyesgUqm%2Bmtrc%2BtFK0OzH5EFTnIxdvvpkvUgpss8bPv1AMNYAe7WzdBzjKGz2nRcXk6qF6Hz3GNy5cIrCm3h%2BVjV1Zcfv2GlUCvtigHdsz2TKC3SylpxH9e%2FgqWwkmwNjNvAq5A7lfv5zl8q6aA1w6KSU8f%2BpLzmD3IopJQAcvKS%2FOE%2FBLVAYPUgKQIlO7x2%2BDKurm0b1Kf3oR2aFo75ggsSm5TJP5AYz3oeOKWLtBxciATvzHevkD4nwH6C1Ms48jCVuLiM8VZC8fNYEQe%2F9Mq1CKelXnEtMKq8WMPgsE8aq9sje3Al%2FWekcGtsUpyOcY9eByc8N1ahqbSE6CzLixJSPoFpq8Pve8atQLTOlG07C1GGab3NXERz3iWZ11612dIi94XgTvWpFziaQYJuym2zHbcAT2cZIC0qnid2N7JV0BdfIMGwesoDEMAk9mZGzgUBLL55bdGB%2B8cKAt42Q6emEuvo3DNwizUHDhfrtTvttOe7tvVrNMGEo14nhfRCr3l1ak08vMkFYOwfBs0SRJJ1cgjTZ5H2zdBKq%2BoxsdjN3RMr03kVDHIyqPZGHsZTp%2B3MpySVVZsSEtAMP%2FNjs0GOqUB2iXif0XsQeAO1yXWgUBdrdC4qRUv1MRWT6VdjWZ%2FgPFv1cN1%2Boz7DQbH4lw1bOxfHkV%2FNIUZIRzOT95wIpRnoFefenkldF0e0XE4JjjXs4oxmgWrs3ykurEwhJXROWvCWEokFtmAzhxmJHNBEPmQ9QP2n7c9gF9Bg%2BWX4R2SKRXewLNg%2B5NgyVpgWdqfVjyuU%2FSzVpZhACBaAmGy1o9JwPbGWmEw&X-Amz-Signature=eaf4f6870800eb9962c729e4094dc64604cacada044ae4784c43655b39fe89a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

