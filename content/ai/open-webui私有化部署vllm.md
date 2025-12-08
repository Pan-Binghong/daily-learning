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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/a06394de-df12-42ab-8865-819098e568c5/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HXBIK4E%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSHKDeI6bH0ylw0I2OSzrcTkGOZoqHUXudaZ%2Baz%2B7IIgIhAKhYozaH6dNido4mCkKx3MPmobHLvvLwRgqdg8zSqAUlKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyKTF%2FXHTxN9ta0ASEq3AM07ZIfhJDPZ9NIEsV7MCBQparfx9MeP9hzxfWGFx5VliLlSgkNL0PbXE23VuV9oUA9ZJG%2FEZ15CqchKD96OGsTt7K89%2FrXKw18R2r8bEVdVSrMF%2FhuqtOp4QgghNnsxAYH3YyEnJYVQTQ5ZwW%2B7svQJ5NVUQiQb5zLCMUQNCNF%2FNYrW6eN5%2BXCOvU9pzez8Sq98VequzTBMnpMWpBWh%2FYlANUZoqxx%2BPyiGwG4K8fOp1I1maWQbjXPnas6PKfdEM26GQu2XhfiOW5%2BoFqZcPBShVUrgOk99RgauDrN9VMP17tKQmJKW1eTGKf6L7HwCEVnzZNHAAD7Pj62fEY9Iwl9GIa98P3b%2BVcWqpa4QCpTNStrGDw%2FdBqLUHgjaHLRU0coSMbQ%2FgoiAXTSioUEm%2BxNDfKaGKqHVfOf4SNWmSFrdD261633Zc7FiJuuz9AzUY9KF6qYQajAY6DwmtAjt%2BWOokj6aTf14joL7JXKrr%2FbNk7rn6Jf6mPx8YtJzP8e%2BhhjSCJ62qF86NUf1zB2rpjrjo8NMPKmA1Fy6MnHx6lvP9D%2FoEK%2FX%2Fj3sm6HFd2q9wJBGsBGV5DLJVZunksA11AZg4EtGvkgkadZ%2BRfGXQe0NBDBzFvBJtPF7zaTqTCT7tjJBjqkAdGhBoYnoBfhYh99Txgvj7twybQBN4gyh5sQm5064inyQbPkiCG29St2T%2F31f5ip4dlT4D7XM8Jv9QTmYkOaxEHqlikoH%2F6bWBIJaYLf%2BCpVLn9XtkIg1fQ6n9dyoOX2CGyZ4In%2BSZgXZxlc8LqXgHEi9I%2FuPA6ejjOn%2FFj4FCslq9a4r%2FnsAf6UcLiEc3wZFQB6LyXus07o8MlorjF8RrKAEWb0&X-Amz-Signature=8d7c22bb22bf58fff154ce26d4e499a86e2567516a61cafc6188d9674e0168d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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



