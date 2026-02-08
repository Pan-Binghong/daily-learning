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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QALAYDGC%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBSZwhtgzxwnu2Mqqls1e%2FdKZgmyDO1ycUE6VhDc5V9IAiBbrp471wX3Mtb29ddkxC2UHVESOH0Rl8d1BWJYKBushCr%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIM9c%2F6iodBepnLitHyKtwDI2nSFXkjLAknCBMMke%2BATLKFGyfobTU3U7vXPju1scuPP9n3GcKXnytGmzPIOoSzP1pFRjQR0x%2FuqUF1LMGwEexUo0t2ThTYn9TpMYQIha0rsDDbvMme9EWMSnG6jV8jDXTwXjuv4vvXSbPgwOzdE4I%2BaK9M6nxIk5kcw%2FkxEceGESXLXTOdwd6bPkWHpXWRxI8p8pLAcX1Z3iWP%2FCzt4yWOuQnA6un5s48Qk%2B1A8xSjEogGjmQ7%2FS3ks0197Yhmb%2FIXwS3R55WlyagxVEfpWf%2FoFvzGUBNhrC7xmeFA3YG2UFzN5Km4xkPfUo6qCcnXalI%2B2p1H6kIGGoDwsgqsIgeGcdgVYWuZXNQ6ARCjW%2Bx%2Fmd96HEDaBmoRdisPZbzEVGdonAh4BT58LtjhBr6BtIBr5KMTQ6bs%2BTJAOYDm7KmUsBVwi0JBAPGhcDuavsO%2BjtVkaR59AsqZZXC8miaKbpnHQLMEIRSoiVl5LCNKJBLQK3h4f2suiEoxmEGw2MqL4AX%2FE9xZmp9WsOnys%2BSUz8fcFjCScOLTVLlkMS0WyfvazDb2epOd32tbnv41o%2BbBKgLGOKfuZC1Ezt5ppGZClJGhd4%2B72%2FcNVBWZjPmpHEStn6Wy8Cw8nc9HGPgw3ougzAY6pgHkDemm0r%2FvSI8ly26%2BpqBBf9%2FGJ60hNSUO%2BUGE5HIgRijlafKuqySX%2FON%2FMAAtXcpCkPeRR6K4oZgSLalU5315AEROLMit3u5elvBuqLZhs3qj9eStihrPogExFKmHZO1rL8nUU8KXpy0jiBhGs3lDSNB7i%2FSpVyKX4PhtpooFRkGn5YabMF0P%2FdC%2BK9%2Bw9dwS8cd%2Btf5MDHJPbuuyoWftOiAZCAAN&X-Amz-Signature=1a9c84709ffa61b485f2f730279c73198f9b5433920147cadf030cdaf307dbc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



