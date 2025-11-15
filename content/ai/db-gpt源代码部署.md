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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URLYDMUU%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsrxfsiIc4S%2FEEPWU0y3lOBVp3OOX%2Fw%2B5DRHYP8ajb5QIhALN96U4xLXeZkGTj4Npe3sEIvnDfBLaswLnIzaTPL6uFKv8DCHMQABoMNjM3NDIzMTgzODA1Igw%2BtMnyEvAw5NywchUq3APmX4YH3%2F1bp9%2FmHkzBdCcm%2FxJvAy2Zu2YJrM4aBxVJqDyom%2BWKNuJeBnW%2FGKTG83koDOyoYe5nv0KwoyIurRczi1WzhxiBMcwicdW8HQZz57DPC2DN6KwzqNtTQZXfFjU%2FTqfQjMKaHIekq4dooFwGUIJ%2FWiQr52dNUNZhThUqyE0B7Z3PHWwwvYRsruUcqP%2FSzQjUxTrmK1i4epRaFlYe1Kfvx2jrdce8mx3WmGWweTvRjGewCcy6OFhB8uv6w7DKOODzz5X6sC3J48IUjMW8pOJzySpOjYrEh%2FN6ylU%2BtbPCZXuWS2JuvJg3NZPay33rppnMbBmG67Djr6RgqpDlDw%2B6uHDVLxO0U5SGDhiEp0YYkYvHsu%2FwhkgCT%2BIkwIK%2BkE35X2v8Ph2LRsOrjlqR6LyFyIUuHEEJVSy1ATCc8VsSB%2FsNpOD6QIbE8VeCd%2Fj4TkrKMyof3nJPYtjGmJXoKQMucOknq9XJz%2FQgUy3K0uCiuGv4dd%2Fk3fn5LEfE2m76Z7V80KNSLbGypwRwZN9lCv1KOmK16rIgekNIB1w4tQb%2BEXGQC3PtTZlvlVWwbg8H%2FJspe4YCE5QDwKGk1H4qPLz3SxqRAFaPERDEkyldUG6fnphoo%2FrxIojukDCdwN%2FIBjqkAVLgKXgE3%2B0wNVgLw9THEc19v%2BJI21uOJcH14bu62%2B70kWdFULvtSqpFmQfrsfw0qJytv0N%2F7XgffPCu%2B5rwwtybiiYqRl40WrxYN7FxWrAnwo3%2FNcfr25JV5kJGIllHTqpVAxFyyBT9HoZbhrFQ%2FVy2sPl1tBADi9Mc4mAWBAY9fWqdd6R%2F4T59NTcU9ZsqD2uJiwpxpvuYXu9nXnQ7B5UehEWg&X-Amz-Signature=0c000fb0d63bede9d4dc7990503e61f6e47b6e8c6aa5897aae3ce0079b01e5b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
