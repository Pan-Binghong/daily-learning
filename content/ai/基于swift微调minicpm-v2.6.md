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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WTFTXPQ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNyvZ1acuHsZu9D1Liw38MA8CODSU7MmTSGVvFzCfenwIhAJ%2BKJF1w4gqypM806bU4qSdBigpTJZunQSAAlTPDsQLrKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0kqgwlSWw2dTnlE8q3AMGdYoJ44NH8QxZBmBEdweGkrRUWloyIkLi3pOAIrT0h2pxtu%2BMYfI5fozRr60ReiFMsxpuU2wQvpGr2YDv%2BuEXZfi2W5aIXA6YhHMDWPZvQ7NZnY90pDKW1C1pFsrWjwD0PKksLqFzkzi8rGC%2F%2FP3%2BuAbo%2FwrdEJbQVQScNyHfYYB6hH6lIP5Vu6tI%2FsiSXGeeZX3ercIFRAhlwpVQSNh38m7nC%2ByQ%2BWurdR%2FN4t%2FCoXCaFaX7gqTnbHki7oJhbbbua%2FrE8fxMN9BCPxV6yNVJ84OaxnPDowul53BFeP0h3ERFjtsLj0sGKFOX%2FD0aKTHHRAnLkk45Y63k2E%2BHtDQq81PHWPHEuALbw%2Fl7B4L%2FRt4Tq%2Ff71Y08PCX0ueoiQqigzJ%2BIPHPxRS0wG7mMZIph%2FkBQ7WKiasX%2BuieRT%2BMo6ksBZw9OXajGEAlDGmdtnaBNh8VkJUGe7yQgo4%2F%2FTUeMiVsl%2B11mrdqtucKrstKP8xNoBGOmz0RbbPAl0kGQGMpeSug2Yl3U8s2G%2BPdNptl15R31VPQEfSrePjeaK%2BPvNWDe%2FIOfKByPuTcjzlkKKtG5TZWcLBu4EF5pWq27jwsprXyZiK%2FG2FpIfim0O9R%2BMdlAkGHUPCxPORP2pjCEn9TMBjqkAaoank4XuXMmMjidzRQ6fz7elKZS4iIxg5YJvJ3l30jQcB7pv07dcoxNSPWQukTWVF9ruMg1jATVnsuBoDXLIPAKGRuje9kz3WJARg%2B%2B3O%2BHIboJspZKI3L06gqXv8J9vDWRNUn5%2BjML6ShE6IjHEd%2FTVadXnYsl3yRTpVw7k%2B8Tt%2B6Zr1KefBRWyuUUT%2BX5f5bMt3UAPgdPiZMacyWiWUT0EbXx&X-Amz-Signature=148e4a9b4b54521dfc06058352d2d4fb7ff7377adebe2b549560ba2f363e9a36&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WTFTXPQ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNyvZ1acuHsZu9D1Liw38MA8CODSU7MmTSGVvFzCfenwIhAJ%2BKJF1w4gqypM806bU4qSdBigpTJZunQSAAlTPDsQLrKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0kqgwlSWw2dTnlE8q3AMGdYoJ44NH8QxZBmBEdweGkrRUWloyIkLi3pOAIrT0h2pxtu%2BMYfI5fozRr60ReiFMsxpuU2wQvpGr2YDv%2BuEXZfi2W5aIXA6YhHMDWPZvQ7NZnY90pDKW1C1pFsrWjwD0PKksLqFzkzi8rGC%2F%2FP3%2BuAbo%2FwrdEJbQVQScNyHfYYB6hH6lIP5Vu6tI%2FsiSXGeeZX3ercIFRAhlwpVQSNh38m7nC%2ByQ%2BWurdR%2FN4t%2FCoXCaFaX7gqTnbHki7oJhbbbua%2FrE8fxMN9BCPxV6yNVJ84OaxnPDowul53BFeP0h3ERFjtsLj0sGKFOX%2FD0aKTHHRAnLkk45Y63k2E%2BHtDQq81PHWPHEuALbw%2Fl7B4L%2FRt4Tq%2Ff71Y08PCX0ueoiQqigzJ%2BIPHPxRS0wG7mMZIph%2FkBQ7WKiasX%2BuieRT%2BMo6ksBZw9OXajGEAlDGmdtnaBNh8VkJUGe7yQgo4%2F%2FTUeMiVsl%2B11mrdqtucKrstKP8xNoBGOmz0RbbPAl0kGQGMpeSug2Yl3U8s2G%2BPdNptl15R31VPQEfSrePjeaK%2BPvNWDe%2FIOfKByPuTcjzlkKKtG5TZWcLBu4EF5pWq27jwsprXyZiK%2FG2FpIfim0O9R%2BMdlAkGHUPCxPORP2pjCEn9TMBjqkAaoank4XuXMmMjidzRQ6fz7elKZS4iIxg5YJvJ3l30jQcB7pv07dcoxNSPWQukTWVF9ruMg1jATVnsuBoDXLIPAKGRuje9kz3WJARg%2B%2B3O%2BHIboJspZKI3L06gqXv8J9vDWRNUn5%2BjML6ShE6IjHEd%2FTVadXnYsl3yRTpVw7k%2B8Tt%2B6Zr1KefBRWyuUUT%2BX5f5bMt3UAPgdPiZMacyWiWUT0EbXx&X-Amz-Signature=28213d6fb32c85531dd801c26d782a8a02e82e1d5e9bf619c41d526a51710473&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WTFTXPQ%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNyvZ1acuHsZu9D1Liw38MA8CODSU7MmTSGVvFzCfenwIhAJ%2BKJF1w4gqypM806bU4qSdBigpTJZunQSAAlTPDsQLrKv8DCFoQABoMNjM3NDIzMTgzODA1Igx0kqgwlSWw2dTnlE8q3AMGdYoJ44NH8QxZBmBEdweGkrRUWloyIkLi3pOAIrT0h2pxtu%2BMYfI5fozRr60ReiFMsxpuU2wQvpGr2YDv%2BuEXZfi2W5aIXA6YhHMDWPZvQ7NZnY90pDKW1C1pFsrWjwD0PKksLqFzkzi8rGC%2F%2FP3%2BuAbo%2FwrdEJbQVQScNyHfYYB6hH6lIP5Vu6tI%2FsiSXGeeZX3ercIFRAhlwpVQSNh38m7nC%2ByQ%2BWurdR%2FN4t%2FCoXCaFaX7gqTnbHki7oJhbbbua%2FrE8fxMN9BCPxV6yNVJ84OaxnPDowul53BFeP0h3ERFjtsLj0sGKFOX%2FD0aKTHHRAnLkk45Y63k2E%2BHtDQq81PHWPHEuALbw%2Fl7B4L%2FRt4Tq%2Ff71Y08PCX0ueoiQqigzJ%2BIPHPxRS0wG7mMZIph%2FkBQ7WKiasX%2BuieRT%2BMo6ksBZw9OXajGEAlDGmdtnaBNh8VkJUGe7yQgo4%2F%2FTUeMiVsl%2B11mrdqtucKrstKP8xNoBGOmz0RbbPAl0kGQGMpeSug2Yl3U8s2G%2BPdNptl15R31VPQEfSrePjeaK%2BPvNWDe%2FIOfKByPuTcjzlkKKtG5TZWcLBu4EF5pWq27jwsprXyZiK%2FG2FpIfim0O9R%2BMdlAkGHUPCxPORP2pjCEn9TMBjqkAaoank4XuXMmMjidzRQ6fz7elKZS4iIxg5YJvJ3l30jQcB7pv07dcoxNSPWQukTWVF9ruMg1jATVnsuBoDXLIPAKGRuje9kz3WJARg%2B%2B3O%2BHIboJspZKI3L06gqXv8J9vDWRNUn5%2BjML6ShE6IjHEd%2FTVadXnYsl3yRTpVw7k%2B8Tt%2B6Zr1KefBRWyuUUT%2BX5f5bMt3UAPgdPiZMacyWiWUT0EbXx&X-Amz-Signature=03c23c8f1eac770183bf07a30eb0f88845263767c7aed4b3d1178eeb42362637&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

