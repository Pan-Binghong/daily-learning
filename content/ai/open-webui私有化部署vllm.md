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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OQB6VTL%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIAVL%2BPOtdYqRJpfWZtPaWprkfwsO7n%2B54hmeX6ZPNT2VAiBISYDf%2F%2F5d2Ih0at1Z%2FkcGBcEe9Yz9pggV1SnjVU749SqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMQFkuVYb8ABKVeYLnKtwDDMDOYVepjNk5tm0nV%2FgMlgsTpzHKhRXAt2Rrs4CXWHEVxJcGykQ23%2F9GTPw4Q9gbmYuPBThtQYy3LiHAC%2BLuAmV8JPrx0TwD%2Fk2PQ3%2FuALD364pENGUIvqe%2BbFIVP2vtXXPuIBLjf%2BhXt7p6pCczWD5F%2BLVM7l57lCHRSNEXoiuOs9%2BANiJWX0YaV5BSB4H6MBeuqDolylZmKDTl2QCTdT9rKzORXluvPoeclgzx6MxljtLjmLacFVrqZYLJvvyBGZIQkP8ZQ%2Fj2i3xR4KlfgUQf6tvn19VdR98d4U9WLUzkcdDAIpskS5RDypbw73sZpWp03otNoXN7Kq7SAnabm%2F5rBeYoc5o6rEbnAjLLeXHoZ9gK82%2FkhoqrpHiUwPLUpe6JFGdzYE4OdL9ShfHCq5RoSV28rgWdNkKYy6WWVukDXwfSP1%2Br2d5w4TVMXwOliILQNMzxQLUsabzWwBgk%2B05aBzvoy%2BszUhg7VHgWv7B9bBaoDw68Q1jBL6LCV3h7PgqzqGyu7QsN72wz3gVxcc7xtPFzHw%2FQLNtbBgwNLhSwEd%2BZsyJURx519NqmI658SA6RuUkW3BgEfocRbTV2fvudm4b0wZkThwR8er9ALB4yDmOoFTsUC6EC9%2Bswg%2FbRzgY6pgHBGetLqMreD51%2FEbNbrhz%2F1kikL5IXy0dwdXvWtzeEc43GyCAKDhs83ovpXcIal9d%2Be062IfeOWTnkqgA0XJFhHZ8iTskgCXKpELvwuYnsJHBC086GEcPfSchXTawQ9ApnFPGJRkQaAMFyqntsJEDILeGpe0LVcQr%2BIUbXERB2iY4fL%2BVrzJvjigS2pntliXn1%2F5Vrc5PRt7TEH6PT%2Bhv7TQOoNwFK&X-Amz-Signature=bac441ac258c6c9f38bf639ec6bd3a2840d6c67680f288cbbe8894a55d883172&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



