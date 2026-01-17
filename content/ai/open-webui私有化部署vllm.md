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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG6FRIOY%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID4drfsY7ox1RB16FcVPn%2Fi7vcdJwUwNDnHGr1tsadF6AiAICyZrrEv6jr2f96AoQAenI9ZhnmolUGqQdS3C2QGaIir%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMgn3aJcCORPG0tTsBKtwD%2B1SfQxX0rCWUdgRIxsn0%2B3M8hjDihMbm9CgUH72uVq90req1NZzpr7GMh2Wtdg92DRumnEjccPXiWoA8DdQ9TQqWuBhmaa8TwvMBgZy0YgVFeG26cK%2Bz%2Fw896CIEdy950btFEmZ2arJJrz3NsjNV1Nk93naWa%2BwsRCd8%2B6eHCR4sFPonKFaMQyMCFvcbPW5NrW2X2wnykFRiNY8sOSIt151GZ8UfBVimjOaWCzGq3ZAVK5Asv%2FVCBeoRNsXmQyM36CFSzHdQssjZ2UhWFywI6GHPWS0HfIDeSazFGF291UfZuDUXoRTZjQ%2FhhcapEDZORPxTy8%2BjNsD5eaf55GDhce6gicMV9IChnhH8qdGX3M6AqBWYLMGLGDZ6v2cXiU2OiouZujEK8uUqER%2FxRaBfi1CyaZzL1PV%2FxeTt%2BlJTQz5T78j0DKsqyk4AAMq%2Bo472S7ugZWDlGRS8coFAc9blpBSuGxwdwPSL8ztU%2BdoJ3ttRvMQyDI2DOyCORMihiVr95SKpOGJ987XufbC34i0KCuU03MbL2rw7VqVsNwUs3ZLWNXjfSymUoFHhVMjXmidZWqq%2FDzQJdBgFYRdeO16UUDekZ7G9PJgScpsGAppABuduHYFMoXE8BJsMX6YwhNKrywY6pgHSNk7P8CnhWi4hHpVA2PQucmJRiq2Wl%2BlqE9stDmD5NZx%2B%2Br%2FpDnIau2StE87JqNRLj8hd1IVUhCnhu0O%2BoglR%2F1CVwSV6KG5cToswpQuV8JpaDczJ%2BkVvDLdfndvXqgITT7cqsap4vsV9r%2FMJ8hLRXx6uluegXzaqxApYn5HBxjgTBrfuiR7SxuDxLHxSppWrr0xEhYGNXnhpu3vIGM0s%2BxWbEg%2Bs&X-Amz-Signature=e90037311406597ac43fbc13bac0d4fb8b3297b9663be7535adcee92e40f579e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



