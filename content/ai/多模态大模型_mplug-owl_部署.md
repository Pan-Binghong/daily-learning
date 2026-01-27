---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN5ZOK5E%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2F20i7qehjuVhA8Klt8r2i9TGPR0F1PjdB7tTWpbs%2BiAiAjiTw49TY8fYTQfqeTG8g0EY0HNcogWnwoqViKt6H4Ayr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIM9NXS%2FJLWaNzYRZGnKtwD%2BCutB7k5yvLHP89kpTx4I3DmAbKcaCHHkMYCNCWwL0owX75w2rQa6CtUhYnUgqA0ZIVP%2Bmg7QPqYpCAO%2FrSY9N9AXUJTN5BmrYvTt2JMtqUiy8NrTW2hEHFJamePTHSBbn3kBMf4U%2BI8%2Frk4e4yL2WlgIM571OAM%2ByFU3ety%2FP9gV1g3EbLbvq5ws3B6Hx6he4KjRJFcDYwt9WujxcoB0wuxfritgdNosrPQRpzBF5ZW63u6UoWVNjVYUSUJk5cLXqSh5M3IbXHc7Rn17AQZSIWuv%2BkML%2FGJG7y9%2BB0sbfE9lcRBe7YgJwYUyogkdztspXB9yOd7Anh6ELbJzis%2BhYCzgbdBUp1ZHmrzBXroXCXPFC82Cne6uG3AfRz67ut13V5GP%2BlnS2HoNrvXj7U%2BeMrjs06g4jwiQlJWZn4WNI0vwwkX%2FSUAWb5J4B8GQmfmFNFsojAO0SOVgzF6Upm8LSmJufML%2BXPqbXak%2FB9bx%2BB3ZhWvGJSvrT%2B6k0lguxcRkynwQLQuXZ22AFMnBdgDTXirIMruOvtmQDNcOZ8rBLtL8LHF7LFlsiEJUuhMPMGKXK1ww4z%2BOrYFme35v7ZXRs%2BGhHn90av5ZZngj20h%2FD00QNqeAofAHRjA3BQws9LgywY6pgH3B72pn%2F%2B0%2F5kEn7vX%2FqTGZQtfDh1KsAqUM5ZZq2A%2FSfifCVsEyDkmR%2B1CiQxJA%2BVc6nGIhl4r%2FnXbi9VGKvPa2Y5L%2FF7WQSaeEaC5RPOnzvPCM50BhqgDB4OoR9EtAyHTsNQuch5yR%2BLc9cpbTLzt0fuwYkkkgW9fBISVq5Ri2hYqkSlgy71W84aNqiB34q8J4cKhSqApjwxhJhKwERAleSnJWRBz&X-Amz-Signature=c23dbf2e29c958dd03852e4f9c9dc50f2c899e2ed8f343b0b12f16c9027786f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VN5ZOK5E%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2F20i7qehjuVhA8Klt8r2i9TGPR0F1PjdB7tTWpbs%2BiAiAjiTw49TY8fYTQfqeTG8g0EY0HNcogWnwoqViKt6H4Ayr%2FAwhMEAAaDDYzNzQyMzE4MzgwNSIM9NXS%2FJLWaNzYRZGnKtwD%2BCutB7k5yvLHP89kpTx4I3DmAbKcaCHHkMYCNCWwL0owX75w2rQa6CtUhYnUgqA0ZIVP%2Bmg7QPqYpCAO%2FrSY9N9AXUJTN5BmrYvTt2JMtqUiy8NrTW2hEHFJamePTHSBbn3kBMf4U%2BI8%2Frk4e4yL2WlgIM571OAM%2ByFU3ety%2FP9gV1g3EbLbvq5ws3B6Hx6he4KjRJFcDYwt9WujxcoB0wuxfritgdNosrPQRpzBF5ZW63u6UoWVNjVYUSUJk5cLXqSh5M3IbXHc7Rn17AQZSIWuv%2BkML%2FGJG7y9%2BB0sbfE9lcRBe7YgJwYUyogkdztspXB9yOd7Anh6ELbJzis%2BhYCzgbdBUp1ZHmrzBXroXCXPFC82Cne6uG3AfRz67ut13V5GP%2BlnS2HoNrvXj7U%2BeMrjs06g4jwiQlJWZn4WNI0vwwkX%2FSUAWb5J4B8GQmfmFNFsojAO0SOVgzF6Upm8LSmJufML%2BXPqbXak%2FB9bx%2BB3ZhWvGJSvrT%2B6k0lguxcRkynwQLQuXZ22AFMnBdgDTXirIMruOvtmQDNcOZ8rBLtL8LHF7LFlsiEJUuhMPMGKXK1ww4z%2BOrYFme35v7ZXRs%2BGhHn90av5ZZngj20h%2FD00QNqeAofAHRjA3BQws9LgywY6pgH3B72pn%2F%2B0%2F5kEn7vX%2FqTGZQtfDh1KsAqUM5ZZq2A%2FSfifCVsEyDkmR%2B1CiQxJA%2BVc6nGIhl4r%2FnXbi9VGKvPa2Y5L%2FF7WQSaeEaC5RPOnzvPCM50BhqgDB4OoR9EtAyHTsNQuch5yR%2BLc9cpbTLzt0fuwYkkkgW9fBISVq5Ri2hYqkSlgy71W84aNqiB34q8J4cKhSqApjwxhJhKwERAleSnJWRBz&X-Amz-Signature=2be9bb4e8c67084f862ab9088cd73703a1f803e1f90068a17cd48ae53fddad2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

