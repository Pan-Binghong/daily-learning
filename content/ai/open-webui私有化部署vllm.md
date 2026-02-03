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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YGKN7GY%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJGMEQCIAyYn%2FDx2DxTjzTXPT3sC8uJ37mQ37VISyMxsXh0hCo9AiB1cQjTYSb8HUMY%2BQnBak3mf%2FLVt1ZTAW4H1ta3cgu93SqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPvruFyChgvz1KA9vKtwDN7XSGe1t5oVjH41YLYN5AJAonjmSqLoPyZdvkFEgIHJzMVPJtWtVQFdpqgTinFWnRk8teNqj4HIP20KomOqolB5JAG%2FwjrL3asVhaRgfVAV%2FRap1zLbXs%2B5%2BlhnV0v4%2FfxM4sZDxHKx96cACNhb75R34Tl8PazWwdEWkHgCFEqcZxxuvt5H8AyTaxE1NyXD5QtrpEoycwy20EjHWfhb6FsSg9gVU0bmlO7qQNRQj7r4ADhJ8kXiQwRAGILj9XSGUkqfSw4ouM0zPqnXoYquAPX28F8YaJ9%2Bxq2oyEpV9eLvwiL6dtwo7dwXgtSat3wpQPJxwjyVhzMT6jc19TajY40rtgippmP7F9nSp2kbeRNkS%2FqZRUJpIyZzTT7N89R9KAO%2BlqryrWDkPZoiQPr2l0HHz5QYg4skQhT0Fdrn6CUMJBZuhID5SWO7vz8FEUmCRfTmEnko8Qcit71Wn3DPPfQchRkZGwMzBz5xNXI7ORmNd4HAnmJQvcSjFriJ%2Fy0XN%2ByUoA3%2BxZnJZsFvMuGd7EoDoN79n%2B7sjRXfPPvEeqiT1cWQifuLfeI7wF09ysWDFZZTrsPCc553qZpH5nvN3GPGmEmDooK8m4QgEwBQt%2BoK0pWAoEKD5oR%2BILmIw1NiFzAY6pgEHiYVUUMZ9wXNp1KlweiaEMrpidR9sORc%2B%2BZstJhxqk2PV9GrXkQqJFSL10vRv017v45xz9Yl3XlugPrMxT6wYjOh4nJA1%2B0gAg48NNX68y%2Fwo1j4TkmITaQC4%2BsQrs2vczurXq0gMpCzZEi92hySjVwa3pyNmgsksP4Cuu2nMdUrirfOS9odGzjTF05OiHom%2BtFrVf3OfKlplGq3y5foQbRt6%2BT8f&X-Amz-Signature=9c65cf8c8788be0cabfa567550d49bccc38003b5e9945b10d809c90fb606543f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



