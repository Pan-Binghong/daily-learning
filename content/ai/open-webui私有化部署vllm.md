---
title: Open WebUI私有化部署|vLLM
date: '2025-03-17T01:36:00.000Z'
lastmod: '2025-03-21T02:48:00.000Z'
draft: false
标签:
- LLMs
categories:
- AI
---

> 💡 在裸金属上对DeepSeek系列模型进行指标测试后，有点无聊。随便部署一个WebUI玩玩。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZEND6K2%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzBiB2cOTnWHDSTTLuQZ129jE8gbRqBcpaSyofkCHdawIhAIgMP%2Bq7ZGiU6whSobhxhaNZRrv7H6gknG%2Fo0QI8hF8GKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw98dT5fPmtUwBniRgq3AM94AcOxKbDAWNVU1a%2BmmE0cB%2FTPjk7uTJshmSozoXlNl462FDlnXyYg2BpBYihRwakgAtRME%2FDQNmcw5tb8Vgv%2Fs5WSEsv64PkFN8Jnsqa2dPHu1owd3vrAFOlknFlfO4KRPVxKwK7GckRliY0evBq%2BsiM%2F%2BHmzYK8CtBFpz%2Bl78OongnT1xGLf6qrRTiDcBFngOfWqXg5rOViWEoeiHSFlDeRiN6GPGmnkf%2BRRNcXe6ITDPOJoqc4gNlBCDtwyLkxvDZ1%2F3xUOxrGeiyj7FavwaGY%2BhUeQQkd0sh6O0GUrq7X0ch18Rzm7tzEJvwLlIAk94kEimYzuoeNuzoD1%2BZooUZcT41Wtb%2FtlyFTJdtRSmiFQix8AZbx0asW485vqv7nr7PoEplUPL07bCyIHHePC22Ufjinnx2oL%2FiXdrFq0EghyBZXVbmqRuzXYDK%2BlmyhIsRwM193gaaoLfpFXrcG6NLmg7TW%2FsWR7fCdpnNjOgI%2BrBKiWhvupVu6enADgcf%2B48Md6ZxzsQI%2BoARoIMNP3sEAug3Wir65i4ddHt5El6kMnSkWy%2BhC%2BLxebRUODhCsqdU0Tqkbil2KypJABclMKDmlpH4udpUe0GpA90ANXeQjJvrKUDI%2FEaYMhzDhoqzIBjqkARiAb0njUsiDFKec0Bahph39Oh4BQYtcgWAFGp40NRUaHNVTb6HUD5A8jMq5Jfojcz4F83xxdm6pJEg%2FENEwFmdXmRrhh5KmKTqOfTbfoC1eW67%2BzmvN0NL4n9tVPZ1ct64alylvFQRL%2FFHamKFm%2FS9N2mX6otTdvW1U6Zacz5q6ueXG%2FUdCMszvKy285175y3XdSUvyfuLxAgPxy%2B5MOT933XWM&X-Amz-Signature=85327fca36d0aa9e87ac674bec0193f99463ebcd4e7b46ab37b49be87fa3f930&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



