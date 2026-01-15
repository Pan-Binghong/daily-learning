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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNJUSGYL%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQD%2Fm%2BiyqXLND0CZ%2BC5ajsqmTaguGM3aK84jd21m4fQtggIgUdx2gJhND2ZLLlhghWzQNSa9YL4ollWsZ0TDG49BXogq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDIWcKj8Nt6f0MCTiwSrcAwE2rJM2FhWfvWY2bBnky2zzhnDR1QN2l%2BIEhPsR2LCEecRfjMYZjsCR%2FONqqveg6sWvSyMQlfPENX8fafsAct2NXmtVSSOqlfMhYL4VEXaUm9XRDU0G%2B%2BpsFc9%2FZvmHQv1Gg4EUck9poK778RSu0O4wL52BZIXE5y9Cek8KhQ6xZ6NbdlsnfESfPR9%2FOQ%2Fj6LK2w%2FAYhUIX0oX7hv4vd6AoVuPaQYscql3jBpjKx1JSukFYI61Ihu%2BPxfdUeEYUtadvOY2kH2kz1vCwC6mza17ALfAqlTyIoWo%2FbjAZ274Q8PngT06k7eIyBw6Us5KsljqCKC%2B8JQN%2BwjWvhP4oiLlVSeO7dPyLD7DBPdmURDI2Nqaij2rM9E8KkWkZoohGUF4L9bl2PAla2qxdrUwiThtl0Nse5IciOoBG1Vq1rzDiQp4mCxSTH33ZCP5pP6N1DC3JDRFKbywwDmy8iN7N9MSLff%2BZl65vkkMcMIeFqmBz9n970yAtFqefNDMHBxZNKMs1qtz725FkSlL1kzI8IRtfIYsoqxH0IDGnnyMx9wisvx7Kup6v%2B%2B6fwkDKd3yjGZv8Vs3giVP7MpI%2FH3g8nlvCEWmvwHGgaIiP3RJ8UE4mxXWLblP7mTqIkmRsMPGaocsGOqUBiPnIJ8yo%2FBZGXCcuym5y1B2Bs6%2BxZCsESjg52mEDEPUePJjn8fgHI1JX2%2FJoJYCW7SCuJXXsn5gGCULElaNkT21RIKMok0ZEUhfLGaSMsUG2yn7PF7wPm6X%2Fe7TaKIoN8TWghmHaaF4n575eb4q4N6WB13sp%2BsciU67NpQy7I6b%2FddAR%2BNiL8jsZpgh8Zn%2Fzat1XP61sOpg%2FRwoLNC6vnebbQv3q&X-Amz-Signature=969f480ebe63bd841e70f8f5dd3f92d9824f7c66e005cfc7b8b37594f0752601&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



