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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VXQXK5L%2F20260128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260128T030431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOXUEW5s%2Fc0NzKx%2F3c7VDEbYR0VX8rIv92uPPHE4k5bQIhAMco6m%2B4cQo%2BmoXoZOvGltFJKXn24wY%2FEYvFxDPfXq6fKv8DCGEQABoMNjM3NDIzMTgzODA1IgzVT%2BLq%2BKvwaZjW9%2Fsq3APZqWzZaVSOzcC%2BUcMWqh8CWLx9opNlM8feU%2BKI%2FQmCF2pbdkQE3u9SN%2BgjZuq6riWDM7sssfYrvnPnfbJJMjYRNOlATwRAWcGyndG%2FjVd9zjEV8fSEEwJA2ScYhPPbUxMzRlt9wSCz6un9X87KjBGPW5oRPRL2RryhcLncX3NEi6fZbnk67%2BInBxXL9wRBGKViA0eSXGqEtUXJ8TEsdzYfQUoHnoMx%2BuRjMBTJAknfQH%2BAvEjsViTI6sA6n4Qw4%2F%2FSy5tdPjS0SJmNUoeRPAqzADs6SZ%2BURZ9dNpwe360uL9Pn3iHKyrGcI%2F7T0UyyD9yS85siJilLCyecR49SJbqvaXAWGtDmVj3a%2BvicyKL%2FBTgKECsUwVVwt3hXxFgPJPDQP3%2FsNi8m0GLWfg7RMjSWphzW5UNTsa%2BlqpCjd1G8jxf9Z9ZzqbnpaHVyLRqaZ3X%2FwVc5rQxGrABwJj6yhhiuTqZiV01YH2Ex4U6aXTszDXjwv%2F7iiK%2F40zmoVMcEYZhFi5qCVuEe3MYg5MZgKBzJ4VtToPSsyHJ0xFu0VPvAx5E02W%2Fp1NY0lZtijBZ%2F6yr9956tf0L3ic1Bc%2BXz84OdN8Edcq%2Bnhy0hK1LsCFi%2BLM3C0Wus6OPpq7h3XzCGluXLBjqkAQAC3DAFdjK2wQAamkzZTJEHs0NaNlrEEAn1ewJlIRNv4MGZciS0uc9m9pRE7Q5dakV3WVglH9UxCAAQ7bakUkkpILNjmKZ%2Bp%2BFDL4oytfmv%2Fgu%2FFJuYuOIftIasOHKbiUrBmZKKkmPDK1PexOgO1YmR5cjyz2ZnSgNuEBZYH9TME2bP6IrbTNPkyYslaYRelJioHqmXvIXUH%2BuCnflg6F7bWZzS&X-Amz-Signature=a6de875c73c9f6337127f44d4e2bb69fcbeec9f665a6e658ea9a61b3d7e8af6c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
