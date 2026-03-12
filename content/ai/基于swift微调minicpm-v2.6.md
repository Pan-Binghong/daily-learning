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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRCDOS64%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhkqDY6ROxwzvEbkZ2MdTubsrNy7WQrU6Y8UVwykdMwAiEA82r%2BhL4jsWtWAuuhIvgkcyKCLb3gCVXOFcBe3Y44xXQq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDOyWdCP6uoxKcddG0CrcAxWYl1Fmi9c01QaB5jIlNP3Oz5yRmo2c6edkiC%2FwKzza%2FOP0OKIE3RViIUpVzv8XQu6bCvsv4e%2FxoyYnr4171T337q%2F9RJ8OaIrfEhxaM%2F1VxJRi5e8InM76xxS3Yjq%2F2xvMJmPO8Wb9YNODk6A7xv%2Ba371UZsQBGhnTJKG%2FGmrrdEtiaVIDvHS1u7S49GYiR0FucaVhnvPx2HztvGqAsvZa6x3qCZ7NMsTkpxo3Abp802SAi4px0NQDl1aT3vSyypAbdJD%2BnZ09d5lTywMyK%2BoZ7RD6HIJYvz59ApFmHXmKkrl3CmGU9bpYMXjgr5QZLBlrB1hDChOKrO9%2BxSzrrK5yn0Xn%2FIO8yph0v2%2BEILiKZ6K%2F3hsuh7ETmL4G3ujNcnAH9PK3RX9gk9IfKb52agA6MFsVxtQ3extRscS%2Flzz84epicFxHFQth13MrAGnW8s7KahLFGhmEj%2BrySmcMVQPlO5V83YCZhjubjJUzWTTEqGRN6Z%2FAu4CWovPkeeCcDuaGL9j89UirdqxO%2FcuNZ5Glfh36wWuto177Qh6hMAkHNMv1o8LckpKBgjG%2BYi%2FYiEy0hke9ZgR4MzeNEk5h1jPDAger4rtE4Du%2BWVbAGXNq5J5K1n6mxEG5Cz2DMPSxyM0GOqUBMo1Y9CofjZKfqWcNGbdsDX5oi942aQ84Byg%2Fox%2FwFcXpCNUGTbT6IK8BL%2Fcu%2F0E2YIEM0hgLgjoP8LrC8l5BkX6l1bWbR3rVFtw%2Bu4de8hnuWMZWgxgyIHrtg8slmUOPXW2hV43my9ZvuwVCeV2pK4%2FTEh4Ucbwk8ap%2FbxAaGPeyCQQXAnwtPW46saBf6XsGOWzKwNErr8NNd1rO1acVhslebnep&X-Amz-Signature=379090e96053aa711578533a31cb82fb752e48a07b5515dae7e43017c4ef5861&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRCDOS64%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhkqDY6ROxwzvEbkZ2MdTubsrNy7WQrU6Y8UVwykdMwAiEA82r%2BhL4jsWtWAuuhIvgkcyKCLb3gCVXOFcBe3Y44xXQq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDOyWdCP6uoxKcddG0CrcAxWYl1Fmi9c01QaB5jIlNP3Oz5yRmo2c6edkiC%2FwKzza%2FOP0OKIE3RViIUpVzv8XQu6bCvsv4e%2FxoyYnr4171T337q%2F9RJ8OaIrfEhxaM%2F1VxJRi5e8InM76xxS3Yjq%2F2xvMJmPO8Wb9YNODk6A7xv%2Ba371UZsQBGhnTJKG%2FGmrrdEtiaVIDvHS1u7S49GYiR0FucaVhnvPx2HztvGqAsvZa6x3qCZ7NMsTkpxo3Abp802SAi4px0NQDl1aT3vSyypAbdJD%2BnZ09d5lTywMyK%2BoZ7RD6HIJYvz59ApFmHXmKkrl3CmGU9bpYMXjgr5QZLBlrB1hDChOKrO9%2BxSzrrK5yn0Xn%2FIO8yph0v2%2BEILiKZ6K%2F3hsuh7ETmL4G3ujNcnAH9PK3RX9gk9IfKb52agA6MFsVxtQ3extRscS%2Flzz84epicFxHFQth13MrAGnW8s7KahLFGhmEj%2BrySmcMVQPlO5V83YCZhjubjJUzWTTEqGRN6Z%2FAu4CWovPkeeCcDuaGL9j89UirdqxO%2FcuNZ5Glfh36wWuto177Qh6hMAkHNMv1o8LckpKBgjG%2BYi%2FYiEy0hke9ZgR4MzeNEk5h1jPDAger4rtE4Du%2BWVbAGXNq5J5K1n6mxEG5Cz2DMPSxyM0GOqUBMo1Y9CofjZKfqWcNGbdsDX5oi942aQ84Byg%2Fox%2FwFcXpCNUGTbT6IK8BL%2Fcu%2F0E2YIEM0hgLgjoP8LrC8l5BkX6l1bWbR3rVFtw%2Bu4de8hnuWMZWgxgyIHrtg8slmUOPXW2hV43my9ZvuwVCeV2pK4%2FTEh4Ucbwk8ap%2FbxAaGPeyCQQXAnwtPW46saBf6XsGOWzKwNErr8NNd1rO1acVhslebnep&X-Amz-Signature=4e3e83d64e35db7d759112c4bdeaa121177eecb85fd3e8231fdb5998a5bf6cb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRCDOS64%2F20260312%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260312T033336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhkqDY6ROxwzvEbkZ2MdTubsrNy7WQrU6Y8UVwykdMwAiEA82r%2BhL4jsWtWAuuhIvgkcyKCLb3gCVXOFcBe3Y44xXQq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDOyWdCP6uoxKcddG0CrcAxWYl1Fmi9c01QaB5jIlNP3Oz5yRmo2c6edkiC%2FwKzza%2FOP0OKIE3RViIUpVzv8XQu6bCvsv4e%2FxoyYnr4171T337q%2F9RJ8OaIrfEhxaM%2F1VxJRi5e8InM76xxS3Yjq%2F2xvMJmPO8Wb9YNODk6A7xv%2Ba371UZsQBGhnTJKG%2FGmrrdEtiaVIDvHS1u7S49GYiR0FucaVhnvPx2HztvGqAsvZa6x3qCZ7NMsTkpxo3Abp802SAi4px0NQDl1aT3vSyypAbdJD%2BnZ09d5lTywMyK%2BoZ7RD6HIJYvz59ApFmHXmKkrl3CmGU9bpYMXjgr5QZLBlrB1hDChOKrO9%2BxSzrrK5yn0Xn%2FIO8yph0v2%2BEILiKZ6K%2F3hsuh7ETmL4G3ujNcnAH9PK3RX9gk9IfKb52agA6MFsVxtQ3extRscS%2Flzz84epicFxHFQth13MrAGnW8s7KahLFGhmEj%2BrySmcMVQPlO5V83YCZhjubjJUzWTTEqGRN6Z%2FAu4CWovPkeeCcDuaGL9j89UirdqxO%2FcuNZ5Glfh36wWuto177Qh6hMAkHNMv1o8LckpKBgjG%2BYi%2FYiEy0hke9ZgR4MzeNEk5h1jPDAger4rtE4Du%2BWVbAGXNq5J5K1n6mxEG5Cz2DMPSxyM0GOqUBMo1Y9CofjZKfqWcNGbdsDX5oi942aQ84Byg%2Fox%2FwFcXpCNUGTbT6IK8BL%2Fcu%2F0E2YIEM0hgLgjoP8LrC8l5BkX6l1bWbR3rVFtw%2Bu4de8hnuWMZWgxgyIHrtg8slmUOPXW2hV43my9ZvuwVCeV2pK4%2FTEh4Ucbwk8ap%2FbxAaGPeyCQQXAnwtPW46saBf6XsGOWzKwNErr8NNd1rO1acVhslebnep&X-Amz-Signature=877d7bdfac1d3128de41dccc2b52c53ee8b01d459cbd1ba8166f5bdefe291575&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

