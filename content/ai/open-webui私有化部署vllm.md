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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIEULYI6%2F20251122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251122T022637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFIaCXVzLXdlc3QtMiJGMEQCIBqVyU0AHde085RuuL%2FEWakur5w3Mg71eEhNaH8ejpnLAiAVxr5TqTdr4jZl%2BQPpkNt3n40BN9mANBC1oTrP4qfutSr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMgPu%2FUv68vNIgWURPKtwDoCm4p2L5iSb1LYmRzFD37PdRo9bMPEUVKibSVoDeNLWY7FITVh3cedER0dCyGD4CgQso3HvuNCoR0CR3YNq9k18%2BF4cBB6UVJh4QLNlei2yWokMrpoYnJHM2T9eAOxC55bn2MRhciBnAJPNy89%2FhcoYQ%2F2ctzJW%2FiCeV%2BXIP0l%2Bl6J23OQ1z9fzSQKGuPNWRUpoULsQvbadb1%2BPJ4eSn6q8IGVsWRu7XOXshvW1RHACqAI0pWEBuSPltVlPv2CC1nUpz0tAV1DP%2FANHKlnWkxDoIVFzCRoegGSkO1xKUAtoubY3DlUiEERp4U0KhLbWhKwH4rWKw3nZgBCtPz5ebbtJadit6ACdC43gYB9tUrBgJmMX9UWOuY6HuEv0S1%2FuPoF7buSqs2qKdKgKHFugb3Ll%2F3neh4Q0O4zylE95D%2ByFh39MF84hN4q1ILVHBRj5%2Fkwp1EcotFNcyEg0rnlZ%2FL6TQ9j3y%2Bdho9HjT0FObnZDpuiDsnxFL4S8TKDZ0uV%2FImaFTI79TjikXc63oDX2vgENTwK1rKFaikwklvtgPrTnm9XQIpKRm%2FC02YdPKw5xpOvYsDa1h1zj2hJysP9LmvrmD77wgj%2FprevqynuLp7tZRoHcBtSIbot1hgwAw4KGEyQY6pgHyJiKjH9u1JZ4RH8dJpSqKeqqY7JYz9qCSWf8S3KbVzDvsPtj5pyF%2B78AE5dbkW7QsewwcHOTdIsHnx4B%2F7aiEgQzskBCiewOdp%2Fke5jZvUYSmggyUNAWFmOAlJL3372N3g5RjsR%2FJ5v0WpPISw%2BE0EOjJ02cxz5Mf%2FakrXD7ZON2J68AQ75%2FnhQmP7uBivhq49Zw1j3tN1FaZr45rlz9uIAUdDMsH&X-Amz-Signature=7983a5d54f30c12b5f31cc9974a2c3f793e03e65fa4f29176e7b7c92e9302aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



