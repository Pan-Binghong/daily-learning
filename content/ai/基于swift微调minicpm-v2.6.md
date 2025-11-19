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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAD4UTCK%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIG3q3NU%2F0YnpjDQ6C67NV%2BwQhwQlygsUnIbPOFXGsWgSAiAxVEwgPxCuVcyx2MdHZC%2Fte0r3HH95v1ZKnYh1vi%2FrsSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc%2FS5VUSLy%2FL%2F9pVXKtwDoldQpYUy2XA7mVw4P3aJVHYZhFekkutD49bEqQMh%2FO6frJl8gokEcz6hvkAS8ZeYruleAO%2BW3q2nVTvtG4d3XlT3Ak%2B1UYJfSGxO91p28DkENZh7IYdnGH2LuX7FLMRvVPGDVuMx34rJdrS%2BwqYlOgAcN9QzxkeE1SD66v8z8S1lnuNB7NFVB1K5fYiSZpg86Uf8Y0lzCTcYAn%2BIxs0g%2FdDa70IyifT7cBR%2FMHiV4TumZrcqaJNpNunPDJzeBksaobgs7mIfgxE10gQRy%2BPyO78odNHUXrKiKoFUvVSk8o2%2FI25bZM%2BeHES6Qo%2FOgDUw102JgActuY71wHaFOlpemOVLCvRfm1scgDD3yAnDE4h0zyLkWRlUfwNwOXpC7%2FUreDhsA1zyUDkuPKE0oXBsfMtgesbSDp48g%2BxsHqKdOPxwsPtL7nGHCwtd6tuIvW23sKadceX2ifSg96XiAP094xzh3I3oAcCvmMXW8GBt%2F%2FaQ3GVWwOwHPAvnpFlJPhp5DyldE%2F4CJ8pYLPrQjELZBy7FiqNm88%2Bc5vFGcm6L3URZLkdzt9p3uGkaR48NWWtBtXVyAhOI95X9jQZGHDITwVSwlbtPy5Q6kCVe3OW3yfp%2B%2B2rVTRn78cmKH7Yw2sj0yAY6pgFgOY6bN12yTzkH841uzpQBy%2FdSRUh7zJ%2BI%2BJ2OAkl%2Fe7lztNGCsE52tKDAYsYRJ1AnbcmbJuE2z4uYu1IRmeXg68WHNc%2B%2F8SqLZoSc3jucZ3dO6OIRHh6jYYN5N9F%2FiTzLqleTYAl24WuksMDj2GvnT4pGNkH%2BclkF0mZJ7J7mxU9DuAPf49%2Fjbw%2B0TdDoKVrAsqf3%2FxtTR0FD1MBMyvymTieWsZLF&X-Amz-Signature=2b5a37df604871d9aa7be3e6c7566e0ee82b86adf3af9d21c79f4449334fa3cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAD4UTCK%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIG3q3NU%2F0YnpjDQ6C67NV%2BwQhwQlygsUnIbPOFXGsWgSAiAxVEwgPxCuVcyx2MdHZC%2Fte0r3HH95v1ZKnYh1vi%2FrsSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc%2FS5VUSLy%2FL%2F9pVXKtwDoldQpYUy2XA7mVw4P3aJVHYZhFekkutD49bEqQMh%2FO6frJl8gokEcz6hvkAS8ZeYruleAO%2BW3q2nVTvtG4d3XlT3Ak%2B1UYJfSGxO91p28DkENZh7IYdnGH2LuX7FLMRvVPGDVuMx34rJdrS%2BwqYlOgAcN9QzxkeE1SD66v8z8S1lnuNB7NFVB1K5fYiSZpg86Uf8Y0lzCTcYAn%2BIxs0g%2FdDa70IyifT7cBR%2FMHiV4TumZrcqaJNpNunPDJzeBksaobgs7mIfgxE10gQRy%2BPyO78odNHUXrKiKoFUvVSk8o2%2FI25bZM%2BeHES6Qo%2FOgDUw102JgActuY71wHaFOlpemOVLCvRfm1scgDD3yAnDE4h0zyLkWRlUfwNwOXpC7%2FUreDhsA1zyUDkuPKE0oXBsfMtgesbSDp48g%2BxsHqKdOPxwsPtL7nGHCwtd6tuIvW23sKadceX2ifSg96XiAP094xzh3I3oAcCvmMXW8GBt%2F%2FaQ3GVWwOwHPAvnpFlJPhp5DyldE%2F4CJ8pYLPrQjELZBy7FiqNm88%2Bc5vFGcm6L3URZLkdzt9p3uGkaR48NWWtBtXVyAhOI95X9jQZGHDITwVSwlbtPy5Q6kCVe3OW3yfp%2B%2B2rVTRn78cmKH7Yw2sj0yAY6pgFgOY6bN12yTzkH841uzpQBy%2FdSRUh7zJ%2BI%2BJ2OAkl%2Fe7lztNGCsE52tKDAYsYRJ1AnbcmbJuE2z4uYu1IRmeXg68WHNc%2B%2F8SqLZoSc3jucZ3dO6OIRHh6jYYN5N9F%2FiTzLqleTYAl24WuksMDj2GvnT4pGNkH%2BclkF0mZJ7J7mxU9DuAPf49%2Fjbw%2B0TdDoKVrAsqf3%2FxtTR0FD1MBMyvymTieWsZLF&X-Amz-Signature=76d2163380f78e246109798ed6b37e1b3eb40bd94310daf1959e0d281980030a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAD4UTCK%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIG3q3NU%2F0YnpjDQ6C67NV%2BwQhwQlygsUnIbPOFXGsWgSAiAxVEwgPxCuVcyx2MdHZC%2Fte0r3HH95v1ZKnYh1vi%2FrsSqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMc%2FS5VUSLy%2FL%2F9pVXKtwDoldQpYUy2XA7mVw4P3aJVHYZhFekkutD49bEqQMh%2FO6frJl8gokEcz6hvkAS8ZeYruleAO%2BW3q2nVTvtG4d3XlT3Ak%2B1UYJfSGxO91p28DkENZh7IYdnGH2LuX7FLMRvVPGDVuMx34rJdrS%2BwqYlOgAcN9QzxkeE1SD66v8z8S1lnuNB7NFVB1K5fYiSZpg86Uf8Y0lzCTcYAn%2BIxs0g%2FdDa70IyifT7cBR%2FMHiV4TumZrcqaJNpNunPDJzeBksaobgs7mIfgxE10gQRy%2BPyO78odNHUXrKiKoFUvVSk8o2%2FI25bZM%2BeHES6Qo%2FOgDUw102JgActuY71wHaFOlpemOVLCvRfm1scgDD3yAnDE4h0zyLkWRlUfwNwOXpC7%2FUreDhsA1zyUDkuPKE0oXBsfMtgesbSDp48g%2BxsHqKdOPxwsPtL7nGHCwtd6tuIvW23sKadceX2ifSg96XiAP094xzh3I3oAcCvmMXW8GBt%2F%2FaQ3GVWwOwHPAvnpFlJPhp5DyldE%2F4CJ8pYLPrQjELZBy7FiqNm88%2Bc5vFGcm6L3URZLkdzt9p3uGkaR48NWWtBtXVyAhOI95X9jQZGHDITwVSwlbtPy5Q6kCVe3OW3yfp%2B%2B2rVTRn78cmKH7Yw2sj0yAY6pgFgOY6bN12yTzkH841uzpQBy%2FdSRUh7zJ%2BI%2BJ2OAkl%2Fe7lztNGCsE52tKDAYsYRJ1AnbcmbJuE2z4uYu1IRmeXg68WHNc%2B%2F8SqLZoSc3jucZ3dO6OIRHh6jYYN5N9F%2FiTzLqleTYAl24WuksMDj2GvnT4pGNkH%2BclkF0mZJ7J7mxU9DuAPf49%2Fjbw%2B0TdDoKVrAsqf3%2FxtTR0FD1MBMyvymTieWsZLF&X-Amz-Signature=80819963b034b2f752bc6267ff4988d2e49bf357ff504deb639f0886cd0bdb63&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

