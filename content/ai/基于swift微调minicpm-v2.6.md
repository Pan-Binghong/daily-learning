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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OPVGZDU%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDe1DnDMX2QpaPtsEyhuMNjZruZaexrsap9Ld4cuCXlzAiEAg0RkxcwSNNnWQBZHHD528rK99C0wQFn4plSsUDHMUfAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICsM9bJtZcirJeHGyrcAyrMJBbmn7f26SIHFIyBOTD%2FBGaKzOU5FyUB4Y6yvSd%2FvGCKUXtV0VqLBgcmjVijMm3QcJ4S054Vt9Jj0ThjD4xn4mrwORlAHaUwtntNnPOafKZYykXt%2B%2FiCDMOLTIMFcN2Om1RzTjk8OdEtxMsx73SQVrGBauHIiWpVVYnI4I22D0%2BRzWL8RBMkDWAJ6DzHRVPqqC0KRZVzzbuee7TE66CHaghYpaRhKfbPFlCjwEgLsvJJgkySbGdp27RpeQv78uWWNpK8tpEvQPx6025pC5Ykp14ak1tbA2JOuPuzq8dv33iP%2FSzC51jQvC9wYfz5XdJXc2AjXkIKKPWRSn2E82%2FacjTaTUKGYux6CYoTLbWEQPEMOmEfRqUzOUd9zmhxbOoZRdqLaLoLYzbBhuL%2B%2FyqNE22w6eTcKnKcHs2qdQvsJlwyPTb7CohkGUsS%2F1Bgd2jDVIchcmYLdTYqv%2FEz7uQnG2H5QifV6eaMSgxRt9OE%2B7yr62OO8iVAkVduXCvisCCuJES2gqN1aMl70MUzetDCISBZf%2FvEVwh2PQrw55FNFdw%2FRW6b8Dyxz%2FBMOUFCXAtSSBGsssxMFipO5Bm9ZInhp9vL9T2xwbzi%2B%2BapPkTGLM%2BmuemSaCI5LB2xMOnM9csGOqUBwQv3%2BSXjLIlGNMwKAzF7m0ojH97bQjBnubIQ%2B1YzBQacgrvapkkNxRWivD0E4Y8tCLFrIdLKIyLOAdotyaZZpES0UgpkhUZN%2FV5tIreT5kkR73V3WcK2TTIe2R4ILzXk2qigHjgWLbXK93bjehGxSZ6hx46VZ%2BwS0iRozKKn78GmpTkfawBsRTzhrC6IPnNVcFv4eKHMnablTao0RvKS%2BEIMP0k1&X-Amz-Signature=5617427d0b4954b4aafedfc407b58a9d2b7e281a825a6fd454c292c58027a14a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OPVGZDU%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDe1DnDMX2QpaPtsEyhuMNjZruZaexrsap9Ld4cuCXlzAiEAg0RkxcwSNNnWQBZHHD528rK99C0wQFn4plSsUDHMUfAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICsM9bJtZcirJeHGyrcAyrMJBbmn7f26SIHFIyBOTD%2FBGaKzOU5FyUB4Y6yvSd%2FvGCKUXtV0VqLBgcmjVijMm3QcJ4S054Vt9Jj0ThjD4xn4mrwORlAHaUwtntNnPOafKZYykXt%2B%2FiCDMOLTIMFcN2Om1RzTjk8OdEtxMsx73SQVrGBauHIiWpVVYnI4I22D0%2BRzWL8RBMkDWAJ6DzHRVPqqC0KRZVzzbuee7TE66CHaghYpaRhKfbPFlCjwEgLsvJJgkySbGdp27RpeQv78uWWNpK8tpEvQPx6025pC5Ykp14ak1tbA2JOuPuzq8dv33iP%2FSzC51jQvC9wYfz5XdJXc2AjXkIKKPWRSn2E82%2FacjTaTUKGYux6CYoTLbWEQPEMOmEfRqUzOUd9zmhxbOoZRdqLaLoLYzbBhuL%2B%2FyqNE22w6eTcKnKcHs2qdQvsJlwyPTb7CohkGUsS%2F1Bgd2jDVIchcmYLdTYqv%2FEz7uQnG2H5QifV6eaMSgxRt9OE%2B7yr62OO8iVAkVduXCvisCCuJES2gqN1aMl70MUzetDCISBZf%2FvEVwh2PQrw55FNFdw%2FRW6b8Dyxz%2FBMOUFCXAtSSBGsssxMFipO5Bm9ZInhp9vL9T2xwbzi%2B%2BapPkTGLM%2BmuemSaCI5LB2xMOnM9csGOqUBwQv3%2BSXjLIlGNMwKAzF7m0ojH97bQjBnubIQ%2B1YzBQacgrvapkkNxRWivD0E4Y8tCLFrIdLKIyLOAdotyaZZpES0UgpkhUZN%2FV5tIreT5kkR73V3WcK2TTIe2R4ILzXk2qigHjgWLbXK93bjehGxSZ6hx46VZ%2BwS0iRozKKn78GmpTkfawBsRTzhrC6IPnNVcFv4eKHMnablTao0RvKS%2BEIMP0k1&X-Amz-Signature=c5eda5041006cb72d9b06d36b646384053ceb90a081c21581cc86c5203c6ccd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OPVGZDU%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDe1DnDMX2QpaPtsEyhuMNjZruZaexrsap9Ld4cuCXlzAiEAg0RkxcwSNNnWQBZHHD528rK99C0wQFn4plSsUDHMUfAqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDICsM9bJtZcirJeHGyrcAyrMJBbmn7f26SIHFIyBOTD%2FBGaKzOU5FyUB4Y6yvSd%2FvGCKUXtV0VqLBgcmjVijMm3QcJ4S054Vt9Jj0ThjD4xn4mrwORlAHaUwtntNnPOafKZYykXt%2B%2FiCDMOLTIMFcN2Om1RzTjk8OdEtxMsx73SQVrGBauHIiWpVVYnI4I22D0%2BRzWL8RBMkDWAJ6DzHRVPqqC0KRZVzzbuee7TE66CHaghYpaRhKfbPFlCjwEgLsvJJgkySbGdp27RpeQv78uWWNpK8tpEvQPx6025pC5Ykp14ak1tbA2JOuPuzq8dv33iP%2FSzC51jQvC9wYfz5XdJXc2AjXkIKKPWRSn2E82%2FacjTaTUKGYux6CYoTLbWEQPEMOmEfRqUzOUd9zmhxbOoZRdqLaLoLYzbBhuL%2B%2FyqNE22w6eTcKnKcHs2qdQvsJlwyPTb7CohkGUsS%2F1Bgd2jDVIchcmYLdTYqv%2FEz7uQnG2H5QifV6eaMSgxRt9OE%2B7yr62OO8iVAkVduXCvisCCuJES2gqN1aMl70MUzetDCISBZf%2FvEVwh2PQrw55FNFdw%2FRW6b8Dyxz%2FBMOUFCXAtSSBGsssxMFipO5Bm9ZInhp9vL9T2xwbzi%2B%2BapPkTGLM%2BmuemSaCI5LB2xMOnM9csGOqUBwQv3%2BSXjLIlGNMwKAzF7m0ojH97bQjBnubIQ%2B1YzBQacgrvapkkNxRWivD0E4Y8tCLFrIdLKIyLOAdotyaZZpES0UgpkhUZN%2FV5tIreT5kkR73V3WcK2TTIe2R4ILzXk2qigHjgWLbXK93bjehGxSZ6hx46VZ%2BwS0iRozKKn78GmpTkfawBsRTzhrC6IPnNVcFv4eKHMnablTao0RvKS%2BEIMP0k1&X-Amz-Signature=27f374a41949e3e993d2dde34b6e08c6f4d3d0effabf2c89668bca1b96a83975&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

