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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I3WAIOA%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHeFxJrEh4Sn2I0JN7yukJn8Eb%2FhSCoAX5UpjBS7k2uQAiBSF1YpfjjdulZ6YnkfrNV18qTN0MqgDm%2BceaP%2BblJfwCqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyY8Sc5X7lGzAUr3CKtwDHDuVKgXJGp8D92BSClB%2FQXK37vs7HKdVcD2xb%2F6Tm9g6%2FODf3H3ILyTohFxJmhBqgXJfLpSsQFFP4kkKTC6JRxRE0Fi1xt3tyFSyfsFH%2FBqgXGsJJR0yFw7cE65C6U40un8S9oESwEq4r2V4lPpbaupoYbK1%2BWPY62e0TtKB%2BeYDSSgw77%2BvHW7sz4p0RJX8AR722MPDKA%2B%2BglBkeYwe%2Fj%2BlfkyxqVh7sxLY0rs53V2YUxocOy7lqaHW21kBI1oBwlN59ORD%2BuhP2hxoNj2cu4F0kEd8lCZYZXtChSy2JhW%2B920HrXyNlnYO1aRetOgfFR2pvzXpdwNyW9UwlT7GC3rH9Zh7YUe7rN9AdnayViUkdYxXDxisWjKMX0RPyF60acFMLvkilT6i8YIAZwPpb0XxXc%2FQY212an%2BF9pk9cVOfKJKwwi1o17A60RBRwFN5p%2FlbHGSE5ViPwf008lz5Bv2Wf3kHNW24%2BrldCKu1nMCCc482L8az9gV68IaYCI1TaEhtbwRi4dmjbVgQ6M14pi8titgpgXGIvOaD6gjKeAMqpXIyG4IeKd4fefBlb4aWJTFm4017JbtrJAshIRriveh8Ii1LA9OEbahXKTF%2BBAAeDe5F63%2FYM2DCdaUwqZelzAY6pgFuHwQO8zlhcUdA%2F6MERavCKfFpSTdWFx2ErSmT37GW0a3I8NS7RVkXSTkVLFJ5SaVYa36X6pxbjrgvrX0XAYHxC0qUlZNoLrZKNyXPKkfODepI5YniqEU0hn3FBAakpTa94ljM47rxJi1cXyjERdasWE%2FeHyQ84e%2BJ6u51%2BVPIw2j%2FHzH0mH%2FPX7QMMeg5h3tAeht3Gi2lzCLmYOn8z5whPFF5vwRU&X-Amz-Signature=be2a100466f96af7b6279cd7b3bcdef05891fcc6c09654b1a47368f9c5123e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
