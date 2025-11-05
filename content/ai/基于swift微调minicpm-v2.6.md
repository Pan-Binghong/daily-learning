---
title: 基于Swift微调MiniCPM-v2.6
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- MiniCPM
- Fine Tuning
categories:
- AI
---

记录本人使用自定义数据, 从处理文本/图片, 到构建Train.jsonl, 最终使用SwiftLora微调MiniCPM-v-2.6的全部过程.

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJS2745%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGfjM2uXK3GCUNXwvRYNim%2B0%2Bh6TROXFj8MeLyc95vzdAiEAxTtT5vBxEKrwjk0Kk7cq97NukwreuI%2FhdPdKntWd8AgqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGc2LvQm2OfPTJ7auircA2oCgz96LsOXuchB7FJiSJuV8SNRVJWK34cuW9M8gwtolIQ5DJJBT9sISZVQqnYSqaZfiRGmSNYmbGVwKkKybd4t6nrZqNLzFukiRiEoFZvo5pk83bKZVUObgtcomJNHw6QX0N2cMkRKqJwb6IKeHETbLu2fBdnPuX05MFaOMM%2FKTt%2Fz1XDLoMigZ9u7qXIOh%2Fkb7PE70gsMBwSF8d8D0aK8a5dueTjBwlgy1v8%2F1LdDABWX7nwDNXZrgZiacgNDoeD%2FxAVsharAgjcznUSxvR0La4toirVu8IFzmK8ZmN8Gp6HD%2FMcrnDcVrvRBwPocABjFv8%2FeebK37Fa6pkDka6Db0BnbYWL217hfCA2NMHV%2Fo9qJGYavzh7wIx91BXmLRXhcs7y9KyTWMAWhG29aNml0icZlKeSsLGQBvsZCtd%2B1r1Os5sFJtWSez1Oe8qVkwYAu1qEQjrX2mOpSUjAu8mIKrVXsAcPDzqsxUIvnQSpWzAGbjHGPYUUcgb0zPe3wUVL1bLXOOlfzRI8KY7nMXlF3VXl1anSmNgtJx5SmK1AtuzupIqWBbxZiXJsfKyxUptFOfaAuIRmrjLN40LVi9V0kdMFWurbYbsQl1YCLr%2BJ%2FWU7LlCuEHNHLcGgBMM2irMgGOqUBqE8uVClqVAai3wNXQlzXTmgQjPuiTPgUPbR8c7CgE11SwBSix9eTXHEt%2FzmynpYypf8xWTrNhwpQglq6dJfGBjq3NBSOPpji1oOhTXJathir8oFkmql45TMxv0SMjiBOZRA%2FMsAFS2km1l%2FPYG3ggD48%2BFgSjImwrAj2H21I5BYWbbDn4sN4Woor%2FfQeAHlM0ZmxyIZMFSUad7RPwm1UdXUxz1Tf&X-Amz-Signature=aef3178846cbae4701f16b3f56747784c70be49a6b078f0da307ff501e62d224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJS2745%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGfjM2uXK3GCUNXwvRYNim%2B0%2Bh6TROXFj8MeLyc95vzdAiEAxTtT5vBxEKrwjk0Kk7cq97NukwreuI%2FhdPdKntWd8AgqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGc2LvQm2OfPTJ7auircA2oCgz96LsOXuchB7FJiSJuV8SNRVJWK34cuW9M8gwtolIQ5DJJBT9sISZVQqnYSqaZfiRGmSNYmbGVwKkKybd4t6nrZqNLzFukiRiEoFZvo5pk83bKZVUObgtcomJNHw6QX0N2cMkRKqJwb6IKeHETbLu2fBdnPuX05MFaOMM%2FKTt%2Fz1XDLoMigZ9u7qXIOh%2Fkb7PE70gsMBwSF8d8D0aK8a5dueTjBwlgy1v8%2F1LdDABWX7nwDNXZrgZiacgNDoeD%2FxAVsharAgjcznUSxvR0La4toirVu8IFzmK8ZmN8Gp6HD%2FMcrnDcVrvRBwPocABjFv8%2FeebK37Fa6pkDka6Db0BnbYWL217hfCA2NMHV%2Fo9qJGYavzh7wIx91BXmLRXhcs7y9KyTWMAWhG29aNml0icZlKeSsLGQBvsZCtd%2B1r1Os5sFJtWSez1Oe8qVkwYAu1qEQjrX2mOpSUjAu8mIKrVXsAcPDzqsxUIvnQSpWzAGbjHGPYUUcgb0zPe3wUVL1bLXOOlfzRI8KY7nMXlF3VXl1anSmNgtJx5SmK1AtuzupIqWBbxZiXJsfKyxUptFOfaAuIRmrjLN40LVi9V0kdMFWurbYbsQl1YCLr%2BJ%2FWU7LlCuEHNHLcGgBMM2irMgGOqUBqE8uVClqVAai3wNXQlzXTmgQjPuiTPgUPbR8c7CgE11SwBSix9eTXHEt%2FzmynpYypf8xWTrNhwpQglq6dJfGBjq3NBSOPpji1oOhTXJathir8oFkmql45TMxv0SMjiBOZRA%2FMsAFS2km1l%2FPYG3ggD48%2BFgSjImwrAj2H21I5BYWbbDn4sN4Woor%2FfQeAHlM0ZmxyIZMFSUad7RPwm1UdXUxz1Tf&X-Amz-Signature=01ecf6d2cf84247735dd77f3b2b21accac5fdfaa9744dcdc39c1148324e32353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBJS2745%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGfjM2uXK3GCUNXwvRYNim%2B0%2Bh6TROXFj8MeLyc95vzdAiEAxTtT5vBxEKrwjk0Kk7cq97NukwreuI%2FhdPdKntWd8AgqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGc2LvQm2OfPTJ7auircA2oCgz96LsOXuchB7FJiSJuV8SNRVJWK34cuW9M8gwtolIQ5DJJBT9sISZVQqnYSqaZfiRGmSNYmbGVwKkKybd4t6nrZqNLzFukiRiEoFZvo5pk83bKZVUObgtcomJNHw6QX0N2cMkRKqJwb6IKeHETbLu2fBdnPuX05MFaOMM%2FKTt%2Fz1XDLoMigZ9u7qXIOh%2Fkb7PE70gsMBwSF8d8D0aK8a5dueTjBwlgy1v8%2F1LdDABWX7nwDNXZrgZiacgNDoeD%2FxAVsharAgjcznUSxvR0La4toirVu8IFzmK8ZmN8Gp6HD%2FMcrnDcVrvRBwPocABjFv8%2FeebK37Fa6pkDka6Db0BnbYWL217hfCA2NMHV%2Fo9qJGYavzh7wIx91BXmLRXhcs7y9KyTWMAWhG29aNml0icZlKeSsLGQBvsZCtd%2B1r1Os5sFJtWSez1Oe8qVkwYAu1qEQjrX2mOpSUjAu8mIKrVXsAcPDzqsxUIvnQSpWzAGbjHGPYUUcgb0zPe3wUVL1bLXOOlfzRI8KY7nMXlF3VXl1anSmNgtJx5SmK1AtuzupIqWBbxZiXJsfKyxUptFOfaAuIRmrjLN40LVi9V0kdMFWurbYbsQl1YCLr%2BJ%2FWU7LlCuEHNHLcGgBMM2irMgGOqUBqE8uVClqVAai3wNXQlzXTmgQjPuiTPgUPbR8c7CgE11SwBSix9eTXHEt%2FzmynpYypf8xWTrNhwpQglq6dJfGBjq3NBSOPpji1oOhTXJathir8oFkmql45TMxv0SMjiBOZRA%2FMsAFS2km1l%2FPYG3ggD48%2BFgSjImwrAj2H21I5BYWbbDn4sN4Woor%2FfQeAHlM0ZmxyIZMFSUad7RPwm1UdXUxz1Tf&X-Amz-Signature=109fe2cc5c78c3afc1243792893b5b328d4e07544429e152e23604600eea032d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

