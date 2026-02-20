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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOPVZ36W%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033346Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA%2BaNGIHzj%2BT6OixH9GkSKiqYUPnQA2jHc3iq7PRmU%2FAIgDhNabKRDDVk5NsshVkofjVzutg7gm0LO5ncZN41jXwsqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDILlI0WjnProlwZ45ircA1jGXm%2B2DBqakEeU7BY0h%2Bz3Am2%2Bh2Rbt8stGhJNztVu51KRfNsZm1cLpw2gX12F6iRekJqRKW59jEk80f1jZJvuC3lTcPWbRe%2Fyzk4%2FrtO9ajT0TGVa09IK3I65h22F%2BsjQlx6N3MFkSsvjjZ7c892J22N%2BHTpRLY8jPY4O2eBeMnb9Vhpcv06bejaRlLzLMxDsTXcLbpozvGfp4n91VKYrdqDJyE%2B5LyjEeKGhfCOFZqBEOKel8mH0d8sfYcGrqUpjKuxLpxCf9DDDfovTfSZoFJD08EMcC5kHkAWC351xlRDSgY2oPtOpPzhqJrsP9IP%2FQ4dW8DKoU0chwo0LtJF8ZgHox%2F3%2BY3iK2D5H70zMrvax3QadJx1qiHhzCMbr1xFslHcsGmm3cf%2BUix0twA6KdZW%2BKhZYvkt6ySFqTtkLlVx%2FGxSdDW0Zwca6KFAv15msg1M92otSuKv8eRXtfbKHnu382ilEYbMSoj9eKgEPg6kUTjmVbS1ySaEtQinZzDdUzlBPfjvyaHRUw5kZHCTMv2LPO9DE10iSreHQtbbcdZ%2BR%2Fp16%2FfMPX8fhn0tzSodb9aPVBiERHvCxXj9EbDOa3E1fpxaD06E5aRE6AsW2fN3HAH3RmpiGfUwZMPGQ38wGOqUBs14X7jICIQLaLOMMw1dKOeaWWHIy4KQp6IpRfIevMdlY7hus9ShrehYZspEAmazbIxzTABzMm2LcYBZ8LVXPFc1H6vhBCvHBR4stcZPcC%2Bp45kbAcM77qyKm9eI0wsnVxsejiM6ZW%2FZu4f5VGKQMBCQUsf2f03bNWqRtsOJsuSZgFckLuDwuoKd6s%2FMmsDMZ18NOusyRUUF341xC1jZGuqDUTMWc&X-Amz-Signature=6f3addf169cd9636ff376b96cf172309998f4c83d5a077a21f0d3267034bb2f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
