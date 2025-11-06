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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UM6LF5Y%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSjGcpN3eq%2FsDbHDmyuG%2F%2BVxbhEUwWDOzhvTKZUEaLigIgNy23xhZfis2%2F4iKoB7MwSrZkzIy878J9hpyQBpdHuv0qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD%2B4GHLaUDKv781QHyrcA74fkQQyvK3cHEW%2FSQbnThDgkLJMH0EA0ngiS7xhSDDCMWNOXoc%2BBZHXV3e0Ho7MxR9Oluuc1zVv0iQKRZx0C8Unsq%2BSi%2FBWDXKUPhEZ78Ke5ixnLPx8nl%2FrqD2Lsy%2Fa9aZWnkiQQkkckolwqC7DJDER5XmKOGteF%2FcIqkgzSz40mPaZVULeWCbucNQQxA66PTpUqV4K%2FjbGYLGv%2FPNEU3M0loswgkiIun37rjLp%2FjAroOy3XQDNju%2BxNBA%2BU%2FChOTVozzN1Y5QRjSfV%2FGXRUk5wqk%2Fmfl0IkoNXMCYHifZwMSzE2McF7xla9AQSLZQVeiTwgVjDPNR9Q71wncPvIjK%2BJRfcbmZJpuk9nVuwaMvRDxqZTWlbx0Q3o%2Fe3Xwha5FVWUWp1syKUZpIYKZunHtrbMiIvYDkBlWMo1nhT4FVo%2BX3c1%2BCAE%2FNdhm5oIjr3c8ntb3xkIx33yErZ56NvMKtf9HiOsbFJfGEiAdJgV4A2yD1m4rk8zscHHBnKkTZ%2BuFG42GOnzEuU9fHLSdLjujpDWsgnHsQJCLvKw9eKgv3z2vdbbnR7xKWtn7f1fErg2NpRCAt147PVWNsZbLArRINGHI1ysjvzBQbNwr4LP%2FiKJ2S1FI%2BXL7PYK6ZeMI6VsMgGOqUBfEfQotQ2zKuo7MrM75RA4uRgIiJUa3uXkT%2FkFq7haXSoI5arAkdEhS8rfitn8HszncuKM27LtYD64HEX4qm5UtNKKLJypeid%2BPMt5lEX%2FkicrIKbeEhbnI0vCjlmB5OcSE70rRL2%2FRzHqRNp8wNQ01jQ1GnRV6OFRgu11%2Fa4jc3AbniRvHTQaLwB669h7k38faOI4VsTI0hkBOC%2FQ%2BcMv1AzrWAP&X-Amz-Signature=220da74e2f03383d5fa00cafb61d7dc18c96e887b72e255cc14a92ebd049a791&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



