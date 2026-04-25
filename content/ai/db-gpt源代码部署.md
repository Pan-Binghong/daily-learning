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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XYQQCYB%2F20260425%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260425T035312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwwAThTAe7OUuK9COteCpesd%2FVnGg%2BzX%2FhuKRZTx9UGgIgN7qdRe9aPuof21IIwlqHLxWB2SLu%2B%2F8XD1d3FAR2mjUqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEQG5kIRT2ANg7eSSrcAxcxDXfIsk%2BdFNqgUbFV9cDu%2FUdIWGZ7%2FXiwKP3UbKRfFCCTaKqB%2Bxa0iq7W1WQDV9X5BsgVjX%2FS7m7JyHdxEab1zxdBeYfIesQUpnoluLV8q9oZ8M9jJNNJEd4JQTVOeF3QoXtgNCm0HT2IudrsMSvBtk1sQKXtnEOp5pyoXW8ABtA9pHaDzBU%2BpkTDqxeESvH7Var7Ax9Yu1Y%2B%2FMoMg70ZfaBoV4%2FBO2g8H9E6fIZJz%2B6gmcCORhC4du0cUtORpGTGzkahu%2FDZtC2RngTfL5sjNcYe%2BpqcxPpGQtI5M%2B4WZjx9qIIm0LMHdrKyv8FuE3NrGvO4qxAhnXRcx5IV34SxXgp67DVhZfP8iHgl%2BYjOkiZ7S%2BX51KC7zwdtVMCDwSU13IZAgwSxNR3xcsgDxOYwezcZuClg%2B7mEJ9KjKvqpUCBb%2B2nFvOiSWlyi8NUhsCkjUYBjCTmdRqfSKsz2M1X7W1PRmRpnVw1Xuqkz24%2F9yf1awGVPfVnP5zmjZQMmcBwm8TWcegiFt%2BdAAiIj05AsoLX%2FGeOxaMGkb4Ip9eBPVyEfriH5aqIs8GZF7fTZihfhAcKY482x2P74LQPNyouLEvKeifbQNOvKhyvmNFhFauA4LzjBYcja3%2B7VMKHxsM8GOqUBhrwR02BlQj1KtPoO5Ah9FXkaHBPZLbvpqiXXsNilvNwNzZJLsMSSqkNVLGDJO0xJQE5nTKL5Wqw6lHY7ZRUT%2BFMc2qVNNFxh9O3lqAkvmv4WU6H6p2HX9CkBjUg%2Fl1NLU1kGQN%2FBhz0%2B7oR0TsAMNDqmkNqIUFrQ5OKvY7Mt7jprgM7uE8V55BuN3g58ykKRomYoKEu8WAGxEcBNVCId1CUjCu0h&X-Amz-Signature=52c99f2146d6b6ae0c14a78ea2be5299bf2bdbebaf5e29e5dca54c001730f97c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
