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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WVVH2JU%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHf47RQ5GNYzCYV9dQmT8Jk%2F9H8BcdsuvWAiR1YTm%2FbwIgAxaWvhKnanwrvNL4XKiU1UoRSi6xpZ6xyzrBOd71kQoqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP93McqQb0pGDSkPXircA9P15A0QAhDKTsMtoWhV%2F1NCMEgtSsOsNhw0CyEVL4JkFA6Da5FDN4IacfZs5P2klUsYkYID%2FFKmvT5NaZTLCSRO6sZCAIMEWX%2FYWI5hIA4tpwGSe17sYXDLioyOYeY24tzAZH42lM857n5dscMXcx8btgvt2e3Yy0zVy%2FN4CvaUFHQ0Jz0KkkBsutrp9zIvtDpsADztukAg4%2BDRJnHXbr18JtIHPevvRc%2BQCgqlSuPr3ixPWOI3BoX%2BAP4iBlXoVpiTRihksP2ngiINREL%2BvMpttM%2BwRzWg7h3SEdrHwnx4HLN7Xq%2FX2fwj43RXxjx5k%2Bhu%2BE2FfXhdIyX4drLOLypsWFtAM5LM4sbSUNAqdPJQYYYPG6VLh4mVnw3UFpOC5wWjzEgvvzlGjcGJRBjODxsT31JOBgmZI%2FPxMWiAA%2Fd2G1koKdxuN1b5eNtiMCVizbDqfhZYw5QJjMWgfKNSObHgv43cz0iZkXfWNdrmiWCIfa%2F2drtA5u7v%2FeFbTUyp2kaebbdOpoPjR3ouzyMb5XVL2bWVa5Oq0ORCQKVZFmIXYuzlPxGu2WJcH1DnVcLGaKAnd2BWH%2BnIAOPF%2Fs96TEuYRX7cgVzobrOw0xrJ7vh9fRSUDfU1S0%2FdeJEOMNLdtcsGOqUBWVJ8IhVgn4FH9O3ynoDG78IMad%2FqUOGia1NfWRRnH5G%2FJFcE7uV%2F8RGJuSkpZCQ9WLJ3H8e%2BwnnyRNUCwKpxLL4FqIJr5pqvkGjnXh3O7w9m6k17ON5E8j1nbXp%2F4JEUvMvOtDsfgW5KmnKWwYLZU3bxgHSlUdAmWTZNGZsG6QANhGHmP7qcEAIwwUKa8rMHUSA0cUaScP0SMxDCBH0JxdpfrtC%2F&X-Amz-Signature=624402f00af44d6530939505761a81c748ca86c34701041dadf819508adcdddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
