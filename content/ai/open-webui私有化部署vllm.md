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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULAAKFSJ%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCICh%2FsNv57ausfGJl%2FAAGeYSwQcdTwD7Kq2AKwtIZYNTNAiEA4XGOcBh31yJ06PrZBw3H%2FmsSnsMhgpvb%2Bne9wyKtsEYq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDFEQJGSCfKxv6Iz2aSrcA90dnoG1hmTRF%2BTownOSZTOZCL3FAM6flBs6Kpo7fAcPnP1Sjd8AS0GuYhXXBe8T6trZOCn2p%2FjQb6SyEFS1k6B5ABXckRF6V%2BkKSkD0iP1EB7IvKDDI0xUlleRgkpxP2evR4aVvDHNIi8URT59dv0TyeG3hAXt9%2F%2BX5Vx5uOzQHKTGFL%2FzosqdebiHFKDpDRNnL3HqbU49m%2BfF4dTFrGgOzRxz84qYOrOM9rrPT8coNFy1%2BsTlS9shD%2FfVdOVENCEhFtbROsjvd0pDF73ApTzg4MSIde5iW1oVWbtdKk53IO88UGIcuY%2FGqqoQHpM5Sj7KfyWNlwuCDxpFkehgD056ImxEWJ%2FLktIdFjKhjZMwvAAMU9kvuiKmRWdKLWrHc5IbOyThHO5EfEx1n0ndX9dJ9pBPDySE256%2FdaaxLvoO4yHckUwd3hODxyTw9LvSzoteGjd951pFSS0%2Bjd7cae%2BwVa8vWBn64Bkuz91GEzIwNezgnO%2BCAdWhHVRVMgtBeafOrHAQIOygYhTQqXbaTJMeTHaoxM8ZfNwNjfr84wstBFBChjuRtzzzEdPhZQiZNCO3ehlgEmDh4crPIhO%2FdBg4x4QLFnfC3vh1DIzYJ9sEhNg%2BtvRa1g1OoLZZXMJKw%2BMkGOqUBksJLrw1%2BjkFIS35%2FdHeWBPps51yeJe%2B7gEfUoYFCc5e7O4zu0jGNbwI6CNENz0fKdMGTHjFAf6uYBH%2BGJLi43k4wYsbKX4OB3uFE%2F5OE5zH3D4mvIonow%2FA2iqwVTntH7OrcSfFTbJafO7PiS0I2P19rryWuk9hwqCepmmzWAwzDsgtJNT%2FMKzmlkd7xRntRqOw6YLsHvATe%2B%2FHk7OzIaeJbWwnZ&X-Amz-Signature=a3c138737774454dd7bf0d975afe5eccc5f56e4d06da17a38273915b5f50dd2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



