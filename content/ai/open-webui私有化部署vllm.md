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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YT6LHT6J%2F20260424%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260424T041905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6KbFYlY85SonjcLx5HVFA2%2BmugFiEcoxOI1hW586GuwIhAINLaGqLnG9o8ouGCR2iyg5cTWz5h%2BgczI7WUk%2FNw4lgKv8DCHQQABoMNjM3NDIzMTgzODA1Igxc2n111jpJDyotlYoq3AN%2F%2FVixDa7%2F5tAg7JCtJOswWqROdJ%2FkLVrugDSYR4T3Nig8V6or%2FIw0nHoCElhkho32jEy4FSqicZs%2BE1NciEsCllvdUOJWkU9xqHNZ95BWnBVFFhwzhy0L7TH%2B54nZEu9Ok8UPHoQm%2BmViJkIEMbMbFGq8JF8if0zc%2FPdmk15Hxq0P40m4YoztPyF6kjwffQgGFZi9UyBKm4d0kLglfrty0klFHoQv3LqG1qJryXJb9yQnrlBl5cG80LpFxpWYkACP%2F2N6xY8QpXMsr5bWRu44l2LDSoGMO8SSDXDmAYt%2FyZs2yFvrow0Rdpq%2FeDLnp%2FQoSbqJu1TTsXZTwvI2yPBfrjPfFhlfTbxGuq%2Bl%2BiHPbPiigCjoX5cUGKWc1OWee5ymipWjuL5ErC8VA%2FBjquorBFH3nqWsbQ71xd%2FNUSKI%2BIWOeFBg3Mf8%2BHw1%2F2cQtxb0lN6vGe7UGIlnw9tl98bxUnC6yYaKv%2BVQLwCxv0mOHKi76nzxcJRwBuDEWSn9yUjzjYPGbFA7Abu9KueuGQwO1D7BCmkZdUuNhObanRLABOcXF%2BgAs5FCo7RPQuWS%2BYC8RgzZnYWtdCSSvfywkVkzq%2FKfNxPuEfuKdRdFmSNU1mcfc6t7nZ6cMPMiqTCdsqvPBjqkAfmORbvHinT4k2nuq7ajRTU7xXkmxcp6l3HRG4bhBYDvQ7RQ5cytyWLZqWD94GE2O9BpV9aIN0St93OlBs2oC4RG0uePZLVUEASgZBHg8Dkkd2G4Bfgo4TO3%2Bhe6NAwax6NoLZ1I6Ptks2h%2BSS4v%2FVsZ7mFiR2435SXJvwYdIWsog8sq%2FwDeA%2F6b9gRIqTyvvbJ%2Bte%2Fk4kZ52aMed4z%2BvIlL3q5o&X-Amz-Signature=ebb5cbf4250eb03c57a40b88726db211360fd1ed6e9bfe2989a2e8cc262aa04b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



