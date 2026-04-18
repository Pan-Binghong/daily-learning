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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IK6MBFK%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJHMEUCIQDvDSKLi6%2BJRPtZuoOBmQRSJgqizRYR35gBLjd3DEVA8wIgT1seONepI4c7AdnOtDIKnsHJx1tBvFEF7Vxs7HIXopYqiAQI4v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAOGFwjUa15Sq4nAkSrcA8cQNpvPLtX5T7ApAkAYbU51HByPug4xDw4qyo6GpbTJygMApHk6zCU7uQgoJ9%2BAk6QiFQ8im28ESGIbVQ9B45c94jGqtGUC0ojyJwuWaWlDFbi3nmTON3zaxJdVg8kXa%2BtKycdsoeaz3USQiMRNZPHe9nkgteIYKwCOwx0nbV%2BsgFDqSvR7s6aQms2CZzD3ErFxXhiBXBKedcPSoILa1poxaFUAwRxudjnOsodHu15%2BdRGnW4gXqzBJC1TZontgyHGRJNl1DfqOI4swkSFL6oVohSI0BwE2LFxmlANo3E1BhIm3oQNYdsNVTdvZVizuVU%2FA23sl7u%2FdXRg8V7CUGcsXAWKFxuJcKoPGFYBVx0T7Jvx28wN50oI4ADDYiThJy5cwYxImSCJN0sH4EcNsZ5IBAjr4iNPhDzKIXuJUAzWWzHSXJdJIANXbp2kD5fuAnL5YeWMh6kKgQu8vw3tr28JWphTTnXE9JLy4irok52ZLw7bnHUs56MiH6%2BlJ5MYWMW3nvEDJJ7MOhJiIIXH%2Fb5PUegFNesfHjie50AmfZJbqW6Kh1a8LOA5gRBxzf0paqWfUV0d2ZODV3QvxohzWu4SLn3ZEucXI1QqZ4UnsNkZwzAMeZjCAMhbo8BWcMJSvi88GOqUBdcfBkA3Q7FYalHyLegDwn16Vi68sT4xUEFoVmF0%2Fce8YrEQxWO4KyRvyvPR8ueTMGn00z9%2FasO0v18eGQZ4yE%2Fgjw95Fe4kYVfYjGUkjGjdSZr7llTh9DWgUqKVDRf%2FUG9Kr0SDscDY9qKNNl64iahk0A0pC5woFddBw4sZRWDBtS8hVjeJcCdzeNf5utHd9CN9jBWji6DnuvuFBgCCjm3IChDn%2B&X-Amz-Signature=91b1406b5bc149f287ba20a3911a9cf02ed16294e4769cc731d9b2fe4dc43b78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
