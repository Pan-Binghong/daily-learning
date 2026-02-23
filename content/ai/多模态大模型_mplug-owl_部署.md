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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTQ3R4EX%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIGXmtsS9u%2BQmSD5llMpogVAzVlusukyqMsdy3cWFmEMsAiBypy4UaT3Ud3vEUwcscJwnRuhTXECtucrJ8aJg3xvaGSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5oMoyjum4f57VpiTKtwDdkqPcBcNVvMu%2FqywkvpH%2BZhe1SJad8gzzfYUW3BX2%2FuxhTIDTDnieTzqUuu6NU2%2FpqBwemGavbUw2%2FDjPAK6Cqnem1fWwFWb8Kh3UCZh8i98ZAV3bIeo7txMvTnnis0WJSAf9%2F4xtrKVy3Z0sbCeyr82fltITl34IsBRs3nIA3Zc3lxLI98qJOJiqQ5xm%2B2teJ20Bpc6B2rXvu4VU8ZY6zJfFdUJHyGIynCkbOkqHiTgBXD2wKUZEGafiOw4WIkI5qezHkIMWGSodjXnkW9qZKoeUM2WFAcJoYvef%2B8EhdsLbs5LoHOU3PjEGH1%2Fj%2F7f3eQgQhyGAsYrFXOwlasxbgBzV5aN5PbV7QZzBcBYukeTmc2IC4cd2FdR3rHe3pw%2BkbdfbXFVmx2fQwYIWrfYAKLNHDsjdJbCg1Rb8j7mtouQy2BjaRvUh2h07J9EVkPYnKtpQ8yhq9UGjWPx3raO3Oa1byfa7rRUGLtyJIpvXh7q4bG2NMZwDibZ6pIU6eIaJAuZconRivSQqvJEooJbbfc4qzs7PrHqknLcUX612Fngt8MJVlt%2FDDew5d9D0xKREP2ctZ%2F1AQy665mlpqMveLK4P4PxDm7YdYKsTDYxk9q5yGr99HV7pIVyLPwwrpPvzAY6pgHzUuRkqc8M5SQUbXJ6hrMfbEMObGPvWNYKRVirKebixBddsvDrr8utJiDC6Q1bCQIhAeBqqa1wxwZY0Fq5FeBcvhZqlfIcJ32deYth1ioA6BPgJRjoxU9nYEK7r2WugEUOsSN7zaZmN20V36PfgNI4QAIby%2B7wMHwE28ctLaDYe3GjJ0LUngmJergsTp1rPnUPdCBMRUrMJIrwU8kQQqbnOp3pza%2Bz&X-Amz-Signature=4e7ae530d83e6dfe7f8274ac7c6d42dafbf72ca9f6f6dee8ec60cf210dd55e2a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTQ3R4EX%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIGXmtsS9u%2BQmSD5llMpogVAzVlusukyqMsdy3cWFmEMsAiBypy4UaT3Ud3vEUwcscJwnRuhTXECtucrJ8aJg3xvaGSqIBAjU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5oMoyjum4f57VpiTKtwDdkqPcBcNVvMu%2FqywkvpH%2BZhe1SJad8gzzfYUW3BX2%2FuxhTIDTDnieTzqUuu6NU2%2FpqBwemGavbUw2%2FDjPAK6Cqnem1fWwFWb8Kh3UCZh8i98ZAV3bIeo7txMvTnnis0WJSAf9%2F4xtrKVy3Z0sbCeyr82fltITl34IsBRs3nIA3Zc3lxLI98qJOJiqQ5xm%2B2teJ20Bpc6B2rXvu4VU8ZY6zJfFdUJHyGIynCkbOkqHiTgBXD2wKUZEGafiOw4WIkI5qezHkIMWGSodjXnkW9qZKoeUM2WFAcJoYvef%2B8EhdsLbs5LoHOU3PjEGH1%2Fj%2F7f3eQgQhyGAsYrFXOwlasxbgBzV5aN5PbV7QZzBcBYukeTmc2IC4cd2FdR3rHe3pw%2BkbdfbXFVmx2fQwYIWrfYAKLNHDsjdJbCg1Rb8j7mtouQy2BjaRvUh2h07J9EVkPYnKtpQ8yhq9UGjWPx3raO3Oa1byfa7rRUGLtyJIpvXh7q4bG2NMZwDibZ6pIU6eIaJAuZconRivSQqvJEooJbbfc4qzs7PrHqknLcUX612Fngt8MJVlt%2FDDew5d9D0xKREP2ctZ%2F1AQy665mlpqMveLK4P4PxDm7YdYKsTDYxk9q5yGr99HV7pIVyLPwwrpPvzAY6pgHzUuRkqc8M5SQUbXJ6hrMfbEMObGPvWNYKRVirKebixBddsvDrr8utJiDC6Q1bCQIhAeBqqa1wxwZY0Fq5FeBcvhZqlfIcJ32deYth1ioA6BPgJRjoxU9nYEK7r2WugEUOsSN7zaZmN20V36PfgNI4QAIby%2B7wMHwE28ctLaDYe3GjJ0LUngmJergsTp1rPnUPdCBMRUrMJIrwU8kQQqbnOp3pza%2Bz&X-Amz-Signature=e3dd987d968d4c30a9b18fd56339e7cd39d9879fd2450219444dabc2a492a4ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

