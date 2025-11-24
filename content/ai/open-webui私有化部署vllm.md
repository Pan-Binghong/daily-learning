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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672MPBF5W%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025438Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEHAd6yVtsAQwqVW10er2%2B1oVkznl3hdw3RvuTr3nnNzAiEA0EDC8NZ20i4JiEEVL%2BMiJowBPhgDmsFlYL%2FzJ98NoUsq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDHNQdEEX7t9YwQC%2FFSrcA%2Bc3yYwe1zVo03MVnXg2eicEGbPk4LNXU2V0e9KztWvx81Qgjd9MMaX5Nis8cDTT6aDU0lYcLlQREj9MitvyNfALcczKax6k%2FTh4NHIhkTuSVPD67hIE0MCChlkXXIhjnElcUJxfEKre0gAqbq6yz%2FI1KwVeB2fSKtowe1nBsw0FPQOxYAMXrDLL6%2FBcy1dKdJWjkAl6Y5XJyqINszoga2AEgAY7zWdikZwIuRHv7OZ3f5NPJ%2F4jnx7hNIJcI7eKR1wjvQcNaydHTmDeKlch9V1R1bbknOPjKAOMbHo5WiFMGM9sUZ7jU7eHLNhqTjWHmMJkvs5uMvFoYGIgAvOxLpb7tf4%2FwZa%2FjaDGkNLp4lTVrqbKzYLvM8NzarLeafKN%2BykXu4kiszYHx5mCJBN4M9udktWP5rEqF2dCU9YQIUb%2F5jhOqv9VRZ5p%2F4dtCCYzSc8tIqbde9h2oQSouaENhdVL3kb7gBbKMGiSbJIIko9ODyAk2mI6dAO34YSA%2FH9FxlftnDi3yuzXGlqLKdyB%2Be%2BLKVl%2BTbdpahTiWXf7g2Sm1SFmRFx6SDRD1gzrR9ClH6WOAPWo6i9nYpF4oom%2FM7oPef1g3z73o8mxfT%2F0SnBpAHzGYQPRQeFPGnDKMIfcjskGOqUBDgiwUVO%2FinwkAPPXMhf%2Fh4bsv5kPwO2OigUsHVawL80NaasHtSSgUDSa5f62J6Bz9yR4l3%2FrE9xgEnvRL9RAESe1gHtRcYPi1ds9zeGoogL3WzfZ9UINa4%2FdTOcRU05AHIqn%2BaYkox8kKYqxvqljlaVQLStuQaommX6XQ%2BvLalu%2BSlnyJz0Vwvtx%2FIb6AEhmknmcZEIeitviijsgL27uoBRDBIuD&X-Amz-Signature=d5708114a0f3f9b15084446f9b40b9b28e49c42dbd6b3d7b97df14dfe4b600bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



