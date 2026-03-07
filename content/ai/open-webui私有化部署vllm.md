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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2UEPAVR%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIHUNs0Q9uVnLXAoRB00tTGtByHk4Mkirt%2BG6s8YxE8D5AiEAhOaT2SCpHCgYi11iueKB36vrc93o%2FqRJfmbLTULeJXkqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVEVtXxpjIxlGWgzyrcA2IRD%2BO9p8M6JAgox2ym%2FD87Gb1v3kEp8VvUH75VZ5eKfZKu6oQfL9d5oJswBee1SAEHJVJzObLGt%2Fr5aTZK2tcCnFNcPQ%2BJtHX4pT2L4akiReopuxia1iW7TSsO6m%2FQ%2BUomcMmEnaVmALid9Mr%2BHnmOuVB1euugkPwJMbhQWhOSRLXOdzLfGUWDophDwdpJWhIP8VbIKDpxPzccExH2Tmt6FnToc%2B7ciO%2BB3DWacTtqyiL70PTUj1SRbwukFRYo2xwFRcyJBqprDhZuDYSX8VqZVfEJ%2BFuqAM2eGtzuoKV%2BSSvBweAdLHvp7NRF8KMGc0jTCZF03VHzUgchrlQLFzSdpTIPEsGPpARgHOYJFGGRkl505y7B2WAEdpLZ5VRc%2FCdUI30gxKoebubc7br0Ogv9NZcRLIDmZ24V4Sw4PoGsh%2FbkyFrUlv4q0jGfUuvEdEamWRdGQKIEFJA28uH2ItOIyOGS5F9PDMthRdmMsOiViI%2B1%2B8yagGjC1AhwPryXUkljkopfQdki4bsa1AdlDkb40cJE7gGyYp0AShkMVyKsD7ngjoc0%2BOJogdhvJkLqnckhQBXxYC3jVBne28WMlQOZYfbemXpbBc%2FOmoC6Aa%2FMySqh%2FxZcF8bU2xv0MN2Trs0GOqUB%2FnSPEd6MU%2FFaezNzVa9H%2Bq4tdTrvEKMmkAu%2FUcelw3CeQFfRpBAy%2BKy4ybNMA1kp9yYcTy7g%2B3pSkpLvTqQgUiGtOcjzZh14xu5xeVjer27%2BsFN%2B9UTBO%2BKQnktxgMltUS3H7SlI5UjSakCpMC8braJqQAft6ebMY9x0VRVKurJsT1JyJFiCab3rsr3IPwheoHSEYSL2pwYN1gHJCSeHyPVU%2Fk4Z&X-Amz-Signature=539a6169b074ef3ce9e88c9047f85fc64328477c7b466db765aeb9972807b95a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



