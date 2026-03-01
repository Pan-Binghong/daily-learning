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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLCCFHE6%2F20260301%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260301T034254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2BVwY9tdxgDtL0sWd14wt7vkVJYv6bUbjXuL%2FX%2FOoBpgIgLrnu6lC3Re9o2lyfIyYIE3gkzk7Wntck%2B%2BJ7z8DkwnYq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDE39BMglRRtYMq02OSrcA%2B%2FtCy2b0v9siUdvRCGVH1uQaVuNf9ubaalHTh31R3Lsgszu1zrLIjXHOVcrL9YNnio%2FDEPlaFNuE%2FqcyqvElbTLD9CJlBzzO678oE79hGSpnMEmK7qCq%2F4uG%2B9McYHF1x%2Ficau4XkiletG04NfXsTwjWv2tnUj1kM0ZRRS4hc7C6aF3Ut0xTAThhfjcmYO68FviR3qfsQQXqjFnD3%2Bfn7yGeXZLvzNKW5cJrW%2BwzBXd66KUm%2FYpg6qeqDciZVz5qOAxqL1y1PNSIRXUT2BXeWMjuMdCZyJybM5sGoTuZpOaN8KZns2aZCXj71kZOpueaKA6DmZpjQizqJvZrliERXZBWFv9QB9sl%2FJCauDa3C%2FpGurysiP0fazu9seFqaXngmP7M908JnI9TkAU30OFOoLO4swt8szdqDDxxWbdNeeGfGkRQof%2BJx%2FNowDdkEd2MA2j7duhEA59njXo%2Bw1eI317mFO4VrAxqCRzHrag5IpnE0jYAeg36YYt1f%2F%2FRC6yaLbpp7HGpIclcHilTCzu36i0%2F%2Bq2sJf5vftd%2Be4TKzMLoEPcq8dEi%2BfO2vASwnDMCH3Hk1LexrZJWSx105cB0lZdaN1F0NBZk%2FIACrBPIREkfIvZED1dKwqs3gh2MILNjs0GOqUBxK1z0UaITFAsh72596f02VOI83yrOzrRssIsbg40Xvqg4PEgL1Hh%2BuW6BjTsZ66O48vSn%2BVIEyb5Gc5WK6KVauocIaqZNwa1cpHn54tOX3oaE1l4Q4wtHJ7LnsNk%2FYHalc%2BgLBovQzcOGkQRb7Gsd2Nc3GuPyMVe2InXrKG88ZpwE1nbDU4%2F2fmG%2FEVtKayByBcVFbcGGhxPWZM%2BsauD2vK0iT5Y&X-Amz-Signature=8a89b8167464b39acaa534d59805050c29f2d1f48efc0b2ba00d6fc3d64d7a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



