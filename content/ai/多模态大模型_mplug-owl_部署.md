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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIBFRDGJ%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4ZZq%2B8XcVZTZVgHRkRYYX0F2mUhWVEGmmoWj4nzONHQIhALs%2BeHlzOW9r36W6scM20DkLDIHo9jtUhdj%2BKS0dgDwqKv8DCGQQABoMNjM3NDIzMTgzODA1IgxJHdB%2FDKboDk1Cw7Yq3AO9dU5bmTEvWuLMcMottLmqZc2siWe4n4w5uO1vgZ1UHfFchnXV37XJChqjHxxzW%2Fr5Ugh9gJYp0Qj1ukMk8yunWMFBJ8iv0%2F9NJl1Y6aShANEgYNJ9Qn5BZrl%2BU5ivNM1wfvhgMyHGZJ%2Bj4EBjy2PwzY7GkZrkW4pf8fs1924iXVOJ69PG0y605kDTU%2FO%2BVY%2Fj3Bko91ZI6eOKZuiEsHrQF8c%2FVF1kE3H4xQlwZMy6%2BHSwBmPb5QwRRx9wtnhmGbGiIKucWyMTXeBK%2FqSTKtCF9xFK4ZsuU4eY3hbVj9wQdKW7L8hscTgx5obdw76WsbxkNEveNEyz2ZjT3thuU3VfFnNkCqDn1SaV2%2BQoYnmREVo6DR2bnV3dMe%2BbsmX2JqYEUC9qbfJB93jzeCKotFOb7l8NeQVgeDSfCPGIKhVO0YGQkiQ4GTLfOfr2dlbq7DK54wvrU77Wfu9mCwFX4u7q7Pb2LJaihm8%2Bgx0fvxHAyoN9U1eNiNF8ATX%2FnMt0hWeI4CUt4fmTHQI2MSGIj2XSMYyPd6LWUKKuY%2BadUEuofUphAVvveayR0NtsyVru4W%2BDnNRKEPpcxg%2FundDTFHtH%2BJHBxqR3MV7vJaixZhqXAIj7iP%2FInmdPcUAT3zCFrpTJBjqkAYBlMC%2FRi%2Bobd%2BotzJauPWiVvTGsV%2FZOwUE3SLi20vHXzwf4sLM9ccMOPde28nriq2%2FmfXxM4GtVBUD6OkPuP7MzxWeDrYL6gIgECUdFErivwCtvyvDd8P0mOhErDM0nPjv%2Bbgj4DsGkKWElp8K75M9Pad8nW9EvH88usjkSuKJKUUV6RxdcpdaxIRuQj5pZS7WcA0QOn2dJKHP6ZEv9U%2FOmiusg&X-Amz-Signature=5e35abb7da1f0678bcc0828cbc93805e4fbea27f6ed93d04ade99dbacf96f85a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIBFRDGJ%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4ZZq%2B8XcVZTZVgHRkRYYX0F2mUhWVEGmmoWj4nzONHQIhALs%2BeHlzOW9r36W6scM20DkLDIHo9jtUhdj%2BKS0dgDwqKv8DCGQQABoMNjM3NDIzMTgzODA1IgxJHdB%2FDKboDk1Cw7Yq3AO9dU5bmTEvWuLMcMottLmqZc2siWe4n4w5uO1vgZ1UHfFchnXV37XJChqjHxxzW%2Fr5Ugh9gJYp0Qj1ukMk8yunWMFBJ8iv0%2F9NJl1Y6aShANEgYNJ9Qn5BZrl%2BU5ivNM1wfvhgMyHGZJ%2Bj4EBjy2PwzY7GkZrkW4pf8fs1924iXVOJ69PG0y605kDTU%2FO%2BVY%2Fj3Bko91ZI6eOKZuiEsHrQF8c%2FVF1kE3H4xQlwZMy6%2BHSwBmPb5QwRRx9wtnhmGbGiIKucWyMTXeBK%2FqSTKtCF9xFK4ZsuU4eY3hbVj9wQdKW7L8hscTgx5obdw76WsbxkNEveNEyz2ZjT3thuU3VfFnNkCqDn1SaV2%2BQoYnmREVo6DR2bnV3dMe%2BbsmX2JqYEUC9qbfJB93jzeCKotFOb7l8NeQVgeDSfCPGIKhVO0YGQkiQ4GTLfOfr2dlbq7DK54wvrU77Wfu9mCwFX4u7q7Pb2LJaihm8%2Bgx0fvxHAyoN9U1eNiNF8ATX%2FnMt0hWeI4CUt4fmTHQI2MSGIj2XSMYyPd6LWUKKuY%2BadUEuofUphAVvveayR0NtsyVru4W%2BDnNRKEPpcxg%2FundDTFHtH%2BJHBxqR3MV7vJaixZhqXAIj7iP%2FInmdPcUAT3zCFrpTJBjqkAYBlMC%2FRi%2Bobd%2BotzJauPWiVvTGsV%2FZOwUE3SLi20vHXzwf4sLM9ccMOPde28nriq2%2FmfXxM4GtVBUD6OkPuP7MzxWeDrYL6gIgECUdFErivwCtvyvDd8P0mOhErDM0nPjv%2Bbgj4DsGkKWElp8K75M9Pad8nW9EvH88usjkSuKJKUUV6RxdcpdaxIRuQj5pZS7WcA0QOn2dJKHP6ZEv9U%2FOmiusg&X-Amz-Signature=78fdc037cba9f9f0c5b516a73e2fa27aaded013aa288c69b5fbb7c3abfeb7a05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

