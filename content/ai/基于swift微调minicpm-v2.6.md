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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BYMLXV%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDZ%2B3Q4%2FsOm%2FfTARkTRhFf9rb2g8bdIMwbcJzF7q3yBYQIhAMAYn867y8vf4CeICnpbsxhw0obM3A%2FYuFNtdniNJb2EKv8DCCwQABoMNjM3NDIzMTgzODA1IgxlZUhIp5Yjnl4SUmMq3APiJ0XU%2BHVmTBzs%2BvC0OZ4CcicqG8Zn1VqMKVMiFTz1n2mdaE03qLz2P4mZGS0Vz4fuuGHTcQfL3B6vt9eOlwh3cEUChHwE6abCnXmh6VGs7q9XZ3JvpO0cc0vgmU%2BrXmH4AwXVA495OTym%2B0SAbj8G5El79jr5x26gSKZ707%2FkcKvWnHQarmurMSl86HvNl3QXIyliKCtJzSvTD%2BJP2cT3%2BJCfF%2Fv4CdmJaNLOZsBm%2FHZw%2FcmpURKbgqXGtqJhm7pikaotFuF6Son9B%2Baug233gjDFzJt4bxiB1PA6XDaqTpQ26EMQAtY%2BGJEq8iOciM1lJtAgQbqoWn3hlevSjgzKZ1FSM4SsMrkObHSRQrxUpxd4iEisp2AfgqtbJ4ICv%2BIx%2F8j5iUhMFb7Qn4TUupY5iVfqGuRZadOlEwaEwZGiEU%2FzF%2BS7AxZ9MAGUE5S52A44875M%2BvioOUdNwxZK7NHOeNhCELSEp8yMxT59dLCpCBnerjgl7ee7qe%2Ff7o%2BXNuIpLOb6mHlOI5dTjtuoVygYv1JH%2FiXdr0zDNNTAUEGFsxjjWBRPoFDH%2BNQgkTPGLnETNR0%2BKIE6scJtS77C6Pz4weybaA84pYycTinuz1iAvgTIyeNoeidezt41mzCB1ZvPBjqkAR6lROjaAEaig6d801x2A3oFtzebqB%2BbP8NQfinmkDIyn9YEFO%2FVlbKAbnSM9ZXL8DslVT2s2R9p6klci5SjB26UlCt1WCNTAdbu8svfKT7f4nhR1CqZ3PSEaOu2IRya9RvDnE0YHy1nMuKPt%2B35snseqjr%2F4r7AoTQlh7lOcUCk1YODfSCEyVHHsMDk6j3NcHhiOSX4gKQXradnQU7IQW7cukr8&X-Amz-Signature=5156aceb383e83d46174634363bb867e9055d26f6f157467fd9ef80c25aab3ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BYMLXV%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDZ%2B3Q4%2FsOm%2FfTARkTRhFf9rb2g8bdIMwbcJzF7q3yBYQIhAMAYn867y8vf4CeICnpbsxhw0obM3A%2FYuFNtdniNJb2EKv8DCCwQABoMNjM3NDIzMTgzODA1IgxlZUhIp5Yjnl4SUmMq3APiJ0XU%2BHVmTBzs%2BvC0OZ4CcicqG8Zn1VqMKVMiFTz1n2mdaE03qLz2P4mZGS0Vz4fuuGHTcQfL3B6vt9eOlwh3cEUChHwE6abCnXmh6VGs7q9XZ3JvpO0cc0vgmU%2BrXmH4AwXVA495OTym%2B0SAbj8G5El79jr5x26gSKZ707%2FkcKvWnHQarmurMSl86HvNl3QXIyliKCtJzSvTD%2BJP2cT3%2BJCfF%2Fv4CdmJaNLOZsBm%2FHZw%2FcmpURKbgqXGtqJhm7pikaotFuF6Son9B%2Baug233gjDFzJt4bxiB1PA6XDaqTpQ26EMQAtY%2BGJEq8iOciM1lJtAgQbqoWn3hlevSjgzKZ1FSM4SsMrkObHSRQrxUpxd4iEisp2AfgqtbJ4ICv%2BIx%2F8j5iUhMFb7Qn4TUupY5iVfqGuRZadOlEwaEwZGiEU%2FzF%2BS7AxZ9MAGUE5S52A44875M%2BvioOUdNwxZK7NHOeNhCELSEp8yMxT59dLCpCBnerjgl7ee7qe%2Ff7o%2BXNuIpLOb6mHlOI5dTjtuoVygYv1JH%2FiXdr0zDNNTAUEGFsxjjWBRPoFDH%2BNQgkTPGLnETNR0%2BKIE6scJtS77C6Pz4weybaA84pYycTinuz1iAvgTIyeNoeidezt41mzCB1ZvPBjqkAR6lROjaAEaig6d801x2A3oFtzebqB%2BbP8NQfinmkDIyn9YEFO%2FVlbKAbnSM9ZXL8DslVT2s2R9p6klci5SjB26UlCt1WCNTAdbu8svfKT7f4nhR1CqZ3PSEaOu2IRya9RvDnE0YHy1nMuKPt%2B35snseqjr%2F4r7AoTQlh7lOcUCk1YODfSCEyVHHsMDk6j3NcHhiOSX4gKQXradnQU7IQW7cukr8&X-Amz-Signature=4fd33d2805dc1f8bea753019d019135064fa201dd2820e8d45f1dd60c8f0252a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4BYMLXV%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDZ%2B3Q4%2FsOm%2FfTARkTRhFf9rb2g8bdIMwbcJzF7q3yBYQIhAMAYn867y8vf4CeICnpbsxhw0obM3A%2FYuFNtdniNJb2EKv8DCCwQABoMNjM3NDIzMTgzODA1IgxlZUhIp5Yjnl4SUmMq3APiJ0XU%2BHVmTBzs%2BvC0OZ4CcicqG8Zn1VqMKVMiFTz1n2mdaE03qLz2P4mZGS0Vz4fuuGHTcQfL3B6vt9eOlwh3cEUChHwE6abCnXmh6VGs7q9XZ3JvpO0cc0vgmU%2BrXmH4AwXVA495OTym%2B0SAbj8G5El79jr5x26gSKZ707%2FkcKvWnHQarmurMSl86HvNl3QXIyliKCtJzSvTD%2BJP2cT3%2BJCfF%2Fv4CdmJaNLOZsBm%2FHZw%2FcmpURKbgqXGtqJhm7pikaotFuF6Son9B%2Baug233gjDFzJt4bxiB1PA6XDaqTpQ26EMQAtY%2BGJEq8iOciM1lJtAgQbqoWn3hlevSjgzKZ1FSM4SsMrkObHSRQrxUpxd4iEisp2AfgqtbJ4ICv%2BIx%2F8j5iUhMFb7Qn4TUupY5iVfqGuRZadOlEwaEwZGiEU%2FzF%2BS7AxZ9MAGUE5S52A44875M%2BvioOUdNwxZK7NHOeNhCELSEp8yMxT59dLCpCBnerjgl7ee7qe%2Ff7o%2BXNuIpLOb6mHlOI5dTjtuoVygYv1JH%2FiXdr0zDNNTAUEGFsxjjWBRPoFDH%2BNQgkTPGLnETNR0%2BKIE6scJtS77C6Pz4weybaA84pYycTinuz1iAvgTIyeNoeidezt41mzCB1ZvPBjqkAR6lROjaAEaig6d801x2A3oFtzebqB%2BbP8NQfinmkDIyn9YEFO%2FVlbKAbnSM9ZXL8DslVT2s2R9p6klci5SjB26UlCt1WCNTAdbu8svfKT7f4nhR1CqZ3PSEaOu2IRya9RvDnE0YHy1nMuKPt%2B35snseqjr%2F4r7AoTQlh7lOcUCk1YODfSCEyVHHsMDk6j3NcHhiOSX4gKQXradnQU7IQW7cukr8&X-Amz-Signature=56946d7e11f0fc5ef8856dbd6488859931eb7ee83789b09d73808bba914cc032&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

