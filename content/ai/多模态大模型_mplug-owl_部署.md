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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGFOBDI2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QffaKp7MKZZGnCN7SPXa56Bb5IBunOyMJKyWriu3KwIhAJxXlwIix8e1D6gM5LLqfLzw8HvTf5XKvOm%2BUQavvykUKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwe%2BlV4caxiXpL%2Bbj4q3AOp7CdQyabtAcmxkMf3mIshV8l685vuQrQ2JZIST0u8wSYanlWf9DO76h2%2BPt19yt0uZpV8A6z0yp5rqXwrSfhNYr1mVo%2BlSrHzHBlnjCOHeeo6aK%2B2mJRQcqNJjaAxX7S1fw0YwvSbvZfrCKUpKhOoK%2FE0oIPi%2BZZsr2T2oh%2BD%2FgutxitZL03fd0SzJcmVQYAmVVQlej0fUmkH6uY2wQ08cc8Dp%2BvADfAb8HHtgrruXTLRLD6cgtdIMRK0rKc0SqrqRARxFQ2WodHqlmlLFnf%2BAdDRSEKm0XiyHkv0IkfFrDYM3IvNABrRJ2HI1ibuX5I9tw69xls00ASoaOLdr0fNk%2BvSx%2Fy%2FI8eIcnzHPsqSsTLKpcosQTgisrnbYGMPtvTR4GYs17b7D%2FjFOCYskMsepzULB2E%2Be%2BRD5LpDs%2BV3TxTMf%2F%2Bz5tH9tZOi4bwN7qO499O3Sb6Lsw4XAbwi1noUJFsBhWeGL9HfN%2FnJt%2FY%2FMX3Wwr%2FrX0zOU13Xucq%2FA4pyJ7KN99zEpWeZn7CtGr7FpP0dgtFh5fyNIDTNXMRPxja4X7YH5Kdtu5r3FsnQzsS1ti3qeSSK1N%2BCeGi7dZixEZvO7lXkuzAMttMN30%2BeHFlUtaPiOr1c1vN%2BhTDUl6XMBjqkAb%2BkbJsXimusGXnpWzYh2H7kVzbmSz34cixet%2BtNQ9VWKAwwxi8neFrVmzZ%2FEaGsNc3rvWiEPZxCKWpXzry%2B7P3EjDLDOX87wWQkrQuwqtEhQTe8h5zszIUXGm5f8fSOil9VQT3pXjwYrQkFETmcS8aRaKkUaeULAZz%2FKxmiSuU%2Bg72TDAi3NcmL1lzgZrfNsHeFrlYqQLT2L%2BuO1OBEW9K7qn97&X-Amz-Signature=f86457e065ba8dc00ca3a457e8c7d7e09c0ed5e6540d85be185224fcd9629afa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QGFOBDI2%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC1QffaKp7MKZZGnCN7SPXa56Bb5IBunOyMJKyWriu3KwIhAJxXlwIix8e1D6gM5LLqfLzw8HvTf5XKvOm%2BUQavvykUKogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwe%2BlV4caxiXpL%2Bbj4q3AOp7CdQyabtAcmxkMf3mIshV8l685vuQrQ2JZIST0u8wSYanlWf9DO76h2%2BPt19yt0uZpV8A6z0yp5rqXwrSfhNYr1mVo%2BlSrHzHBlnjCOHeeo6aK%2B2mJRQcqNJjaAxX7S1fw0YwvSbvZfrCKUpKhOoK%2FE0oIPi%2BZZsr2T2oh%2BD%2FgutxitZL03fd0SzJcmVQYAmVVQlej0fUmkH6uY2wQ08cc8Dp%2BvADfAb8HHtgrruXTLRLD6cgtdIMRK0rKc0SqrqRARxFQ2WodHqlmlLFnf%2BAdDRSEKm0XiyHkv0IkfFrDYM3IvNABrRJ2HI1ibuX5I9tw69xls00ASoaOLdr0fNk%2BvSx%2Fy%2FI8eIcnzHPsqSsTLKpcosQTgisrnbYGMPtvTR4GYs17b7D%2FjFOCYskMsepzULB2E%2Be%2BRD5LpDs%2BV3TxTMf%2F%2Bz5tH9tZOi4bwN7qO499O3Sb6Lsw4XAbwi1noUJFsBhWeGL9HfN%2FnJt%2FY%2FMX3Wwr%2FrX0zOU13Xucq%2FA4pyJ7KN99zEpWeZn7CtGr7FpP0dgtFh5fyNIDTNXMRPxja4X7YH5Kdtu5r3FsnQzsS1ti3qeSSK1N%2BCeGi7dZixEZvO7lXkuzAMttMN30%2BeHFlUtaPiOr1c1vN%2BhTDUl6XMBjqkAb%2BkbJsXimusGXnpWzYh2H7kVzbmSz34cixet%2BtNQ9VWKAwwxi8neFrVmzZ%2FEaGsNc3rvWiEPZxCKWpXzry%2B7P3EjDLDOX87wWQkrQuwqtEhQTe8h5zszIUXGm5f8fSOil9VQT3pXjwYrQkFETmcS8aRaKkUaeULAZz%2FKxmiSuU%2Bg72TDAi3NcmL1lzgZrfNsHeFrlYqQLT2L%2BuO1OBEW9K7qn97&X-Amz-Signature=ba0e861ceed6fb71631aa368a63ef8edce5fe89cb272ab36528f0c91b94d594d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

