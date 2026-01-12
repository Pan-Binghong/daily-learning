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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNJB4DDH%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICK%2FumY4Ci7AsZQS73zt3yTefJwvaDjbGGKEttIclwjdAiBcUcXzrFhsKEkUHUGE4JCpoXoC9TXofDeYh1cXpMB%2FMCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMm1Gvne4HQboDgQl8KtwDc3du2sr1jXzUP4OfBuj9R2foxcoilgXoEpfHkUdKmBnAeWC9Kqh%2BItbitKi73CnIECFzcYreDg9mYf8vfXLqIS%2BAM%2Buvw4GDlZbLcr3HmEaV8Z6%2BBJ4ggKL6vRf1RRNK9%2B46E0TIqK08t7HHWLoOEyVPrZdO1O8oFOzE0MvfrYr%2FSAPH9nl7X2DQAOFjXz%2B1MGvKb4jXbVJEXdBUx0g7njRQ8g37Kg20jEd9fE6AZyMiZ310bzJFornuMDxrvg0Th9Z67jUDwbY310GpY1qeoobsS2ag97c%2FCmuJuzS0AagdWcAMxq0qNlp4%2B2rwCj8RStE90Z5odcr4MnXoNz0JZcwbWVHBhhep36O%2FnUZaVp1blW%2BCO3bTVFZsg%2BBvfUIjy24BU9iSQ2%2FvmYEujiW9Uz%2Bn4CfZKUUt45LT0jPnADXcvJo7ifmzymOf%2BaQKzW%2Bv%2B1XOPB0xwo4gvM1004yNF5o4ZNRPO2N3DLpdBcjkjOgRfeXpIe1PLROfx9QXXgDjIS4DdTWcVgF3%2FjTMbVsp7GDdcJhgKiCQuFynqRJpZIHsKyH5Q3wMphczZ0A0eI%2BGDKtu60GvoLs4TWm6QVKOtt5h9hfGwwRzOEflu8%2F347iS7%2BB3YAhbABNTGOUwx%2FeQywY6pgFCvQjX9xxbSP6BW%2BUQQtcsvPuwsKWyANUoYM7wn1579Uqckic5fr7l%2BqA2QsDskFU7buxlVwoVQoGWAAcpD3kiibl18AfN1DeKdKdQjpaC7ToDtL5tCTUpVJ5W2tYsk5RMmR2v9vY0wHlNwAYUOXCz9pMWGVI534CirEOtt7qRyQ3KzUQA45YuMqzvgq4SBE5Hr7I33RwJv1h1ZkKajcReQK3UdQA5&X-Amz-Signature=ca2c3ad06de0e0a2670c26fdbd047a09f6f8f496d0e80514b8fb842369738087&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



