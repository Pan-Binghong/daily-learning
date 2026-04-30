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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YG6EWCUZ%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T082122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIEmtnH2QmknFQmQ4x9%2FBLCMPrKtzaIftEPx0ty4XwrKWAiBYRbwYwf4VREv1O%2F895l0WqTdyfaM0CMHejgsO13spHCr%2FAwgJEAAaDDYzNzQyMzE4MzgwNSIM%2F14TkXIwFAkVALPtKtwDQYwBsFzl%2FHgnTJYiIDd4s3mPFakK%2FO9M7YXCMaWumnCSyegg1ZL3G8BI6a%2FRAqmgyrlyRj4ry25DPyRSP%2FSyhOWyjVYIHiulf71iHCc3WGxu4%2FTODNNAbLTVAqBfngJJdrZTj%2FDHProw%2Fwa1YUpG2TQN7LO1x9Su5NDo0UpXwYqeBSdAA74pwIn28ClZSqULsVeG7xNfjsFhF2%2FyqmTy%2BLGDLlrszU%2FhZcdZZEumuThx96Hv5vpUNMCzJqTr4NnQ5ADs%2B%2F0aj3%2Bc7fooFV550Lt9mACmIGLtuy%2BO3ylZ1q8izOBKdtKtKA09LnOhtYX7a05dgfNc1R2awMlE%2FxZM05VvwFBImApzEbwhCcDwcKfW4OEQmQItb3w4%2FOvD8%2BClx0SKGwB9w82hCTitXqExTj%2F%2BxbrWuOuKyx%2BC%2BuYf%2BRb6MUthi%2F0pbCnTCfmOtk3LaEz6KJ5W8GPb%2FTZ8hBWBbGrNRaKdK0j2exQVnwieHhPsW%2Fq0MOMJ8DbxQrHhEKgqwqDZ0YYq4B8MIDjHwXhKygcFY7bEYrZzlOjdVdKLqDLzljUC7PFoIpJJbh%2FkEMgulYIJoXwqJgMXiHtzg7JVOqtFC9OkkhUCNaS4%2FoCIqArBD2dArGKViNGZL9Yw35vMzwY6pgHrJvCJqXNw9Lji7F3OBGPK66bDiAFCONcfzyXDS4FFvauJZD5Jg7qiW71oRTHdLOpCSlMLpibh1gcJYppuVGaT8hNpWxEEJQXT3aa3arwU4lpKDuzpOf%2F17gf%2FPhMrH0WjM3dpccvkbKRXvaQt8fvAUPY6jgws2iMzF%2FpzZEdntt0dpcEit8%2BeBAg9W1db9HRaKlLWtHAH6Bj2twKqydllt6hCtAT1&X-Amz-Signature=fed551cb59c0427f46d730d09e072e1b9908aeaf0c3d59f26aa3ab6583ef65c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
