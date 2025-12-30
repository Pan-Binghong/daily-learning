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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/8a18f17b-ce98-4b1e-a6f3-5808468ecb85/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664ETRMEB%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Uy%2F8TNb4GIM%2FA9n6IF1fbUfJeetzSkf7wak8JpX%2BEAiA2rv3NQ4hXFN7nLGoxp6s2Ma90MYEVm3V3OLThWA0xRiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXMTVs4YP%2Bu8oOJJ7KtwDuIdO8rnkfPZx9aZ6OX3erp6inQgbzDdNPMDNiLRdkgujbHdc5WMcXO6nQDLr%2F5TfVDtg4IIyZ0w9%2Fwe5X9YPgh43pXTWHnG1XbjbzuLLF7uhFJgP5VjZOgCIKXAqnv4yksg%2FO2TbUSCbWRcL6q%2Bx68m69EoMRsKxhVtnPO4uo%2FIcqq36wC8ZyODc9LjSIH04AQytxibfGjucrqINiXcP5uz6a17Qsgtz%2FvFlVgz9n4laFSD2rDKMdQUMZOpmk56Vkhv%2FJI1m5XL%2FdxgLxFbjyQMv3Kwml2TuAVqRv6M4gyMYYLX1KyDFcr0kwLElBCUQGimk4pwBatY%2FolV05GgWe9hm3F9XYCPEU0pKYV6w86uaXlakvBMfoGHMj6o%2FY0%2FqHsKtGYLBVIXr15DA0HS68cEsG1kmG3LzPP%2FzPfeBscBEFbQSwteDicoc%2FYB3P5Km8dohnzxLBDy4Ta4RIrcOj4usgXa2b37Mhq4ZqaM%2F00QsCb2xi9hJuYxqfvDDUhdqmUdtdSCZ5wbzmepiSCEmqkSZjG%2BH2dAzlMZqCpzpvBMN1RfkuArcOYKwG7pyFAFcVzHehrqhRefEiwr9BwHzre98%2FFZlIki4ysjdykBKXnRpnxNk2XmNMc5nz8Iwt9XMygY6pgH9WxD8Qs8eTw2Mj48IkCy3Oa%2B%2FozguVA%2BpRwsZB%2Fd8f0cUo2cAsCAv9KbC5GmR6jsokD2PFLlf72s%2FZweb62G2Yw1ydI%2BXcwlQJyxkj12YU9Bq2a5e2nGE4olTiInFeYnnOq0EVlm8SNEsXj2H0oUgXk9cZi7K3Ojar0RbKnIwGG5ctoT67DNAQLTWnw8ie94%2BWrT%2BoEKlrNTWAprLnppEfv%2FhO8SZ&X-Amz-Signature=fa0e4eef51e222a5bcdda8e4cb99de741e0d7c0abc090a7ff4ef65fc9fdfc21e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/5b893c3e-69a9-4859-8eee-92f1caac826b/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664ETRMEB%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Uy%2F8TNb4GIM%2FA9n6IF1fbUfJeetzSkf7wak8JpX%2BEAiA2rv3NQ4hXFN7nLGoxp6s2Ma90MYEVm3V3OLThWA0xRiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXMTVs4YP%2Bu8oOJJ7KtwDuIdO8rnkfPZx9aZ6OX3erp6inQgbzDdNPMDNiLRdkgujbHdc5WMcXO6nQDLr%2F5TfVDtg4IIyZ0w9%2Fwe5X9YPgh43pXTWHnG1XbjbzuLLF7uhFJgP5VjZOgCIKXAqnv4yksg%2FO2TbUSCbWRcL6q%2Bx68m69EoMRsKxhVtnPO4uo%2FIcqq36wC8ZyODc9LjSIH04AQytxibfGjucrqINiXcP5uz6a17Qsgtz%2FvFlVgz9n4laFSD2rDKMdQUMZOpmk56Vkhv%2FJI1m5XL%2FdxgLxFbjyQMv3Kwml2TuAVqRv6M4gyMYYLX1KyDFcr0kwLElBCUQGimk4pwBatY%2FolV05GgWe9hm3F9XYCPEU0pKYV6w86uaXlakvBMfoGHMj6o%2FY0%2FqHsKtGYLBVIXr15DA0HS68cEsG1kmG3LzPP%2FzPfeBscBEFbQSwteDicoc%2FYB3P5Km8dohnzxLBDy4Ta4RIrcOj4usgXa2b37Mhq4ZqaM%2F00QsCb2xi9hJuYxqfvDDUhdqmUdtdSCZ5wbzmepiSCEmqkSZjG%2BH2dAzlMZqCpzpvBMN1RfkuArcOYKwG7pyFAFcVzHehrqhRefEiwr9BwHzre98%2FFZlIki4ysjdykBKXnRpnxNk2XmNMc5nz8Iwt9XMygY6pgH9WxD8Qs8eTw2Mj48IkCy3Oa%2B%2FozguVA%2BpRwsZB%2Fd8f0cUo2cAsCAv9KbC5GmR6jsokD2PFLlf72s%2FZweb62G2Yw1ydI%2BXcwlQJyxkj12YU9Bq2a5e2nGE4olTiInFeYnnOq0EVlm8SNEsXj2H0oUgXk9cZi7K3Ojar0RbKnIwGG5ctoT67DNAQLTWnw8ie94%2BWrT%2BoEKlrNTWAprLnppEfv%2FhO8SZ&X-Amz-Signature=71fc217f6784047d28dc1bed5d92a6452de67f5ebc252a69703fa11bdd90fb2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 详细数据集格式见:
---

