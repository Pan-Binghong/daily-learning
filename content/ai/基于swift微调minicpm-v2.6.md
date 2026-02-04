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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637GCG4VR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCiG0Jcvu%2BAKJXmFRlkjUjRZZv55n%2Fy0fWDM6dxhtAaWwIgTxPSPvR4kQB4oBt7nLCKRfU5Y4rbyJRHz33bfEkqJEcq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDKQVor13tDmzg2YbyircA9%2BSmaMmewvPf33hSF9Mhl77wV70S5Ya45BtdqvhL8uGQQ4VuTdJ99Cn%2FkXnovEgpVV%2FlgHiHFDJAbcPCUuyipax6DorC%2B9LO3W523fSOaAmLudzsQ%2BrLH6FopOFTi%2B3CLX9G95j01D9%2BWNv1Z2X7AWkJaxO%2Bkpzj7uBuXZsQS8opYpMcLglh0FJPlVvnGqy3gHAz%2FynbKg%2FcHiwRaQbfFjhKgm8S42bfoGrpKmpfdGfOYB1CKB7ksBf7WlrYP%2BjCSexAlcwdXod595kJa%2BfhP6T2BZxO%2BSm7e4whb0e%2FsJk9aPzqZIhcS1NOpLGGyCYb5nTp71%2Bsej%2FmU97WF268HO7%2BCwdvEyT%2FYx8JpzcaIKlWNg7qYZqd1iJPzStw%2F48%2F8QOuKOzFEVi3dVn8juP3y6huGyaLDcpjIj86RHG3ql%2Bc16PfLete7Oi%2B3yI%2FGwtfJVicJNP%2Fzu7bl0elBEhCnu0j8adRHoUr9oogqn5oQFyI7sRGlw3k581So6L3pxl9wEkD469XSJ9Kyst3qOq9qBJsQ9VJY5wz6vY8dFVWd1zEFE3xuBIpmc7JSpO2sjd85CdQmaPlXA7HueIO5IknQIAeK2M2%2F%2B33WUI6H2j51PQLlEUf5UCWOsR2u4WMPnoiswGOqUBtVxgE1ncejKLa%2BcBjFYM7Y0OCCIKCrZ55deHNunndb5HLy43l8AoDnI8DMo%2FnDjpZ0zEGRixEQhk6HFUTrZXXQkQ%2BBIrMVi6JcyIjulYlkJ4%2FcnNm5J1hKuLxokd7BIRAfSEb8JDmodDcUzxgCMILxsNf0nQ%2ByjzxWDjVO1Kkc4pHzjwuMENOApGbpqjBOxvXHjvgh38LqI138PnvcTDs7BMIIHP&X-Amz-Signature=e82f5e71e167c776c4df44bb4de61cd49f77c13c3bab42ce7a5dc237265c96b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637GCG4VR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCiG0Jcvu%2BAKJXmFRlkjUjRZZv55n%2Fy0fWDM6dxhtAaWwIgTxPSPvR4kQB4oBt7nLCKRfU5Y4rbyJRHz33bfEkqJEcq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDKQVor13tDmzg2YbyircA9%2BSmaMmewvPf33hSF9Mhl77wV70S5Ya45BtdqvhL8uGQQ4VuTdJ99Cn%2FkXnovEgpVV%2FlgHiHFDJAbcPCUuyipax6DorC%2B9LO3W523fSOaAmLudzsQ%2BrLH6FopOFTi%2B3CLX9G95j01D9%2BWNv1Z2X7AWkJaxO%2Bkpzj7uBuXZsQS8opYpMcLglh0FJPlVvnGqy3gHAz%2FynbKg%2FcHiwRaQbfFjhKgm8S42bfoGrpKmpfdGfOYB1CKB7ksBf7WlrYP%2BjCSexAlcwdXod595kJa%2BfhP6T2BZxO%2BSm7e4whb0e%2FsJk9aPzqZIhcS1NOpLGGyCYb5nTp71%2Bsej%2FmU97WF268HO7%2BCwdvEyT%2FYx8JpzcaIKlWNg7qYZqd1iJPzStw%2F48%2F8QOuKOzFEVi3dVn8juP3y6huGyaLDcpjIj86RHG3ql%2Bc16PfLete7Oi%2B3yI%2FGwtfJVicJNP%2Fzu7bl0elBEhCnu0j8adRHoUr9oogqn5oQFyI7sRGlw3k581So6L3pxl9wEkD469XSJ9Kyst3qOq9qBJsQ9VJY5wz6vY8dFVWd1zEFE3xuBIpmc7JSpO2sjd85CdQmaPlXA7HueIO5IknQIAeK2M2%2F%2B33WUI6H2j51PQLlEUf5UCWOsR2u4WMPnoiswGOqUBtVxgE1ncejKLa%2BcBjFYM7Y0OCCIKCrZ55deHNunndb5HLy43l8AoDnI8DMo%2FnDjpZ0zEGRixEQhk6HFUTrZXXQkQ%2BBIrMVi6JcyIjulYlkJ4%2FcnNm5J1hKuLxokd7BIRAfSEb8JDmodDcUzxgCMILxsNf0nQ%2ByjzxWDjVO1Kkc4pHzjwuMENOApGbpqjBOxvXHjvgh38LqI138PnvcTDs7BMIIHP&X-Amz-Signature=e7f92f82b4fcac4ff74e9e0afaf7dc619a619dc8a13f687bfea8173741b61601&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637GCG4VR%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCiG0Jcvu%2BAKJXmFRlkjUjRZZv55n%2Fy0fWDM6dxhtAaWwIgTxPSPvR4kQB4oBt7nLCKRfU5Y4rbyJRHz33bfEkqJEcq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDKQVor13tDmzg2YbyircA9%2BSmaMmewvPf33hSF9Mhl77wV70S5Ya45BtdqvhL8uGQQ4VuTdJ99Cn%2FkXnovEgpVV%2FlgHiHFDJAbcPCUuyipax6DorC%2B9LO3W523fSOaAmLudzsQ%2BrLH6FopOFTi%2B3CLX9G95j01D9%2BWNv1Z2X7AWkJaxO%2Bkpzj7uBuXZsQS8opYpMcLglh0FJPlVvnGqy3gHAz%2FynbKg%2FcHiwRaQbfFjhKgm8S42bfoGrpKmpfdGfOYB1CKB7ksBf7WlrYP%2BjCSexAlcwdXod595kJa%2BfhP6T2BZxO%2BSm7e4whb0e%2FsJk9aPzqZIhcS1NOpLGGyCYb5nTp71%2Bsej%2FmU97WF268HO7%2BCwdvEyT%2FYx8JpzcaIKlWNg7qYZqd1iJPzStw%2F48%2F8QOuKOzFEVi3dVn8juP3y6huGyaLDcpjIj86RHG3ql%2Bc16PfLete7Oi%2B3yI%2FGwtfJVicJNP%2Fzu7bl0elBEhCnu0j8adRHoUr9oogqn5oQFyI7sRGlw3k581So6L3pxl9wEkD469XSJ9Kyst3qOq9qBJsQ9VJY5wz6vY8dFVWd1zEFE3xuBIpmc7JSpO2sjd85CdQmaPlXA7HueIO5IknQIAeK2M2%2F%2B33WUI6H2j51PQLlEUf5UCWOsR2u4WMPnoiswGOqUBtVxgE1ncejKLa%2BcBjFYM7Y0OCCIKCrZ55deHNunndb5HLy43l8AoDnI8DMo%2FnDjpZ0zEGRixEQhk6HFUTrZXXQkQ%2BBIrMVi6JcyIjulYlkJ4%2FcnNm5J1hKuLxokd7BIRAfSEb8JDmodDcUzxgCMILxsNf0nQ%2ByjzxWDjVO1Kkc4pHzjwuMENOApGbpqjBOxvXHjvgh38LqI138PnvcTDs7BMIIHP&X-Amz-Signature=6f049dc0ff30dd063a4683d77d746ac98de07e37453f6c30b19afc35e8a81bd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

