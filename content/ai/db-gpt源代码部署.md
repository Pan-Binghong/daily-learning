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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ5B3O4F%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQD7XEIwuYzhr7S1dcVPNB20uDwJyiaWUpTfdvvD22iSbgIhAMKpGsSj04ZmW3gHXVQ5AYl5pnVllUmnf7hZp%2B%2Bmzp81KogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igys79qvvKAocZAReNYq3ANsgI5pG4XxvUrQGy80oOUqm4CKN6YPd2KIiny%2BpMIsGpktZYAx0AxlXDZg8OWkP%2B%2FeO4U8czsMcQLFlUItZ04pnPmGH1py2wMDLxzYC35iQEkvDq6Kk3ooEZ5W%2FGXVuBu%2FfZonYEaoGOQIVFjZAcFBwrQBn9uU6XD22UMC3fvciKTr7kAlE6Z%2BXY3DUjoCXPwfVfzy4w4OK2Poe3rYO4D5PqdMVwt%2B00wIHhrGrLozexgsidU%2Bd0%2FTdPvAInN%2Bl6eLnD4Xe%2Fn%2FC43vU0EE3ia8so0Oke0vWLJcGrAeG6BF8gm%2FksobHuCQXGO9dXWzJLXfSD%2B0DUZSBfoBit%2FCbyHXuzy6n0aYdoxm9nkUBD7%2FeTPcUWLBQojNdJgqaTY67m5%2B%2F%2FsE0llDxxpS%2FBcPi%2BXflvSFXRvYcEZXj20iDSjvhbIoIbL4yLFrO%2FpkI62OCaLVMM1RscEErzIae%2B2%2B72L2s9Jm49Ydfc4F%2FuXvJ07P3o1M4kkppyOtbSTt3RNysXMXKzzaElmSQ2gXZ0AlLf6sfmQQcPNmBBVYMKlxfkZWyj3DCIriWBaHLCKNZ3nqbcN%2FNlE2GybF23cXvwA2H7tzZB6TulZR6348PChr%2FtaoDBhHLaBy7Oydr3ZtvzCyrsvLBjqkAaheg2yuRZh049XUOXgQ5%2FBP6HuYGHzVbl3hC7MlZMDesqRKNaM%2BovwRiME%2BBA8bJOEhwqF%2FKzSQQsxpLooKXR9IRIdcv3OicYUyYWMjpdt7%2FXGgTBbEIX9x0y%2BKSzgpDYw0Np6QsfqjqzKtzcPW8ArW2PkQ38ncNIp9viBtlIk3FgaofwCCaDl4oT4Y4k3niA3d5OXmW6rcOHIsUDnM7U5XDGqW&X-Amz-Signature=0440b531e823ffd94d4e5fb4a39a2661e399cfa2b056b19fbf170e9807821ab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
