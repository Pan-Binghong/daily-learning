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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672TG3WA7%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIAuwL68n5ETmL%2FKroGWsQhyV3nhrGiptcc6r%2FzxSiZLFAiBY4keN9B7%2F%2FQyJoxLWFcX84SAM2gC%2F5iFfUUjLFTfwxCr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIMOtvl8gZtzjmvpaq%2BKtwDfQ%2FfOEhpWIOErl2xuqbUqpEjzYpOMtC6Gfw%2F6Yx6XHrjt9ofGzNLQ8G0VM2JY1mu3HykU2GSMm9Ol4K7nXQXHGnpLUpKFvtU46pTnbrQIEVEA5kuV3t5e8XlfOCq2sZowA8tXRJDI2cRejBBKbJfh2AuhI35Ecnxf%2Fl6tHxHfVQLQp%2BjQaKAKF%2FlluCY0nPJRNSrXjnm%2BQ5EUla7E5ndH9aGfQPXFq4XCczszWnLeOoSQrvExj6zUuXF7VWzdFCL0qxzYfbV19XlHE%2BcTGgXlTz9qvsnVZE32iAmE5JyMt6%2BmR5UWMSJPgc%2BDt8M4qJaP0NwyNolwN6FHjKt%2Fc%2FftIBV1%2F8%2Ffz7ZvEJ%2FMoIUqqZvajicLDg4x4LYUqZm6l2uzq8mnW7HKUZ%2Frgf7MPraUNku%2BmG%2Bh9qyT0ZnawBkq%2BqDM1snlEZ%2BISkVz3ZLpPDRX4CI8iiQk%2FNqSPQurg34uJmDctGxHbEAFP%2BlJW7nR0JjcpNhi%2FNjPlD083zzGl5ac0MyC8CLrXONsOydiqFdHdHcnMi%2FGidftq8mjv7FwXqdEoVmnqvRivBYbgtw0YctX%2FV420jY1ywXkYFCzzLxVgHWebhZOycYDMLv7JASbwIEN0etnlU7MNI%2FkicwgaCyygY6pgHdU4VvOQEd0ad1Yh7DpwEOnIdasRlQTTHJxaiFUIAJJvCGJ1VkM9%2BfUDQ7f2aYHx4s3mJDK7h4QmZZjTKZbbVrf%2FWMR8oV%2B9BtsKD34GD0dENR5wLTIJ9SDdgWZebBo7SsnaD0gkBnqbg3s5T9xQ0UsbCX8rwgLToqGY2Ih%2BLynZgeh6n1hH8F31sRhDsGjUI3OosUYTpHVaFqF7tstqHjCrFuuuZf&X-Amz-Signature=8ebdc0a19d66927799bed92b5a0ca290719109f96b2e79156d0fed8e879f79ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



