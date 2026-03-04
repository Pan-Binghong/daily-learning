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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FD4VMZI%2F20260304%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260304T032705Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCbhLcnL4X68m8BaT%2Ba0tfqclPah17Y0M2BjUV1toSJFAIhAK1%2BH%2B1O4Uj2nc5SKN%2FdbZv3HTAinVGSq7cR3imfiI1QKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxrJ3vNoJqbxIe1xVsq3AMW8bgGlg1%2BAR4Bc0x%2BClZi2X5xYtQci5r1RNfXIAS%2BlxJcp%2Fi%2ByCcuN%2Fyd7lXiFSWXrPMA7XQbXRpDskomeubyR3%2FqY%2FIBwsiNt25k0VW1FKj7c9ekPimUHX9mg9%2FXewTka6PD%2FefB%2FNgMCdAdh9HUDOJm9jl%2FWMWcuH1kdFQJF3nwU1PkuNqomngLEt2qsf4PAncrf69S06n8XnDmFwFUahhsbtHbQDGy7SUxNmu%2BVCCkFkQbuNML46YtPcdeUVrD76QWzP2UxlIFa7DBjv%2BpjnZEYMYQ%2BRuJXz1FqdvPhqZHqp1NbyvQ55wg4P2MAvy7fztwrpvLhFD%2FEDYOI3njUhYB6meU1WCWfZp9LbtAc88AMLlObzgddheA7Qn2nCGkX%2B6bqsev3sksUyCeMZ5hSzQBEfwQoHnNJt3VrB6NRL%2Bco0SzXTK2GHDDRzM%2BTtXLwP25CpN3ftY5lIPhD5GIaacF0bbB%2Ff0smAu9cu%2FRgirbIncP9Oq1Kc3KQAiR983o61%2F%2FDlZ1JXcO0EldhPziUBSrwQrn0%2FOSz3ijJIH2WP6veRz8TXZZh0MhvbGCfCk8aho96dcYuVrDWMygnaNgz4RZWfIoF1ceFoAZ5SQU%2BuI2qZzn6NKZ9CBEbTCWmJ7NBjqkAQUHYjTZbGcqwP6xGV5bvxbZhBVtojo4ALzf%2FXuMPsaBBSh4SnAurGFeQSdlZBayjme4NRh8EHi1BefiGnOpx5vhoGEODQlu%2BUw9TFFn4AAxCpyr0OLE4Qe4WOZiWmt7UfGGsCBWmymmk7DYcqvNfQZ6nRtZs8c63K%2BVZeERF3myk6V%2FvJDw8LKjrESOUcPb%2Fe2uQxickyBzMeygs6p9l2ebEbFU&X-Amz-Signature=e6474d999a66a87370375502907ea6c554ecd6f9ea64d32ad6ef78b5d0fcc130&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
