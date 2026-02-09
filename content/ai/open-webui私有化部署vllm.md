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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTHYZALE%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtyImIxKc8ClpBPgES%2FV08VwsA81bAH%2FGZCrAi1PN52QIgY7q%2FACKjc8qQt8sr0A51Sb35yL%2Fx8rqg7ioizxbIN2AqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKj4nOuS%2Fd5gIyD2yircA5uNuTdZAUYPIoHdrNS7Qhw9QdBwZ4OaN7r4fZRS8VGs8TwTUM2Bi5D6hX4VFEUcbq7hqGtCOf4Xaw8NwgLAZ7JxIDQFrxAqFEOs7qFAhQmepM0qLNXOLKoLKhktH8UonKtCbHqP1XtZJn5lkjuKMmDQh8B%2F7anur9ysTqdPBgSHaPA4PShelM16x0BrBeo6%2BZOm3dhk5GZGRQYJbilLBaXwImgd9toAVDHXZhijkZAeMvMxSXJm%2FeB%2FME%2B7G0yH7wkLHD4dFSFcqiqijJHxZfTSdskUOslVWPZW6Nu8QJDSXoYJVq%2F8DXb5xy%2Byp%2FM8FD4WHXoPiPbwl6%2FigxJFEJvhwSbLQZPnZ6c%2FC7RCV460ORJqe1HnK4Rmae9FAnpuUmyfUkhRUm9kAHSX0jhOXfrcppFEy0FKATYIlIWRKRxuJIpCKJcbWXYHc2wUO2haGvrxLsXkBuXs2%2Flkpolqsyv0xa1%2BbGOrmxzExOrmyIS1hVPmrHbiUoRqoZK%2BSKinRTyCJnpGR9VdIzo2pZsAqeVxXTPFhrFhICecsXjkpb5ce8S%2BTr%2BY%2FIjh7My6hHpVGTdA43ay0%2FSDV9JANYVIJVyp8XrZpjOga0ciszkCIE5XKBOMqu3CGUlsqaKNMJ2XpcwGOqUB6N%2F7fhXRfAEGAzXRnficK4LV17WyhR7hwHh1IdyLRl6yHZvJEA%2FoB3B7abW66wX1MCE2hCFUROzR2ym%2BiJLOVjueHzR6hDfZKyYkLrkdmHWl5s%2B0uZCVMbQ6ugntTrJPZHN8dR6fIxEDhEX53%2Fv1N%2FNUqesOZOtV1o0V2M4c6KmCto%2BlHGVAm870aiEg4NHTPelbyy4J07HHw362eKf9qxJ%2BZgBQ&X-Amz-Signature=9bcc70358c7f89cb531108a601c10fb7771197bfedf6605526973074aaaa689d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



