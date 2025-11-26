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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XGESXDN2%2F20251126%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251126T024644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE2uQrPHwgzyThRBy9cQGcWj8Q%2BwvgK2H9dGHH4hcmFMAiA1uLUoehxx0mADD8H6p3e9uxpux5O8QICd2LwODFPR6yr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMrV7pBBipRk38SLf9KtwD3ScUwT1pyttSt%2Fkp9Ht7G9LabzhBbpI07%2BTX%2BvgtFbuYInl%2BUq7mO37NDX%2BW349zJIRw%2BXyi05WB6jeX%2FUvq8S8yq9mQ%2FW4Lvl13ZpnvGC%2Bcvm0gUQ2MHncGG1CqmQJBFks4QPT364vNRlXxKF%2F%2Ba%2FMeuRJ%2BZURnbMTamJ9ZvUIwXKNeLNi8Uj8rzEotQe6Q4UnkfrG0IdFs9LuVsOSporS%2FRt%2BtIuq6TSh%2FYLqPBH5jkjgPMmH5k%2F0qtX6YRg%2FTlmia8HouLDn2GSYv0V2A%2BydHuMT7hQeNfry93qSE99X4vVhO62n%2BxKXFYaq5GFf%2FSxuIV1wrsZKWfJErwEUlGCWx1JYQzB%2Fu8Zdb%2B7fAQRWseZYmmz8brurimYQX54y9xHvNxYw3haAtAgRRXBFEbpbX7cBw%2B7KTKSrtQ83Iwhz2P9tFD0kQdjG6SngBHzbLfiH%2Bylu%2Ban0NPlQ0Z8QhKZGiua7hcDDXtzet2MWeT1KlVsS7v%2BXiEzwXLf00HjRO60T9zHTs4c0XpVJDarsh1G1uhw4%2Bx843TqqeXpaZ6gSXwgRpaldH5SuimIwK3Httk%2B5gjODvUvepLYGYyfutA0cZO8cqqX9Jvs5h9Gsjor%2F0hUMJLEgw3M41iwow0bCZyQY6pgEqow9yzuCwT0SDMQrmZi1iFR2seuKjLdS7bjr%2BA8CCkSYCMEg2mOZRsMwtFbE4ob%2FTkk8UJ8NiT1ERUlSpJ%2F2ytk2l5Rz91QnP2y6l9pVpSa3rNL8sYwbzetpXZVYlGZLccsVzazhii8NwHSUL6tMdBEAxRjmo8mmz12IuutsEV%2Fqq4hEU3Rs4BD2B0D2%2Bm0OK1ZLFEqp4XMtfGXj1jMe81BerXWFa&X-Amz-Signature=6749d9ed4e1c67a872920cb095b7128c7c8b29a7c52362ba65dedc5f74b49dcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



