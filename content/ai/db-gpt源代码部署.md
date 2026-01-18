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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDWUZ3K4%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH9Pql6%2BIICGuOFP5eLYP60n5FdJJVG3VMQGAKNP%2BGI7AiAS%2FY8HzsuNLkwjKFfz1OOAVtMQ8oTRKZbupdAjBHcoKCr%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIM%2FMh7TPCPRJfGXC%2FmKtwDT%2BMIcVZd2MVK18SI8d6BjW%2B9SOmxUsJYFkt%2FiuRRf%2BxjBYOUcyVFtf5df0W%2BED9gPTlQJeYA%2FkEPQS5Kt15CpL0lIwVLBCmzLyyCS8g%2BCDsqU29pKt7%2FKBj6Ow%2FdmE6cSQwGkK3yeeGlZtqeFGIAaWmgoOdoCYRXdo0wseWZKJ5Yzb3U18eZDvqPHwOd2P09orycUe3Zvx0MFDDrJDRCAOOp1G1Oi9jFlAsUbKQFiDpuvnbjlySvVjpx1dvci30%2FeA%2B69FPwrtWOuYqVdJaognVapS%2Bd%2FvyGgbmU0ur4YmkXIeOXsCrGzNmGSPorBsDywHAlAoPO1LLU3h7S7QJzcqELFejgkplVcc484I%2F2eoh026Z%2B7wUdjp%2Fj8zzgOITx5tWZ1d4jJr%2FzflvX7P4oz2j%2Ftk%2BEuVNNqH5upWy7LKxSUzYc4RnBjM550qviahQt%2FGpmpCSi8DYbtjiENDTXc0Ed0Y844l3doZb9p2sU7OG8YIMvBZu3WSUJ14ZkJNelJodcy3iadD0H7qZcR92CbWQhyS82B5PsVtYNoiqCLTCSfJSRsvqfoieM9nLxgPV8%2FJNdE1iXlUbSZTNYDQJBzQ8A4ZyO4EDbtnkTlD9wFZ%2FR5fA3lUwVBzniIrYw8IGxywY6pgEoYs3IOJgCax8HOz0T4F78z9xcwelJbFygY1JOdoQdBRL4%2Fbf6a71EiazwykZEuBSER8xYyTdaKyfIy1CHfpDIUdXPlyr6DlT6ThaFQxZ6TzUyBptR33tLoTReRSY%2Fz6fSCQARBDJTPWTi5e1AOzpPJLfD%2BX188epV2C4sGksaN3yDd1QrzV40w7HwriSV5b%2FU87U4ZT4Zecf%2Bhx4v7ayIg2BCPmqW&X-Amz-Signature=644661ab1bb5a0ea3f256bf6fafc85a44874a6a7d5ff182f0a38e6f9a9a3dbe7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
