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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSY4YYND%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGjQ07mGWXBQq0BA7jS5tsWn73zoqITXAFQ7Guj2ax2PAiEA2qLtWYMNrz8CXJms8xHfgG%2BVHJM6l0AxxQ0ZI9MN1oQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ41R9AfHCObDjNxyrcA26%2BDPuftrMGz6hAR5oN%2Fgb8BPf6nGv5CmdVG4j8tMuRXDMY4XDJ%2B0l1Jhv5oHMFY8hQFBpquMN2qn48E13iPuJXbrc9jZ7EinMbFxmE4isPoEWh3jlV2waTQlluoT5ZCTXibk3GGkw%2BLQvya2JfrvFMLkObppRaOgp%2BdBEpFtIB0eOloGgdJZs9hAW8ShRdTIO61rtacVl%2BDeauUUClgt%2FEY6dTWBgd37QzqJwLNXOBSK0U1IK89Z%2BNqh7VcxmUK%2FbSuyRBNmT4pyHsn5TSx2b7k0RLdOhGcbBDJ%2Fhm4S4taqraspPpmwyGb3ccLQ4gsr4Gucde%2FtkzBEMTmE4TCp0%2BxoDyIPABU15wxD9KcXvENXOMY4W3ZyvLJ8sS%2BAsSoHrEC3tniZJZBk%2B97m6W3sK4qTvr%2BYjODl%2BH1sH77CwtsLtcFelOOCrOof529W9D%2Fh%2FmWbwj2vWmsoopdlpROuFJfkn4gzjH5Ir73UjhHtvphdGTyCSC0ufIqDpDvn0j8muVrB8ByqhciEWLUi4XtXb4lytvoMs5AxOLfQDQgr1R9Q7SErc6fLJTkNE6S0gEbV8jX%2BoQ8sTh4h5OHQGppL0bqiLPNAXS2C9Wy6xIeTgtDlJsN3hy5cQBcWllMKm2tcgGOqUB0XvYPq4jjQGgpk2frJ3UEiZSbnqV7VtFRRKWC1cMTokVMW8hTh4kwxGnfoNpA1%2BROnxVvnDDjxgzy1PUAAkokdPB90yHgF89Kk239P3O7WM8jkdLIwrVgRewKcKFHeNrSDQr%2BqRrauvwt5TakozczRBWOPmnP%2Fo9wJMn0Ttbvs0Ioa%2FFCd3Xp55b%2FMmyUu1njzukdQYZGFr1deGwrkc8qsmvakTD&X-Amz-Signature=bc0ac8f992a86e085ba8aeeb15c2282e2182f9de0b7e1f92ff24d1ac78f24d3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSY4YYND%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGjQ07mGWXBQq0BA7jS5tsWn73zoqITXAFQ7Guj2ax2PAiEA2qLtWYMNrz8CXJms8xHfgG%2BVHJM6l0AxxQ0ZI9MN1oQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ41R9AfHCObDjNxyrcA26%2BDPuftrMGz6hAR5oN%2Fgb8BPf6nGv5CmdVG4j8tMuRXDMY4XDJ%2B0l1Jhv5oHMFY8hQFBpquMN2qn48E13iPuJXbrc9jZ7EinMbFxmE4isPoEWh3jlV2waTQlluoT5ZCTXibk3GGkw%2BLQvya2JfrvFMLkObppRaOgp%2BdBEpFtIB0eOloGgdJZs9hAW8ShRdTIO61rtacVl%2BDeauUUClgt%2FEY6dTWBgd37QzqJwLNXOBSK0U1IK89Z%2BNqh7VcxmUK%2FbSuyRBNmT4pyHsn5TSx2b7k0RLdOhGcbBDJ%2Fhm4S4taqraspPpmwyGb3ccLQ4gsr4Gucde%2FtkzBEMTmE4TCp0%2BxoDyIPABU15wxD9KcXvENXOMY4W3ZyvLJ8sS%2BAsSoHrEC3tniZJZBk%2B97m6W3sK4qTvr%2BYjODl%2BH1sH77CwtsLtcFelOOCrOof529W9D%2Fh%2FmWbwj2vWmsoopdlpROuFJfkn4gzjH5Ir73UjhHtvphdGTyCSC0ufIqDpDvn0j8muVrB8ByqhciEWLUi4XtXb4lytvoMs5AxOLfQDQgr1R9Q7SErc6fLJTkNE6S0gEbV8jX%2BoQ8sTh4h5OHQGppL0bqiLPNAXS2C9Wy6xIeTgtDlJsN3hy5cQBcWllMKm2tcgGOqUB0XvYPq4jjQGgpk2frJ3UEiZSbnqV7VtFRRKWC1cMTokVMW8hTh4kwxGnfoNpA1%2BROnxVvnDDjxgzy1PUAAkokdPB90yHgF89Kk239P3O7WM8jkdLIwrVgRewKcKFHeNrSDQr%2BqRrauvwt5TakozczRBWOPmnP%2Fo9wJMn0Ttbvs0Ioa%2FFCd3Xp55b%2FMmyUu1njzukdQYZGFr1deGwrkc8qsmvakTD&X-Amz-Signature=4006b631b1d747e3c141fb9d3440a715200ba6f10cf2b9bc505f75490f691904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSY4YYND%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGjQ07mGWXBQq0BA7jS5tsWn73zoqITXAFQ7Guj2ax2PAiEA2qLtWYMNrz8CXJms8xHfgG%2BVHJM6l0AxxQ0ZI9MN1oQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQ41R9AfHCObDjNxyrcA26%2BDPuftrMGz6hAR5oN%2Fgb8BPf6nGv5CmdVG4j8tMuRXDMY4XDJ%2B0l1Jhv5oHMFY8hQFBpquMN2qn48E13iPuJXbrc9jZ7EinMbFxmE4isPoEWh3jlV2waTQlluoT5ZCTXibk3GGkw%2BLQvya2JfrvFMLkObppRaOgp%2BdBEpFtIB0eOloGgdJZs9hAW8ShRdTIO61rtacVl%2BDeauUUClgt%2FEY6dTWBgd37QzqJwLNXOBSK0U1IK89Z%2BNqh7VcxmUK%2FbSuyRBNmT4pyHsn5TSx2b7k0RLdOhGcbBDJ%2Fhm4S4taqraspPpmwyGb3ccLQ4gsr4Gucde%2FtkzBEMTmE4TCp0%2BxoDyIPABU15wxD9KcXvENXOMY4W3ZyvLJ8sS%2BAsSoHrEC3tniZJZBk%2B97m6W3sK4qTvr%2BYjODl%2BH1sH77CwtsLtcFelOOCrOof529W9D%2Fh%2FmWbwj2vWmsoopdlpROuFJfkn4gzjH5Ir73UjhHtvphdGTyCSC0ufIqDpDvn0j8muVrB8ByqhciEWLUi4XtXb4lytvoMs5AxOLfQDQgr1R9Q7SErc6fLJTkNE6S0gEbV8jX%2BoQ8sTh4h5OHQGppL0bqiLPNAXS2C9Wy6xIeTgtDlJsN3hy5cQBcWllMKm2tcgGOqUB0XvYPq4jjQGgpk2frJ3UEiZSbnqV7VtFRRKWC1cMTokVMW8hTh4kwxGnfoNpA1%2BROnxVvnDDjxgzy1PUAAkokdPB90yHgF89Kk239P3O7WM8jkdLIwrVgRewKcKFHeNrSDQr%2BqRrauvwt5TakozczRBWOPmnP%2Fo9wJMn0Ttbvs0Ioa%2FFCd3Xp55b%2FMmyUu1njzukdQYZGFr1deGwrkc8qsmvakTD&X-Amz-Signature=e9eda58f5f8c46a9ae98128b8321dc137fe3f9ca97e59731245cc27f484716cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

