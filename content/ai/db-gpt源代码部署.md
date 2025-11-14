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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMLFDEOC%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T024401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICqJYGR05POx7LK4GtZ8tWwV%2FEkI5NnwZ2qlqBw1GYivAiEAuLyc43WHFuXcn1tKZFs52Y8N3PyttDRkMLMFxYpwru8q%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDHEXjBWxSHXrtCyWpCrcA1XAcuOC50Z5VhQsxubjTm4RNSUqjgkzow91i4bjIwUD15fK2rZO%2FSzMFynP6%2F7br0FLaH1w10djf%2BiIYOfzoQ2%2BrqYGr0gci%2B%2FRGmiubuKsAqD8OdqwgiYV80uw%2F3oK40upEn3y4neTMJsWcHxva1IxXFl2bgNbTBrsxSrz4TOuqBlW9u3NJ5jGc5TdT8oKnqY7961qzu%2FyEZpSzo0wGFErayfK4GzjW6dA57fr81API44bcQUavy83sgYKSCAMARF3htrgVATvgGkaoWReV9gsEdGrvKsB2Gudh7MhxLNk%2FQH%2FQMpcFIGLY9JpRoz%2Bx6u5t9fg%2F5aauWfk7tACYBD3Wo3syx3dLfraAaybuDrvNftibCEBzc8zUfGMIiyDxOS8CNDW4lYRkfM90NPsmAzLChN4WSKNeGUVIHZMYaOT2y513WfAv%2Br%2FOOBjK7ZYApsHKtXvjSnj9TR%2BVG4flKHeXgLt%2B5Rmx5BEgkDWYDx0rI7QqRYJ4lWviD7EeakL%2Bj1ojF2dX6NV0Oo6mipLMNrSoqYRSdEO4RC1RTfAdbvo0XuFkaAZbhrBtXC7kjMNRZx78idjF91iNrJ5h%2BuKriPht29eQM9qVt87fBXtaMBZKYU29trxuelOywtNMNSJ2sgGOqUBncjjW%2FQph%2FcbBx5xRSdlPIoGl%2B8LgKq3nalBt1029Id%2B0caZKkOtrRs3Ak4BNWsAqifTvfHkzMZIekjhmhOwU6fzr%2B1Rjb3AsN%2FgEC3WeFMV9yFXxHGWhaqkRFVLSAHQNTSDrNifxyYyr9U74rzw5o3v%2BBTyqDMPmbKkC3pAZyJE4MSzQNV9iTf3MNaQfY%2BueAE8mq20MnaBL%2FD%2BSyqd6A6WYURL&X-Amz-Signature=6232d3c5fcf316a1158d4a71131d6665146893c1d05e44c8085978a34188880d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
