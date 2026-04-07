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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAAHVC7Q%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIDe0IfAlOZk%2B51HWbIBDcmFALK1Sj8je8MdHmfAYRyk%2FAiAp4d9qsw3SLoXvqK3brBvjoNpcPQoyz5i5KOcsRNduLiqIBAjd%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyd55sO%2F4ZabEYcTjKtwD49oWtMyRxmHal7lcbpEj52GObbsl9SmWEOjMKQg8PoehGlDE3dwcLwRusMKZgo7D4TVYtz3ZuF7%2BDw8QZ3Z%2BRHDurTpFOtC7uRxVre4DbdIuRAScJe7h6oRgYF7oLPodBFtYf9Wv47e5SjEUL2cYVv6WxwXk%2Bs1DLyypjwQdk7XmVqju9KKA2aZOcgkraIALJCnR4YqFyLFRMuKewwqay1kQv4LQ%2F1OOADjLCU1WIY%2BnPyrHsv8I%2BtXRZwJyEfMXVLU11ArQrDNRHkIyYNAhq2tjB8MZuGpADEltaE9dxhuUklLiaH%2BFEEnM6C0c%2BAik%2FXCL6f9uYcvXV7iIcry5BFbj7GYNRlk7OfPxaRicyn3j56fiuOER89vMtPV%2FYJEWRJVKqzNLMeZMhh2g17c4HQdx3SYiD52N8S79EmWM%2FbozbaWzlO304GFNLWYX6lMWC%2FR3Aejbyz6mgUnI%2BueUnvWZiYcA%2B7%2B0LSRBmeBeTDTAY7%2FzH4Pnwf1eZsO85%2F8JfnKEgzpzRCA4TEVf95boI14e33rDpJWy3Dkb2%2BD92Ecmev0c0hR7qIkjoDuJJTQHQkwwvI3qCNLGwwuWQ7266%2F%2FrPhBAQdz7WMdr9LMWK0867THGwCjOo%2F09KnIw3%2FbRzgY6pgEkXiIKDETwzhs4ibWU7%2BEvFSvdjm9iZjQMhWDUrL0OVu2s6BDlul%2FPmI4jSPHegndcffEAYljfIksiCkoILIbmsGAcsd%2BCYSOEKNK%2B4peX6t73RbfHpAQeVCUq6kChhdyxAmugAhFnD0iwGhCMqc6LT3svoA8qqEYEGC1x9JXYEGlLeXBoJMOCFqeOjiUFjXh4EFwX4JhAiAzqDKCgPAyvQoT3wdz9&X-Amz-Signature=3196a625009815f589cb932fad311dadb95d1b4917dcdfc68fe68eb69f0f69ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
