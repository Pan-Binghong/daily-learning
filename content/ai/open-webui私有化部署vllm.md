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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQ323V33%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHf5TJzZtHzi8F12hMbjpQwWc9K8vLjJw%2F5CSBb6u5umAiEApbvvriFHXltaqaDLEvxNCBB3a%2F8ht6%2BnihQO0VqPqTsq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDAQV4fGq%2FALlnxVQNircA0e9ZwBRziyLs3omBR5mI4cLUS74MzrE8Z6GXkeIzhHzYEBHEDVp3jR1b6rkVg3H2Df1LARVAJ4Zs8Gb3DLVQd3%2BN%2BPPrBMWc%2Bc8BMYgIn%2B4vBfD764%2FuMvUUOGVw%2FUho9mKa%2Bg%2BzcGQi6NscRHWkJroQyrnUCNgFrpG%2F%2FOFTdlKRuSav6T0PWEZrQZXs8mczhmyfdC9t%2BVG7MYGFNq2v1GLfFbbxdgK%2BcSKnNj5FQrJsN7RRp2lpO64brkb%2Bw%2BPwLiTXUeJ%2F6M7zUTYnr65ayD2dNxqKnnm%2FJeV7Oa8DrKOYmlC0XIrI4DJ1ClGS79cQ9fh6Gpspm6FfTKcPP6Ge%2FGjgApYf2htHOhpl0hgp%2BMLRhHfdRKfa6kJ1BrYkruGfmeJihzp07uqgvqQ1cfut8Kg3CuIvfDQLr1nYi4BUjB8xmkTo%2FDmfRzh%2BW8%2ByNxqm2mC3BVgHo9gt37tB8AW8QN73VrHHeJOTcG57E8SzoyBflNntdrpocAyoqKAZTpoHavtzUgHgBO5asdr7XHX1RMwyZ4Lp7AtQ9t78YbgmrdFfszLx4pcEGNqlKW%2FANQZ8EVxjEGztFl%2BPz%2FMNIwHIeRxbqqKsx9IdXKplZF0a%2FAEwPuR7uQtQraq%2BhQhMMSsvc4GOqUBaxvcwmqCrScICheNUopr7a9gwno2gIGHbwVfjqN3nKTANpn%2FXcxGIn0siuomFz5IqjhACPdsCBureQmHm4zjioLLwIyWoZmGyM5LMSWUJ%2FQJVOYnE2KyluWVTbR7KVO0KQ6Um5zhVPV23G75pOqPd1%2BXTZd2yj7IECfKpQwgevx4V%2FGDEBlnkGBpDnqJvv8%2BR5Gv%2F8y7kVsWtIS2bhedlOqzbj1V&X-Amz-Signature=63fc8a762508be2ae2217e3695a71121d3bdf763401954c3584caec7c772fc21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



