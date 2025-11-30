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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466REGIYMPQ%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJGMEQCIBu8yLrG72u1xFnQT0IpGWLXpB0VJBPeFLg%2FShJNlullAiAn7nUSNz2YcO5TRH7SFD%2FttzWDouwaef3rk%2FYhVzMqUiqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1E0pi0N6cGGb8fWkKtwDSJyb%2FRkH0VPmBZf%2B7r%2BAbFcjggbSt59x%2FdeBlBM3mcB7PKe%2FMMOpV%2BYAP2Aey0%2BXpTvuyg%2FiUqpof6ca8cAOR1%2F7%2F6B7JLj0uhXdlcHhiF3UFvB3H2fPKMjmH8DYItTxcGx6XKzEug8kvZPIHES13p4IvUVb%2FSpJ349ECIW2CkmWtSCdvxDlyt7qyGYdCOzMM9a%2B9V%2FHMW0CrivCtT%2B7JBafcVKhYkPaF3wblmwjQPbHQvmYe%2ByeMpYR0F3bZOWyruMdjr6SMsK6i%2BvpnIiUfByDTwBn8a53n6S45V6XEhF95nJAr%2BCvPISGsv3e07NwWupHuGash6SIO%2B1ZKkAVTmYHABZHM%2F71GHdF9zRWbZRL2pwDkQsdkBOanYapIXhjDkwv1BzCL5GPbwGQN0oQIV3BcRnp%2B90L3U4drj75%2BHGPx5cF1CSOnt%2Bqf2LyfOUhWU%2F2Sqcgy2%2FxQN7fvD7CQrgetJWNvkwXzAttCloDEOkax9DnAXKL357n7HUgXQnGaKx0bdG1D8LjRObCQq%2FLwQJXqVIu0LUfxqOyfFTLOwTVQQgyPLwJG1rS2DzPeO8PqpJSIWSqilheC7j%2FrRnj6w4U41IzIn4uoDC6yEatXibVeZVSlTLGhpUuxk8whcqtyQY6pgENEdXHimC0cLoVmrr700LfBZ5MY4OlEdhHOMi0zNFW4Jo8CttthFx%2F4yxZg6KVLTnwoPLecH%2FXftQz0Kp5Csy%2BhRsCk9m6ZZARlEoJtnIBXsWy7S0k4e5kazXSI7BYFcfvdo7blwQh1zFVuTzmjmKHUG65NRq2lugHckB88Yoe8MTLw%2BNUdSOYAm8RJmzj1TOAjKqLQCb5tIsqRQa7XEptV4iVJGiI&X-Amz-Signature=60776bf7c38d00feac6e74fdf0634591e191b578eef03282c284924bfa6472fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



