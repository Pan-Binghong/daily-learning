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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JTSCKDN%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQCpQKk1AIjXGJJW2gZcoRWqQqBtHbGf6wUe5H9VHFRGcwIhAKMyXyg7YJ2BUxMU8dJ2mNsUoUdS7wJn4t6X%2B29dLtvlKv8DCCwQABoMNjM3NDIzMTgzODA1IgxZsEEuXuygPNHTsg0q3APkBNKf6FPxCZZ9M0Lof8uYc6IQAZYZ2BytFWJNm3qEBVE1DHzMAcYY0eYfMjL%2FMmW1Ur%2BKQe4%2BIZEMLP1EESQ6h9lrSwsmUJ7X1cMu7Y%2B%2FyxtrwtPV%2BPjOhKSPt6iEwIaVDb00F%2FLKeaxhcscgFQhckoSnE0aSvJdjPzI6kp4R9YOm%2FglYuV%2BIaq86VO1RR4Sn7OXz9vfONSAneDaGMTPY2983X3wSjdY3tK1GjKFTFhnLe6GC56EPA8wHK8ESdkM%2BfQkxmGSFUYwr9IuJjCFO2L%2BIZBJN11A8aanZnHiIRZggmB2UezCs0CC%2BggPRVq3bi5fMADNkQA%2FRfJPKLXBuuuP9CbahGH5UrbXTxd%2B5%2BDZzc0xQyGtygAHP5Y7sSoJqf07i5STvsuiErDTQncwRpXfwqLZAPylCTNUXzGaxIf2Mz0FPdDynFq%2BplJmLpGUj5Y%2FmVpo1MM8u4a4CgbcneDbIHX8ajxTcX5YH%2BQVfoSSodycIsomZKmxENDkKuq%2FA7N%2BDFDJ7lvIrMRphHhRPHnclhHKtQB61UFlavx4J9MAUVxUKiTL9FtJkevpEYha4JjHIA5u8MfcyfPFCjycvgvdXK4a3UnH9%2FawYoN2ZB4FCeIOgOl%2Bg1gBQxTCk48%2FIBjqkAbmVGhpjKPEjYgRaDYRiFVeNkXuMWALtHHC9IoKhOqatsgAe0u4rs0FXjQwCByfaEhkVkmk7Y4%2BC%2BMz6ekh7tCiA7cRjjB6c%2FdevjzVpedzHH8L1oFQO8kNvYAKcM5ELdCWeIoJguDmvfkeppah7Fd0gtXweAKfuWLJwuZfpLpriPemmHvLfvtH3X%2BxpoLZWMWF5Moos08HCJDyH8Z0Jru5K2XZF&X-Amz-Signature=908bc4784806793016ebc0fefc30522fd61b5eba90192dffb441a887b421c093&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



