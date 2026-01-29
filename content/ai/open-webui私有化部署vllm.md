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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674RXAO5H%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032826Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCgRleL5Ef8qRHdnK7ODforf8iPAldcgDcVurmT787MrgIhAJmYN5gWrkTHO24yaKktZwCUM553I9FpHX%2BFg7%2BJL287Kv8DCHwQABoMNjM3NDIzMTgzODA1IgxhpTobyt5gHtIFYCkq3APpmDOkZLaBech9UAzX5EQwsPgvHlHYXhRGtRQR7rGcuC0yvk2Kn7mFGxJ7kSTifUWJMsz7hW3YjSnu1FAot9Vnzj111SUeRGEfZQc30s3Sr9KLqK09OhLWeOpcNoKPNaIk44wHCy9jnkAbqp00PMm0WXuA9qSEg8QR0EaM5ofSiwXFXHZJYsxGKFQ%2F9swlbwo%2FFN7MAULIFlAAmAKP1gcNIoVY1CgOzp6Y6JOTsLbIo%2FqlpV2HAp%2FH%2FRIFjEWgWnbLnri%2FeOO9BCNq90dWHjZmycbjP90dUExoPNQ2ooG%2BiDEY4rPQg74jUZk03WY1UOXK2Mb%2FNF0tl7UquM0yeTVHe3NveGJbJ5o090gWll9MVrWqMuBix%2BNf67QLlKcoVBJL%2B76KmHz5JKq3IK%2BdIk8U1MbcT8TU7hWdb0YztpfMqepiIbV%2BW9ewW%2BvUGRpg2ltBKEwGULephjTKMJ1hv%2Fd4N8jQzv%2BC1vk54fSDXqMI3v7wh6fz2UQXFYGQFLNTOvJ9V6INZUGHVwwA8bPkck7GwFGqLe%2FdXpD3LsBBm0Voq3RI8OPZxFk8nXKRjRtsswQ2E0IXHX7ognPpwnhyMyyLEX4SiS5N7o77QMCJe%2BChax%2BnffwAFUaG7Wxf8TDooevLBjqkASPOaxqVdbza4YbwydVUMt6QB7QZrsGDe82TK2QzTx%2FoLwDjzrXnyRd%2FzT6rwQ54lXiCkPT9bUkDUr9NkkbQH5zigA27fETl%2FxXf9hHbothSA4ZJ%2BKjxJ%2B0HaLB75rJm8WA9DgOfB5ctvfKwWB5LBht8QTUf6REzC235P%2BsLM9k%2Bam%2FkD5nK111ebTOam0dqae1ZfkQTeLYcDwcCGsrqBzqiGo8%2B&X-Amz-Signature=2a10c0313d37b3d5ab3659de16f6b610c994393c2972f66fe9d0753eb8df4987&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



