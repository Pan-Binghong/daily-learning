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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YCZ4O3L%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030538Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDn1C6ZBGaY%2BvQMEo6wSB3Ye4SEGq4YsNRHZh10AGVyRAIgbAIWuEOBzDP9VOBqDPHPancZ4iIWl0LwQiy4nhywv80q%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDJHbC5lErnoNG91xRSrcAxX2jd0gLLygl4WkRkYORFmyaIFhYZ%2Bj5bRRuYq4%2BE3AYH8itF51Xe%2FpYhEXiVzFymQ6U2hodTeMSbzffB7yFZOePGIJDUIGlwv6ajJfjhOatdWVKN9I4QSSGKJMQUKqGVtkXfKF3Z9SD9KwrfYzP7yQ0xeLGt%2FBeWxGIiGcoc5LMciEgLm26%2FrRbUa0%2BoF7h6J%2BrxxX3bdNySwCuy2iSCBnJaHn0mN0WBOulGb6w0iHgq5X6xa37a%2BOH9lUYMloPgSqBFZkZTk4GAoILKCIVFc4Gv6%2F8TPeIOvPcsytk49oK7v160XrC4c3dYURCtXzdDsLEIyhTSZ7Fqo%2FW7Pq2mD2L%2FlWWCE%2B8%2FMpSSqYgfvTqzss90uuIScLs2pY6tkHqeIqXOWOoi2zqwCsGEZdPFuXWDpPJI58%2F6mqQXVTlJ0XA0%2FW4h2yxDlNGei2K%2B9eROQ1MPRThWOlNIq4jUMHO0AovyypiMkB4oS%2BReVpRzE%2BxfYThq8KUAGrUp5UxkQfcfqm3bEgIpc3IS3q%2FE9gSwVmN6RzqZeqPQqPKFBWDADtQ6DIh5YJvMbE0Vr7b0xUuT24TGzPn%2F9tOC6KVVOWavUY6wSm8NcCt3LFV2D07fuWu6PBqoX6awBXZ79bMIHvm8sGOqUB%2BiwshFlg6mX7Iu7FR4TMYTy9R%2BH4o77FwSiT8O2EBk%2FlPpvB3kAAbaWutGxdE6TrKvl60FNbrqjO2gBE0%2FnB17NWP7hMiVJwKgifE4Zkzk%2FJQo5nL0tFggZ13LwOza4prVumc5OYR8Vw0fc9i6s4rgsKbsI11s4BcHpXyKFb6kmMxC0zd4V1UYeoK5CkMoskUFt4nD4rhvHhjaiZn6SRvZG%2Fg663&X-Amz-Signature=22f0d92a03d3665b53f52e2dd5f0565b25a445f5f2496cedbd678324f62165c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
