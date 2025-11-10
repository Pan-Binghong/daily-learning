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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRHV6Q6G%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDBsIhScUVtxyRupLqPRkuaX05%2FGuhasoILZoqOW5AjkwIhALan4dHPjp1CCoatnyrpnBi%2Fn4558xzbpmhofQiLYyMmKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Fh2%2Bu78qKSBEE7akq3AM38Ok3JGWAU1cwP5ResVVblBHvcOZAlvNaPeDmsYFFOcrLunC4KOPG%2FiSm8ihF6K90flna4vMW7n%2BhVRnx%2F0P6InIzBASPPtbZ1hePTjI3Ig1VxlhwZ5W2h0JarhlwYh%2F7ZKtoWSMXYMSyWYBvNL%2FPBPikWULMG5CCOVQvUFKNR8yxm9TE%2BxaZFtPEse4lTX2MBRRF75R8tUZSFR0Kad0u4ImDxIJNQRjf%2F%2F3XdouYgvNm58UYs6x0KhxwYxVjUMSLzMg4NYuomcDaZK9O2UhSSUlGnMqeDeqzLixB95zqFHHg8vwTdRRt4IWWan7lgZK2XN4lcY9rCwVMHXIh5UM77a9MZbXtmObky2rB5mmzdrwUoVp42s4cYM2dt85Ccx8mk1c3ZwmuMONHkxS4XyIglEYj02Fjn8HagaE722evVAth5rcHltNMS1y0D4N2t7wOq4f7CcRLibCDEAr9cFjTm%2F5KswIUidZ3yx6RdIoqdssge1LezdE4cWMhK%2FAacqfiVuFZpU4SGEZl%2F%2Bqc7LbpW64QvWHECNONUyp6s%2B2Qd1%2BOWSiP6AfNOxz%2FXRnjiGSwh1j4pqgYjXBCd95oggeBbYW8ZC8hKzHhlW7dqKLrPohtsLIQQPsyibotFjCVr8TIBjqkATCapkfBQeeC29bfDwfY%2FuKJnE2XYKVVtP9%2FYEtf6lR16JSbrmELrrTF9thIg8Ac33czPgKY2FnhyTEacTRFN%2F%2FSrcRpJCE6bjQz9Q1wQUA%2F5E63mZZYy8mbjbR0NbHb777nwM7Ks8iSOyYZWFA6SNLUtcBlxBr7PXT6be9KoLp6MR4RzwwksA5mkHC4GSYX4pXaLtcvOJmJ%2FFiBOI2XHFnD3zd%2B&X-Amz-Signature=5e34b9e53e546c6b296ed4f980b150d34586756cfa0dca8aa526e320072cba45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRHV6Q6G%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDBsIhScUVtxyRupLqPRkuaX05%2FGuhasoILZoqOW5AjkwIhALan4dHPjp1CCoatnyrpnBi%2Fn4558xzbpmhofQiLYyMmKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Fh2%2Bu78qKSBEE7akq3AM38Ok3JGWAU1cwP5ResVVblBHvcOZAlvNaPeDmsYFFOcrLunC4KOPG%2FiSm8ihF6K90flna4vMW7n%2BhVRnx%2F0P6InIzBASPPtbZ1hePTjI3Ig1VxlhwZ5W2h0JarhlwYh%2F7ZKtoWSMXYMSyWYBvNL%2FPBPikWULMG5CCOVQvUFKNR8yxm9TE%2BxaZFtPEse4lTX2MBRRF75R8tUZSFR0Kad0u4ImDxIJNQRjf%2F%2F3XdouYgvNm58UYs6x0KhxwYxVjUMSLzMg4NYuomcDaZK9O2UhSSUlGnMqeDeqzLixB95zqFHHg8vwTdRRt4IWWan7lgZK2XN4lcY9rCwVMHXIh5UM77a9MZbXtmObky2rB5mmzdrwUoVp42s4cYM2dt85Ccx8mk1c3ZwmuMONHkxS4XyIglEYj02Fjn8HagaE722evVAth5rcHltNMS1y0D4N2t7wOq4f7CcRLibCDEAr9cFjTm%2F5KswIUidZ3yx6RdIoqdssge1LezdE4cWMhK%2FAacqfiVuFZpU4SGEZl%2F%2Bqc7LbpW64QvWHECNONUyp6s%2B2Qd1%2BOWSiP6AfNOxz%2FXRnjiGSwh1j4pqgYjXBCd95oggeBbYW8ZC8hKzHhlW7dqKLrPohtsLIQQPsyibotFjCVr8TIBjqkATCapkfBQeeC29bfDwfY%2FuKJnE2XYKVVtP9%2FYEtf6lR16JSbrmELrrTF9thIg8Ac33czPgKY2FnhyTEacTRFN%2F%2FSrcRpJCE6bjQz9Q1wQUA%2F5E63mZZYy8mbjbR0NbHb777nwM7Ks8iSOyYZWFA6SNLUtcBlxBr7PXT6be9KoLp6MR4RzwwksA5mkHC4GSYX4pXaLtcvOJmJ%2FFiBOI2XHFnD3zd%2B&X-Amz-Signature=c32aa3298cc2ebfeef5054c57e634aa2faf1bb6e6cd5d339893615c59490d61a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRHV6Q6G%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T024934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJIMEYCIQDBsIhScUVtxyRupLqPRkuaX05%2FGuhasoILZoqOW5AjkwIhALan4dHPjp1CCoatnyrpnBi%2Fn4558xzbpmhofQiLYyMmKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Fh2%2Bu78qKSBEE7akq3AM38Ok3JGWAU1cwP5ResVVblBHvcOZAlvNaPeDmsYFFOcrLunC4KOPG%2FiSm8ihF6K90flna4vMW7n%2BhVRnx%2F0P6InIzBASPPtbZ1hePTjI3Ig1VxlhwZ5W2h0JarhlwYh%2F7ZKtoWSMXYMSyWYBvNL%2FPBPikWULMG5CCOVQvUFKNR8yxm9TE%2BxaZFtPEse4lTX2MBRRF75R8tUZSFR0Kad0u4ImDxIJNQRjf%2F%2F3XdouYgvNm58UYs6x0KhxwYxVjUMSLzMg4NYuomcDaZK9O2UhSSUlGnMqeDeqzLixB95zqFHHg8vwTdRRt4IWWan7lgZK2XN4lcY9rCwVMHXIh5UM77a9MZbXtmObky2rB5mmzdrwUoVp42s4cYM2dt85Ccx8mk1c3ZwmuMONHkxS4XyIglEYj02Fjn8HagaE722evVAth5rcHltNMS1y0D4N2t7wOq4f7CcRLibCDEAr9cFjTm%2F5KswIUidZ3yx6RdIoqdssge1LezdE4cWMhK%2FAacqfiVuFZpU4SGEZl%2F%2Bqc7LbpW64QvWHECNONUyp6s%2B2Qd1%2BOWSiP6AfNOxz%2FXRnjiGSwh1j4pqgYjXBCd95oggeBbYW8ZC8hKzHhlW7dqKLrPohtsLIQQPsyibotFjCVr8TIBjqkATCapkfBQeeC29bfDwfY%2FuKJnE2XYKVVtP9%2FYEtf6lR16JSbrmELrrTF9thIg8Ac33czPgKY2FnhyTEacTRFN%2F%2FSrcRpJCE6bjQz9Q1wQUA%2F5E63mZZYy8mbjbR0NbHb777nwM7Ks8iSOyYZWFA6SNLUtcBlxBr7PXT6be9KoLp6MR4RzwwksA5mkHC4GSYX4pXaLtcvOJmJ%2FFiBOI2XHFnD3zd%2B&X-Amz-Signature=f19db8072db7a98f9482559f9fbc16ac8bf7733ad8bfda26dab4c901c1b1d3d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

