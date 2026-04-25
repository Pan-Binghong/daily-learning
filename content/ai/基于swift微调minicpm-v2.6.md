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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654V6QPFX%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb42o0e4hORK4gxg9GO5I9vKzFh3xQj0CDC9aoxuHgpQIgUof0k8IgvBK%2FF3Uon1xmW1f0t2O1%2Ft%2FKNmLLiiBijdMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPuHnHGAN7xie38lPSrcA5xe3oYl%2B%2BKVCX5Gv0Xlv2a08Zn7Wpj6rVAYbUGbIkWVfpiegYssW8NJWeF%2B5bpqDRn5J%2Bh5sMMcLTlMYZQJujwa%2BMv%2BOMq%2BArz582Fse%2FgWXuA2VliLQzLnj2Ti1VjYWwoHYWosD2c3WmN7By87gxbFYKyTcLDRK25GqqO1ZqmGTjTjfgtVS1zgLCYtaWyDecJ4uvX5z%2BOUAkviy6u%2By9ad4SmN272nsC67HeJuxDRzUUo6D8HikLOhKLTJzwqtV3DuQ3Kzuj8sA46%2BcdyikA4vr%2BXI6bFevxd2Cim7w4P2zX2hEAwcuApBRF5Omu9ogLalj2KtC%2FEEOgUBEgXqTy449eeI6Zom4mLO2sB%2BZy0ungOK8qYkh6qCUfQIaPCAOtUZIZc6Xj2ibAqKhhLdbkznDI7nj4CZwHF%2FywnHye0U6%2FFWwFOfsgXkWQ4Vq3UpRvjU7P7h%2FhVsIdZ4WC9o0wUYNUHFYSjnPqd3iqAU96AmIfXv5VsKHkkZFLxOqqBgjRtKNfXjPHKM1SwkLi1T6w8KyhplDaIRDdfvlFWK3b3iapXkJFsRYjfPfytiqVNXDCT%2BFZ7f3kMd9hoNZgqtJUDj%2BS1msofuJM%2BQS8J194Dfo1U%2BEVwwMFLiHOVrMN3ysM8GOqUBl%2B2%2B12JXCh6AYfESOmcF8Br9JAV%2BiOPQ3MSLODILyrEXenahwuyi62TfW5HmOgy2Q7lPGIM%2BTD5cfcG9k4xgMR3npx4yb0W8gFOi7en5ZkRx5BexuosvtJebwb7eNz6Ych4AmVRRTOq70Z3Ot85EcHcERjrtJUjgmWqsNuAOpq%2BA9hHaVO3lnBVlPLE1rZq09S1y9kCHwxAvcnZkNHDq%2FwyaHy5J&X-Amz-Signature=136e111cb022fe9106c8454dbd780d1bde4aeb4588d6fd35f4c98b65521648ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654V6QPFX%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb42o0e4hORK4gxg9GO5I9vKzFh3xQj0CDC9aoxuHgpQIgUof0k8IgvBK%2FF3Uon1xmW1f0t2O1%2Ft%2FKNmLLiiBijdMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPuHnHGAN7xie38lPSrcA5xe3oYl%2B%2BKVCX5Gv0Xlv2a08Zn7Wpj6rVAYbUGbIkWVfpiegYssW8NJWeF%2B5bpqDRn5J%2Bh5sMMcLTlMYZQJujwa%2BMv%2BOMq%2BArz582Fse%2FgWXuA2VliLQzLnj2Ti1VjYWwoHYWosD2c3WmN7By87gxbFYKyTcLDRK25GqqO1ZqmGTjTjfgtVS1zgLCYtaWyDecJ4uvX5z%2BOUAkviy6u%2By9ad4SmN272nsC67HeJuxDRzUUo6D8HikLOhKLTJzwqtV3DuQ3Kzuj8sA46%2BcdyikA4vr%2BXI6bFevxd2Cim7w4P2zX2hEAwcuApBRF5Omu9ogLalj2KtC%2FEEOgUBEgXqTy449eeI6Zom4mLO2sB%2BZy0ungOK8qYkh6qCUfQIaPCAOtUZIZc6Xj2ibAqKhhLdbkznDI7nj4CZwHF%2FywnHye0U6%2FFWwFOfsgXkWQ4Vq3UpRvjU7P7h%2FhVsIdZ4WC9o0wUYNUHFYSjnPqd3iqAU96AmIfXv5VsKHkkZFLxOqqBgjRtKNfXjPHKM1SwkLi1T6w8KyhplDaIRDdfvlFWK3b3iapXkJFsRYjfPfytiqVNXDCT%2BFZ7f3kMd9hoNZgqtJUDj%2BS1msofuJM%2BQS8J194Dfo1U%2BEVwwMFLiHOVrMN3ysM8GOqUBl%2B2%2B12JXCh6AYfESOmcF8Br9JAV%2BiOPQ3MSLODILyrEXenahwuyi62TfW5HmOgy2Q7lPGIM%2BTD5cfcG9k4xgMR3npx4yb0W8gFOi7en5ZkRx5BexuosvtJebwb7eNz6Ych4AmVRRTOq70Z3Ot85EcHcERjrtJUjgmWqsNuAOpq%2BA9hHaVO3lnBVlPLE1rZq09S1y9kCHwxAvcnZkNHDq%2FwyaHy5J&X-Amz-Signature=f2482e2c45af93c42a775523b6c974e61d82ffd708aa0a3c3207a49b3cf0f394&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654V6QPFX%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb42o0e4hORK4gxg9GO5I9vKzFh3xQj0CDC9aoxuHgpQIgUof0k8IgvBK%2FF3Uon1xmW1f0t2O1%2Ft%2FKNmLLiiBijdMqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPuHnHGAN7xie38lPSrcA5xe3oYl%2B%2BKVCX5Gv0Xlv2a08Zn7Wpj6rVAYbUGbIkWVfpiegYssW8NJWeF%2B5bpqDRn5J%2Bh5sMMcLTlMYZQJujwa%2BMv%2BOMq%2BArz582Fse%2FgWXuA2VliLQzLnj2Ti1VjYWwoHYWosD2c3WmN7By87gxbFYKyTcLDRK25GqqO1ZqmGTjTjfgtVS1zgLCYtaWyDecJ4uvX5z%2BOUAkviy6u%2By9ad4SmN272nsC67HeJuxDRzUUo6D8HikLOhKLTJzwqtV3DuQ3Kzuj8sA46%2BcdyikA4vr%2BXI6bFevxd2Cim7w4P2zX2hEAwcuApBRF5Omu9ogLalj2KtC%2FEEOgUBEgXqTy449eeI6Zom4mLO2sB%2BZy0ungOK8qYkh6qCUfQIaPCAOtUZIZc6Xj2ibAqKhhLdbkznDI7nj4CZwHF%2FywnHye0U6%2FFWwFOfsgXkWQ4Vq3UpRvjU7P7h%2FhVsIdZ4WC9o0wUYNUHFYSjnPqd3iqAU96AmIfXv5VsKHkkZFLxOqqBgjRtKNfXjPHKM1SwkLi1T6w8KyhplDaIRDdfvlFWK3b3iapXkJFsRYjfPfytiqVNXDCT%2BFZ7f3kMd9hoNZgqtJUDj%2BS1msofuJM%2BQS8J194Dfo1U%2BEVwwMFLiHOVrMN3ysM8GOqUBl%2B2%2B12JXCh6AYfESOmcF8Br9JAV%2BiOPQ3MSLODILyrEXenahwuyi62TfW5HmOgy2Q7lPGIM%2BTD5cfcG9k4xgMR3npx4yb0W8gFOi7en5ZkRx5BexuosvtJebwb7eNz6Ych4AmVRRTOq70Z3Ot85EcHcERjrtJUjgmWqsNuAOpq%2BA9hHaVO3lnBVlPLE1rZq09S1y9kCHwxAvcnZkNHDq%2FwyaHy5J&X-Amz-Signature=1807dd1cff5157039d7117b150b0747b3fa8d5c884001ae776060dafafa23844&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

