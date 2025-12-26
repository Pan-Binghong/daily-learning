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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK6TFFYW%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYHvL%2FoXRhQIqqzvaiVJWTEZMqQo%2BQ%2BYrxU2%2FmuI1AsgIgJtpHbvX0QGG07jD6qWUKahPIU6iykME9P3STljRVI7Mq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDKN29pOcsU%2BWL9MsIyrcAxCYV%2BQnOdEP%2FtQlxKIbpU5sP919KD%2BzTvC7o4yIFaL8SyZfcZNEP567487HnwA2K7HFurkWSLWFj6WG8au6EB0497eUpcj5cs3MQBLRPJTHoV6ldZMDEWVi0Spapwt2lh05535wqavqGN5f7cHYA51BFqZXXQnWl%2Bq%2B1RD%2FqObqsK%2BiCbtNVE4luLiRU%2BvQ%2F6wDM1FmI0ZST2pCdK7coLVTXuVCuWrS2BQHniiE9sKPdSsBGVzWEZN%2BIU19OZaLb4y5P%2FHx0OM6QYCZtvVaAD3TmmqGPLfp6A5m0wv21hopzsS8OJ6B%2FoB61SDb7ArcTNUJweNt2GeCNc6K%2FNszrUSz9LOzIPzO41uokG5RrRVqwPGDkS%2BXzWRbtkgA0uhzg6fvstFAJx50%2BTpx8wK3abpGxgFgIMHQGXUTvI9JVoNyD5RMOTNiXwzSZE%2BaJbM%2FXAZMS3AhWHKrNtfG4EaUfOxyRGJBvpdnx2lrG4mqJpI40TnXSj5E5eIDzuuVL%2Bgk2s5DqmxsdVj1Nd3s%2BhhBSMHSr2PyZrZzwNfV4OPjxCmUoN%2FkXjjxKsU6J4W4oaF6QXCcja9TtmKJ03Ra%2BPgs7qobWoCGYwTkx%2FKWzE5v9a0yLfALsZp168jWabecMIvWt8oGOqUBWy%2FOqShC%2BQPQrIftaqdUkQ%2F3yhLDcr093VyXHXyjEswV10zLztoRV%2F96k7FHhFLjB3NO0Xfl%2BnrEyiPSsnQPeNTO3z1fWl58Kyvvwp%2BszZaCHjY57WK%2BqFgLqXTdc3YbzT%2FcdtR0gpXKcsqpLFnXdZwdwGnhgve6UYUPiAfuaOE1j1DTlXVAHjIvLKSj%2FfxT%2FU%2B2TFneZcgsn0T930Z6arJCg0ej&X-Amz-Signature=cf0111072cd5a85f5632ba650a9915f0a2aca8dfa3026fd3f5f37a3f48370d8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
