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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRXCE4M4%2F20260417%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260417T041345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCp%2BApH%2B142vRz741oV9Hsy9u6gLq19dSDhbXTtHqNY3QIhALPhsppLwyabidUowt1UVylDTL9yXTojwPLKovLpgasMKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzMTue7xhCtLjNmyEMq3AOzBaka1ey3d28bo1ugevafL3I8gYj4cz5EfI%2Fv17hqxvFDFbTRB%2FTw4xmsFTunh1hNtggj56c%2F0lA83kvXjALDoizaIwthVjUO%2FdUU46D68NMVrs3r6cwH%2F9OnFCuiZpnse%2BUMs2kmfxCc4H2ZGUbnSWxMLCtuv7HXw5y67d2rmgGJdIh%2FEEdMHuj5%2FWbkATFNw42JySmc3SRypZlspEH9dog5hp%2BimXV6kk6W%2FpaVYROgJrXilJZNCVEwtZdH7%2FduEVfRE38OgghwYcPS0r6Lv%2Bmu0Bqsnu%2FFNIszbLlaJDGZM1Q2vtr6qt5j%2FYmAGo1iRpeHId2f1XatW4mj5ykL0cXg94nYlT6JtFqB86e3jZGnZYd8L5eyD2JE1BxUTvBZEFROLnsJPvqcGZsOXuo0zNFtAnggdQ22mE58Sg47ubTq7YhLZs1GZTG0jFVFsbgpRGmiH6xAZ0%2BgwQ7nIRagCt6CzOhdIhXlaB1n0bQMjHM8D6TRrO%2Fs%2BVb9raUArHU%2FADbre%2B%2BmiHpQStkiNv41OxOppz%2BBlsXhJgq0oaRV0k%2BvwjTwYkw4A4Cu%2BDp8aTlAIvltZ3JQsu1fK1x27QfQ%2BdrwQOZ%2FlA87EtDEfXYMwSgKTpxpZjQ9nlx8pzDxvIbPBjqkAYxkBwyMNJNSv22gCMMW5rG6hd49sGt%2BxJEjnzzYtAo8rvCIp94f5To3lLzrx4IXsqMtbIbuFZE%2B3s8sxraCXsR1uchV7AZ96xBjerTZxDVJ0v4NgH3b8MnqMZhAk%2BH%2FTISpiS9gpXQn7Reva1AIvMo6lUcXDAObM9H%2BJNQfoznV%2FYyT3J2fmUiR%2FJoxiNByOwqG5BJLq37Rt09gy75QLCHpzIb2&X-Amz-Signature=594ac067aeb41bf3a1ca3d3d310605e146b613dc04ff36527ed72a57fd97cfde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



