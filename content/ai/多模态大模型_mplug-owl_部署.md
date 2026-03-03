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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3FTDI55%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaoRIluYUeBB%2FiIKEOOd1VS5qYRo4Kozzq4h3sK9zD8AiA3VetrVdUNTRU2ymvxdTndOdYzHlR9L9B2MZ67sfaK3yqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQIuxXzNUZupD%2BfCVKtwDjXVxjVQlFwIypp5Q4LyhAQ1d5fYjgLelm68CW06eV1R2pxBIWPix%2F6o%2Bjhs3AhxARQ8OCSWzcHoTwnsGHAU3fW0Wg1gpkbj%2FZK%2F9bgz0H%2Fwy7fTadj0k5hHZFCamB1tZCD0NpVOqyOsWE8BeaAcqbpoKg8m5vMWRB%2FrXy1Q4rygox3TcknJRpWIU5MPkGGDcpDSUbm489xDzdrJ21%2BGlSmcdArgdCIXwgZM5rA2VujqzNo9xvY6e2pHlP3xj9vzCeX8BVBOf%2BZgV5W3fO1mGPK3ipcPaGsTKwE79A7KcPY%2BjP0Mog4fCswOYj3KAUEHJunv88yuLlyVNNAjmogN%2FM%2FVkpy1uVH0qi7WYuRQCCgmycwJ5gvxa1rcwi%2FzQMNP50EZKR2tfp4WKdZ0mBA1ZToEnC%2Bi%2FwOnGVwso2EH6t1rrROFHaLz8i2HYmAiu98GlVTnzMEBxAkROI04tMhHDD08WXqByPtcDjuNAmfqO%2F1xmxnL9fOct1jwrfWEZx%2BQPN%2BNcKySmG2ThQVzOVApriCxWc8TEnBdQLPjuCTMib3yV2zXOtrQAuq00x%2B%2BaKusijEkDOMFfcCreMj1uRGa1FQfg14vzuQF5bj4vIgScxPN8M4sj5xFvamPrEv4wjraYzQY6pgFH3djxw%2BS%2FjzR0uyvMuiEZA2UW6iAFIB21CcqLgpfwmL4UEyFgYDUvszoRBookapAXv5j4zHiL5B%2Bb4VLMNOxrOGE3dq7m5CW7DNyiQnz%2BGtzFioW%2Bv1LGrrodiuEXBbF1xBq%2BruqKMJN%2Bb0PZewiycIver3R0CbbqCxZW8YrQlpiobVYLDQmc5mTw1Xs0iwQdYEkZQPkvflFhY4N8966eHLKwMMCg&X-Amz-Signature=425c8248710243abf1e8491bf1fe1e5b84d96329a963e3ef4bd5afefbce5bf7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3FTDI55%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaoRIluYUeBB%2FiIKEOOd1VS5qYRo4Kozzq4h3sK9zD8AiA3VetrVdUNTRU2ymvxdTndOdYzHlR9L9B2MZ67sfaK3yqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQIuxXzNUZupD%2BfCVKtwDjXVxjVQlFwIypp5Q4LyhAQ1d5fYjgLelm68CW06eV1R2pxBIWPix%2F6o%2Bjhs3AhxARQ8OCSWzcHoTwnsGHAU3fW0Wg1gpkbj%2FZK%2F9bgz0H%2Fwy7fTadj0k5hHZFCamB1tZCD0NpVOqyOsWE8BeaAcqbpoKg8m5vMWRB%2FrXy1Q4rygox3TcknJRpWIU5MPkGGDcpDSUbm489xDzdrJ21%2BGlSmcdArgdCIXwgZM5rA2VujqzNo9xvY6e2pHlP3xj9vzCeX8BVBOf%2BZgV5W3fO1mGPK3ipcPaGsTKwE79A7KcPY%2BjP0Mog4fCswOYj3KAUEHJunv88yuLlyVNNAjmogN%2FM%2FVkpy1uVH0qi7WYuRQCCgmycwJ5gvxa1rcwi%2FzQMNP50EZKR2tfp4WKdZ0mBA1ZToEnC%2Bi%2FwOnGVwso2EH6t1rrROFHaLz8i2HYmAiu98GlVTnzMEBxAkROI04tMhHDD08WXqByPtcDjuNAmfqO%2F1xmxnL9fOct1jwrfWEZx%2BQPN%2BNcKySmG2ThQVzOVApriCxWc8TEnBdQLPjuCTMib3yV2zXOtrQAuq00x%2B%2BaKusijEkDOMFfcCreMj1uRGa1FQfg14vzuQF5bj4vIgScxPN8M4sj5xFvamPrEv4wjraYzQY6pgFH3djxw%2BS%2FjzR0uyvMuiEZA2UW6iAFIB21CcqLgpfwmL4UEyFgYDUvszoRBookapAXv5j4zHiL5B%2Bb4VLMNOxrOGE3dq7m5CW7DNyiQnz%2BGtzFioW%2Bv1LGrrodiuEXBbF1xBq%2BruqKMJN%2Bb0PZewiycIver3R0CbbqCxZW8YrQlpiobVYLDQmc5mTw1Xs0iwQdYEkZQPkvflFhY4N8966eHLKwMMCg&X-Amz-Signature=b18658f7dfffab21e19ced7d1ebcfa9972ae40fc7b1bfe580fb13685e008ef29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

