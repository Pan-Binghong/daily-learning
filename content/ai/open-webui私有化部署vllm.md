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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FLLVP6A%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJHMEUCIQCR%2BP4K0BnF30llyN6sEGUxEO7PXQksmGwC8EiIWZ0OAgIgFEuqkl325x21L6JgWEGXs7pfbd%2F%2FA4khT0Ff7LVAvpgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDI21g1vrjM2Kzel35ircAx%2FZPrKQVfKd10kg7qhrC7r3DeEuYR2MMSAaOnGdG2rMRPdaGXJEuZWQk9j%2BvQRfCRsnKwr3Eh7F0iVSzfOpAMvD9xOw5pDbEYrj6IH%2FLBPvUd8FM%2BazARZ23P1VdQxP7hODpk1xQ1y2DOCbDYO5fj9fcFcbm6VyoUjUQOEmKhNyt%2FpI7Ndgz9Ov5qRURt1gfo9RAxzRlnPkWv6c%2F8%2B0W8ps41CmO2GJkHi65bmLQPk6nAmGMpa5MrKzDbnjNmueGA55LXUQWMmNnB1F8%2FKWC2%2BCGRZoghTZL6WOYuWz0foepRdqPHnsAgkjmiWZ1IgGLV%2BATwqbyrN7cXZbqACA2xqo%2FaP%2BwqeGE8ji9NRxwLnzsB3ZhW9gQc69f7zkxZkbad5TiA9%2FO2Dpxrj93sS1NiqLqHxkZD1J7yj541p0xRBnEyedDMMSvn7LnpIrbqhmSMiS5AhDfUB4zfIqM%2FkCEj6Sx6%2FGMWkNT7KoYrrwtdlBnxRp%2BziQlDtiBfY1gYJEiVgxPExGmxfPrWcZWQzTytRepfDj13hP%2FDyIuleZDQ7KuZIP1rEyTGxydjyYnN5hLBlN20TGwJcXKpHdaFn7ZqWByG6Zddf9J9yCpgfngI%2FmDxf9xX7pMUsukUb6MKGP%2BM0GOqUBtSjjHPIOtzx5kPlKV%2FG13ogOjhFnBgx0hilYJPFNjJjHD2om5DeIs3m6uO74RvJlPaYa3pr9DyZ%2BCe0keQ2TTNJM%2BSUYDwyTHytagG4AtZdJM9Br%2FdlmskaaTRjlFnlht3BtnHLXKaFc6U77kFDL201ZfYLiTBg53a4AcXapi1IGVW4VW2R%2FEi8Vpi2NPo4PEq%2B6vWSM0Jvjt4F5qavSPsQcv5g4&X-Amz-Signature=2939b1883f1a68ac77d856df2cec679e672188edf47c61ba744484dce613488d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



