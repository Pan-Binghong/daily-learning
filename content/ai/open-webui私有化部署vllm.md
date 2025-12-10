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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663APQ3EII%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQDwN3hM7AD4fnQqy0drWLz2G4Z9r777IZVRdg9wsXkCqgIhAPn%2BOPD9ag9kqVWMZwMUciYVIt%2BMrXBlkgfHYGRN5UWJKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5UMiVfm8Y6oyBZcUq3AMBnMmkUOT7sJpRfI1jvPmH1xkv14Fm3E6%2Fp%2FFNvL4AZ9Kl9reNjhlojfG3wylhqCFelpfZ1QKjPwwBpyFVXAj%2BskfsWYM29q8P46pGHF17gDXY4K15zo2oajjLOZ24Yp6NvTFvQwHK5PRRqPTltwXPgNXyvEiDmivpfzoTIQd6LKCAocq2563PVFcRdsTKx6kGb96MNt%2Btdn3csPpdRsHlDY3LhaHfS%2F7P3x3q0ECycBrNMde2uWXpXToYVqnItXPZlxNSkMUoV1tkmhHo1SfagZgkg6GV9QF8w4VMGQJ3btg1jhl3iRYGuEa8QMnV8Tn3UK%2FRA4Aj063g%2B6lPX4pbORAWGCi5vGnMbxH4bVuZQ6dJi9z%2Fd5gdaDxl%2Byam%2FpsOTDT0Pr4ttL%2FsWu2unJddeC3DAPuBhriytBF5kyhPI3awlJWTaA3tW2Qq3t2%2FzLlB0dRaYsAbjaZ5regoWh3AEMtkWUaYAspUsfj4K%2BpjrXL3uyi40dgQr4t6r3FaKasl0QBvEBnC%2Fodw8ctZmOvNx4uKEVEYpbkn2oTpH7MGdtev9LaDNKssDWb%2FgZ4c6d%2F1zVF5531rTOevBevzSf0kkJl3zNLrd4BZTb02jl41JkDhk26uhb5soOLPiDCIkOPJBjqkAfsgCLz8HWJZiccH%2Fl41Ln74m1v6e7%2Bg6%2BBrqwZf3%2FrRcEMw0PlNuRqLSXpnKkl%2BoWWD3nfrNVigS8ZDp7pKmUWtw7SsDj7j%2F2Yokhq6wSXn2UdIMyb%2FgWaUnYCj5imlq%2FbL%2Ftnqqu36f09wBDlkfCicRa2auRNmyny92uHFnn10U0jNzqm%2BDwe4MJzd59hD8PchrlfYEHDa%2FuVHv0BH09hQGGcz&X-Amz-Signature=4190015ceec95a47234fb2b304ee9c15dcf73795462d51aca1346eadb99e26c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



