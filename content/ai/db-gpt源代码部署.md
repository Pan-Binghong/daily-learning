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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VKF56346%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQfLqx2TDqYJTluBWK16NJLDL%2Fewp%2FYAAiqcK8vjsRXwIgJ5RIdDKPGzU1uunFuwkAjwh3pmcKawnxaEgZ0un1d4sqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhEpU7ncW5BSbvP%2ByrcA2bYIRnITFA7UTtyzUrBCV8NeHcKOVTLzLWcjRlPNj2qefRdyOmmB6Fe3Cx1YZS%2FBFhvAeHdWm6uaRFFk1ZXDlbsgKIbqfEEZ%2FKmp5mko6%2BlSgC%2BEqqQubgRgp%2Bfw1AXCU8cwuhZMFcauR7Bbg9ATHVdju4A10bnTV8xCBx1jq5i9hMdvQg5XsgtV8RSmgrARJ7tSLw6C614rb6d%2ByXlhZs%2Fr29deXKNfAZfJwAxP3JUNUm8ZnRFugjriAVKXyKM7ApNfwpGe9M14FREemWDWhhUWByLxbi16UxxeF8CE2fqDB%2F3PpRlVdT45D0A9aeGBueJ%2F6oVcrfLdPFgtBHSMcLP8R%2BlHwgFXllSMNo9ZPjgjabY6jirrA7Hgs3L%2FNZLjwHQfkatWrD5UbhPFi75zqajh7COh3vJiSgnukgTo70PrlkGI5xv4tCIbW%2BxRdX2b0YL9EVMcG%2BZOb0bTNsGAJxshRUgtotDC7A7U1G6v6gRWZufNZKopK9NklIYK%2F%2FJu54YAQIv%2F9D1CjavhazDIy1eqSxhL1eZuofSH9Z5gUWVi5s6pBUnWU7fadwxtP9jO3E8xt7Pv9JFfhkVRtxmazL7ojF1TaceihqtdDSLIO5tRls4upq9Bfk8o6AyMOm1u88GOqUBC%2B5Y1mdccVH43HAJUPX3T%2BUxq27ifvMqwMbTjy7K7LGoQo1WKr69J6fsJjwk3EZOEbsRIA3ouHnxyUa0wSuE2NlobXtM6F9JulyRO%2F0PDUJubxMC3qjDiJJfLLxhEZ4P%2Fnx%2FZHt3JU7%2FEjmVx%2FIZoWZUR7UCLRlr3nwk87UeTJdIXiUZ24r0XcATvK4O0OUZRoQrc%2F%2FrBl46GbP2Ha6VvnPl7S1g&X-Amz-Signature=bd5f8b62f5ea965b83ae8a17e0d4369b2aff50ec2bc298134fae0ff0a170e096&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
