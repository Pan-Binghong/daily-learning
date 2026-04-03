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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJTBVL7V%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T063430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGuI%2F6MoqoTgpRa2XwVAiXxtj7Xk4OyIfK%2FAKhVr1ciQIhAJjydiuXL4P169tfk3WyOdkaWhYj08QqGCbNuQGgBZHjKv8DCH8QABoMNjM3NDIzMTgzODA1IgyYorQWH9BczGdndxEq3APNkRa3Jwfz22h9nshq5IB%2BZmtt%2Fn2OzQKlNDSH0icuXuNtRPUcNLPWM%2BB8wHEz3Pa6QsswVwSozgVTdMc5X%2F4CMt86BICbYbmu%2BaEU3purXnHBhJX6SHQfAainrZqnryAbzmse%2BvqYdGNyLvEZ%2FroQw5NL6ToDlCnqh%2BgdEMNKlzo4KF0gXeSpUgAw8GVbuyo%2FeQE1OyS%2FwkILfMczZILn7MBNQ7%2FzoYvzlGG6bpMcgrtg7Wnb8cBYo%2BgJA2qgdQJAYehxjOD8faEmnbna5BOWxVeTkcxsF3kPd6ojOBkg0pD%2FMmYHGP2GFqfQ3%2Be8e3nYmx3ha6MlbnqhHY5AI21Whd9NITY8TLfJGxgAIHfkwKfhajCOCfvq%2FR5KY9%2BzLEvtk2EL2xtOtiQyh3UmG3iRmkk1oeSuqPkFLRkwCvuzNxVneWiA7r7VyDHClS4ttPSp%2FNZiGJDej%2FRfl49mIcIzEgvVSY%2BHrayr56tGiLUavP0KasA%2F6Jv4Goj1a%2FVe2HG1HOXlp5YoDmdnFHGXboMhIi2IgELeaoRKC%2F8ikSaoQVOUxeoeFFLwViM7ZGlEngAccmiDLTT8jRLDDU%2BJIUCdGs599PTVdQikLBFB1QgsEOwP53PM%2BAO7ck56pzDDrL3OBjqkAZzknpqnyMM9FOAlL0ouyvz3V9vWnPKf1eK%2BCunifJa2LgnIfVbOZTFRNtsl9hyAzsUfyj0Rt%2Bo1C1%2F1xksXBr8%2BHwX24XoFYUaLxzLVWgnt5mVbyjEaZGxBlt48HX2kiPaH8pyN3mwzcf8jvYtYVqLjH0PgTDeXPPh1RlNRCh38U6fc2LQ%2FGc2tysTsVU%2BPXM%2FtAakvdGRxgyyTc2OD48o6bOP%2F&X-Amz-Signature=687a20040a4e0fe86fbbec91b48d12afe115657d00e32706b1a57b4e9cf73d65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
