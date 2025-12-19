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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNYH2TPA%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDfn73XB8S9XSgMh4%2FMBQ%2BIcKTDYclnmvAkou0m5dx9ZAiAgffY1wrG4uaQqe5HDv5MwaaVmdOo%2Fbt3FAZDsNVMPASqIBAij%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyMJHw6a1qucSblZKtwDH%2FRMLLIbM7KjxEgLBzJNafNasdvt7pFVMtDKKS2A8VwV46OknHiwsQwPws9kfn7Qi8%2BPx0Or2dOPA32muJHo4cNx5amt2mP38PClk6mZBfYwsZpyTEPab7fh%2FNOgjd75gGhct422fkI4R2Nx%2Bs8FykFJAv8c0O44Hx5xA%2B4nnzRMxvppVchWsdLOeEfY%2FN3i2dmYqTaAq53HRqypG3nx255xW41k0cdHh6mOfpeE49L2w43Qec%2FaUZ29De4Nh6wvh3JnZPurOX11P8Tz%2B8JvRWJKk%2BmV6G%2FV3jnSFsh3fHdQ%2BNfiDjFTNzosJyTXo21bS7qBWV8iBNmf2vxnvIbHJumeewX11DnQmXoAlEaktRZkqV65w4dfRGu%2F3GSBlgBOBoGgSK6O5KY8LsTjjbQCFRJp0am6OX1ofSI%2FLg9hyms%2FN%2FQe5NPMaIbbcA3So0Bb2qdwGnGqUAUGyEO%2BYGSrGN6IAFGQLRGzlcuAOC0Sj1NHDUlDYPTh%2FO8rpAdrDpbmRnNd7U%2FsY4OZaB305Je5HAzuAOEPHtk33MjuHrrtKU0hHSJRzi0RHx%2FpLkN0LR%2F0Va4SN7EI86aRe0%2F%2Fr54d2VtszqAvQbKFqf9SdJvivahBK6Q9dZfg7gUwGuowx%2BGSygY6pgFVxLCiJrXvdMhlJKXToy6JW1%2FYQsjg58%2B%2FKSSNZwuPCwc%2FnLR2Uebxr753rQ2GlMLWmwKHgfJJhOa65%2BekqNZxbgVQdZh%2Fvx%2F%2BaPbVDp164fZfvtmUMDGQrBmuaC2D7HsUAvhVDoZ14FywZHgzcozKQ4CWxgLj1RfVfRt6%2B%2BpD4NDc9nHofWH6UyNYIZSVw10kerFVLiWNpEg8E%2B47NQJbZ8Y7rygS&X-Amz-Signature=72d3f9cb3ea5330f56e729a9a1324c679172dee52aa85080ec7b7fbd49d4d558&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
