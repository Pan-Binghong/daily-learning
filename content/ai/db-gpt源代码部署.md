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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7267GTG%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC9wkw2FPW4o5dDCDAA461jMCI%2Bt0Fe3Y0Cc3%2BSy%2B%2F3LwIgFhz07lXdU%2BgmQQeWwmqMggM7vqkJG5EYQYHf1QHYcW4q%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDKwLF3%2FWDzqDAZwzaCrcA2VRts3E%2FiUndNambp497iSkRo2CsXA%2FkKY4G7oSz6xnkx92yeU8yC4okO2GwafHjz7qKSr2ozMk106MhuQPcNpSl02Ts006I8X1J8qbWqoD3fW8qfMTz4yyhhDTzaH5hPmsk2blQ9U7pYR%2BHDKR5VdPe8%2FTPI4fh9QgGcZt3gu0Oy%2Fj3F4KXFlefWrfUbzJl7XBouo2vzUCxDz7Kqm40ilIa%2FoxHFPCkxrULWNzAPVNaMlJKfDt8s7rp39lmOd5YZ1gpHFrlSR8a7%2FQ6VfeZKJMn6jPEAHbKug2PRwG%2Bylax9O0%2FP31aoyw8ksD6mGey6iA%2Bs7dUqad22PWuHABi4wqqdYe1azif6n4krEwHJZy5fNF9s%2BsGWP%2B6ps1Dzbi4JYIvyeCxGUCBkVSH9vuC45C2MY7bFca5RTcVgj3ViqgbHLXAjpbCN0xSWtYptZ0i8lpPTfOkQaIG39Fm44ObrfyiKsQQ%2BydOK78jz3qtNNXR9zoOBE5MWT0co5Wr2u8UkJ6SZDgs7b1z5E9vU%2Br%2BSNAU6D%2F5933IlJFx%2BHcPDx%2FeBBiAeTU0W1ghl6BUVcBzzjNmTHlErx5OBbFP%2FHg8o7BZ%2FBn6La%2Fp0gBYEYYr%2BiZxFwfTH5giq41zn9yMKuuvc4GOqUBLQWC%2B%2FEz4Ka%2Fg3Dj8k%2F6EQmtp8FqEdGxbsOx3bswUMkwyAaHSSkigsb5hTmo0LGCmfigfXlrT8vurzOVkmo1tjtMQaiUdIbuqZ1C6%2FEQwhBAUc1PHD2W%2BBCLiUzjgoaQfOJrzKsXodTTob5AJh%2BolrOjd1c4NQsZ5Rv68FykcKD%2Fl3bo5U%2BNVdZiSJbM18ya99I0OjqcBubSjkeKk692QDSqwLti&X-Amz-Signature=d1cf2ffcb4b8a4dffac13209106240454f9600b1cc4dbf4a8bfd04fae61d4a35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
