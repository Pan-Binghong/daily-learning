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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGANAQER%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFWW24MDEKbYpDj4D70%2BS35wQ%2Fjm03X%2B0%2FFbmhVD2C1bAiADp4BpuBmcsrU6cuU0FDOHI5BNoh%2Fd3hLEI22lScUkYSr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMGqkoKxJ28q2cRKyYKtwDoVR7Z6neqXzvhi8hmfXqmMgf4oH7FOPCkDW%2F6wNHvSs8HMJtNYQPKWu2laFgRAIV4Fli6agSbLhlpz314hxgyPzX02n7jAWCuOsCLCwZPMyMQRheKJaWJ7AiSWaDmWmas0IGP5fT%2BENhgzoY%2BZ1yVCqstjgJ2YuK5M6r5Kmy6arREH7z6ibFdQcCuw0QmOuIgXc%2FlaOEuHeqUaRrwxXIUzfvByseEfrQFo6C7L0q2XJsu142XrlZz8UIu1hkbqrBjoRpTs2Ca9iVyip6IGM9%2BUHUEqj45314KEGz3HN8JrrdjD0%2BXAaHWL0CLFGpbTwetEeI%2BVOrHc5oIk9sExNB%2FjbCMH0Z1k4mYEtzbSdw1vhuICXdFJsWTwiobHlvOh4pFKvPHI2rnEbtPz7%2B4ee1K%2BX8cpnl626R2t5h1VB2hzkVGBw8GSbNc44YtMqVtkb8xU0Olp1UK%2FvNKBCqa1MhgcVRcnSR48Y4JE2bNUPJEzSW9DnpZ9F6uWCzpRiWPpXeUMPUzkGIBjJxY17pW3pJ8KX7CMRQVTJPvGYE8hdyNUv%2B0Hetbc32gBE8IhyWytp6IP3Wwdudfi3pfTVLkq3y5TROKSDP5LzO47e1uZ%2Fw5tfvqyfxa7ROkh5Vsaswtq7xzgY6pgG4INNbskuwtw63XmZX0uldO54GnkTA04kkvKQ%2FnCtPb7aa7MymEgp6I6hDU0eOAzbWtfB8EE1rxBh3HftxQfyiSBP04TwLKtyTY5rNP00WSKcj%2BeyxwVDgD4L2gX1klv51Kka%2FBcObuM%2FddUcXNK9dp5%2FVTq23WzCROhmVF9S%2FX4TBLVd9FAVNsykIB0%2FpGSU1Wkp4iJjZNDRi0fj5bQr74s7EXvMc&X-Amz-Signature=9a910cd71ee5ae0f7838c371d88d2a708f882ca9122aded73b732011b5843667&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



