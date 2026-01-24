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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHZQ464F%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCrNkHDtHKTF7K7ExRZiT4aBRVT%2FWsbbpiCySTFJbYupAIgX04R5zyw7dn6PkttAMSnut635aRIx56RQbNXzpzk4oAq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDKYng5Et4f%2B4EBTWgircAx2jfgcKHyd94NXNEx%2B80RTTZwVfDGcY1FEJN6UEuKC185%2BeRc9MDCRjHVKzoQFPi0zINDFv8o0o%2FMWVxgbpHMb%2FwVQfImwdO8NmUiuxh7OfV5YQ825kEeDW%2F9bryhHB1t%2Fdr7cz6v0vKmFFxl2TLEWhEG4Rf%2FpQOuFD%2F5Bqic9nMcslDPP7OuX0%2FJ%2F9aVal8y0P2Ra1n8UcqYqOHPh%2F7az4K9778s7eGfWBIygzz0WPCDH3vx7ZkapiTNen6E%2Fl7qUb7XfnBqz2PlSeneEs4WMNM4j8ibPMPLE6K86GQfTgz3bBD2K%2BqAj2FEw%2Bdz61e1ZROfTheflS2txPxC1QMCPB0RKZkcQhr1ySoel3W4nNmHM%2BQMJ3QL0wihUS24FtYLdz6efT02pqletS8xRrJwn2jiNyUFtq7POSRxjlDWOYz9fpENOJsdxJa%2FdXvdtP3m8nqidaKGK3dajkAK7odpZvJw0kfrHq7oL5SaN5ul%2Be9Tx3qYdXXB0A9TpvmYjsKoYieuWY6dEv03eXo1UW2IkN2nivT3OdPYEeO1v4ZUuWGTaRaRnLExqNH0Krf00xSLW%2FImGkZ2rPWueDpzuwd9cR6ZWF%2FprgLA96%2Fgiiu%2B5SNyY3lz%2F4Cf2stB%2FkMMbO0MsGOqUBfLrrhBMlsWx4TDNiiRwAqK1rzask9Yp8lXE9oVAhJJs6a5rI%2F7AajWwt5eL0vquOSQyov2h3U7dwOqhFa3v2f952pP3B4MpWscE%2F0gK28brYxjaf2uK45G9cdEVnguy1rK4YnU4jKuT32iLpsZCY3o40nDJvqzNDWnqeIK0Z7hpVzJQHDXtrAey9nKQ3B%2FLi%2B7q%2BLNEXK%2BMyEMjyhOXQca531gVX&X-Amz-Signature=e7fad69522e0eaa330890618ade39d715074111082e551e2c2ecb7fc33e7bb04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



