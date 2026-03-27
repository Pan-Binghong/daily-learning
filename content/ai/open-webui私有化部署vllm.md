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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BT4X4YM%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIELxJltPAG%2FV5TH8ewxOIEVWTayqK3SkZHpv4heWLOxjAiEAsX82MPN1KDDcO00jjYdhrOIPnwW3BE%2Fqd9FjTYt7p0YqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGiLKLo%2B4jOgz4XVXyrcA4IhBrvauMZQO1kt6Ocerg7sQPTAmL5nRNv8vvvt0gYIz4rkC%2BmQo70WEEU6ZpB3mBJR5yt1%2BzipiF%2FYbQKz%2FsUYUlXhq4Ux%2FjM770dA550BCGNan8ADLgpU8yiXP2tRj%2FASY%2B%2FTVPzpYgb4AnTby9vffwTK%2B1HOQ%2Fqf1Uc7kAc5%2BSrHhjen6%2FkuozZjNUlEcJkUx%2FdbnJT8%2Fw5t54FyXBJDzOd5Ogs6fvdb7fzGhtRaFl8hMmKADYJcR4BEZX2C%2FwWfPDFUtz42yxUcHm2TMUSauZHh2CoQDcuQ9D0fz7M4RFAOWvf8qBmi0QDtGoJyZdBXEaXWsh0g5TLH8WcsE22tHW55V%2BKbC6GeYQS0zUALOcfyURckLhu73L4mG08Yj2aQSSGGrFkITIA2s2fLiA3APhiE40NkBMBwHAKVQVkDYds01vGpL0tC7vUkpT19ORbxD0pAZwLOAv6PkJ0x%2F3WzprrlxhhwiOCbXHdulh6SZIyop108rijrBMeVoSdQkgbWtqen6HexiBG7bPjTTmtIx7XMXbVIG3%2FcPclz0mwBJu2VIUH32sTZUaWZxeK8iA45kfabp7C5yw2%2FzfzvYPmLo1MdiBQ0OxXmxT91uAsJRI7z93XVok69THCxMKfxls4GOqUB4Z1HAnZQsUN%2FhwNYhgAPReWTaadc14X%2BCLc1gqe9iOWVSdBAfP80E7Qbm69KZAA8v2I9VV91M8n%2FXQgyuU9SgpKYeLqctg02o1061QSBTFrs0UuTJV7lMETYciC9AC1j%2FaRNFTN73qkjIMWoj6fw83uHUjlHkToE3rCBjmS64EpYGTP87YoIqaq7v%2FevMywbZ0KdbK0JiJZrsOqXMjI8mMhBaz4b&X-Amz-Signature=c0d8fec5e39c63a6e7ac7141f1b378f1f9264d00cef1a24e9dece80e7a2da9fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



