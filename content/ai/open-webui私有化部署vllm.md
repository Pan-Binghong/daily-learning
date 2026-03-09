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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SX4JW5CM%2F20260309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260309T033558Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIGwEPukfJ%2F6im4a74YnuJKQDJj4U6PqRzp51S3agZzRxAiEA1IY1cE79tL0hgi%2FEkhtLAixs3xjtWCCXWrhNcDkKChkq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDIkAi1wSD9DxBSG4jCrcA2brXgybuFy2vse69qgEoaO6vSLXRZIPMD0J%2FGwQIeYn%2BV29opo3GGyRm%2FzN1vywbZWwSyRBfVC8aKh2%2F2sJKSrT5yAGMId637k%2FQsHhBDC%2FFE2nHkEHTveNFmC5PbZp1qQMEh3V59%2FR%2B3ARbuyejgfCE54KxTSD0gODU%2FQkrMMmRKGE%2F6wtFtG0Px7rusPnIyyQdwABme%2FTWtOCl7SWMVAUBqvro6xBhPg%2Bd6qnw6VrJBz%2FKWPkQnuVUr%2FB6GwftxrYL711CQ5N6Dv8B25ZYTnTdDysMxLV%2BnMoqrx6jCOislfcR5b9fXir70RKhXNiPZ3YO9Hb2I0kxIQFDq0YUG%2FItEPE5JJbe3bj6lTakgi5cOHVXS5Psb%2BdEuFvjTojothp7QQp1pnjhMMu4BlDwzaZYfC%2FsmJcTJCKXwD%2BsW1DZTqRefXy%2FHw2rYAA%2B204ct9V74ewAjcq3W7isuUhhEwWWHgOhuVtlxYOr%2B4Taas9YKCsRW9Rk0%2BClWxfapQV0VqF1SoRS1GUZxK%2FjtbYmNJPw6f895KDidp1w6lCYN7b6BCEovqfYTq8zAkKHcsuyK8I8Q4QQMNv779H3Ajp0F0LcvuXMcvkJHNl%2BufHiB62bCJNk2ygFEW8dUPhMNr9uM0GOqUBCyLa7R7R4NvwzGzN0nN2ozLt5AWXk1uUNVkWcTqDjXCrE%2BILtzUwL%2BT0NYgSrECrHjBDDwcM6t0Tmpyp11Rjmct1SDAV4miEtnaF6a1%2BX6FR3rnuf2ZK9ogvMmAkEltF9y7WyiTZHU8oNXAvkPXmtbtgwKCHWnSmhhN0JU5d%2F5LElCEuJEdEXuoo3x4zUualzFH4Qgs8Ge11MhG7gOJz9G8ankFu&X-Amz-Signature=43ccbafd625eb7e5c165fd73bcee8ccafba70089fc20aa2cf3886bec209a175a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



