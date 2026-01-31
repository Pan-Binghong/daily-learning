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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FTQFIIE%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BjuZ1Ufr6SVw8yoBspT7aJP7dFGf7XIlciququp7HsgIgCxjpXl2nzOfDo%2BGXCxzS44aQEbDrUkHhQqQL3d2RPucqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHOIoxVJ0QrcbsDT%2BCrcA%2Be0wJPBgpm%2FwZPLxE4CE0mfy%2BKnkoBj0LqiG8Y3xsjH4vgwy%2BoffTcdCIqI39HmB8omQURhrLd%2FUOKmDHy5Tr2GsJ6wWALLvaP9BjHEAr22MrPpayRog%2F7sd4U1APcfjAut8Nkjxgcj5n2%2FoRng4%2FBF0i%2FJuIKvOaA1aUYNbD9aG5myqjaGR7cygJxMGBHdXXDJ6zrVQHyEqtI%2BYjdUnFoS6we%2FOaxVPkrGZgx7YefwirRKaCt6oTXrEJ8cgI2NCbAjBi2Ta%2B0Gt2kyRLZF7gDz56av%2FFgPfDktrw1m69xubu%2Fs1Vvi5BtrNLEi6ldfrPic%2FALCSr8uZDj6hndcITmHFxiJbM%2FEHQzddGqKsaE6cFYGsoRjPn6DrRlqYnz8agN2lBDvHXOg%2FmhKUbPfW4iSsuzkqYwXZQzsdHADapDW6Ef4QhybqwNTaXUrP9LZd%2FMpDDbRpxdmqmuVBz3hncvAWqiNRJhDuCHrHAGkHXgCIOU4EbQe219Y2CvxCS%2F0YJ1R%2FNOgIUt1sYvlIbF99p7CZob6bXJ4BqA%2FCAcd7NVVxNwRG1wNUMra6Do1RJeJt1DAz6LazfY30oxDSsUIF2Gwn%2FtfclG5ahqYM0cBIXga3bFVgR7YvAVIt1SzMJDM9csGOqUBsajDIUeDOmYbO%2Fj29PVbe%2B8UTmKPo%2FzLb4Ep2eNVcZ5EZclri%2B19wW1%2BzJYQB%2FNHoxjvI8qryDo8ohkOrxpnJNDa%2BWx7Iu%2FZzqbM2fzao6jQUR8DP2fh3lrlaX%2B2LroBYkW6Ov%2B13QsXupzATngIGKBkJ6qvo8260rDiar4YgVJLvQUf8zlEQxnJy%2FWX7%2BZf0Fx%2BgyfIqmx6EnNytjETktX7ZVoj&X-Amz-Signature=9ff6c0f1e21a0168116644c9d1912c1806ff5aec2b16bb8f96c9f35c2cff0ce9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



