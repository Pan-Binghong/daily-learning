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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNX6BEC2%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCAHHf2NF%2F7rGBzV7uZf9MTjGQDpesD%2FEXm5VNevlckOQIgFmBG9OQ5DCHExJQqGris3EcGKKcdOG8zXq6VONGeiAQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDK6Df0wceF7pxcKwgCrcA3NN4mkft76LMucv7k1og0ywMvej8wSEcXy7aB%2FU8YiLdapNCQpgvX7zFS%2B4PYXRWPvk7DUrDyN6%2FV1P%2Fx8JLwXVUlfRulo%2FccSOtqE5xtEKLpW6vi%2FNtD%2FyhYb8Yb7XhMzzhZ26SrO6SWTcdeQtJ4sV2oz%2FuqJOkdZoh0ntGtYCQq2e9Xy%2FR5V1ILQ%2FJvn7iiy1y3AmyyMI4wre1oGiQvXVVwt5DrfmVyryVL5s2kUgEMebau6OCUJ81gPoKkslRbk0CZD%2FxfN67EuiV6YCKdLsm2nbTktBlBNwPhVFH6EcBa%2FjLyTbOaF3biG2SKdY4n6xyRCEjtzixB1GeXFcfQW9V3pc9IaS%2FOGafYZU3gHTj%2Fn9czigXoEIg0PH2t6tc8j9iAlKgfiN8VH%2FeO5ghFI2Z66GkuMAzHDedxFQYtm2qDykHVjtc5%2BtFZaodKuvFZfMBlZg0hFg3lcVUKGnfc4w6lyGUA2yjj0NoHbzlXKeEi0VuqzaUw2P5XEAedTA0NkpAOtW%2BmV4JQuj%2FCUspXwuNjG4K4KRhEJM8f3sa0EA9MuJQHsYXQLavGg596pjaTESBWV25dP%2FZBFhZH1kTmP%2F7oR%2FCnC4JW%2FLkoSK9oUGsBAKgukv8%2BwjHZbfMOjjz8gGOqUBCweEUAB42XgyujmlCi%2Fa8r2vhPxj5o%2BlA5PG3jCRyY9UbAEbt29mfi1qHw9iAeEO0g7RL6m4r1gwBg15JOJ6N%2BnLrUzmGhDUzZHPxdRG1dQ3EGohL6Yitfd%2FzbXj%2BemCNo7XAZoGGjLVgVcSTmNOPxnuMkqFRadzi8kLCblGedfgorsWFKITQpmcstfcbkI46ekqrKnaBlW%2BARmukBGiwUMSfhcP&X-Amz-Signature=05e7e60603663f408a955cd19c13eeacc02580859f5a745d072ebd1b82582513&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNX6BEC2%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCAHHf2NF%2F7rGBzV7uZf9MTjGQDpesD%2FEXm5VNevlckOQIgFmBG9OQ5DCHExJQqGris3EcGKKcdOG8zXq6VONGeiAQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDK6Df0wceF7pxcKwgCrcA3NN4mkft76LMucv7k1og0ywMvej8wSEcXy7aB%2FU8YiLdapNCQpgvX7zFS%2B4PYXRWPvk7DUrDyN6%2FV1P%2Fx8JLwXVUlfRulo%2FccSOtqE5xtEKLpW6vi%2FNtD%2FyhYb8Yb7XhMzzhZ26SrO6SWTcdeQtJ4sV2oz%2FuqJOkdZoh0ntGtYCQq2e9Xy%2FR5V1ILQ%2FJvn7iiy1y3AmyyMI4wre1oGiQvXVVwt5DrfmVyryVL5s2kUgEMebau6OCUJ81gPoKkslRbk0CZD%2FxfN67EuiV6YCKdLsm2nbTktBlBNwPhVFH6EcBa%2FjLyTbOaF3biG2SKdY4n6xyRCEjtzixB1GeXFcfQW9V3pc9IaS%2FOGafYZU3gHTj%2Fn9czigXoEIg0PH2t6tc8j9iAlKgfiN8VH%2FeO5ghFI2Z66GkuMAzHDedxFQYtm2qDykHVjtc5%2BtFZaodKuvFZfMBlZg0hFg3lcVUKGnfc4w6lyGUA2yjj0NoHbzlXKeEi0VuqzaUw2P5XEAedTA0NkpAOtW%2BmV4JQuj%2FCUspXwuNjG4K4KRhEJM8f3sa0EA9MuJQHsYXQLavGg596pjaTESBWV25dP%2FZBFhZH1kTmP%2F7oR%2FCnC4JW%2FLkoSK9oUGsBAKgukv8%2BwjHZbfMOjjz8gGOqUBCweEUAB42XgyujmlCi%2Fa8r2vhPxj5o%2BlA5PG3jCRyY9UbAEbt29mfi1qHw9iAeEO0g7RL6m4r1gwBg15JOJ6N%2BnLrUzmGhDUzZHPxdRG1dQ3EGohL6Yitfd%2FzbXj%2BemCNo7XAZoGGjLVgVcSTmNOPxnuMkqFRadzi8kLCblGedfgorsWFKITQpmcstfcbkI46ekqrKnaBlW%2BARmukBGiwUMSfhcP&X-Amz-Signature=3cbb18e5b6b87dc7b713eb7ea40e3c278c8205a4c6f4dec2058b7b74f989b016&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

