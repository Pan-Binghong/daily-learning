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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVXCAMI2%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQCvFnE%2BhKePeB84RpiaHT%2ByelsiEYLcoVm1o4N5HIGWzgIgSUSGLPSFQUqopmLN6NOmeEK%2F2UW8U2GgNQ46c2xYDW4qiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIqUaMXOh2eUhcroaCrcAwP1IRX2nuOa4cv6y3vfmiq%2BgHyWKTnDvbPmfyh9eGsKlQ2BXi3q%2FKMfhj3q632Ykn%2FesNuigbipFqXFKF0swuNwZVok2O4Xl0yBq5lLKNUTI1CCyoEH1sVjPfvtX1LpA%2B2ujRexgkhVdeVEBFBYODUY5Uq%2BZMzpIzP7%2FenLRThaLJOYAvngbqMWwDpWWx2qu71Uv6%2BmLfM4dLT9nkF%2FzI0mXEramUaTdBD9yUFOunkiBlHNxH2apf3%2FmWEi0oS7Nq0xnD%2FqICXt8udYAmwag5eQd4QwHN2ZQr3bBk%2BLfmyW%2FzZ9bn6akXQBv6l2fOIbHEetMOliowlnfQC1v0epLLXBDM2jWMJ7hxVpwL057kVmyMafaFRlLRlShfUjGuVbJch5BtMvhqG1IMVWOpHHiiWV1NK9GLzwdij7JIk5KWYVI85FvYuQeTUWYRPZK4vYngljj%2BHlL6DRdN2T%2By%2FSsYrpFH%2BrORb9YuFsNrKdGQZn%2Fcjs6rt%2BZPswH9ALsBPddDqYymj4YmN%2FuzRpblFE0qpa6bhpHtkZSthfjF%2BXvq5LbIB7%2BbLL8ctNPg8lw70TlsKwTuhC3ojK1YMe3EdvYrOrahYCNFI9mv%2Fm499S5resmghdaF4qqNDtk3YvMPDxls4GOqUBELLiN4FUNHXJgiOzYoGXxWHgRMCpxhGRdmshcNsbzTEjtH64BsXIrKbdVanWoScY2JSIea6O7nYu0c8wFyvDZJOSNUxsahbiypdFMJMXli7CH%2FrtBwKhHYnZubW0srhD9hSE6f2Ol490KrPljGhgqeGbGu8pHEtHtFv%2BKVYDp8N%2F9z224zky4tWR7cJFBRa0Z6Bm61GRtTUz1ZveRHQxsfgN8Bns&X-Amz-Signature=d3e14571eeb77b548c3b404102b3dfaac8ed055c17dc2f633e5ed025650ee6c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
