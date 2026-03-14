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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SN2Y4HP%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032848Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGZZjfVwrKaT0i%2FxfXjvermSnwAJP3MWDSSN0w74JnsdAiEAuOrVNQmJQ4BRSNuY45N9%2BCMHR1GAmPewt%2BTyP%2BsD%2F7UqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOaqBe3F9aR1wAdznSrcA9HrfwXJLMesidzVU1%2Bk1sfd4Nt5OGfYnEvLO97wn8Tiw%2FT0vP9HL8BIu30v%2B7rvrr6kphtCIzBJipYa2DKMFqbWUOcBl%2FoVSu36K6WJ6pVnjeQFZxKrm%2BU7bU04ad83x6CdU5M%2FkwJf%2BfRbPbogGJzv5qT7kfodFnTzpBWE2RjNEOfZZpva60ZbMUwtCIO1GLKVB57azrHhMJgIG88cqiRZsC5JHzBGHMovTU2avBh4G2BXCMOqJfD28pBdGQ5ypJTSUiH7G0YFflKzotKRGASs2aWQfU3LwaVBg7qRcu%2FbrvcZfmlQsE8GXp4LiIwE0A%2Fj03P3GTgrr0wXGXsiDxED%2F5QsEWuTxubD0Jikn3HBY0W3tkLO5wXQLZJ%2BYl7m%2BsRdXNh0qmtAXizgSSRpF93L5IDA%2F5jdeAvt%2BSF84O9ZvWpYiZeESZ%2BAgkCDLfKT0DwSriXVzwYWXU%2FqgpPRC09yovkDk%2FN4xNNejCYgnlkMpAWgbHAyMHNj1BRPznA2VEWypllW82Q1v0tG56djl48jz%2FGwVFihkbGlOe6bEmHJHxA5ZzcEgpqVWZI9nqR0bYsm65iicr0vIlPtSgq6VtDE2S7Vc727I3C3ko7sgcSEY8DNJxrTM4wOA%2BdAMKKC080GOqUB1sAsSy4dFCLgmRddNG6m6vQTG77li%2BUbgsMZoOzksZznZ1bguX5FBflEBzJJ9BB06M4E8sjQlA1%2FN0Km0rg0ONO2qlMhiEW2h7q7AMk0r8wA7wkxrMGQTkl4jMFbWa3C1wTyhQYBIWawK5ikpsMp9v86DQmGNVScVzb4GOQib51ypNnwB9gAKROQJWOgaAs8u8m3cHCsD1Hcc96WdUZqJjFIQvgj&X-Amz-Signature=5dce62b543178fa69db9bd2eb3b3f106a27c63f89620605a88a647c99ddf6917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



