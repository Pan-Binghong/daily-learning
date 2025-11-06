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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCJBKCSC%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1EapifIz246aiGuSiWEPmgM1qW%2Bg3PaB60XfsAvwxtQIgZSGjM%2BTJyWqZ%2FmwXeLCZdq7fLoSX4KRIAaOcML1CQ0kqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLcl1N17pFmCF%2FVGcyrcAzAct8Rb4gFwlYud4uPt5sHxzyfd3Qq236M%2FI61KqDNcFYfgBXjpnAPH3URJ3bTuFVwiwNQULJz9E%2FQpXe9OUFsSOY1RG8Fg%2FRoiYD9H9y1AFTC4%2FG%2B7kcoo2mfWi3QU0ZQ%2Bi40raMSUk1ppsZQUTHD%2FsWZ%2FS9Ja4D%2Bq%2BG8y8NP62%2BwhuYSFy6mUpMEu5j1VL0g3Jxc4WBqMMuTGxNu%2BtwYTQMwkVlDS8h5YMo8qcnGjKemr9nOt5bMFM%2BnEJVBW8XwP8drEyY8qvdO42QurN7%2Biex0pAuMRCNALE4H63cI5F3z%2Fef%2BZh8CSe%2Bz52tdCkUybcY6Kt21%2BgrhdtPs0kP4N7VBq2O4pDgjOchdMhGZSHoNbOGj8ZOv0lmFA63NuabwuZTn%2Fdgms7ikoTN%2FZVIWWofj7L6ZbZ%2Bha%2BZv%2F8oQ7leORAJBJ4t3F3meClP40H5L8UO%2B2Xm2lgw8u0WGKxGefJX1wGzYKxKw1Tpqb2BoL0l%2FGKktRrg6Wasm9kxg89k%2BCP7smChtX0%2BnrfCtvFYoulM1d%2F6dvsIGvORQbx3ClTzUzr1NceDZUuKqDECN0EM4RoQcgtcN%2FQs8NDnr5Lsq3lbaBFnVJQLe6x82OJqRM80KxLDubshPav1K1MLDyr8gGOqUB5N9fX4cbjWP9mmBPr1hag%2F0kcVGmMHgm0DkW7SghZv3gD%2BRETjIlbDGD7oPvBBQPjHhNUhFk%2FamnzpOpzADXg6LpB%2B8si6NkUpBqmzZm3EwCgGZ5nfu%2BNnOyg3G%2Fo3NnE3zLrnIlmJsvs6WamAkOZukgt%2FFkzUbWvy2TRqLrI0GL5lreWSmlIm59dRp3elm2%2Bjfce7IQanU15uisEcrwoAqj8Q35&X-Amz-Signature=39b94370fd8ec5c3f2bc4d3e046aeb31b0975b8abcdfe6a519ea8a24b6bb1a5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



