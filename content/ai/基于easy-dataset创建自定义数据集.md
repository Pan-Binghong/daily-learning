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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6ae31304-ff2e-445e-847c-f0ffe745c878/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667TSEFTWZ%2F20260414%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260414T041106Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAywlXzS80PfMH6Q%2BIC4%2BZOcubHF9r2PIftB5DyQsy%2FHAiBA3Sss%2FrQk6lNDBs%2F6O22JzoEGscgkheT2WY4b40MbayqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2r2E4A1EUxp6J3WEKtwD4vUtDsASchp9N%2FfdfOzqzQFd9nahWly8MCxNM7Dahr63pu2v6eTNrshtC4stU%2B08yEQU679Yw9XrM%2B25k8yUDPBWJOM%2FuukNfKun9Itj2NrwU3tCeDV%2FwTDbIILSZxgD1TlsqVnrUCPl%2Ff%2Fw4t5%2F3kM7NG42Rxw0YbpKKmgi9eAjykpdY7JLwSAt3VHBtkoyf8btvvcUm75cGOjNFsMea6oAXBoJJyKPyP5Zo3lffqldud804D0iFFAmgAvyJ1RghPTQ8bfvzSUNEtggaCcTfaKJEu6PNmhE%2BCx5bZLkiQt5NkFRcyT5R9jJNZg6r1MKusldyKF8KePRWf5CBZsYe7qok33jZr%2Blm%2FXQTMpN5b8GLLGyiZaIsKbXyO0t8rvKXmPFI%2FegOO8v94kP%2BCrO%2Fyd7svZgGSXR4zokQg%2F%2FuKrQ07CCKAxAnBLNlap8u0hFRUF42F96u3y9Cadz0HyICvIQRk6%2BhUb9MzKfHAEXFO7QQDcGBZoo0x0Bkq5O68UoI2iV%2Fno%2BpOtbgnY%2BI4SXwnTvGyYiYcjp5KuXsQ1TZvmt5T95T6QnUeHT1bi2Ktna2PMYwW79Emufe8sJ4k09n4jg3pn%2FgXBGzguUyrQBK1H7JAlLX05%2BtGdLm9Ewn972zgY6pgFul1Wxq0vNxE4loWwbUVbokJhjmy6y%2FWnBcclCkbNQkBKsCWcBlL0gVVv0PMrsvp%2BBQwtWXPloEvKbDoAiIu7aO9R5TUwSFmdbZETEUOQCEQoNtAZYjmYN%2B0I%2BWuJZjyL4c%2B%2BKLhj8WcABcJc9WiZX%2FxGPpp%2FIJ%2BFrqNA8N1gtcH9oFwKW5Bni2bobtP1i4fa6tmlBWseB3Zpk7SnQVD1x5uatQ6Yo&X-Amz-Signature=fc27de874cb2989fe5f4dc66208f76bc40550a0262e99d185966df93816a3cac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

