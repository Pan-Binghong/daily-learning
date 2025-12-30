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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4P4S4KO%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAPIuapT0NdedYvOFXBa979d2slBK4nLr9doGmvMn7MwAiEAyz8%2FySgy8WPg%2Fe9DcXb2DX9d%2BfhwYHn3klkUjW2NtjUqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRUivv648M%2Fxh2IVSrcA1HCc7DlOiuNQCmPqlZU%2FdnwQgF7AJYOt9j1c7febCyhAlgnITalFsPugmWJnKE2OoTDNP5nY2jx7i8rZ61waGhh55Zg6zLvzC5z1NKBkWNN2W0WtNPYyuIb4FXHzR7dZxnUevoxFGi1JTDUMovATMiHV%2FEbJPiXEd%2F19ooigXlOFLNXT8JB5Swf%2FMmIvqQKHeWiBJx4m9pGmJCJkMv3fMTPz3R1Yv8SoybZr0qC77Ag%2F1QFT0sZ6%2FYRWuheYSkoHLTrsFQDBiN6W7gWAeYEeZrrv%2Bmow7bsRvFDNZnJCIswwShcvKmrbZKZY8PrTO%2FgxU8DCf7StM0kqD5eM7rf3O1qrZdX2RWtBNauiz%2Brnnv7UM%2Bybg8nqN1M%2FO2Y73%2B2E%2BkwKt7wwAW1J10SbHySGe6oQU%2BiIDXszRxe5113MjvV266UqqH%2FEu%2BqK4qMdjdDXJoB31U4TQud50%2FMRDPdu7AAeAW63WaW6gZMNhUfV9yyW9ULTLwrEAoiPHGrjsLWLKNh8ulk7QKf2oxfiL1AewTtvx%2BEL5GUvj51PKuDH%2F7MwChUYEiaOSFsljyYG2ftpGlXEfITQYnl08c6hOTtaqai8Jyy01Jb7BUKspYxYhounPAnvk1DAoVlsa17MJTdzMoGOqUBAljEVm5TSkVMmpwEetwxAY2QKec0jqU05LurTKBZ7TIKSB2oUMHuoqlhWS5ZXGz7NNA41W7IaqZ%2FmwEjlL4z1TqtRKTSGhW5LfdlikpspFBTs0HypUNAdUoHoIJCWf64PJ42WDHN%2FdsHdozA6dP7fPSXePC82rJJWt6ODVsICaArY%2BJkkmvpwPSG2ArC4N%2FZbC6d1Z0OdOHK4mdPoIOJrOEAusoq&X-Amz-Signature=a3aa40998bb35e767a608ab77dfa469d677ab3b1e83c431942d8ab2ba1e01268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



