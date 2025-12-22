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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XW4EWLUC%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIAqR3EbEYW9Y8U%2BhJmb4vBZHio%2BGAljZ%2BxAsRwD%2FmFj0AiAgmsXYxqVWd9qqQTAi%2FM9p9qszAgjL1OeJoNe2HsZW8SqIBAjs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMgYu%2B6lA14pGfqrzXKtwDOhIai%2FvqXKX9yR9SeCOUqboo4nQIF64KzZUgIGgRK0dyrcXkKRos1McfWutXEgSJhh3ICZ2hvBVDpFgkxIz4G1h%2FG%2BSiib4JfuyhOpoJP%2Bs7X15SIO9eGdF7%2F%2BLIMPj7jnrhrFDinm2Eepwd%2BiIojT%2FJH3GJurbfTaG3KifXeqc%2BeoxWOvNqUbOdSN80JRyysw3SFat7bFuUx5eaWl39upCSAqY%2FIxqd%2FVGHc3gjXDXL5YlneTL1IhH8PxlGDw%2FHBpSP%2B%2FPPY7Gzv7XjDRzIE82XMx7pLGZifdCZXB0fIMDD%2FPew6wppQDe10TGuTwqzXzl6D3Mrt29L4c5RuD4ULPeCQQ3ccrwEKAssixiSLLb4lW7ryJ2yVQ7JC7xFJUeKxewvW2ubB3NfryE%2BSEQqg1vJS%2FTg6Ei1IDqMJKtvs%2FJID1Wxn3XJDKMoDwPzSx3HUKt4W5scU6%2B%2FKtYIXmkUJWRkPSgb1yxhKgzKuKN5yutYsKMqP8zg9Ww%2Fs0BW5FcPzV9Q3crUAjxVathja%2FiC8T1%2B0LZAgIT7nBkjtSxNqqh5%2BIKRLxcNKHR0FJLyyscIYwioK0jb1GyvMkHGf9TVr9uVkhJ5NMtgDCaNZe5RFUPXQt%2BttTXAg24YzfowouSiygY6pgFbrdJKm91wo8pR28KhW6AXykCbtcRC3hlcqs4i1aPbPlVxg4kb4Il0PD%2BW%2BJLoiaYHn%2FmzXk%2FMTDrO9KLI4md0US6gIbXd%2FHlLlpJzalub09YAhCwVbjuWozlr3EGfemZsMPVKbvK1%2F%2FtarjWbd19KlI%2FG8CZtDpVIG5ioyUuZMOdHZxIdf3fzidzs13%2B2PUm2y0A8vSFq487BpWK5gR%2FrmR29HM8h&X-Amz-Signature=78b2d0407073b7517d718b1936eb2159bd50d724f17a4fa53d1f04a7883d3d6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



