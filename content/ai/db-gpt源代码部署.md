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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQBEDRBW%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJIMEYCIQCFR%2B7dsnP1vAnsyOpyVuSZEdIAvDRp21DW31WATiB0zwIhAL%2FQoh%2FzjzPlTRNLcu0u7AxMDMrWUCVEmdsZ7TvhbyVDKv8DCDcQABoMNjM3NDIzMTgzODA1IgzVbTdO3qECW4M6SWAq3AMXswjqvK2VO5J0dQFmr6I8c8vdATip8ZP98BzXHHY6I1CWUxOhHLlcMMK4wQ3C%2Fgu7NbkTklt6t0aNQawzK3RIlxY%2BUrjLvCzMGytLduPNq8qSGd48qKN3rNpN4rKNjIWufCdsfP4EgnuziLb4ZevlHSaZTxKTMFWkmaNFznr5zY%2B4iHdGBebBevieq%2BEefs8Fbsb8HhtPiQwqEnC2eAfXcTB12GyR82a2oLpP%2BNEEg3MFrYJrcVpVO91uy5f%2BsULsvzM1fl%2FaJJsnwj%2ByAQhJUO987xFM%2FtLmYog5CEow8RLPbh8lgfQOayxWJGoA3%2B%2Bl6JamJjKJLh%2B161r8aZROdcwyIaHx9H4TBrGqaD1zJci9Sl8Fgb49y8d7UYBHWbzecZDkopB%2F50QdKcl4lf24BMedQLp%2FEXpbMDCY3DUIk3fGNCCyqhROv0mKz8M14GA1ei793bxd%2B1y5G%2BEtFOac94%2F6qs3q4E5GVVVvoGH9ii%2FVqJ%2FUf1hZRwvTmLAAc%2FZeBy5O8o%2FdSCgRUPuxFuqbjyuMzC6B10ncsn%2FikzqYm2vrlylOMN2VEQe7zu0IavZVmIk4lzgX03VdFNjAyLkE0XeEAO2UVJdL9NBZJ%2FtH6CFHJsGULZQEe8LAdDDMxuvKBjqkAUdIRZnwjZKMIihYLr3N47YQq%2Bl%2BqfxbpByyO%2BwapB00wPr6qyLOVhcV2NB8%2F9AUl1vM6KhBKSzHcC%2Bf26ma8g%2FVKBJxujCBs14QrPVIJBvaH55cFgBJq9jEHBez35nuTkz2Wc17%2FWn5XA0tMboNPI9QlheGMUsqAOfC%2FyUpbORE8Zv0hkYVqtCTVspeagoFmzOcT17c5Eo0fxVU57r7te10kBZM&X-Amz-Signature=8dff9939d610db3bf9bac59b4626dd581447fdc9ba5f1c6dbfb5555a0c3e671b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
