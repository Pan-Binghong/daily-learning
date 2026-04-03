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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFGDVQKL%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071447Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCaaDdOwzxn0Faq3ThJ6OiwxHvRr1Zpk%2BDmfG56GfZ%2FngIhAKxwH0Ii%2Bl92CZzwF6TV9dlL%2FsZwTRGpx8kWeg6hVBW6Kv8DCH8QABoMNjM3NDIzMTgzODA1IgxeNsZq6lMcqGVlwPwq3AMuhuCAiiHA2xbchRaSgQ3B9V0kOZFGyTPxAKfaD2wvpLR2JdHpdnZW0l5kMGTACEGlBPZk%2FF4CR0d1CLgsv1rnbCbDBiWz0RZeyiTO2uy98nTFRaoPW8I5xEt2v1h6sqJMIWCk7eXVmjvlDJbCSvHI1CpvrKPsWxfc7bfbN4Rqdju33DobffEPM7MO4Dvdg4vpmfPKEqqb1nIXXFFh0fscYGoKrrFN%2FNqgdzL%2FSIocfmuv5BeE0NFCkCSP1JGVWQLcFwmqH1vX4FClyvYa4yjO3679JWDimXbRlN5R6Vh1fyz0yEZdkvCPdzFXrTS0C2KkKBsm80%2BJ7Nchue%2B9AWNue4bWG%2FSz5QgqdPlkcUn3cP7TFBEgsQgbsgFg1E7etX%2FMapS%2Fly%2FDNs51cUsSVuYTxkAxkDzd%2B%2FUFRu6sHEEQBypNvBopdEYUn0t%2FPtFoVfSdD7UKGyzaMgbTsyQxJ7UwSkfwV1n8Bc3KstWX9qGg9xKMW4gpm1M1neuP4p9KEmRxyD%2BV8zEXg1aNqraaS6swCjZV1x4VaBO3KhhFJYUeAQoR4sZvDWAPAGG%2BIq7v4zvX%2FoAKDja4RRvMuiKi8jbPI01raRF9ERMHZJ6yNcj2v1MKTxHeiWr0LSPXxzDGrr3OBjqkAftZUiG9WWRuyBkLTYS%2BgpXUwW0ZpnpiuLq8J9H8BdwRCwjCmv0zzTxaAJGrrzbti%2ByHpmQogxsLfdV4J4yy80KFOMPdzYLkqtrpjMTxH6Me0cytaIB0x%2F8%2For%2F1X6u6%2B%2Fk8rs8k4JpMV1B%2Fnt0tqJSYUuIc0Ssw060P6tSxcgz0Xf2Tm3U6u%2FZT%2F360Io8EsB3C4NMx0%2FgT815nfAUUAOu4KB1E&X-Amz-Signature=3d66ec369e7cc078a4603206f28dfd642a22afd9395ba5a3e09c3c5aa55fcec0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