### 训练

- 将图片以及处理后的train.jsonl、val.jsonl放置指定的目录下.
- 源码安装Swift
- 训练脚本
- 训练日志
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/16224622-1cd1-4465-9847-e485546450c4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664ETRMEB%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID5Uy%2F8TNb4GIM%2FA9n6IF1fbUfJeetzSkf7wak8JpX%2BEAiA2rv3NQ4hXFN7nLGoxp6s2Ma90MYEVm3V3OLThWA0xRiqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXMTVs4YP%2Bu8oOJJ7KtwDuIdO8rnkfPZx9aZ6OX3erp6inQgbzDdNPMDNiLRdkgujbHdc5WMcXO6nQDLr%2F5TfVDtg4IIyZ0w9%2Fwe5X9YPgh43pXTWHnG1XbjbzuLLF7uhFJgP5VjZOgCIKXAqnv4yksg%2FO2TbUSCbWRcL6q%2Bx68m69EoMRsKxhVtnPO4uo%2FIcqq36wC8ZyODc9LjSIH04AQytxibfGjucrqINiXcP5uz6a17Qsgtz%2FvFlVgz9n4laFSD2rDKMdQUMZOpmk56Vkhv%2FJI1m5XL%2FdxgLxFbjyQMv3Kwml2TuAVqRv6M4gyMYYLX1KyDFcr0kwLElBCUQGimk4pwBatY%2FolV05GgWe9hm3F9XYCPEU0pKYV6w86uaXlakvBMfoGHMj6o%2FY0%2FqHsKtGYLBVIXr15DA0HS68cEsG1kmG3LzPP%2FzPfeBscBEFbQSwteDicoc%2FYB3P5Km8dohnzxLBDy4Ta4RIrcOj4usgXa2b37Mhq4ZqaM%2F00QsCb2xi9hJuYxqfvDDUhdqmUdtdSCZ5wbzmepiSCEmqkSZjG%2BH2dAzlMZqCpzpvBMN1RfkuArcOYKwG7pyFAFcVzHehrqhRefEiwr9BwHzre98%2FFZlIki4ysjdykBKXnRpnxNk2XmNMc5nz8Iwt9XMygY6pgH9WxD8Qs8eTw2Mj48IkCy3Oa%2B%2FozguVA%2BpRwsZB%2Fd8f0cUo2cAsCAv9KbC5GmR6jsokD2PFLlf72s%2FZweb62G2Yw1ydI%2BXcwlQJyxkj12YU9Bq2a5e2nGE4olTiInFeYnnOq0EVlm8SNEsXj2H0oUgXk9cZi7K3Ojar0RbKnIwGG5ctoT67DNAQLTWnw8ie94%2BWrT%2BoEKlrNTWAprLnppEfv%2FhO8SZ&X-Amz-Signature=7be18b1e744312bdb0043f91953141e275027737e9da8b66b3251cef3b0fe8c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

