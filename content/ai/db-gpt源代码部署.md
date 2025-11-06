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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCMSFYEY%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDLDxnzmmG2dr89ZIX9IuAzKjd5NsIDcO4sf1cBLvoNbAiEApQb3kWsLER6kkMU8VKr743dvXzI%2FG6LMVQ9wirvX%2Bh8qiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIuvN%2Fgj%2FL5o%2FQDLZSrcA1IH4YiJIU5Hb%2B8eHhwkYm29R5eVXerbH0XTZYJXsg5DKJpCihDKXJ6YEbFcFUhvEwgupd4qmSpTinqeVdJLjOehL%2FG7U8RPXBIiuB3ZdcxL3y6Azxo6jqPxaid5QE%2F%2BnXZdj%2BnwA2eJ81tXhzmBfRjKBC14AjWuCbLwCQze%2BAKps48AlVjWoccFLHj%2FIm8QOX0nv6Whz1XNk6cJag6Z4Z7xnnk4Bg4ThPa92bEJ7FVa9EBzygj5b3eDEGKC%2BgFZoFLn15I%2BB4ahNKAMdbQiO4SL9h7s43j%2FgYYx8fsZz1uKmqNL29QWmmrUlHV3NXNwHoYi3a5Qs6VlOr3on5Vjfj1NQWqAzpJmSKMRYps2%2BXDvkqdT1gBU%2BtBHLduHCLWFJrjv8i4KihBKYYPx%2B9ICGxlH9E4UxU1lwLK7KlRPr9v%2BBv1L3XMt9QSNqEHVeZ6NtrB9ydwXIG15qIgV0aRGExY6kuQA5cS61JEm4YYDNhK6Hzd31ZKl2rj0E8kjQjwvIaqguyi0ht3prGsr9%2BgMlAE5LZg5%2BXMqID1vPLGHSrM9%2F%2Fbk8UKXlo1yB6YFhc69AFd5KU%2FC1x4ZIl8fn2VNtatr8FO3wxN7xjH1WltJSe9TfjobZEooUxcyYh5cMITyr8gGOqUBLctd0sRL3PTJN%2BHZBSV3HwQIyNYgupNAMTYLeYVNEYqFWEiosXFO8%2BvgCo0KkLrcLYGs5wjAs2VUpxQE8zvs4zP%2Fq6Z6JDN%2BhFMIC427tihfM867d5uLOTWT%2B7eLy4HimIQNTUt1a%2FfINNNKEGREf7wsOwZBTXxvCFjM6ZDM308c4uMku6pnJtGX1E2PKheMCpci3zHCsO3tBs0atg3vuMRR4eoW&X-Amz-Signature=cd163c3b4c5e1389a92a5812c9d7180a4d9e120c994d2517ba0a793ff05b3278&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
