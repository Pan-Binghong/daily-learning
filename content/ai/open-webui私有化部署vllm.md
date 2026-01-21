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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E54D3ZZ%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD95YttaJdipkZxm812%2FDGSd0dKARD9dYZfA3JvjNxARwIhAKpMGKzKKdPlJIhF0bAFetIVpy1V2q9O7xnMqOBUhakiKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzzRZUBaspnWsYOsiYq3AMV4ZyZNf0SAzHW9DfarOW2jrjAVuwqy6w%2FKJS51Wo7vpjp9UdtqXPOh9WPqg9ml%2B8aMDRdXfpjKu1oHOW%2BqkDUUX%2F8te2wfe1hEB0KiC%2BFXx2IXPkAELX3LhDFojBo3I%2BhyMCpx0M7qjXfozFhI16%2BF33tbIaWJg%2FXjUaI%2BFnwvANp%2FyHTbKEsD34OngMu5oKn2IdzYiyzrj0AhQ2wCMJ96RrrGZ5ng0ShUsEhZjny%2FY96Bqg763qnLE5kAkBUoCl46sxB6vnY6FJxIfAKrcEps8qKrfi0oXT%2F7stEnEtF9WMdxlduB3vRmF8CfVmbZIUksGLety2%2Fgkf5O8OXR3YSI8HA7YxbJJ9QHcF9dLaI7Mgq%2BUDvQKzV4omDymSo82llHSjsUTOxaaml860bZHIYQaDKTCiibZQ%2BvheKe%2BUTGwgQ9fsGOOjYnKKSh5RQ45jVNhnZjzVTDXNhrVbbFKIQ59X0EDV8j0QOaREHfRko%2Ft9KJ9HPnCUc9Rk3k5EsQgkD4C1nQ%2BJrdMlM8M94T5ZxN4snPCtsV%2FUnleTVHezmlCb16WV%2Bct6Pr7Z%2B%2FC7HEaeSbpyjBNiDnoRPYF74JGIX3fB2ApuJPegwlzZ6ZJZdLlfzXIE7Kj0AqBqy%2FzDl2cDLBjqkAW6UEDUrIx7mqdolqr6kft%2BZaAMsoGfq0PIyofSDTnMxYHEoxy%2FQj96Am1OTL%2FGqvq8MveZYxYDbBOVmGOW2xVKixksDzkpYZ%2Fa7TO4FPIguwCiTe5eA6fHXSuCA%2BpgY%2F57nOQBF9gxxHn0iZ7c1j8ZQPMFoceQgfnWvTwEAjNNSoQ1Mz5WH%2F7BuYxgR%2FR2CVR1ThI%2FB42SnIdp77gE%2FJ0mdplbV&X-Amz-Signature=a91b0487ce636c6379e79f615f44f74a7409d5471ac3c6e518d7e49afaca393c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



