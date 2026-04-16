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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPBNCQPL%2F20260416%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260416T041600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsxJgq34lQh4E5hl3mTIqLgGDWIGiIZC6IlnznVcaLXAiAxvOzpOyaZUL6Tz8VY7i7PfefCnPCKGmbOATbSA%2BZUkiqIBAi1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkTFOTNixrPi2RWlfKtwDVFqjZBdNDluxM1uunxs9HlhWsE6ZpgIEU%2BNAYu91KtIDuL7Kv8b4k1cZ%2F1HH%2BSo1W%2Bb%2BpxUrPUFvuW%2FCtN55da4Ofh9HogfD5yRfDVOnaH8IahXy%2FEcCIGhsqkSp1dqZEm0w0t99HLsAVpHRIhGwehirqk3ikwx1YSzKDimrsItb5OztT8HlCfuAVbVsiteS4Fc4XWY2mPIDGzlvjC3aYq0fPi7OfoAU%2BdLSHGmRXhD8d6oTN5BahSSgcqaHGOPKSeeBhhkQ7gREbAveJs4nNpWr06JF%2BAc0pNYDU27gBSnPotWv0cPdxxZCIzYmWFt0GM%2By%2BtGvvjv5k%2F3ElqUTjY1xEsVwM%2BrqUuEIk54U4wFdfZ%2F55gXrxTUtuROY9Ids3%2FG52jI6XH6IoReVafChXoby7Rz8pO9Xzf5OQZxYqdM9z8bxnjnCPZtLDDeQxmH4Jgxrzi5v06M%2BaIzgCSbv9Yortl%2FNuF1Wo%2BNJt36D0wXzERFNWyFZxsrjfeTtQ9yL7to7KJXoTVq4rv1tUa1YpBf2BolybIZB0%2FL0O2jkWsOqn5ClzbxgwXdiL6lOHjqkns290Pa0B9qpkQ67Ev3JQR5BACDfmi4cSDmWHRUNPRxAPFkjGenKigd1iBYw6LOBzwY6pgFe%2FdNHDKginj9lOQriZSg6Y7lUrCBqnKw9yYAiSrjHcvpnUNmyRg%2B8p3YPEi9MG1mJ6W7uC5YBqCWsjaWg4758WnaqW%2F5HJCOdVpEL9Hq1DlcI8K7FZChKwFH8Tl31bmbdO9NUvxlF4qO2JdnTVjPbXVK9%2Ficzto5pP6BdUBEa2scKpG%2BI7G076TiiOhXx8LmE8jPaY%2Bv8jBQAn%2FggG%2FW723e%2BOZj9&X-Amz-Signature=d0c97e75c5524230879a658670f8a24ccebd2727b8e9eb133d230f37f7ecbc3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
