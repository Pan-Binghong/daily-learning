---
title: DB-GPT源代码部署
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
tags:
- LLMs
- DB-GPT
categories:
- AI
---

源代码部署DB-GPT操作流程, 含测试, 部署, 注意事项等。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VADVUM4O%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICVNZsAjRJm7Ml3wy76EBjWFUBOm3FPpXinVxgUde51KAiEA6YJKDIC4IReZQ6rEvFtqH%2FDVN0m3%2FKoAf6s35z%2B243kqiAQIlf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbv%2Fc8cVcr8bzqZuCrcA5gezFcBsfhUK1z4SurzcPnVhEIzrROCcmW9fhnBqWKXiV6WbpXvgEvYiEo3dutTVWnUme7Pw6RdN6Yey6c0C%2FU8knAe8G%2BOUf51XnMIt9ySE5wp4IoEqgUoeyi55xTIsiYIKCZVebrl5q2LylVuMahogNsU2Tlz%2F58F5ndFIR1It2cZ7mHjr%2BmFiwqBoFMg4IBwWYOcaw%2FzBhmmMOoIxrCMjf2BBHFF9yVXRU4q%2B5P74Ne%2BiXtiQ%2F5SnHqq9XpNfxlD4zE1KxNhHEuIJ6S1U%2FJSdEpvEE4%2FQ9Oyyt5OS7Sp9wvKZ%2BYS1ibAGvmLi5W6t0rDFup88xIryEn5iFBulX%2BT%2BsbDjXjND4bBLUmbU50T3SBeA%2BD5h4HukbMZ5bXIhMch9dVHkD3Zk4bqh1QsFvG%2F85paMgkgOhdYmpnFnyZjXCaA%2BefY1mZeOiNeFMydnI8Jm7WiejvbX%2B%2B%2FCwoOUAv8ExSFsa0%2FdXL29G80qpJ8Eetsbsyc3MTdzZ9blyZeIydYo6g09dVzNKjYKKZwR0m%2BYxr%2FT7vZgHx1NP%2FTrJZDK0b8Hm8Q16xJSGL%2B61xBwTJt4IL%2FkL0MQsDTvmdZLe20OcFTGUcuQ7dvvmUWzxVP628Z0s5s%2Fmu5OvFxMKbI8MsGOqUBr%2BvkTaXJ6Uh15ob4ffVUIuhf5gQN01zFNGrAdwpldwQfyxdpKo5jtM0OZhXrZOUK0vubjT5GbkEQvrm2%2FAldpPTWXkUlsXa4U7zB6P%2BQuRpyhexE9MAb6rbA06l5Dq0UCgcRA4yYU2cSliGxh4s1T5YU3G7lPQ6KcPNU9KmIYoLb9QYlzcvdrS2%2BzXTYUulclUWpG5t3yMo%2FU9tCVkpCYOyKHZyk&X-Amz-Signature=93c3bf1474f34f9c747e301732bcb1d7ae5751b02883ca85c763a15d553e0891&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 1. 下载源码

```dhall
git clone https://github.com/eosphoros-ai/DB-GPT.git
```

### 2. 安装Minconda(运行环境)

```shell
# 新建文件夹mkdir -p ~/miniconda3
# 在线下载minconda安装包wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
# 运行安装程序bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
# 删除安装包rm -rf ~/miniconda3/miniconda.sh
```

> [!NOTE]

```plain text
初始化
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

### 3. 新建代码运行环境

```shell
# 基于minconda新建一个名称为dbgpt_env的基础环境, 且python版本为3.10conda create -n dbgpt_env python=3.10
```

- Conda环境常用命令 :
- 清华源地址
- 修改pip下载源的地址
### 4. 安装项目所需依赖包/库

- DB-GPT下有setup.py, 为作者写的安装依赖脚本
```shell
pip install -e ".[default]"
```

### 5. 安装可以远程访问模型的软件

```plain text
apt-get install git-lfs
```

### 6. 调用在线Qwen接口进行访问

- 安装qwen接口所需依赖
### 7 .下载Embedding模型

- 在DB-GPT项目下, 新建文件夹models| 用于放置Embedding模型
- 在线下载Embedding模型 | 目前好用的有:m3e-large, text2vec-large-chinese等
### 8. 配置模型

- 在DB-GPT根目录处, 复制环境cp .env.template .env
- 编辑VIM .env
- 按照文档进行修改
- 具体的模型名称可查看cat /home/ubuntu/DB-GPT/dbgpt/configs/model_config.py文件
### 9. 安装SQLite

- sudo apt install sqlite
### 10. 运行服务

- # 在DB-GPT根目录运行 python dbgpt/app/dbgpt_server.py
- 在浏览器输入:http://localhost:5670/可查看web网站
