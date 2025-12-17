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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTGHWSWR%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFakjcyr%2FRO9bzC5drlZla8AL54ianf77Xnq5CqZQWEtAiBjlXohP1ZgC0OxQ5DMG5HbGMHFH%2BEG55TLv3pwTA5zYir%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMOfZ1YEWK%2BMlgTLrLKtwDZtuvJ0vls%2Fu128z9vbnQVw0DoNX6RbLn9C4KmeFJ1DTXt1xIna0qcNJi6k95tD7JoVXM5ZiPPmrsh1nMx1Ugh2%2BlYjZwo4UA%2FarQNpqzjpXtJkWKEsxOdlaCCZl99EWLNYgU119mkscyTWcATmFxvmZBmGCheOrzfrTSmGI%2BuHy9vzCkHTszcxvo%2FhU%2FoVSOtDlaSlWEADvXVUdFNI0KhvLQuOKqwJlJ4BOSB6pZxoXacry85CTbyrls1oNP6%2BKZ6mIupnNxMyHlY6evyw3EE7ZITdUiTdKUvEIrSAUOq%2FVGi3BTG%2F98AOBjieFm6kwzH9AQvlcDsfnIpOv%2FZU4ySwV3XJ1wFD7POnIhErXi7oHtiR8f6MCNzrO4j8O8DZzbXqhDYja3AX4HeSHvT2%2BC9mhSR8tK008goauLNpNif4On7xt3GcfjCTqdm2HGhm4vMQ6gK%2BUelVAZT2dV87gnYyBmXnSzl8%2BtMJVcrUtiqzc%2FGsxsYn6sH2CEJRiwYunum2Q6aTc1FysH6xlLz%2B8U4bCj5NDFrXKlTP4khYPtQRIPaDGLV3U%2FQY77zI1yOA97B3ngwH6OotVRX9pYZBUtcns4rOTpSES3%2FHuEBiO3D5SPkf22JpXl94NR6QAw%2F7KIygY6pgEyqJizRr6TXKlSz%2Bp6cwxAIBlKg9uuXc3kecl7x%2BYbnpv%2FffkngF6493tzRrVfMEC6MM4b5nPjos%2Fm7Uj6qHt3E56jYa8k6i9E9bt9CLmVIJZnL7ayZba5uSNHt2vtI%2F0Q7fFXh6BuET2cEEB0tncM664W9jVg7oPTKkQNVsRl76iB4edLENClJYu%2FU5D4z8gcsJVqSe5ywBm89fY0rhyHtFvC8AGI&X-Amz-Signature=fc9d28c3bb62d90306bf3c4ce1abfcdaab08fec614ca9ecfdd9c9eed86739715&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



