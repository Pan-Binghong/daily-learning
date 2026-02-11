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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVDVQNTF%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T034922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOYdlpT3Rx68o7PhpPuCvuy8OKuYp%2FVtsATvkOgie2BwIgd7R%2Byr3gFMeQTrCn1kmSBMJSMYS0t5aTExCInySbcpoqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBL0c2Mx6waCodIrRircA0fhnoqmsnGy1yJadr%2BYjhFDOJ0QhE5KVIoiq8LC1gyPPrOFsoxdSk1Ll3v1S%2FaJGoDP8eVsEACGnZMeaCZ2HI8FcOfPDcqz5EeEJF0K8%2Byp0fRx7xk%2Fh2xxNcTuLy%2B2vNtr8TDOIJXXq01vNJVZyOSnLtUcjEPlRba0KTGAgEZ5D4iZJ2pV6bdzwTvP7URaEEdorKyzB9jSoOb7gDrpBNUh3ZNYfioDerqMEIrgQST8Nar3TefYCbG2J8BM3bMR%2BUgjF48sLwOESfxzZtBRYNMSg%2BdM2z64EnPyMJX6xHmpAdfRK066dMOToX430QqDS7G0WlIUBLdFF%2FZ4z%2BicAQamu14MGYL38sBmodYCRhtrhgl1eUOPxqN51FC42%2FjWrbP4FQS6KCuUxxwc1UQWiPJEBNf6XLUgUqtBly5YpPZoS%2Bkjdnh6yqzFs48xQ0Naar3KWcHGBpz94BtDSqyCyrFj2xpzWfPFbcu75PP1vY%2BYM0okjO7nNraw57dc6vbL9FCv68XaCXkrdoDz6BCAaK6dsR6WBQnT1GZKtrftgcGpXO4rmQVSBGG9DNdRtN7MXybTpiShdFT6yP6SJrBQdlDlFvOPOSe0xhVZZLWe%2F%2FvEggFez7x2Pfazjao%2FMKTLr8wGOqUBmBZeX8SvMHNJCizkjqOyfT8zCy8oqw5b18aXajaGPhFtcUiiQ0WkQIREtAv17uSGjoLrF3oJdiUR2jOLiY8SWwUrlSyKgXJGeX8HYOJPvhtbQchHUBNbyyiLgs%2Fd%2B7jwEC%2BvwRrtAaoxlmdCs8UeDBEeTl5vW%2BWcqKOeTCk1KlWjgJ46HYsYHQa%2F92L7urFajX6UdvcaZtO7mSZRGhkV%2B02wdHJt&X-Amz-Signature=89f7a33075abed2c0c1f1aae985875ebdb48b70a6bc17186d51fdcca7cfd58d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



