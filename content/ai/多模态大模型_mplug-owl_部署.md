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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3Z3ZKEY%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIC2EJoZacV18Qr5BgQ%2BmAjNzwcOHBaRnVtpH%2FblQfekUAiEA16X8rrJAJnZxfFJZIZHqkmcn3jIGeekdPLJq530p7lkqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFpJ1G%2BmKljzCna8qSrcA7m5XhlWslVwJ2UZ4ONvMJ56Y%2BFonB2I4TkUbXXU5hZdEQoytda4qpzbjGzOB497BIOcF9WCeXRJXt2c3KyhV84sc%2FqENoOOQ6cXUOLxlm2zKZsrVwFpkqGkxHtVwoRO2nNRJqbMc%2FyhMDN%2BKvNoIoPDGOrpVXWLpQ43SkstxVINVbRGF%2BjaztxLR0I7IsYiVijTZY7mq2z9CNmFxfsMcg1RDl4ayyFvSTWUrQxlWu5ibqSuvOLSNIpGjKSvSgtYh4tmfFA858HKme3saY1ROsVW%2B73M5KjAwU03NLYlC%2BGw0NJotak7bcAPZKTjWyu4FIcqSjf7SZQ98NkXoG%2FjJV6GsidCXkDUyAsD045g4UuEf0206iIsuCv8HJntFwBxceweVmK%2FOreiPNfGejwY6Jc1m1k5wWnIHNKWzJGMbOeDmotY6OPcr01%2Fa6SqRfrmXC9j1dU0gqKrUm657DuJXiorzXKjbKfOzxwB%2FIj9tqLZlXOXCc1hnkxGA5PhsukGQmD383LKtRVr0wRl7spGHFqeZz0YjiPs3U%2Fanq1e43g7%2B67fCCSouk2orklBUIuEK7gyxjcpbDDF6hVj%2FueUfb37OM4Ler1ZH3Es4Ei5pJlRnr%2FC%2BkQZ5DKQZ3mGMIDZhcwGOqUB0zW0EG%2FOxOIgZ7ZCuACLdJfxaUJqUzva5m6UQOHfZT0ifm%2F3QL%2BIZ1B7v05h%2B2SsevqT4UPQRG0r4wYwXuodfYEWQT5Wicmwk7QHFVbekg4zDGDsf%2BWNq9b0yNBz5delFKFnjdxdWGikx%2Bbc8iGsqZ%2F7gNKic8zGqeZya%2BDz8cA0cwSRgAGwDHHT5oKAgIwQxs3Td1LmcwCTfA5Fu9zLGVg%2B0T1r&X-Amz-Signature=f51fd624d7e35c414c93e93eb990a7b76bbfee36ca23a0fc58b004c56984d3ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3Z3ZKEY%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIC2EJoZacV18Qr5BgQ%2BmAjNzwcOHBaRnVtpH%2FblQfekUAiEA16X8rrJAJnZxfFJZIZHqkmcn3jIGeekdPLJq530p7lkqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFpJ1G%2BmKljzCna8qSrcA7m5XhlWslVwJ2UZ4ONvMJ56Y%2BFonB2I4TkUbXXU5hZdEQoytda4qpzbjGzOB497BIOcF9WCeXRJXt2c3KyhV84sc%2FqENoOOQ6cXUOLxlm2zKZsrVwFpkqGkxHtVwoRO2nNRJqbMc%2FyhMDN%2BKvNoIoPDGOrpVXWLpQ43SkstxVINVbRGF%2BjaztxLR0I7IsYiVijTZY7mq2z9CNmFxfsMcg1RDl4ayyFvSTWUrQxlWu5ibqSuvOLSNIpGjKSvSgtYh4tmfFA858HKme3saY1ROsVW%2B73M5KjAwU03NLYlC%2BGw0NJotak7bcAPZKTjWyu4FIcqSjf7SZQ98NkXoG%2FjJV6GsidCXkDUyAsD045g4UuEf0206iIsuCv8HJntFwBxceweVmK%2FOreiPNfGejwY6Jc1m1k5wWnIHNKWzJGMbOeDmotY6OPcr01%2Fa6SqRfrmXC9j1dU0gqKrUm657DuJXiorzXKjbKfOzxwB%2FIj9tqLZlXOXCc1hnkxGA5PhsukGQmD383LKtRVr0wRl7spGHFqeZz0YjiPs3U%2Fanq1e43g7%2B67fCCSouk2orklBUIuEK7gyxjcpbDDF6hVj%2FueUfb37OM4Ler1ZH3Es4Ei5pJlRnr%2FC%2BkQZ5DKQZ3mGMIDZhcwGOqUB0zW0EG%2FOxOIgZ7ZCuACLdJfxaUJqUzva5m6UQOHfZT0ifm%2F3QL%2BIZ1B7v05h%2B2SsevqT4UPQRG0r4wYwXuodfYEWQT5Wicmwk7QHFVbekg4zDGDsf%2BWNq9b0yNBz5delFKFnjdxdWGikx%2Bbc8iGsqZ%2F7gNKic8zGqeZya%2BDz8cA0cwSRgAGwDHHT5oKAgIwQxs3Td1LmcwCTfA5Fu9zLGVg%2B0T1r&X-Amz-Signature=ab547ddf85907a7270fc0a95ad46d030ba603eac527a7e985e95313d4adfaf46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

