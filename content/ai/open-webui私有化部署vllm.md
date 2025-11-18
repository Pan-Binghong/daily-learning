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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q36QKIGQ%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDt3vpySLnR9w%2BISenTKHv2YMrL3o0f8H3swSRuXRXchgIhAILnLTnuIHAhgqCC2XOJFo1cpiZ8id88MQx%2FK%2FM2Je2gKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzlDlKHbiARGQ4%2F6E8q3AOlfG5AIbsTRz5GyIel6ImhVs4i7FS7LoEebR1c5%2BAc9zFT%2Fv8oFXwHsTtf2q%2B3Z4Y6R3fIP%2BOM4JTDIWvJ94RY94bOXvGM4f354M3yGOgs0irvflkpLfkjGy1%2B7aIQMccYL5yB5rTw%2BlUASVZph8p%2BreAR1zBw%2Ffs1sTkzlpBSm%2BUuU9u42hqrPEmWOVExjwPjez1JQZycOuymlTWfM7%2BAIU8tdAdPt0I2bPela0FPPXeUz%2FqnRZK5KCADqk6aHBHahR8zZayeEFoiiwkn5jAlHsOLf8HNSh3FnBt4rX17PRhpC%2B5qljSQ0PBnmoW0PZZ%2Fd8uoBVE%2FV%2BDSt5ZJ7jiclFe61hK9%2BBGb0%2BQbhEQMxk2aqokfWo58BcFGC4FcxDkuT5El9cU1rgHw7HGRKjQoNK0i4JwtFmN6O1LVW1JXNWYm5MZYt7nFQ1Fvaofltxq2hArMq4SSclkykUKWwCJpgY%2FZoLPQGViFhUeBWO8Fxg99fHG6RJtPlB%2BN%2Fc%2FRZ7lijjYWLWU65F%2FG2d7E33VOOcqiSpY9cvbLKGqXczSAMIDwpC7kF0Y35vsGfL6pEP1lrZ4m9KzxI%2Bl%2F5jnyC7EC8NElOI4VtyBsEkvzemx7W%2BlfM4uhtAaEn%2Fz8ITDNmO%2FIBjqkAVyGaWr7AJrTqD0tYWLM%2FgC6XO1ShTjUtvN5TZHdwmG1CTfq%2B%2FkQyfx5%2Fm5TC%2Fb5jKVfDhA%2FyCEPnESuCpEm1Atmk23U3HUY%2BOiyYjg6SFhSsWegxnutwRxcHI6QAkCzB0ty1lS0HUzMxdGNDVpi9c8KM3e463NoRyFamgeV7GDHkRr39MjuPUPRqC9bDkbYvI%2FS8tjcS5IYfcf8Nm0Q6bTGUBF9&X-Amz-Signature=a0634d4857706219cac6f839c1bfe5e302f3edda98d1a622d3bbb13f85f5cbf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



