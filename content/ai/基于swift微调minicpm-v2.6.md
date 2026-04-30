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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QENEDSKY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDxtmM2TaJ9mTG97xtkCdabSUWCY7M83HU7qg8IKSQsvgIhAKlzLS500wmKM9k2aUdLtRsb4pWt3i7r5pr6wAaE4UiAKv8DCAkQABoMNjM3NDIzMTgzODA1IgyiXrG%2FFC2B%2B7ibmvsq3AMDxz4k2UlRRZ3%2FFUWw3hgQ8jhORr5QydizU%2FudsEmg%2Bt7j9dfjToaocDsZW%2FkKkj2YcYvs8x%2BnxmH8o3fRIYcqdpTLN0rXZh%2F3UgS%2FQmWq2X1g7%2FgFmefsjboLdTojOs7kZRCKs%2BMW4T1KbuACHE32bmQjEftVPr9kq4Ll8wjfcEhaI1AEZFTMJqSZMOzQky7W93HV%2FEg9SzocwLmXjq1oIs%2Bf9jvLX3b76EoYp0m5aHr3Q0eoI8dbROWaXXZ7CJkxvYqPYI5Fii6l3gSiMGAhLfaUQwmVrvZZ854J4ftmeBW3FmlJnKgeYU4KPfMqzsAv%2BPhPoqDan5cIY8Mbu%2BJzEX%2F2nWtaKgq1VCHenQgd%2BOcvt3p8jhvpwAQjOqo2f2%2BoQ7lhEgQ%2F9xNcZ4KLNnO4bhmAW1Ghz9jvsK1i2JVSjGTpUjOGGYbtprptWp%2FXrQli3XzaEvsMqPAmnTEeVaeMfHYC3B%2BVNKSqpImO%2BFxLYeTh4N4Rzq4tYjjHjcsSWjS%2B9VECAzf6P1x4P4eMyvMeQz0IKkjKeYzCFce8iz8r8hQwmbMTgN4BBQY1XJ8cgjeuRTWOchdB6nmHxvw6lUQpeRAflpK8couPBMepYSVHl0YeO%2FlQvIt%2FNxPAvzCQnszPBjqkAez3PXcCygHvx%2FOKOdG%2BenuGjB7AXwhn%2FhdUVl0QRgCgMxAZH%2Fc0Bp538SKIGUv%2BhlfwuO%2FrGzKKTa90ZE9R1wG83cldRNJtVuQEGe8rxidQLwt8hajzn8ZG%2BQk8NtBOnlP7JMQsOTDrbFua2%2F7siWBcdIKwV8s8hut0IlXiLIy5cpy7wQMr255zheISQZEgkCfphxhtscYtQW0y%2FnbH8YDarhqK&X-Amz-Signature=54f414a5e486bb5bef1dda9814a6dd5cc36f7a0994d23b6624c05afc5ae09699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QENEDSKY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDxtmM2TaJ9mTG97xtkCdabSUWCY7M83HU7qg8IKSQsvgIhAKlzLS500wmKM9k2aUdLtRsb4pWt3i7r5pr6wAaE4UiAKv8DCAkQABoMNjM3NDIzMTgzODA1IgyiXrG%2FFC2B%2B7ibmvsq3AMDxz4k2UlRRZ3%2FFUWw3hgQ8jhORr5QydizU%2FudsEmg%2Bt7j9dfjToaocDsZW%2FkKkj2YcYvs8x%2BnxmH8o3fRIYcqdpTLN0rXZh%2F3UgS%2FQmWq2X1g7%2FgFmefsjboLdTojOs7kZRCKs%2BMW4T1KbuACHE32bmQjEftVPr9kq4Ll8wjfcEhaI1AEZFTMJqSZMOzQky7W93HV%2FEg9SzocwLmXjq1oIs%2Bf9jvLX3b76EoYp0m5aHr3Q0eoI8dbROWaXXZ7CJkxvYqPYI5Fii6l3gSiMGAhLfaUQwmVrvZZ854J4ftmeBW3FmlJnKgeYU4KPfMqzsAv%2BPhPoqDan5cIY8Mbu%2BJzEX%2F2nWtaKgq1VCHenQgd%2BOcvt3p8jhvpwAQjOqo2f2%2BoQ7lhEgQ%2F9xNcZ4KLNnO4bhmAW1Ghz9jvsK1i2JVSjGTpUjOGGYbtprptWp%2FXrQli3XzaEvsMqPAmnTEeVaeMfHYC3B%2BVNKSqpImO%2BFxLYeTh4N4Rzq4tYjjHjcsSWjS%2B9VECAzf6P1x4P4eMyvMeQz0IKkjKeYzCFce8iz8r8hQwmbMTgN4BBQY1XJ8cgjeuRTWOchdB6nmHxvw6lUQpeRAflpK8couPBMepYSVHl0YeO%2FlQvIt%2FNxPAvzCQnszPBjqkAez3PXcCygHvx%2FOKOdG%2BenuGjB7AXwhn%2FhdUVl0QRgCgMxAZH%2Fc0Bp538SKIGUv%2BhlfwuO%2FrGzKKTa90ZE9R1wG83cldRNJtVuQEGe8rxidQLwt8hajzn8ZG%2BQk8NtBOnlP7JMQsOTDrbFua2%2F7siWBcdIKwV8s8hut0IlXiLIy5cpy7wQMr255zheISQZEgkCfphxhtscYtQW0y%2FnbH8YDarhqK&X-Amz-Signature=096bb8a764d2bba4bbfba08d66fc448e57b7933a531c1d30c8507642d0b31e7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QENEDSKY%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDxtmM2TaJ9mTG97xtkCdabSUWCY7M83HU7qg8IKSQsvgIhAKlzLS500wmKM9k2aUdLtRsb4pWt3i7r5pr6wAaE4UiAKv8DCAkQABoMNjM3NDIzMTgzODA1IgyiXrG%2FFC2B%2B7ibmvsq3AMDxz4k2UlRRZ3%2FFUWw3hgQ8jhORr5QydizU%2FudsEmg%2Bt7j9dfjToaocDsZW%2FkKkj2YcYvs8x%2BnxmH8o3fRIYcqdpTLN0rXZh%2F3UgS%2FQmWq2X1g7%2FgFmefsjboLdTojOs7kZRCKs%2BMW4T1KbuACHE32bmQjEftVPr9kq4Ll8wjfcEhaI1AEZFTMJqSZMOzQky7W93HV%2FEg9SzocwLmXjq1oIs%2Bf9jvLX3b76EoYp0m5aHr3Q0eoI8dbROWaXXZ7CJkxvYqPYI5Fii6l3gSiMGAhLfaUQwmVrvZZ854J4ftmeBW3FmlJnKgeYU4KPfMqzsAv%2BPhPoqDan5cIY8Mbu%2BJzEX%2F2nWtaKgq1VCHenQgd%2BOcvt3p8jhvpwAQjOqo2f2%2BoQ7lhEgQ%2F9xNcZ4KLNnO4bhmAW1Ghz9jvsK1i2JVSjGTpUjOGGYbtprptWp%2FXrQli3XzaEvsMqPAmnTEeVaeMfHYC3B%2BVNKSqpImO%2BFxLYeTh4N4Rzq4tYjjHjcsSWjS%2B9VECAzf6P1x4P4eMyvMeQz0IKkjKeYzCFce8iz8r8hQwmbMTgN4BBQY1XJ8cgjeuRTWOchdB6nmHxvw6lUQpeRAflpK8couPBMepYSVHl0YeO%2FlQvIt%2FNxPAvzCQnszPBjqkAez3PXcCygHvx%2FOKOdG%2BenuGjB7AXwhn%2FhdUVl0QRgCgMxAZH%2Fc0Bp538SKIGUv%2BhlfwuO%2FrGzKKTa90ZE9R1wG83cldRNJtVuQEGe8rxidQLwt8hajzn8ZG%2BQk8NtBOnlP7JMQsOTDrbFua2%2F7siWBcdIKwV8s8hut0IlXiLIy5cpy7wQMr255zheISQZEgkCfphxhtscYtQW0y%2FnbH8YDarhqK&X-Amz-Signature=0acd10c4d4507d56e1d4c137a9eafbd384e2209aef3a7c122d32df4bebd66368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

