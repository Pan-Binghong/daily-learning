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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZEH5VCU%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJIMEYCIQD56K%2FvjyAHtutwniAAe0bqjiqNrFPJRJspJH81aWIjgAIhALd9cciAHi9HVp%2B6645YhoC1zyHA6i85eutLjna0crVeKv8DCAQQABoMNjM3NDIzMTgzODA1IgynXNxKxRF69F1ju4Mq3AOHdS99YPvN5heq%2FB%2FsMGRKl1Vj0Y4mnq3wVEHI0fmCsqUZoe0T%2F9Kri6WlTEQ58dDoDiJ30wMrVutSWYWn%2Faj39UiwnhQmcLA6%2BsBc7oTIYNhIzoBQblmsfkRQNzecD4QH5jbA5iTiYi0%2F3GFOb4JQqlqykYR3XRFNAc%2FewNC2o%2BfPTA6WsWRgL0rgqHG7ZC8lA3lW%2FjRxK1tzC64GPTEIqRqh7Bb2SmI7ZcwVb94LQhsb4h10jhN6scM3UPW6pr%2BRX%2FpcmCLfnLPbwGIsfj63kT6lQUq6XuCUZBRP5cv%2BIQLSXlCugRmanlb9jEdh5MkurmfzVV7ue%2BShRwuUU8Pb4vnk7GvzNRAv%2Btxjd07qMSYhrXWRZYmhGRfBc6e7%2B%2FbVoiFXHlfofUu%2FMfWj2IEqXiLKuXRz8cBk7aduuaqHOmAiVvrR0hBMNrFicYVi%2FgdC0uk%2BzAUxBaee8tztK8rCaMsXy7esmVXbwCTpDtgsIpTBdLjUQeIDgMW6CJoKXONtHmb8VMyEY4PW4I123qw6mRmgTLJehU4gSWdchZa%2Fqdzw8HGeZAVLiobm3FKxMlVpfrAxQ67rh7ZfM1l9Vlin8gJhx%2F47PyOmEnqslWPD0hqNNjt%2FRF3NY19KajDLnv%2FIBjqkAc7vseUZUtgWXqKOmwlL%2BCRZ2uR0kyUkcjjCBesF%2F1x9LOwVXCwkHH%2FRhgLmsQeXYi8Fkp3hWu3bmUQho5heYA%2FD08CTR%2F8kyKR6mdCSjIaeqbtHSR%2B%2BmI3OIDDo2rignrcWrMFYS50MNDjZzbVMJE71HW3TFq4QKt65kEbs%2FBZUhzkmVZK4DGZbnyQIkZpTUmhIxUijQNKISLZiAK0y1GogGJEI&X-Amz-Signature=6fe70c835e830becc69f67c7ef50639cae5f1cc3dfba7f88829569ccf1175f5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



