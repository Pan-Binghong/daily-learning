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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIVYAI74%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIFU6i9%2BxKFdfzkg7Jw1B%2Ba7VlsnNR%2B4kfJWlqMHqvJpEAiEArt2jNtn195X9csV2rH22aDTgpvOC5PjaXVyWTQ4cQrcq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDAyFv4zUSTGMeJj%2ByCrcA5GnGWQtNle8CUUJF9CTiIYJ3CqBo%2FHYpUgM5qTdASQPTmVe%2B7SVfxWdi3%2FDeVrztgBFChokvM6kRVoBH719Ct1JGMqXyTID23PH9Jr4pXkn488lv%2F65EUmWL4RwVOsDjUU5EQN8XBvPl7mGjIk7nD0Q32fg2QLayDq9%2BcDD1fOU4mey3QLhAMEYCN8AiUveihRF%2FgGlnJk4N74%2Bundweei2l3pmC7ccJyV5fSqyI7rQhA%2BqVpDWldbSJHagoCd16yCZ9UvbunuNeeonDU6X7xxw0%2BxmuleeY3zgwPfN0eLZreS%2F4QuoZyu3Et3wNXrFzKb7WFprOB3Sc5FYwwzyVXm1Mn5a%2BzdgCLBEb5KpURp2NiXzUvEurFf7wz7hqnARO%2B1pfpJDkCVf1K4qJ5loyIREBT0qvZRnHY61oBNI9vrLYqVTtwhpyenU12E4DM1kKSp5zfhyiCVUe85sudhN2G6zecGQJZMPLgKtlXtBSrN1Jme8YaIM7Wt9tqOJj9EAR4LK7%2BcDkRk4Wn3OYs6QAtlUFOH2fxMm2abRbBpD4Gbkjtx3djoP6yfWEuZATivF1LzFcZfPqQNcEYc5DYsoLx1Xoj3sVkyDPjk%2F926gA5vc2efVX1sbVcH0R0UgMMb7p8oGOqUB4bfG%2FkQTQ4cQRLLD9cBuCJUhWDDTIoDnKalkyWRZPjSmdwvWa8BdUsqR6jeLDmqbSTyn8GfgIr8iJNmeUMqMQ91sK7POJitlFBejswaTdoK0JblibwziPHEbDy%2FE18GvfyMd52uzBrJzxBaBlwiompzYMzP%2FcGuyOEZf2iSWOQe8lqTa4SC0rMd%2BKwE92RWdRNp96eW1MMj%2BfuAXNLoHr7R44Cv6&X-Amz-Signature=64b2445f2cc0884f97c9435d7138573d00a281b5b9fb5825f5e1915b57ca2b9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



