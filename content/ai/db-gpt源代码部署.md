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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SL3DCKCU%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T024933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJGMEQCIHe0yjTDTR%2F8Nw4XjzsT%2BUtE0C50HX%2FJuWv5LB4xXMcqAiAzeExUyvev9m9DlUrNMv%2FhYlIaX9v69mowqEympxzUQCr%2FAwg7EAAaDDYzNzQyMzE4MzgwNSIMyWBEqVrkht52jHa1KtwDhit8zgxGfPprYWlCkNalF3%2FR74AlCRHVjmEe8Li5oyeF%2BZg302aJLS3HmcIa6GUwVfls5eKeJjM6WPvCLzBIkFFsJ7M69%2BhF3XGVwaLKUGkiJYSo353HPBXfR0PxwMMK2PGKPB5XzAj04kFwvIGTeIybefqnPlcNrISPgtv5OO5%2FlukbNMJ36J15GZ%2BUcggFZQTroA8BI44aR9KuWypW4H8QhWLTA8isO4s3PhpSAtv9AjiNYkLCI2rNH7ohLPyxwfNrhwzUWpfr1eV26LKMkrU8%2FafV83nwNkzm0%2Fanb7nqsRJ1MwLon9rcWpArJf7oNuK2SV%2BEbksdPQ9SB7Nv%2B8dXZKS6m891%2BeppVCeRCUgCKQEq98k3LXZ5AzdVPi93G0UuM79zYQE4hfdDq2UpmyNbOVNcaM9ociYCDdQLIq5yf7xeT%2BIG12eFjkcxpythOJlQv8SR4b%2Bb5u8Mo8NyF8YJC4buTHkOS12whqxhqF6Tt3eOoW3LvDAJCu38FWRq0l1VoDlbJy%2FscBYxLZX1JFaArpvcu1Y9yKjBFmsksA%2BWjf9vr3Q9OIdoaofwBvMu0AWz5otlTIcTdnXuQpHjuo9kq2TiWI84xZ5R8LsRTRYibo4ke0pOIZm995Iw59TDyQY6pgGtTs91VGS8pSsvGODrx731CZp%2FJYG7dLhyMf%2BbYhf1ZrkdoC4AWcWphMQ%2FEV3codcANpP6CTdACateNGp%2Bu7wy6TG9XBURWc026J3idWUjMrfbALeF713NlxJ24Bjx3dfehRBPrqwXT3s1jHSS%2FkgOSS%2BfGL9XG1PdYK2jX4PTSYsslxtsHzQ4UA3IaCqjNdlM5uZ9laK8L9KgztpQaMt3cwEbKUfX&X-Amz-Signature=dcde8004d52e314e7bbb7c994f56e42ccc9bcd88eede80a463e974d500d17d58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
