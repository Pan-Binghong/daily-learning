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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHMSV2SG%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIB7r3nXCsnyP1KBOoasdcbcwMbzWaGLEW6h7TcuHje6lAiBK21P4OxayZcWDrLRHG6AwNct9h8YqeBbC1ESxwmYu1Sr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMuJvKG3xYDTgF3TnJKtwDABSFO04%2F8phhiH7uEdgDL3tc10A60ZmX%2BFWEB80Nch%2BsJB08t7nIMAuSjDqxD0uok0heUpVBOONDmPGEUkbNPefsWyLdcXuqgrawYobXZHl1H41Xz5ExkOmsSSFpZEjjCBGTIE7BI%2BZ33ixr7LeRcVjpAfapcwItg32kmeeWBfzhYmn%2FmH1XZEUe%2FfUwFdRx%2B7RtYSHVnZ%2B2MNBBMHdNKSINQ4Y00TWxF%2Bjt%2Fin4oUAZsl5kZ5LZXz33TH8vK3prXaWoR78ATA0kuyzjWbGH8qUoofWqWSrKM9DowVScpnuVxDV14adQHkomFdIjjl0dhAYEiBASmyPXKaEGw5zX9tHecWW%2FFGI6ZIE19Lkf5aJV2lQjbHi8lJhtySDByk8XpGssC1v1Vt2RjtwzgqA8R1m1a33aW7X0YxzVHh1%2Bg1yOElnc0EAvkvN55tTs1x3RViij6mMd5IbdMFF0t5Z0Y%2BuwxkkUlL9OH3vuu9ncIbm1QQYNr5Yk0drzxX9kVkQAwXk2B3Lz7xre1qLf0boqfGU4K%2FLHm%2FoZCcopnUUYMbzHbXzw0W7Fal1%2BcgqQXtg%2BdYQaUG2OnHk6eK8qczzps1lMKCi3woQwdL5VZWsJez3aY%2Fq2iEkgnEN0T4UwjL%2FPzAY6pgF6GTmDJfB3s1SqN7JTtDHvq3MxuYU4xOpiGKP%2FfTABgdHbXi3qrZ2UMwZQC7dilDuTqYk5y27F%2B%2B%2FxdTlot2lrEFnWfLh2vzzBYgnk9sJjOeaj6A3k8fjoIEAdP%2Bhe2xQ19X6CPuzMcS9La3iLxJVqcBngXtDizOcdARtHJZPARqWELlVR6%2FJ3nhn3fhGnVY46PE5cYznhzJ0DtJW%2BxYyoT%2B20epEf&X-Amz-Signature=7713fda117d215356cce7a6e50ae141865f1980cd85a5e9bbd0f776233371b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



