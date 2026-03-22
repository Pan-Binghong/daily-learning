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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXO22FAL%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJBwECTy2pNeWJj5s%2BH2ZsezEB70HUcl7Xud0jt%2FbnJAIgHzy1iCD7904HP3jGMgCXrbuwJpshHZ%2F7LMLw4KYO6cUq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDJT4fdY96MXCPB04fCrcAwvurPJIoCuxW%2Bdsz%2Bv9a273zLUcaqgU3ez7qOtH5165d%2BK9E7696FxZf18xMJc5bbiISYbb7o%2FmBrZGiZGBbWFDkuJMCVGQnoIRgpPoBhkqjDFsS%2FHMKKXpaFUUziimlPcVTNgoh5N8uu0Dlugkl17UWMSOQdpXEDbeHwdu3dTLX38sYnQfdibU05sV3kFU6x%2FD9sTQSyl5alVxz2AdFnr8l5IdOmuwcXSDr9yH7J%2FE8rFuJ1L3YChXh9l2gGMZarZY06%2F8iKHRH5NIEmY1iGHTEm4Vi5dytbJe4URTnbbzB%2BLHVaMp7W685zx4Wt3o2GlkIV44B26VfCrtxfprxaqUXS1vuPd90Y0RvOdHRo%2FSwHGmrz3O00SfcpyPR9HsPmdq0Cxra2ZhnmhQq%2FNHMiPA1McWJa4NHfaOEpfknKcL2o%2B0Du9XD5q9eyCmLw3Y7keS4Ht5onhhjV%2Bu9MV1Vedy9%2BE%2FH1vjfXvbE0kz%2BLAny63K8IAlktI5iTT3fRmTkRPH2Q3oFQ42kYO8WOIE6C%2Bc1QGxKTLDJqHIkCdiDLM3FIIvyDvbmXbY7fpxD2ijcSedJ9d5XslLLgEmXdRrYTPNbwlt1H22fGE6UxB2F%2BsjfBnxAD7QnC24g1uAMLas%2Fc0GOqUBg25KV5ATRkMrMj9XcP1nm2wmSDGXELYR7IH8sbtNBbco4qWY8v5YZgpCNlIICsha%2B0jVXFTM51IdOoqbZ2PjCbpGw%2BaivlYwnKKR10%2FSfG0aUkRj7p6bvbPMlKDtsef4lPzTpjrpUl4B8ERBNUFA9QhATfmqDrDji9KYv3AJhAKbhYhHsEk4xGtmP2hB0KVUPMjzEIs6PgwT1cMox5tacZeg9PwX&X-Amz-Signature=ce0ad14286feedb02a1078c74bc1e091da10954b38721f748f4b459bec472483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



