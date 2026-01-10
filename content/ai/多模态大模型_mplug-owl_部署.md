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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIYCJEN%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRRjK03TMQA9qfGeRvvMSx8AxgMYbESjC9zW%2B3qbeutAIgBp6t2sP2qvQPbo2t6%2Brb6%2Ba89V9gFo4Ya8qXHGY%2B9N8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnGNS87PUi8xXpmGSrcA1rmeILDpJy%2BDgG%2F8UHGH%2Fh2h%2BRhKdTpDWvGDbu%2F0DkwNB5A6HPeORmO%2FfQ1%2Fxmg1IlmAyxZ54SroW82pRo7CUWovQgQOp5srCSTheOtBUTmZnp0ZmcMT1rM88iohtnb9gObNcTwF1Dm%2BUKuh%2FoS1vYOoTqXm4KOkdcqgRHRPBc6pJc0gWn2gU0aL8ybqUCF%2F5H7bpDgPKsXQ5OW300EdFD2dKcb6O4YUZMzg18lUBBMqOF8ItA1XOXxLQoPqU65DehMhF2PSlOVl0CtgDIZY8ui08t%2FvYB2jEyTlJGoZqGDMYIKyMDDMW3%2FPJr94%2Bs1mRRbf7qUAL15Xrzv8YMCr0qCSizLdNHkMN6ytHfr2YF%2BeO5ftEjhQQMTQSNNxEdt4FLg9c0lsTyi0A%2FeWC62is2rYOn30UBfvyKL6J4zru%2BknSCkdxq3BihiENL%2F4%2Bec0ky8i%2BC5pEE0X6DkM0Wx46wpvKJ6LTy1VLx6bQ3ordWhAt6sG4Q7NV7VSsCN%2FDjitVUxQGAnZZsEBEBpDGxZWzSa%2BNajvSc99sHlcUqJTbjK04D6DX8tRiiku1RG8V7igDbQS0WwaHjmcEa8CO4uh1rxS3UhZhp67FhKdER%2F0R8jwZJfF752omAZEIXRMKb5hssGOqUBMLCzZCNCr14svUcUFCmbW3xKTRgzCN7EnSTWYLWxz1nCtJIKwmTnW39BA4jT7rkzR8O%2FCQKKagI48xTB0CScDX9u7OG2PQwtVJS%2Fb%2BDeQplfrdqfokwaVrZtEeP857Mr573aVHZtwWTBKdFZViI6nXqW9%2FugpkafFcADotsGqiFNOWUIaAN3wIJ1x3%2F47VmGJbtSf6nvGKCn5yH4TcLS0Iqhghe0&X-Amz-Signature=0b404cc0e32350b1fb38dd7bbf20f84b4f0d86fc682c86af3ad050d0d1620621&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XIYCJEN%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRRjK03TMQA9qfGeRvvMSx8AxgMYbESjC9zW%2B3qbeutAIgBp6t2sP2qvQPbo2t6%2Brb6%2Ba89V9gFo4Ya8qXHGY%2B9N8qiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCnGNS87PUi8xXpmGSrcA1rmeILDpJy%2BDgG%2F8UHGH%2Fh2h%2BRhKdTpDWvGDbu%2F0DkwNB5A6HPeORmO%2FfQ1%2Fxmg1IlmAyxZ54SroW82pRo7CUWovQgQOp5srCSTheOtBUTmZnp0ZmcMT1rM88iohtnb9gObNcTwF1Dm%2BUKuh%2FoS1vYOoTqXm4KOkdcqgRHRPBc6pJc0gWn2gU0aL8ybqUCF%2F5H7bpDgPKsXQ5OW300EdFD2dKcb6O4YUZMzg18lUBBMqOF8ItA1XOXxLQoPqU65DehMhF2PSlOVl0CtgDIZY8ui08t%2FvYB2jEyTlJGoZqGDMYIKyMDDMW3%2FPJr94%2Bs1mRRbf7qUAL15Xrzv8YMCr0qCSizLdNHkMN6ytHfr2YF%2BeO5ftEjhQQMTQSNNxEdt4FLg9c0lsTyi0A%2FeWC62is2rYOn30UBfvyKL6J4zru%2BknSCkdxq3BihiENL%2F4%2Bec0ky8i%2BC5pEE0X6DkM0Wx46wpvKJ6LTy1VLx6bQ3ordWhAt6sG4Q7NV7VSsCN%2FDjitVUxQGAnZZsEBEBpDGxZWzSa%2BNajvSc99sHlcUqJTbjK04D6DX8tRiiku1RG8V7igDbQS0WwaHjmcEa8CO4uh1rxS3UhZhp67FhKdER%2F0R8jwZJfF752omAZEIXRMKb5hssGOqUBMLCzZCNCr14svUcUFCmbW3xKTRgzCN7EnSTWYLWxz1nCtJIKwmTnW39BA4jT7rkzR8O%2FCQKKagI48xTB0CScDX9u7OG2PQwtVJS%2Fb%2BDeQplfrdqfokwaVrZtEeP857Mr573aVHZtwWTBKdFZViI6nXqW9%2FugpkafFcADotsGqiFNOWUIaAN3wIJ1x3%2F47VmGJbtSf6nvGKCn5yH4TcLS0Iqhghe0&X-Amz-Signature=5a408a19d0fe692055969eafe394beab29d9aca185ac9c94dec9665e2a0386ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

