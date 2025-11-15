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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LZKNTAO%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023903Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFeqZzi%2FQez2hOAUTZ7HTVgEA%2BAdUPXrI032K6WtOFCpAiEAw23ea4aKwv%2BOjAheh6usEf0NWbpU7yyeG3dmDPgPQcgq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDG9uff2o1SmLlnj94SrcA1PpfI%2Bt6I6vkg7FO546srCeKgpSK%2B7miEyg8AJS%2FeqvYehW0tz5YoJRZZ1clSOh3GWXEv0aO9kIYslqFCppUpIQ38MklFZqOB9WsJ4eq4f%2BiUCrImH0L0Q4BHmLxqJS35ena9%2BX0nmvfCyjE65oYrnuG6iftbVjewHaJbA7%2B8kHLGOBXShPUhhkBt5PyryVJF2iCu0jOksy5nJT3sxByqZzU0QVIxyUOc5wpstlwI%2Bz5lzfEELnm0tceGcvz%2BUBD7xvPzd5iw6q6NZRI6gusmwvohgayi8UD5yHIsUTUMHEyohAIQ4m0ca%2BWshEv9YfSeiwrlIz2uxy4cX4G5N8LnH6pSjvjW6L1EiDjv13w8gUNtqyntdtvSkBlethw%2BmdDYRNw7jUm6yP16EdwgLclbniq0jLLknqBW9TEMa0s%2FeJEPqRDcDxmQgeX7ReyYwAfWHQVM%2FvP5276GR3tt5hSgENfCYJbIzy5sqz3mco9mTWHQT6DH4LqMO%2BIijUkJEuOHNsWqZcIYMnpq2aZCGUNKIuzCjFHxfCD2sx770FR%2FfVnghdw%2FVp6w4y3tVPgIR3QTTV%2BaFXFkUeZOt5AWUn0fCG8eIXn3uIQvftJDCQgpMM8AfgfE8y1UHYk0xHMJfA38gGOqUBftyYqAq7TO7LVloZNjBuRXIe3RVYGLQS97eft2aK0PbX0B5gnmu4H50RvvYqjERPCxFbFy1NiTxf%2FmYPpkgF7FbC7ICD0ZA0scGC0KwB%2FZ2jnzODPRaE1elK6o2wALU8AL9odkuUxWrRz3exzV4AJalEL2CixGChj75am4gmYW81kgJ6sWs5w97tvQ0l%2B%2FxsjlqsX87%2Fem2mgmhPPQvfuuYvqxTi&X-Amz-Signature=1f42fbd18349283dd221ebb02b03ab019650688a2b53c8853f951e2a15fce364&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



