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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYPYOXMY%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIDnKRFtZ6awc9W1anGHtl1Mq3A369xxMUu3SCa%2FfSz4TAiEAsKKWS8LGvgdjK%2BdPJundhTdzWcNrNBlRW5mEynDxsggq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDIcXEineH9Vi9A%2Bd4SrcA5%2BxfDFKSdCLKITuS%2F80jVKe97IbpAkAmpBlYRJpRRUNJ0Uf6erHpyxwdxpzTISUUI3NPh2LKs7SjBqfR1Yj2cKn7XY7xpEvjeLOuCdkC2VgmXXgvOKFWryvqDzp4bZPtj8%2BPVAY3YrxoowKPwfqXKQMPUEWt3M9iEmOlDJqYerpaiFJP8LQzPIo9GiQP8ewM5WTi6QXDHDnbrPwef7ovGrytdw5w%2FyVEDxra%2BNeAkGj2TuoSaiciIB%2FzWsGI1IXtdR8LdArwYyr6HJFxO5CqrswGvAKeI8iRAwv7ej7qPQTSai2sh1B5izwbODY02kmcMon4yQkpA5fyzs8KDzOlRYnor2jvkc73yyaJrvAHonvYHyIIADQLM1o%2BmLFOSLQQjSyMPK27w5Xo3VT4dBnKDqrhqxnLzuFbfdDZNiSwkMquzp3YXcaCIw%2FWlR923WuR%2BspAkttamXxr7qi9ZRS3%2BxmJK6IQD7zyUxbOcDGtfpdfZSTRlnGy6YQHbX2RF5pqC9J7QyPUFXvdgUsOgNCsMWW6WFK3fu4oeDLXX9FnsGzbbTkEGh%2BYrMgqAabjvCnKTCdhIAs4BZRhiW8PX7g%2FJS6mai60lt%2BnnhKf%2BKc%2B73vnSCmrLHpu1FmujJ7MLjCs80GOqUBN9OejWIT1%2BFD%2BO9aOaZ8YiXF2PuKcpA3RL5v%2FRkxyMS6%2BtrTeL7yZo0YZXYWuQftYipKW8fbNnajzYh0ZsYmMrf3NWiq6k%2FjS7UbH7OV3JgMR6Fmpn5koo2wRSNqiBTYgWu%2FwJNwH8bw37gfDAsrfQSeMOpzwLOBTlcjvr4dadzoTKiLcUjvv39jW2uxBkX9Fyk6sOrwrYzkQLlYpZReQPour%2Bxx&X-Amz-Signature=3917b51596d9977361808b4fb3506de9508e86b59e3961f97cebb1b9ba65ec2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



