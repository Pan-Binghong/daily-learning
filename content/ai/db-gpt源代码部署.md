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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDGZDKKJ%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034204Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQC9yuvxQ9pivpMZGUo5Ynf5E3skH68Qb2P4X7%2Br6daVQwIhAPajT%2Fz7tMIA%2BQ%2FcsgFyC1f4IzdvsLaaAHoURNVcUwO3KogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzsj2yk1DVrW26UEJwq3AM3aocEIcgGhW2%2FpY4I09PqlPx%2FgUqacTwXvlUzSrXHc0nUflBcIljQUvdjt9BYU6%2FQ8zeIDNO0wgDeSn5e33PuZR6n1bnMCXUm8%2FLOjDcHXFgd9fddnNbS2JKLWbHgmihpSxXGPO80PtOi6MXEsjOKZpkl5DbbCDJMBovTpSWH3bXo8I87YyiY%2FCCL4plyNQ2FocqkGn1QaGkvrE5Y%2B5HALSs68RPUXrY7w6izu6H%2F%2BTMe2akNOAVW30YDnir2uvnA0wM38xbOMXopVziZi8mjJgxydwjtLjjFzpD4a%2Fu6Dmn8i5TSI9iiWO4TYY9SRz7miSmlOV8y4QDaYOWfkeFyJ3DCRyDjqApWpbYdPyL5qL8mY6twl8VJSiTOr7Y3GuEO%2BuXsYi3qcKSOw%2Bz2hBmv%2FkbiaRKQvqoKQrl9%2BZLCUDXxvnxLXG81NW53gl6etDgMSnTg4nn1dZ9Qsu91hLTrf9FeHRZhCBnUHNURQO0mr4P2jIjWHzkLNOUskCgFSclSAfaeHjGY3pJeVX7C04ZkI0PRZ0cuMOP1Dm027FImNfbuo9uRECGL%2BksfTVpiVHBeQuTPEwDnqi6JoQDeFw%2FPNVDmyXZa19kPBckPmyODmypH0s7YVApto%2FId3jDGku%2FMBjqkAeZZW5WS%2FDGz4S3g9WwEyva7SSBiMr9GaRgZxMAAzAOs5uXU9qP7jJtUSXwFGFjPJ9arJPoOp4OHR49YMBE5fvqpFK29F3ZDLIRHd%2BwKImv40Mvw1pcnVaJ55rtO7MLPdR4O5uoixh1bXKwv16G6%2BOryCmhWDZN347gkIz4ce1ptvtdhZWjwBsnYCO6%2B6JvWzi125sMWPWY%2BlZ4PYPTmcIYdUeJr&X-Amz-Signature=3709fb081b9489e0a0b7c560e2fe5dbd875e7b6e07fd93fd7ec667349ea8aa16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
