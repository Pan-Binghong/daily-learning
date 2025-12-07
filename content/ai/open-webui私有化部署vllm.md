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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL5O4KH6%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025811Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDA9Av51Fif9%2F6Flyr2vmCGBEIZDvLJth90Dns7KDo7RgIhAKdareKwiKdAk6IJEUfYEwAnx2r3DUur6kK40cw%2B21GXKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzrbRFeLOq%2Fq3VIWu0q3AP2Lbo1Ai%2BUzGRvS2Ac5ShlWtXTeBmXynVUkdlk7HABLPR4RtFYoZfV1iFSCoOU4W2hRxt4I1tZK1UIRPvPFjKH8lO8IDPMdl8HkZ6TbUnVa%2BcKgGAitZymfINyNxCbnQJ%2BcYM13nv%2BBR0LgKn8Jc%2BJTEbyGnDxYovRijWfWDfrQ9Wq8lHFIFBaT25c4dIUjXIUO0LHmIxDoPkurm5UkbebcQfKJQlUfwVE4nnlrjItKhYln10LGynIDXKwdRhysEOS0Hlm8vFpJM5tV3jix4o0fxwIWoAcYP9owd%2BjnVKhh5jRzxye1l2ovvQF9636mBqecenvq3CWf6sjQu0uPzGkArs7Q6ta0S4GM%2F35EGLqUDhMpqopaiRNH42tl4%2BYMTehHksBgjqXlSvSFwhiDEQPaM91PK5MNR6pRxd0XQlS3KBoGgOq5Yoe6jZKBc9uTQnUXJ27lPHm2q5R0dudEUYcOebtSCovGezs7PoWsTiOMbrSGza8sffguoxvqCCQdaRqRFiUNCVl%2FZxZMUTmluojEBCEjoDzZZWr48MlJhoGDLIYAWBZbQPMWOQ7gCkm5U6fp1k85fMyts4GYM8GgpF4y6hMOFISsu270PTNZqEqOzwlOy2Xup%2FnaFS4wjCu%2FtLJBjqkAZ1M5sSKlmVz39%2FJPUM905hmHk5%2F5MR6KcHU9bNxbabEGuMdKEHUFHya%2FR1KzBVWwf2elmcFtohSN5J3JYQP92h9jtYdVD8O6nepeF8oGVXJ4OjubIiQIxZhnDZfLWiEiX7AG4HmoRU6NnZsgIFKZHHE4av5YRumS0vd3WSj3PTgl4%2Be0C2qir1IGb8sl8NeHyLqicUztSnaJzmv98EDaPo%2FjSwK&X-Amz-Signature=94ca5398a83b85e1893722cde92e812ce02b0bdcacced0ced47cef9fb3c3ccc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



