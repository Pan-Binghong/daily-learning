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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DEFCDZE%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T025946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIDDGUYMVfL8tQdeojb1ipQM0NyrSrtYz5UxhZ%2Bj05%2F%2BLAiEA5%2FfvgNFCeyI7FE3g5xb7IOu38r%2BcqlJnwFIRl9nVUekqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFKoiiJczuFtJx8LRSrcAy3dD8ln%2BG6b0bdeo%2BTmeQmXUK1IX0taeyy2azVaIYY17SZ8YT0tcLNVfLcjlEXedFS8uaZf3Xk7v%2BHZ9FdFyE8WYz3obaRAnOo69ymW%2B7nY45F19lSBJjJXDyml4bwDtyP4Ak1K0YGqb%2B2GC%2FZCHEnbI%2FjHnohh%2Fio9paeZ48quRGMnAGp6VOTBGEAL1ZZcVuyz%2FNuXb6%2BDkoVo%2BH55EoGM4HzAFbJF%2BassKyXkf27qPsaBg%2BGgM70%2FDDx14lGxNdFbWvE1lHJj%2Fa0iqmdR6aauauhCMKPeFGjwGrLZ8ZL7nbrDdx9548OPYbMNs2B9Ll42qYuv4%2B%2ByYexGpmBwU4Trah4HLgq8HqDqg86zGb4gyXWeWYELjFuBH5rTtambH1ebuILVnEQRFu%2BcgrjA%2ByV4Vn3oO7Bnew4qw6iO3jYjjE3nJE4piQnIzgudkOq53l6zXlq8LlqEbYsevgfNQyWq0PnRKrURTVFafj6LprPYxxkXgWGRPDNhVD57adsZugsfo3BHC18ppjefhQh7qYqAjvf05We7IscXBEtQCAYoUUqQsCQq5pYUOcl7l4fYUusvSlwsn1z4RIhdWsUBsB59DMvRsqh0SivmfzR708eO1vlduomqNa%2BGg2CSMLKj3MoGOqUBeT8%2FQAFjzOvHB2dsgteafVJPv0pj2EJaI%2BGTShO5%2BI3Fg0xJnGzkQ69h%2FcqzptMFWgJkbTgWrk4ukmIUG%2Fjs06eQ0U%2FAXikB%2Bi%2B%2FU4bD%2BTCc51xrV8QR07K0IacNGsKte6CMOSbf5GPgCdHfT%2FdJvvvlsDworpBrGCGJkcxaPKUb1Ap9rUzcrJ74xOIABJAPAqACTbMyrfYIV3XJCB5IoWLTd1ad&X-Amz-Signature=9796a740b01bd66acddf8953396284b86a40c74bde306e40128889aa1a8c5d3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
