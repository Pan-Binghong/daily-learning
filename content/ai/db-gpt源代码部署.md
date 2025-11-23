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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZOHRJ3S%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJGMEQCIAKFJPdnGwR8qV%2F%2FoupIZXTM3vTpLSOWGrs1oA7UnimEAiA2z8bqYl0ClkVd3Xsj5cxqdX1%2F3IRfpYWzrLsnviXbXyr%2FAwgyEAAaDDYzNzQyMzE4MzgwNSIM%2Fi4e%2BY9HLTS5ylYmKtwD3XJZKhcppaVymWwXuQ96xtNLsKFFsev9nhSCFOlguZCNMHNPoShuIx4P0US23ukcCnZeoIRH6x7nZWLOwZWROWkOkJJpVJu%2B0cLYlVU0xLftLMDIN0bkjhSrhbkzTuaZHTjGKzZNa4ihsgWQ7%2BIACbVTg5%2FBlFWbrASup59U8b37Atkck8gj8cAcEhiocW9nMKvhyYG3NEGZX8ELwvGRWLEMYiSYf5HORwDsnqk9SFXVm6YXWHEDfB9rFwhu2slQRcmajQjMgPX%2BN5hDInTH3b1cFf5tZbHmpLklkEcrZa7vv0eWAvLTUnXfpQ7fujuFbOxkt9q0S8yceGovwncOcO0TjNtUhIKejLiBnrfRE23j4bi%2FAaWSz0d7suQ8sbjr3IVgVw2Yjk3g7eYeFCOOqa%2FSqRxUEQCWGTN8PcE6txx%2B7q1R3li%2B7BFEgRHUEcbd4MnM4yrjY8JEmUdQgTj51VXQm6vSX%2ByEdHDf8zQuXcU1UoA74ht%2Br7ugxVqOUgCov%2FkTUBveGQ5%2BdCXo0olNTtuwTLBPyh6QqdWStAY%2BF6QIqQ4d3Eq74T19gb85O0plzvFuEj3KKHRlGzWvlg2R3WZv2UTYRBYRlh2JsQWlrRbGmkDFKKJZjlNYHxww1LCJyQY6pgFbQCAtbIaWXnG%2FH8kPv3lxADEZAIC%2Bm94OLtjzUnYKOcPbd3Ejlnbvh2P%2FsRYIpzbp5p8iAGNVuigsd0Dhq0FjOEGlDAEC1mbjKz1OeD45Btociq43ZH78wqrVcciUrJiCL%2BPn1A2nsOGL6QWvA6%2FrOCbyPe0UxPVh8o8JCh00pB6cxVf76WLUYMcMtB5n%2B1BSQoYzGZEkH3wOQZBljdJ2iunvVrQt&X-Amz-Signature=9d2a2c394f7ad42ab8cb9d88425c4a6b9377393a898e8443160bd0ba7c62ad8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
