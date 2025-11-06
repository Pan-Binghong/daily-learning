---
title: 基于LLaMA Factory训练+推理Qwen2.5-0.5B-Instruct
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- LLamaFactory
categories:
- AI
---

## LLaMA-Factory框架总述

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/3de256cf-4100-4fd2-96f2-cc014c18015e/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXXP4P36%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtTw%2BqnvyNExBnJGAkyqGiOtm30yhoSRKw5Xm7fCv9CgIhALo0h%2Fz9%2BiASsENmMqjyfVH7hgI0OMqXq7SwCl%2FF8%2Fh8KogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz0vORqkRo%2B3O%2FzzJQq3ANwI%2BwhZf3pNsM9W%2F4TTUGk1ow8CH12gcxc0XfkhjI2JploWwj2jxtZF9GXhnFU8YIgbHO%2FNVuOoxsdsLgMYOEs1I1MNB71Hi4jUvRh%2BGJNBJE1kSxKezw0sPDfiE4kQA2gAdldcf5jTiMdyjxPctLGckHaQ%2BiKYib2wv1pSHpyGd2XETB6JJDhkk8OfqmvyG7zdvQDg%2FsQTCPTgaMchvZO129kQu6bB64yEHhEctV881KvRi0iE9FXjOpJ8OpZdk%2Fhzzi96jfRNwv0huqbZnhgHZstyvGIB0hBB6IVPOqrCad58Lk4utAHBTOd0iYgxSTLQ5XjKVOUdXbwbSnlMs3zRX%2F2sNzY2xR18cnYzqTqYn2Q15VlpHl8qCOQlXAMpl%2F1eTrOt3wR5AHp9DvDYvyQ9lnhIWcYF%2Fb1UI2JmqIiTcHmc9yUMvJ%2BqVA5LWumorRklMJS6omjRE5rtZqdz4kiXHQwruOZ%2FduADqzMDlY7o6O9u%2F9m7NehrSqlvtoKJ%2BeWeryBeGRFMH2lC6nvdEsiH3Uq%2BuQxJ6DHQuBq%2FxrS9cRXkqcIqqqZeSw8A86gPkS70js9bm2n63B2OwNFpbbzfs%2F3Y%2B0cOEYgVW79JoNR6Xx124mttWT77DvfMzC68q%2FIBjqkAaR38Lv6le%2BoFpvnbwMxo6K2d3LGWGNvLZlLTgFY0F2od2W7apteMDLncp2YpDYfWGZBRYvEJIhATFTlsYOI4%2BsP%2BzjxnQtkevJggDEV0ubOjF%2FLI5GIt2Y9EExX9DrA4KETjSl7OIEDsAVypsTv2eEiX7ZaEl704V79SuLnNWih0XhZ%2FEv4oBtcoab9%2FvqEves9OGsl35JRhqWvRbgArLcNnh1w&X-Amz-Signature=f8099e9666f539d1e2faca9adf5a5ac9d5644ac4b93d15f961b68f0d183945ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前置条件: 环境，模型

- 模型路径 : /root/autodl-tmp/xinference/modelscope/hub/qwen/Qwen2___5-0___5B-Instruct
- 微调完成 : /root/saves/Qwen2-0.5B-Chat/lora/train_2024-10-10-19-48-53/checkpoint-62
- 融合完成 : /root/LLaMA-Factory/models/qwen2.5
## 数据

## 训练

## 推理

## Reference

> https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct

> https://llamafactory.readthedocs.io/zh-cn/latest/index.html

> https://inference.readthedocs.io/zh-cn/latest/



