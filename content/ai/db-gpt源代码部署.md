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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2X5RO5T%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T032931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDXEtaJI7v0yfZwIvCz3uTyoXmyz1jb%2FytQBHQxnwE4DgIhAMCI0%2FcLyRzBoYEAhBgC3V0dfe805l2MZRuWqcWCom6qKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRLaN2UtY%2BqjdfnNoq3AMr14HHnOiYxutGB2p2L1XApkIVQs5akir131w4K%2B9z14XKC1fx81QV%2BQzRiNkcO5l9%2Bg64JtBAy3xyzS4qjcihsYRMC%2FlRR3qyUh7VTul8Sy4DOMnEs%2BcdalFSusZwQANvAVgP%2FzUyyG1g9DL0vaDyPsH8fIvymT8kVv80MHzc%2B9KuSo7ydfqb1NBRYX2%2BTyNdm4VZyio9jrv8qkT9X9zS9G%2BBYjY6D0aHVfdBcCNFfm%2Ft7eh5ylQwfykOmVZpHlRA0fPezNWwtMLVasMyLRtS6BPsuE53giaMd8afSSaEcfLw3eChtBhwLtsQ7FRqAsTfi54A6oHTxwJWFx52VNoi3Q9eciSv%2Fhtr3LW1QXVtfK8betlx1Ovm0CjRj95CgYOHRElrMQgI5oSvVgzcY%2BWn%2FSIpLYYrarHrsGY%2BCWUms8OsnXHQZ%2B96GNXIwON6gkFWaa3%2FwQUHQ%2FiYzCIklLlA1sgY%2FLjNEfabR2hUMH%2BjZX3OnDvcPU529DYDD8qBLaTb6AvljHKm4YQt033Cz8bjFrYdbOf53o3qK4mRxwoQt1fLZmzntGpOzSBk0AqCGKIe8pHakl2IAVvGmcevnVndyhlBCNsrZdJ6p3Iz4YxJVacXbDwtpEQfNTeB8DC5wL%2FMBjqkAagPxjuSyVRqfuLueCq2%2FgiLowv36jLKP%2BTO7XgE5xCzoBKr6Xjral1j%2BD20c6W40okslCQ%2BXKADsJsU4GFMfgxnh2aCO9mVgGqO5nbwlEoma9154eFWq32PzgbL893Nqxl4iYmdQFKf31XD2KnWh65DsuAbozt5XfWgRq0OAKK8HUIljAHAgFu%2BqE5%2FJsyOlsqwKDDkxnJZD%2ByY6RHvHqWZfEPP&X-Amz-Signature=eb39b65433fe5f56838a5ac24b79fc6cc7400512601e796c7380745b40b6f314&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
