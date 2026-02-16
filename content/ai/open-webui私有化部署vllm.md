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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YIMN6X2E%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCE3exVFD2XRVDBhiowbz9SUsC01EM%2FQm5wXw15sfqDAgIgCJwGBgrJFf9i29sPxD0TSlWp7tZLZc%2F4%2BEgToJ%2FpgR0q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDPFSvovjJXlSrx4ynircAz3VpxPaWHQayhNJ2WuYiClaDHquqj9SsZGZUoxFlVmzLDwK5UheSrRKsDTZGspgDLABBcFo9JbbcKtLDge2SoZoVpDAK7hP26AevUAIpTP93BgFB1ID6h%2BaWknHPNrCIgR3UefSWiuqvtThC%2BRaTJd%2FeBAdYN9YA7QCLYgtG%2BQYjTAyZ%2BsaPfBS5J2dnr3Pxb9lAkZee2gmElNkaq6Y5lr7M1WmnT4R4LPXLCA7we8ogyYoyddt7sZvthSfjuNtc%2F8UjaVgkmOH7j%2F7yObiKiBs%2FnZdgj9s5OYKsr0zB5NvGFVjynLuljbZSSazHVe3Az4%2FYN%2BFkx3RRlte%2FnZI8CJG8dSwhXBIr42EyeSp4V79FsBP5AuEZPdkPpmFCXItCoCyhv8GlstoozrAsO2DGtAEx7T9lQZZ4YjxD%2F3SdNfOx0%2FYe8jsqmRcOQJ8oPwYkOyPp9dqnbq3dBRwFA%2BbsX9%2FigiKrOIn0i%2BtEJIk7XnQIFz6uOASKTwaJ%2F3%2BXvWwgBFasGcT7OHv4PtvriAaQ8kD5OqdGs6Fd7VYeufzNid%2BlR5sIuyGAdp5n9EJS4UbzKKStsC%2BO7Px8qhtpUo6ldYfUqOOM9lSdL80pr05qFyxc%2BbuFdSb9BejKNujMO6UyswGOqUBl9zTdlS1UKxE%2F0QnOx%2Fb2ggGfZh7%2BhmlOZ3%2FZM0ygkWBCDjuZ%2FRUXqCFFEScP%2FTqUgUZMuEUv8c0X4%2FUEOpBSMWWX44poQNXA3W9mUVBAcc9S8b5pAKlARqTpi51M%2FaPxkJW0NBc8zAzCg6YxRsM6A3e6pXwjhcuw7WcoUUXS0Bi8zRJx7oYrQjMWBZBa7Bpi0byTg1Kl4u9kMM5CDiah0XMo01R&X-Amz-Signature=170c4dc2867937e410ee274f0bf1e865cf77dc47f015d4e6aebda92ade408bb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



