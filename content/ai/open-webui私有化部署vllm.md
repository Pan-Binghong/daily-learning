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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XWDJJ2E%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024655Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIA9ofYhrDZ%2FRfVmdKwT3jPNkL%2Bz2qgjMeP0%2BlV0pNEtOAiEAzcUWW4S%2BI%2BdRrmlPYzRnn%2FJj1JpOMgrCgWJ%2Bx5jbzUUq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDNaw4lHXZP5mZtsJ2CrcA%2Bed6%2FBGAlQW5661tPs%2FjqE2S5O3Asvnb2s5uZYUaXzU2%2F3eNYw%2BhFgbsFKtnafOBkVQrnn04uP7rROj7gl%2BPaIiHseCc4BozMK6c05alTM0klw0FwCkegULugw8Hm3vBmRPi8acPpmBRdw2uw6FBU7Rr8Sd1%2FdqZDqE37IOe54UArsCACmBxoyKvWQbbTrnlI%2FVaXMd3cCh8cGF1fXURbwmPEAkCjqE8B4fWm%2BlGSGzAJOauh%2BBmRLQoe%2FYchRzvThuLJvGY5WD5HlvRp7KopSIZfM2vq%2Bp9lKfmOxSud4R7E0YzcYjyiVYnFIZ13LXugGeURmK9FHuKr2CYpBPaLJ%2B3hAsU%2Bq48w24ev3VJP8XWArakprGfJhHPTAVMAJEYR00DLgnRlSgEECh4uZnpNXEGfil%2FSkWxlB5gkVGxwn2sez8zdu5tktk6rICnfe7SkoLoTzhVSXg32DvupfQEk6j0mcJRM2wCMhlGG8sx2dlQgvayoV9ekshM0eQVKw%2BQ23g5hBb3cViz5gYtO3zj0OjvUXvlzgKg%2FGln0Y9ELKWekbyn65TOGx9tpjt1u0bVIEHhl42vFatbNaZHeyTk2Jq%2BkGHpQmgJbxlV7ga38UmUPdx88iEzdKWYLI3MM%2Fw1MgGOqUBAUOGtppvVLuasdyHRSsv8iyC5OMIk8yf8TRGIZUlmInJTjg6p9CmxUT%2BahT4cn9IkgcM1Kg%2BA%2BAZISnCa0QlqvYzlo6vIHfkym4tDPqe0SBQneDTZF7NVRFEhGxeNEm5XigBKaCAJKzyXjZWti%2FkxDeGb%2FZQyhzgqe%2B0c9MbE6F5pqieb9AvHQkUkqqQ6RBDk9cM9gy1xUNAvtwLdz0jqegHtbwp&X-Amz-Signature=8953d185113f21dee0ef2e37cb6ae3300a53f4e5093594ced781b34d9d5e0027&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



