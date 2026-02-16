---
title: 基于Easy DataSet创建自定义数据集
date: '2025-03-27T03:06:00.000Z'
lastmod: '2025-03-27T05:53:00.000Z'
draft: false
tags:
- LLMs
categories:
- AI
---

> 💡 前几天看视频发现一个开源的构建数据集项目，打算复现玩一下。这里记录全流程。

---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GYT3L6U%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIA5wpJxOZesQG8He64bkhMyCAULDaHih%2BvkBlVBA8VXSAiBRkA0BdO%2FaAp%2FT5cYK9Kgz%2FiK3bLdhC2jBj6vEk%2BObDyr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMfYr%2FSe1Zvi5FTIN%2FKtwD%2BvAdiRvY2uX4McVRamLhOJZJRH6A7MO47GusN8DOZIxOfLF8iZKgSByCSdLOFuU25aaGdn%2FuIqcZjiHVg9fJ7WUtnjABpv7fOvUrmGSGp73lM%2Fi8Pp%2FzxSjUSZwq8jAH%2F1423gRGO8uuoZg8mXwAUHYcJ3Zjno7vHa%2FEg5fnwMkVqI7fixX10jbT8xg4NGqZn7V7p3NtEeY4e%2FoS1Mp3P5LQ3ywj4taif%2B23JVu%2BN7SigtoG5PsR9Si%2BTJBLZBuuyvkQTQFZ35wRCe%2B8TLMFl1kwcItTQxFoeHGcVLps3Hk3BnaVVZVM6QweKmY%2Fuh%2FipCJgicrZQDMh3DYHdide2s%2FT81CzkwxdYMJN4ZgMudZKMuGFQ%2BEVHgSAK%2FPmoy%2FcTigV%2FbeSAcL7GqRBjssUecAHBy6bRH6pikHdKjACtPFGxWviulOezzKGxKn41IsE5XYEU09VkA0etGIyIc4inlT2aWiRRrqipo0cSscJhlFF5guN4DqmWal6GJdME7lfpwHnyv8ovT4bg4fYUksUH16csgziXsp7gaaT%2BJXrbBdvdJEE6bvsAdCNUFX5KAUvYQjb%2BjRsUZdq6qsSAptEDoOxXv37va7f%2FRZ8CL9Q12k0rxyGpQ3O2DL%2FISUwzpTKzAY6pgE4lKfEqruqyYumMU%2BOURAnR%2BbyIcJAgXc%2BOE8bEBEDX%2FKM7EizoiexiVI7EbIVrf5rERhA0PGa4r8tmnZGuVqC3SAY36KjGhKgpd2ZPFQWU2iqCrJwLp4amNhMNxhdL16Jm2KqOeseUo6kxzh9zAfUxlgN99eGZ6j4NBp3THS998R3fJl5Jf4b%2BZVONh5LQT8BdEipUiPTgnM4zFm0KvyJXW5VgUlw&X-Amz-Signature=849835f190a10a3058a3a4e54cbd565539f73c6564eb7934411aa2fea320e93a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 环境安装

本人使用Ubuntu系统。首先安装node.js以及npm。

1. 使用nvm，安装nodejs以及npm
1. 安装pnpm
1. 检查安装是否正确
---

# Easy DataSet平台安装

1. 使用github下载源代码
1. 安装代码所需依赖包
> 使用pnpm的特点:

---

# Easy DataSet启动

1. 基于代码构建项目
1. 启动应用程序
---

# 怎么使用Easy DataSet

1. 新建项目
1. 配置大模型
1. 上传数据
1. 基于分割的文本，构建问题
1. 构建数据集
1. 导出数据集
---

> References

