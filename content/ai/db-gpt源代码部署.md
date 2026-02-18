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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XT3EHQBX%2F20260218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260218T033946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA12WU9enpFUwajDBP6z8%2FLD0DByUQ94hJGprfwK%2FQpwAiA8Jd4RpHr1gNP0QP5DNnUXYZGB0bqz87cZ049O%2Fm%2BgBir%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMohloa2IgeEQ%2FlZyMKtwDuPeXzx2cmr1zUsn57nq6nY7VNJ20NjlKNCjRTpNZk0xQU1gDjY%2F3yKg2JECH1qkVuILqgFBn7WTY3QGMtnykpljICYyfFtwdyMSnK%2BvOrqQ4k4uhxlZUyHHv05pYbUQ0kWGPFqV%2FPeYBToMYnJLKKcff%2BHwAruyx85VMvQk9%2FnG%2Fg8osuQ88AlLKc%2Fu%2BwiBl52Aj2NNsBSXSM6OEFB1VTJcfyGaz43OfvdfFKNbPr6QY51RK%2FCoYJgFOS%2F3Ge8Gp%2B2uAesRM%2FoSig3ijl8s2rXVGeB%2BmhFdzQ2I8PkF8TrTaKwvKIQL1SidKSfj%2FHAUEzH0BtJUbOId85UQ29D7T2SU6JqE2r3%2FiQPYKT7BJ4yPHWgDuPIw75ZJbcZGEU71NIMnZ5SM3wnNIv0UrKWB6heDJoqUCCBwiGwaYKUvX%2BqY1dwT3o%2FfcVxcR2OuG4T8hHBF6L8B3ZgLmLdD7TsheqDTe%2FmRZc9vGiZj5ZEsED%2Bz%2FOmEPTnwQMFaz60hqJpKe2DJ3Ie7Z40uqlvSTYqpIniO%2FYMGPE2%2BNFOEM5n1ssV6DIOv0KvcSm3MBI7vLaGLTrZQRM05I7WTTZ57XKx12iAf6eFShQM0fve6nuCe1zgIE0nSz5hVBOFIuT8cwyZ%2FUzAY6pgEmNmC2obR32GC0x2UYmC2MLCyf%2FwnYn725N3rEs7xJEkK97DAyfbaJ7LB6%2BUIVzZw4jRuDRcKpfd74eQAKXbtECO19hZ%2BZvC4983fdzeiobJcUhMLW8GTyhEg7wO4F41yeux3LN9jgHf6hXdc12xNJHzhsnQlMpNylyQ99%2BtASY6g31JYkhovMvvTJAv%2FdQQ5WdeWLyJydZP6j4F0uhk8a0WedgMBQ&X-Amz-Signature=4938ffcd090d868745edd034dc7d5d20e25734bb0908dbf8089dd2623376eaf4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
