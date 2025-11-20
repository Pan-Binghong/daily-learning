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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSOJD4OG%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIAC4wc7y5H3X08hHlqrw2D5V6Uup3HEGcuLqVMfvcv8jAiAQkwKLX36wex5ghBIaIq9wUJR4xrwvcyTfc7Om6FN48CqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMcysr%2FzEXPqbhwGHSKtwDIQqQGls2nuTGWV52cQx7RE0GfI%2BF2NGdFxLtAgoFvblfHxqjkV17OzbQ7rrZxVN5pC%2FJkcJCCNloDzt29VY8rE2t1xV2o4vI65hN2hh6TgWM29Ibjr%2BVosrcNjLBFbq%2Fx2HQssiV6v1Ec2WDIialbv%2BH%2F5Ej84FdJJxhny3GhqzOBRCnEQ6KCE0s%2ByZjXu0gn699v4BuXMoWatg%2BVU%2BTVYakWdsa%2BLew3KQxLyp0Dkftn%2BqMfiR6pPrO4RZLVAb9gJWi7Ue6m4X87xZCHlVnxftF5LfvITWhfUvIBn35vr2ANgR7HAI%2BZ1GC4JVR%2B2uxbK7xMiRQ%2Fh2SAOCppVIP9D2md48PU9n4USC2g%2FspXytxyM7UDo29t%2BjxoeZqXgeoIXz%2BB6d15g8uTYxMlVRlzm1wDpKI7uspycZG7jyRiZ9a12d%2Fn4%2FKt%2BZr2HiCDFvTw9pbjriKmvbP7bLWEfPZ%2BilW1sYHTUJUYmCXf3LQTXGPJhJ0Djf6Xr5Lpe%2BQuwsbg0P8bsLxo5fhDGN%2B%2BYin2L2yXbtI%2BQorjW4SIanQy%2BKAtpIvC3nFCQsxLu858y0xjuHL7YwoosBfj42s%2FgkvjkKLZyxtdYnCFAiGQctf%2F0Bbq49e%2BW%2BSVI1UdYcw6Or5yAY6pgFYRpe0S0pqUlaoHHsvtCRW0m417GAPVSkWwjWoAjqWC9JYI3%2FKUn%2FEOdq7sGPtW7Te7xnMzFmQxpIs%2Bd%2F735IhHwKUqCaCqQIQO%2BkfQ74LVxl8PCnPkVgkCloDq1AD%2FF9eu7CJdCwTodmRwAU2Ra2vyntJKi%2BC3hHUsVrFhs%2FPYcmNiYtHSG5dACvvQEpzP7BBWEY7ePJUJh9zlyCCNq%2B65vdyjOIX&X-Amz-Signature=27039203aed1d7f1635b5c4f5503d707bbd025ab947c2c6f8882df9e1359f677&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



