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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666INWLY4O%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJIMEYCIQC1vcocymWIvZBzNDFO2fKCBas4SKpmHj%2FDAmNEsqEM2wIhAIs6r08deAeK9VlaDO3Vpd%2BY3PFyG%2BMB73r8afjKpkNOKv8DCBMQABoMNjM3NDIzMTgzODA1IgywcHMo8KJy5gkCzaAq3ANkmHe6vWk6DpwRYvBg5Ed6unueBmwfUWFZxAZdr5Z%2F67F90vEI0MO4h2fWrM0kKSV9Fg5VOQ6SpzD%2Fz7K0pbq%2BITLvBLF%2B38NwdHiIcZAJxvl8NQvCyC03%2F%2BtHo81x7uivp16JV3Ga8dx1ODUlDOEAokxkjCKd8m6SO32R29Z6brCYAlzr00yRuw0Suh4LdP5STerBohxAW1ULyyXFDs4YgGkyw3D2MCEWI6zVFsZ9fu4PiKIEzXOcgreK75T2nmshGCEIfzyGqOjFTKz4AvBnOWLXNMlShH1kgKA1sUeB6x8YgfYUJmn%2F2MZwY1FPlAbWVdQZ6aa0MUcQjkswDyw8H0p93QYUOGOLLzpOlXHtCsCfP%2FzUG%2FMb%2B2YIPiQMSNHXM2p5f7KynrcMu55cKcEIVyou6XDWV7H0FgI59ZwEP%2Fvs0j%2FJk2MAWJM5hTfrpr6hF58I5%2FzZRhnoTDMFYUl2N9Wy%2Fvt%2B%2FR342ptMbnEBD9KsQqw3%2Bh0%2F1nPb2721szkZa0eZBzZ1zZ0n%2BymZFl2RYE6rjng9qlG8oQab3f0N4DacLhNnGMoZshaLkfK8gmu2fW0pE5EClkoABerUnprJdvMOghyS7PUYnLWoSPq20zTONK6m70Dfzk5bgzC3jPPJBjqkAZr7i%2FAQPuucODxXdphd1jdn6KaPGENyCBcAp2l2ow9J7pbsuMfD%2Fn96cc3WPjmhdegXZnS9ewmYWq3HoAUxmipZi%2B8EDbeJ6aiQmmCvflYBDGZd7M9vb081hUbo5OISp6VtezZd3zWT1%2BIJrcoRI2OV3PnZTxBPw4IpwaBLXMaO4%2BfoSejwEtuyvZKcZqqQfIc9bikKAUvTWL63MrS1l8lSyup4&X-Amz-Signature=f14383ddfe4069f9cf5575bc54c9b2ae44e88a4901d120298f49c5399074ee95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



