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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666J7KZWCJ%2F20260326%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260326T034943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAJvX0Bvgd6SqgHZGBF5ncV5nWj9aXGvfcOSPpR1N8RPAiA9M2RxS23UV74TYwL9taU%2BIQZ2QOb0Wf7qCLgVcZ7OlCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFTyJ64ON7CkyUJOoKtwD4GLdfoUuOA3OL3Hijdi6QrFHFmL3FuJHBt5AIk2vTZyzzSEFS8yNjZnzsfFscCVO8cwD0DyoKUuYFqJUrQREyOLjUjf7T%2F15n9yQm0XBtJugJOL9vLirm7LaQhLpvWKCfO43%2Fxh%2FDtfGgmz0qUNnpM2esybEuDC73X6%2Fcq2LIECEQtuQ9aJKnFrXmNgPyRHZcWJYjLY5IYCwIIDtYoFv43eMdzMd5I5u3ysA7F6uds%2FsF8JgvWzhm5o2xfsYWujV%2FOFe5teHEKsNMEjjP76zfNdWPOBnHS7JimVQmeibWUNZw9jOAZWxDdnwmSt2MgOhsLy0tN9VOE618VrDS7Vf%2F%2B8%2FHntAauGpA0KJFhOH4z31MB6c5ozK7HAOWyxQGTSUhG4C8jpfC%2BBm4Zdmn%2BnG%2FxyTFpsuKGlZpl%2BJBfels1Fh0K6wrqQlR9RrF4A4C4XNGpKopkNEsScBN6QuH4i5LTvebEo57iaFVstN2%2B81cmXhjNCBiBHgDZbd12w2xtrAQWHdnY00xNNdNv9w0WuQs3ocMgzJ6SjNh987ZB1krfktQwJrLqF%2BqT7ZQMIrAst6mIlip6GZeZBj9xY67oaVAY%2BH%2B8570HXWI4bqY7VtYv39K9Zl3yJfy%2FdnguQwusiSzgY6pgEtqpJi1MtPbKtEYlwR1ff%2FPpcmNSfeNHHNfU1bV6kl7yORQQoAmv2tlGGqHQCG%2FmXY%2BanXUxvdNmFgx8FJZx8x92BANylD%2FYUJjL%2F1O9lOOcyQEqHq25LDenY2%2BFCmsNLEPtJod1Xc5JFx4Eaa5ZwLf5jdhlGguSnpl%2BSm8m0j1QM7q2n08OVHmdVci2kSx1NG2TCEa85zMQXVAyNpEDts9JTPORS1&X-Amz-Signature=f6fb99e583ac94d64549d5e72fcca3676a7f2d6744b0144dfe81cddb8ab6e59a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



