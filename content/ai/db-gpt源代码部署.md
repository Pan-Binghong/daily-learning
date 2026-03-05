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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUYH65WL%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDG7v8IAgCzeMgSP8w6OQxGxELYB6wYt0CMZN50Ik025AiA75X2NAfxvhpp2X4ECCMe6%2Bru4iwKmY1bdEpvZ78nSPCqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAk%2FmTX%2BWIUXsIpdtKtwDfqY1d095P0aJRSIyG9oZQaNjomLue%2B%2B0%2Fcv9NiSfofddCP30aajD2kKT4KrPOms46mvXFczs8KAfYMODcitvPlr%2FN%2FZR2dFpwhKFXUKaVYmv6liVwdFjiBQUEu2Cw%2BvZBNLaBYDReWJDLpOj%2F9S2k4dnL1XUSexcxIHzk1SSXICm%2FJiJCvUypB%2F3WY0s6b86wxsi%2FG7%2BrwPWTDW6pJWVko4NcmW%2FeApbNe6yZT833YTgVwvvRZRUhLhFxl6cHfE%2BrGuN3FSO8zui9tNkSLonTzSrVqB5HiTEUwpdarPO5l2%2BtIvnmREz224IPc%2FXA0iEURS9S6aGoL44KwNqYRjEa6vuD64rLn8CAqKwWdSqjcGZ%2FLJJIUjo6Xc%2FxSMZzmPvEGHK%2FDSHuXWA5vdGTlkjWiS30Umv2S9f7302nOWE0Lb0w1sWh1TuxV61IF38XMiUwHuO2XalGYs4W1ve545Qyn21T8rbMpwzzf7EVk1fDAbNLFPmt4vVJkj8hX7KN8MJrtORExQiCJJAcT22ifqJDjVOpVWHIjh3AOYMCFApQRST6fm8d7Aw%2F%2FOFsGvWqS7LdbqcQ61o2CrIlLobc9zAyJRXKUQjfxfR1zQgVwy%2FGURBW5cmWxI2BzQjgv4wh%2BGjzQY6pgEeYIGySGzTJuvCCw3HuR1PRyvnwAECXJE4IsUYOjVWpoQmi%2FoNN7k3z6uv1jAhYAk0okJF50EFkUZq6ToEWy8ssUMa50bxPmWyPxdRWe2tjRIYD%2Fr1UJIHubBdeG28RxIvKaN4v5AdA9AIkf9ohFyHifZbOIH2FBMI%2BuUsMj%2BQN1a%2Bz7ovY%2FKx%2BVqu8TH2wxa7v0%2FjQj8tDnuIo3oV0Rp3m42jjJeg&X-Amz-Signature=3cd0c8365c4ea73f5b561f715b1d1d61c1d208daa5172d6dbda666ec5f709b58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
