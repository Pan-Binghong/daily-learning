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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VUNMIAW%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033759Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGyebSeDwHXqP8d9qxphwjnQOimI99O3z2FRWGm5EMAkAiAPtp54gYai08e87Xk8IOYPDlI07yKZo1py932SVAaz4SqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPIwlBVhNibsOJYxyKtwD%2BH3o7eS8GPEXThne0zd203Y4ClKem1vmAAKeoMKoOSdkpe7snI2eGnxMqsWrObDzlxC1AcmGtaaZttW1p2jX9yhh2LRX9zZJsICDLGz6abkVvOzb1kZvgBUQ%2F9pJwUzsUSnQhKj5TudlIoabLRcXyj73ALK1QGyS2j%2F5QTbhvZ5wmmKwSJpZRKiyOOxYcg0q%2BeGQDO7BVecxALhtWtLd%2Fq%2BtnxXJqZN%2BcDD7a28XIT3BIXz1%2FQg462NJO7F9NLUNKvm%2BDWabOcH6E%2B9p1DGclfDD%2Bl4VVYgT00CddbsKkSYZAqU2uJya6JlDb%2FDVM%2FRN46GnkjOIm6gub0MStbeaAhdv6rOkm0Lk%2Bm8VcUAEsao%2FlMHYjl%2B1c4fpFCo7tRdSqT0ESVykw6oO18maQmOukv4F1m4YcA3e0GqB6aB90p%2B6Icy0x2DeJIP8%2FHMUa9%2FNbayQq%2FC1bEA0nK82BSl5RlUj0Hr9ZVvMdqoOWdKdzxfOs2s7iEECmdUmGYFnwhUNWmavbv21sbeTKCF%2BOeOGgddRnD5qAeOmExXcl0ZMMLlmVkYXuf35vVNzBVS0DKBWe9kmnu7U5NxFfiiumSN36uhRFkqw5Zedl8laHEpXs6jcAlSrY3plYKcy2fww3MzpzAY6pgHsX1O%2FSOCq%2BeVTwLBJ3Qvnn05vKdzNEy3k3b1iLw%2FoniBQ0HUn7i43gzGcm5tA4041WmKUEmJichzZY%2FHcLhscR9XD7mlYkYBt8YxOA7HBJLjja2tm0PF1FVS%2BTFho9VN%2B1rCHTcrsPQ98PC2fzpExGjlUM%2BVkygA%2FGbgN4ma%2FQ79Kdf0t7W1%2FJyZ9mAhRWHYNUJDIEf2mKPqcTUjpL8paz0HUziqu&X-Amz-Signature=e3012c8eca432dc2832776f4336837f78f1418b7103bfdf719c6c8546b4dda29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



