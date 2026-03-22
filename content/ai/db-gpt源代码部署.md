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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3UYCE5Z%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034028Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCumGXsdJQXfezDJ6QZAYo9LuVYfvXUJqPUul3AEvsD3AIhAJkRNfLyLwuiyrQykBTsVxzyMpFuZnATe5dw9f73nCBQKv8DCFwQABoMNjM3NDIzMTgzODA1IgwJ1Q82kndLFqwmVyYq3AO4YtItVdZSw1N%2BuMc30kMMQqsauRs1mCKu%2FR8p3FkN6NJx8a8kugH3wERwuylcmRxQXyJVQLrWiv7oz4EuVNo8GD0wCIoDiXmt0bDF07DaG4wCknPHZV8hRS3VUrvbnTgoqYnK%2BfLIpbm0LL4FWONqU4lS%2FdtOcjkdw42%2BjXEZ%2BSFyuNXi5cHoMDYJSksM2GWOLx9grIc2ZEr0O0Kpup3kXZK2ND%2B6E6CI59PLkVwn0AVLUUO6NiQV2ckwHXtfav89ZhxNZca3174eZqFkjXXJaK8CnxVyqK2SDGPPvboPk9bP43BkZXhdRgKHDqHJCEvRGmHyaaZIUbqkCKrRMGo6efF3HK2b1Z2WPyzHuKtIoTr9BofN5GEWXYx9QYno4MVVNbknffYkVA%2BxG6N6vf52R1CJXICeMqt4%2BmpxFzjKA6gx8BiqCYip68YsXKpy1%2B3iA5Ld4ol8T6TAOdg9cNWDcghs4Th1R1MXAa9tXmyHnwEhCNi%2BSTXNpll9DbZTB9cSUUPiRmhVvCBWfmMmz0sWXGNAMr1Bp9oIF8TuX7H7C2eRii99kURuf45AcrvRQJNLL6ky18dx8G3%2Fr17hK7%2BaFBz6mYfkIKoBjZ9XEKO4yz5twvclL2f9cyRC7DCmrP3NBjqkAZUl9UCUIA9K3pcu7CraQJ2RAt3uPbJaFf6WIt8Z0nM48v3BitouRL6HmUWbT7PG6geq3L7s0Spnn5IKCHZQQqzRjoPn1CGCeBFaJbmObgVyZAXLYWyg8sKRLLfdR5RDCcy2I%2B1nmgv1MruBVJjprvHiYKbRckWe2x9kuKRrIoMX3rj92QHwORMZReDRfyi2veXtZ7dGcAyb0%2Bq1qTobF5H8FvuY&X-Amz-Signature=5a5dc3b0c4d4360c18665de4820c3e8231468f9e160f8cfe6373197fb5a609b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
