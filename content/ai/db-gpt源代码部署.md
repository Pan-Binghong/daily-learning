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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QL4W6NUZ%2F20260324%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260324T033630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDmvEC7Ve%2FwWCbViLenqW6hj2F93UsEZR3uImF%2BX1LB5wIgdTGGwfMGT0m%2BxZ9X8O5lePjk68pnldjiYzPZaoTpfokqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC4JhLuUpGJToyw94yrcA4xGXwaRWWlpS8BMMyUtzGXC63Z97wl3Kh3%2BAtBIsqpScc0NmvSBguw9moziCFoSLJqK8q0AkuNQDiD3kpKFo50w1MNOzOMypBisFYyE7bxol8ZPETQO0sGhKvIKnOqazRawr5D5usicAeZkfL418YFBSiExnYy9BPsftWmUzgu2S20T4JGIQ9bE5E1iXvQ4GQ98JBcb3r7DcA5F%2Bq926opyCQj6uxq5yijN0V93cUCElv%2BV0Ap%2FM65IWfGfdXPDP4iBFcIXnr3CRBW9afl2h7FayJCKzxfLAsgNctbnxV1vB43FENdHtszj2BQ6mPSmaAnmxkOY2xSo0NLUrOGIqD%2Be6dCdCMFzyLisDZN6Fa9%2BZjHx6e%2BXEwxWpZPN0l2UX1RBGqCm%2BPrtJaFtLqFfCaTsqXGJMZmAR2wN5YuCFkQIJ%2FTHjJhJV1fzgPezFWyyZIx8IAGNAr0KVpVhy3XuhIf1RFM0gLwC%2F%2FA9D1oE%2FsZwVWOinIhbXGFO31qd7ZNo94YE5%2FNwDozH8VlypxJd21ealwFLyOTXnG8oxRe4Y1rdn5ONH%2F2XuP4B4KJzdcHlf0KIKXWDBIQb0DeexTuznkjc9s9tjBxKIft2zaYY4hG6mzAFIDNHXI9kPi5EMP3yh84GOqUBD8%2B5D6A8b%2F0O3TkRxxtAN3LHaRqAS1pz8GjPr%2Bn8eRZHJ9qk6DGjo%2FafzHLuWo5EZ4YUbilGnth7hG3Dudoy6wZBuQE2dB4EkXkL64mVtgAUSiSzIVFItDmbjI%2FaqIpkMjdvSPbcdMZ5xEPfxVNRE6zzyMcopZSd6PffAGUr21Ts0Na21z9VOaOHYGOzABFGdiv6zD0EtLOvyZoIqN1S%2FdsDaPlt&X-Amz-Signature=ecee41aaf412cf75d782703174cd4c6ca1ba2f4ec8e34ffd3cfb27b01ed41f82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
