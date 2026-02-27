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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627JBBAUP%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T033134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIADmke%2FVPmmYD4PgHeOXtpW1NfYPrgyfEZh8La8apFEaAiBxFZwBgE2AejQunjOPLhkyG2E0A34hvUhRI1tapVVaQSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMRuh47G8szp57al5LKtwDrE3ZNqVXeOZsfPWskBjf%2FhcSwvrAWnqqhl57Z7zjP1GEKLK6hDcoBW5ffly%2B%2Bmi%2Ff6Xvmv6SY6yDsxOp%2BdbpdUHHWztqrtuqZCTee8BaaIzc4gRYAT6TYrzQs4fB4symNdCSf95AYHzLC0nybpYIY1ZuRrodgqsXVXkcItSLpMOqQA0tUBFItpA0HwHzCG8bJK9WDqbZQgcW2UEc3N7BwTa9rwYGi0aPE7vs7ZTtvA0Zyn%2BqKq4WC78oguB8hoNKdUybRT4G%2Fe7xskIo7kzob96zaTuzwvA0rCK5nCLfR0NtaJOYzePS0bdxg05tMCUVk0OkJmQBrPy%2BqYt2RY%2FQFv1mcZEdtmPOV3SXLXGNsZc7bVKsyGCL4zD0FvH6KZaK5LqgBw68zfF1lpKg3AnfVSyWFNas6vBohhldGJgmzntZWNm2beGWNCdlAc2L6PBFGJZ%2BajUaQ8%2BS0BoEqY3%2BsyUKoH6Lg0TwL0vEMMc1Oomz0KcY3BxxJPwHf%2FWnHWU3u3Op4yqe7qbPR5mdoelkAfTg94I4xDl7pUloNKRa32UfIKWVyqqK%2Fv4C3ufh2lxK5l%2BZufvBq9TtqMMQanXUCYxDqPh17zAmNwqlluBPSVST8LpaSDhYGhY5h24wroaEzQY6pgGBYd%2BTQVF7Ewk5G2C2g3u9C%2FkFYp0UJFMeinayaLeXJiPF4Gx89S4AXoU7NWNgxHWsSmRQpakmebKS5LILOCi2uMHujro9LHtosuesMPyKBS6DxxUKmFPRWNaWdDzTzBGRWL89zhejmBqt%2FNw1gq%2F%2B2HbUibPNE7P5P2jm%2B7JjHJe0Dp%2FWchCD8LEPBlDGidGqAtMLJWycNoQI7y5tsn5WRv%2BHeK91&X-Amz-Signature=8dcdbc9f316838d1547d1dd7405e1960391e37d8873eeaa19817afe6cbba916f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



