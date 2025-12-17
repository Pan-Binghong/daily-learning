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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJLE24MC%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvN9ch7k4G0LS9yYAPmanVFfhluZsjebKvCzdQeldW6AiAfSi70hBSmjfQZAHWJmUyLvKM8pXsQERkT3eqSmvjrNCr%2FAwh0EAAaDDYzNzQyMzE4MzgwNSIMFH5Ug%2F11KZQp%2F%2BODKtwD6CLN95a%2FJz37PESQoDqCEyAhjqZiExZgCjwb9MZIFFNXeJKXer7xnFcDGFCfryVvwMsssZcFy%2FC%2BIlse7xipm57JKuZwySue7fNIiUEs7pkUPx5typdYlI%2FgND980ioJgB8dKB91a64cD5MrWgwwNr08wfXHD4XIEpLASQnG0YD0FR%2FIh4TJbqGvh7JuR8THVbe%2BE7BZf9EmsakDREjHFTNu8UAQBngWvvN0GoPecVTsHaJZ7tIlOTz6%2BjcdK4NDVHDQ2%2BqMnxeQUfNkfTbfZwCt1J8ONh6tZrnn0ZJ5NZuNUHI0%2Bc%2BflQ4ClJapDhNAtt0eB%2FuwPYgbAvGA6NDjvLaUJmDgA%2FpwzbD7Mxs983yDwbz6Ab3M3d6N8losM5CxSgVdVmsOyqMm85Nef0ffGSYcECW3HAdxtLbkgWZP8SIi3hX34ZM%2Fv%2F89DWaiw2Lu26%2BAHhXYgmjTgwi4TpL0ch8RYrLFCAM6abXIt3GNjiWclC08i%2B77%2BCNojlOO2wxc9IAtSTZGE2PBqpnUF2SXgNVtiFmPCAF49UEcSRQxBVMs4pId0n1kJCR7OWBWwgfNCgr%2B2bFTbxurJqGkgT2eJ%2BRFeUvnOYM10euZ9PhHpUKIOmvPn3JiyUINtUswirKIygY6pgE%2B%2BCmFKZ0K2qhXYvYHSQ0Nnz85vUDWeNy3YiTKzKLXNY8dEUBnRNJN6hu3CHNYGOQLS9y7OFfMeblDUd1yCCF58C4%2FnvPizuTC%2FA8gPc%2FR8xVvO381VduLUe27W5llh14wxcv%2Fh0yij5Lf%2BsIb%2FLwVWdGQ63UrpA6lYXz6bN2YPsxzqAZEpVyuPfJpKcVO8iMyIA3N6%2BO69SS06Y1n8%2F0I0FezBi0L&X-Amz-Signature=4bfc4cface03b59d24d279a9102ce7aaac82f86c1d32c21c30c13303fa94471c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
