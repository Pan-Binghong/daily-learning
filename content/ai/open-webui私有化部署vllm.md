---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SFWNNFT%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIAYaAssvFDIaeE%2FfpqJlPoQ7zv9VdevS5F0Jn5seuD0BAiEAmjsEq141y5JXWypATZa1aIFp2reLDJUB30du5yRxiSoqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOUQDxj%2BrJRMokPM4CrcA420ejYyEYnVJaKmvWYIcrULxGCF63kNmXTNeeOXY0o8jN3F3l8c7jNmNKTtehyCTdlQ%2BD1YZj43SaY5aGzy%2BI6gktnIN45sKp%2BRSKmq%2BPGDcKzZDhR6WT4ABIsyToYRKVXdLCFE98sSOeGXmIMYOzptupM1UmdD4TAOWlmra%2BSe6yOM4%2B3DyaSsr6aRqxWvSdD62gdGZ4ERlm3g%2BxmTMxN9%2BbSZiDI9z%2F4Z71GQrqvv5GEWYlqcVTJXkwb0KC2Vi6V3%2BO5YTCafUCLptk8v%2FjtLxa8YBSa3nRkf9rAcsoiQbXeFJIrYV4HXIjuAmjWxRyszjHR6UWCG5%2FIDRjTIVoALh0fN5%2Bwz7SUVgFOAX8mTI2BFNp3EKkMKR4u43CiSYV3D2ImKB7SY5mhsgwm2zh3bSiIV6qUvrYIpejdStqiNifd5yYNBQL9OIjP19tOMlDaXPW6mNoVxnqUv0vtHx3vtOcnGnrCk1WQ9Zh3M7fkdbzAl7honuWEcsVPStr9dGTRfLYBhckvfR%2F6Tp%2BvK5qcKO3J1uIE0c7ggxpWgFhEhenLK7O99qZWx9T%2BI3zqVcNvDuikIvzhhNIhgqFuVBiTlA%2BRARDKd2OnI51S4Y2qX8XUXThNKtl7g2IxfMNCsi88GOqUBWwa1LflFinZ7kymRDYE3jxD3BV%2BEp6RFADWciDU2vstYFu5JPM8Cws%2Btei4C4K8f3iGsvnya0V3Q%2B5HnN0UEp8qYT1RwLqQdub5qlVLjDPknzPNv4Po9DIq7oDaKIoc7LoiwQ5Qes7bNTqQyldJISmNek7wxkujEqBpxZLwu22s5u1D5MiU5Tl%2FU5cleRwOxaMhezHGMweSKeJbpDS3%2BGmt1zpQW&X-Amz-Signature=57978c6af973bacc3976018605204f25147a291129cdecd270b3de139f5be0bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

## 安装

该前端框架采用docker镜像部署，模型采用vllm镜像单独发布。

1. 拉取最新版本镜像
1. 启动容器
1. 打开浏览器查看8000端口 
---

## 踩坑

- 模型URL地址要写V1 
- 使用openai api进行链接一直报503的错，进到backend/open_webui/utils/model.py，注释以下代码即可。
---

> References



