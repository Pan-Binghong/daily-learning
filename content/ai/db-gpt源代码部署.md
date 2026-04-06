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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGDQHPMQ%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPz32md9AIT%2Bx%2B5Wm4BEbg4xhfRj%2F5hB5awSEhniGD0AiEAnxn1JEFXosJRFBphwYtngakq%2FqK7Q1NL0RrnC5qSJRkqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGt2tJKyKxH00yZS%2BCrcA9o%2Foz2JKKRVZNHS6mtq%2F45xp5jeP6fk%2BEY1do%2F3BuVwYk2kbpws2orhDAzxju0wFK%2FKXyBL3P8CrlareKDdW%2FRJZRTh0ao%2FdjZ3NGHIrWGU3MDgIRQM2uYZ9SL7UcrbmSYCA%2B%2FLaGJCVMSXN1WBDgquzxAs29iM8MtLEtMzzQsod%2BsooHijwfULSL7sr4JsojUypAyrfrB01D9NbtXb2hWOsD1WkBsCouW4dRTqNoWGW0AHoTogod%2F1w%2F3Yo2kAtoJf72JM6IvDPqdaveh%2F7odoAPCrw7VHUTvyN4Sp9Shj%2BK5h3wDqH%2BzGYz0f9fCxA%2FNi9Hn4IGalYwNjsikOfYCjJQC%2Bi3hkUQMsqIQNbOfvMYgUVDgQ5zhxdTFMtPLwqY88ls%2BXUquQD4yfh4VbtLTgfkP5S0ZYY7t%2FAj79mTUB0hPuZPp%2BLSyWp%2FQ8J4jZDQetDtSj8yz6WI%2FV1gpEuVP%2FSGMmk5uml5ZNhcZGI3OrCUyeuMRSieZC%2BGqcyl8I6CpUjl8VBx2GvV5utVo2PnFodi30JGNkioBDo8KpNVDJtUw8RT5vN7CUXSYhlTHTpi3WMf7ZkJf%2BTkV4CjGysdBzpBY4a4ET2j3H6c973ELXrrV%2BjODkDfS1uSjEMNywzM4GOqUBYzD1AoLII0alJ7IddFpxnmnyQAvh9ExgJx2BETR%2BfvbMhGdIPfs9jBCFbMQ51mbar6zugxVxw0uEu9ykvzDuOWGTQLXpORS05jvABzSkJJ3cRdwOE1h3qtcJVz5MXulNTJTd25KjDIkfJ3gLLv694RvQfqdkkG%2Ffd908qHDwm%2BnKQgEzeucUPjhtnwnawu2t8mhfGpM6ggxcrVxw51cL%2F7wxNy1J&X-Amz-Signature=8611915e9d056f643b1f022d0536402df229fe302fc9d89dc17a179b0d80389c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
