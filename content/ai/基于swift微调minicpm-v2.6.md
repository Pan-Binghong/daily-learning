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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ5WMFZP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCn%2FEJyrGqZFgqXbtwJ8MggQxruA8dbTDWDXHPNmmzAIhAIkAYwuyk3khuK%2B8Gsl77k6GKGhJS2zRyQTJG7AxKfWDKv8DCH8QABoMNjM3NDIzMTgzODA1IgzDpUJFQsfoPcA4t1wq3AOFnBwB3TAH88XT2cDusgHPsbbjlY0bSJ7ybbCVTeQUO3Qk17akrmBcEENW4nXJpACSBnkIR%2BD8ds%2FtMfjhSkycQvXRIpvTf1BRgRtexbIrFlmp5acBBP7rEp7feZOgWnG%2FR3upDkkFh88rce00LP9JDGv6r3saHdW3U%2BBjp4tJr53%2F55Lo8L3BJ41K%2FHxXtZFDjUKgNB0X%2BpHBdb2xD4yZnDNiE5o0%2ByyL%2FVfler3BKkSuvewORXGfKuFTVjsojvhlLsB3K3YQ0jAAqdD5%2Fjhs8dzvowTsnPmDTDEhdPFcYIZbaUDz1A8KyH6bkHwxeYxIzxJHG6vgxQcucQmaOY1rvG5%2F1tecyTxmId1u54vzgkVihKu82N2%2FftP5xNwP995nTg%2FsG%2Frgb3j3sP2hCfzJOXWFun9K0xg2UBruH2yhWmVlS6pOxn5u8PQk%2FP7GO2V6C0WXycGP7TfqDgDmkS%2BqrqYeNolaQ1uHwlGHrWH9oulRc86AcAu0Qztr4n%2FS7RrkDeblwqEKH%2BYv0l0Q4KuIjIQ5U7tVRUmQPLkok%2BnS%2B7AsekqDa6d3%2FwABNhQl87N%2Fa8o9QZzNlsKYg1GE1rmKfo5kLzO236oeZK4Bio0ukLmYxK%2F4gypFIZ%2BvhTDlrL3OBjqkATr8eoELiXrCi9srEPMLBHoyquPFmu6lQ7JsE%2F8YQnIRjGkPoqHnfN76bkX5WFua4b2COzu5fQ3JO18eRA7j51TNFpjVjwmdvOsGKM8%2FZzvEpcuXUVGDKaGPGQ3SsVO28sFIkrDbZdsZDe4%2BC3AKX%2Fyjob1%2BmxOHh0pHhVtCk9p7qsoiUXw6TPSUzN9rjR4a3ee8pXZNhpcTgpLRvofIX9wa%2BLSU&X-Amz-Signature=d3a20d4344606cbbc262dcaac2447a3bd2b351a2f2473b351b093a2d50435310&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ5WMFZP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCn%2FEJyrGqZFgqXbtwJ8MggQxruA8dbTDWDXHPNmmzAIhAIkAYwuyk3khuK%2B8Gsl77k6GKGhJS2zRyQTJG7AxKfWDKv8DCH8QABoMNjM3NDIzMTgzODA1IgzDpUJFQsfoPcA4t1wq3AOFnBwB3TAH88XT2cDusgHPsbbjlY0bSJ7ybbCVTeQUO3Qk17akrmBcEENW4nXJpACSBnkIR%2BD8ds%2FtMfjhSkycQvXRIpvTf1BRgRtexbIrFlmp5acBBP7rEp7feZOgWnG%2FR3upDkkFh88rce00LP9JDGv6r3saHdW3U%2BBjp4tJr53%2F55Lo8L3BJ41K%2FHxXtZFDjUKgNB0X%2BpHBdb2xD4yZnDNiE5o0%2ByyL%2FVfler3BKkSuvewORXGfKuFTVjsojvhlLsB3K3YQ0jAAqdD5%2Fjhs8dzvowTsnPmDTDEhdPFcYIZbaUDz1A8KyH6bkHwxeYxIzxJHG6vgxQcucQmaOY1rvG5%2F1tecyTxmId1u54vzgkVihKu82N2%2FftP5xNwP995nTg%2FsG%2Frgb3j3sP2hCfzJOXWFun9K0xg2UBruH2yhWmVlS6pOxn5u8PQk%2FP7GO2V6C0WXycGP7TfqDgDmkS%2BqrqYeNolaQ1uHwlGHrWH9oulRc86AcAu0Qztr4n%2FS7RrkDeblwqEKH%2BYv0l0Q4KuIjIQ5U7tVRUmQPLkok%2BnS%2B7AsekqDa6d3%2FwABNhQl87N%2Fa8o9QZzNlsKYg1GE1rmKfo5kLzO236oeZK4Bio0ukLmYxK%2F4gypFIZ%2BvhTDlrL3OBjqkATr8eoELiXrCi9srEPMLBHoyquPFmu6lQ7JsE%2F8YQnIRjGkPoqHnfN76bkX5WFua4b2COzu5fQ3JO18eRA7j51TNFpjVjwmdvOsGKM8%2FZzvEpcuXUVGDKaGPGQ3SsVO28sFIkrDbZdsZDe4%2BC3AKX%2Fyjob1%2BmxOHh0pHhVtCk9p7qsoiUXw6TPSUzN9rjR4a3ee8pXZNhpcTgpLRvofIX9wa%2BLSU&X-Amz-Signature=9d76d4adc53e20f209f988076b1a3f698a2606408e3ba985a27a55a240b74e72&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQ5WMFZP%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpCn%2FEJyrGqZFgqXbtwJ8MggQxruA8dbTDWDXHPNmmzAIhAIkAYwuyk3khuK%2B8Gsl77k6GKGhJS2zRyQTJG7AxKfWDKv8DCH8QABoMNjM3NDIzMTgzODA1IgzDpUJFQsfoPcA4t1wq3AOFnBwB3TAH88XT2cDusgHPsbbjlY0bSJ7ybbCVTeQUO3Qk17akrmBcEENW4nXJpACSBnkIR%2BD8ds%2FtMfjhSkycQvXRIpvTf1BRgRtexbIrFlmp5acBBP7rEp7feZOgWnG%2FR3upDkkFh88rce00LP9JDGv6r3saHdW3U%2BBjp4tJr53%2F55Lo8L3BJ41K%2FHxXtZFDjUKgNB0X%2BpHBdb2xD4yZnDNiE5o0%2ByyL%2FVfler3BKkSuvewORXGfKuFTVjsojvhlLsB3K3YQ0jAAqdD5%2Fjhs8dzvowTsnPmDTDEhdPFcYIZbaUDz1A8KyH6bkHwxeYxIzxJHG6vgxQcucQmaOY1rvG5%2F1tecyTxmId1u54vzgkVihKu82N2%2FftP5xNwP995nTg%2FsG%2Frgb3j3sP2hCfzJOXWFun9K0xg2UBruH2yhWmVlS6pOxn5u8PQk%2FP7GO2V6C0WXycGP7TfqDgDmkS%2BqrqYeNolaQ1uHwlGHrWH9oulRc86AcAu0Qztr4n%2FS7RrkDeblwqEKH%2BYv0l0Q4KuIjIQ5U7tVRUmQPLkok%2BnS%2B7AsekqDa6d3%2FwABNhQl87N%2Fa8o9QZzNlsKYg1GE1rmKfo5kLzO236oeZK4Bio0ukLmYxK%2F4gypFIZ%2BvhTDlrL3OBjqkATr8eoELiXrCi9srEPMLBHoyquPFmu6lQ7JsE%2F8YQnIRjGkPoqHnfN76bkX5WFua4b2COzu5fQ3JO18eRA7j51TNFpjVjwmdvOsGKM8%2FZzvEpcuXUVGDKaGPGQ3SsVO28sFIkrDbZdsZDe4%2BC3AKX%2Fyjob1%2BmxOHh0pHhVtCk9p7qsoiUXw6TPSUzN9rjR4a3ee8pXZNhpcTgpLRvofIX9wa%2BLSU&X-Amz-Signature=323a288b6df09034bdcb032b6889be0ac2ecfb2478709f34739081ea82894d14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

