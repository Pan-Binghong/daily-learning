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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTUAK2PZ%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFTsGkI7%2FsDQO1RNQWU4I3wM2E7t%2FxVOuieNpaU8ijjwAiAT4MeFfUA64o1gvWZUK1zHoZvgBkwG97sYyahx21nOrCr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIMi%2FpoFqUBm8psqKvJKtwDiOFG%2BcRNhjDgb2EiEkrYU4lPv0y9SPmr36kfY7L5HZNjphxmwJV8JF3SfjWHEq2IT%2BFk2Lh3cWHZmkGMYQIP4zIeVznKDsrO7M2Hlnktj2DHJwkBlCpMf8BFZURrAieeAXpu0khXQccdRH5X1r3ufL%2BkmXDH3Jzp%2BPfTKJ%2Fz1owTkDw6tTiN8vH7u1VUzQ5vbJx9wD5riU3dscLHcKur0jPwQNAdOh%2FV8KuJ1F6hJghftpxecz5lAXuqXZFFvWPw6BovsyICM%2FIVTk4kZEheYHyq%2BUWRFVPcxoRHiX8Buuc%2FOOieh6oisW1idR9YH8c55ZSSageFdTcqHPs2H4FLY49vD8OrkoJzNjapIIdKSiDMOzIdcTBuNe1FY873njVNFrwbkMzGoU1Ku%2BNIyoJIvPxnkl0nNm7fqS3Fn4JIYz7b0Tijh9RNtair9dbtWkGAbwqPuR9N96bG2noc5HvFNhdlLwg1Lz%2FLsql%2BJz5Tknmu04oLXYXW%2FcGhA%2Bgrj25mTmUq8EUAwliv%2B8mASRJ6pkaGTmy8xMzVh8ZHu8F3cNYKC0LK0rWlvw6XF%2B5EI5YCcmitZax9i8bgqCtoxkoXUtf%2FYaL%2F0RPbh0N74k9mxL2gga7GLicKeDg3VoUw8PmgzwY6pgFpPH3SOoSN0g3Z%2FS9gRgXpbGdQm7GZVTXk83FnnBwkvXawUvB%2Frs3G%2FJV9ULnWxjYrQrTGXWpbhQ9bud4ibxO4Ypez8NYuIsFTaJTNeaWyakkVWe7N4CvIqpNgcYD7iWXn4k2ms3%2FGU4Wykw%2FskQ0pU8CdBeMQNXaQJoU9pN1hhvrQKROLxMk8bcImu9M5VF0Vh7nCtT0zuOjOypduAcMgwN587nid&X-Amz-Signature=2af1f52af2153b3a9632537f1fb02f31621d50fb94d3e911db42e25d6896c992&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
