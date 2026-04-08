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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662J52KMXG%2F20260408%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260408T035233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIF15sEQ0vfpxiEKCZ8yf1WH9zL85Z1UMovyjFZSBizchAiAp2wbrhCIv1gOoWTYxGmhAgBIxkLzmGIJ4Cg3M7ydwbCqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMr05X1DmfBo5nCPdRKtwDWwx96mBic21yA2KrygNK14y09zPzHdjAJ1kPDIoIUyOuIM%2Bk54gzk6VXqb0XV%2BVSWGP9ZdHhuAcaWf3TvkRF%2B7boxY7znb9lcXl0k74TxrRQjchjBab4e%2F1ZKVlqnqOebXjTXSEsEAsQOdr08Ta9dr6j%2FymjWlBLuaLtLCstR8WOPtc59FNaAAK1gVn5WQ%2Fyr6MsELaT7Nru0H5rDK6fwSPYfL6CvEI%2BYCpBwL57iis0aFN42IT1h82wm450n5zUK7csJYxxi%2FxDgeXx9tM11RGIckThi37Pd79WSIvDPV2K9ZQFciCDECfOlmZQKK5u8w7e1cBOt1RJJgqoU%2FBNaUbTcNNhACWmDX1YUPMDfrLefIhmqlQfyvbbUS%2ByUygqkmeMX5RZ4f1m7B%2FIhTzwd4FxocA%2BUA03Y4qc0J%2BkL0m68yMC2NhaTToVhRiG%2F0J28%2BHFRQ%2BKmqyJdCQYBEUk3PXWTx5xxZMifYWN7pGmORNqSrz8Or89QJu9gnPotp%2BKPxDTN2qZfQ9P3%2BTkc7k%2FDjS7%2FcqH240NhvvCCoxMFzkaOy55c1RwArtdYdVP0wKa0Zz3VCXoSgqnauCn4UdLasZfv5ChcWJowQYZjKr9INJ17s3DZZ%2BF0UPONa4w7ofXzgY6pgHDpNuQ2CzRhXUfzVhTJ%2FL0yWvQbGerm3EpcgaJnW%2Fte0sqJx7%2BJgS2QRXiKaZb88uSi9zor72bkdOCVzDgRu8x55Iq1SevMfwtNk%2FsPjbWk7v1bdlvorIpveVcgKBqlTjUkRAj7Jc0zoWky57LeyaJIWhwBGlNVyFtmdtnSk8dOsvZoYQnElx5i06stPQ7NnX7EbAaqRcIAgbUsbH%2FXXC00KiZ%2Bq2y&X-Amz-Signature=2caa0f0704a9cf4a7a05fe88d6416d1b419a87d0e5014d57bba3defabc682f5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
