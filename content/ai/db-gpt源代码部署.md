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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFLZOCF2%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICYxEltwNAA2m%2FZiMh0R9SHya0wnB2k76Ja1o%2BwRqzhsAiEA9yITGIImXvCUEKqqBrGeGl11JOr2jG0ktK7v0DAwoCoqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMgVbELhQXOV3egP4yrcAxhiJfSglvCsBBikT8lITdGegt390WnggOiM1fCZbbdE1BX3UBaR6Q9BUL1YJVA1vSactZMb79gTxEotmhO2H8fJC1Wsb70R%2Fz%2FiTpIFoNsATlzKnTbMfGvK8E14KH8VkbLPftfndsJ0%2BdnlzWZ7rBdBD26evfLht9X8dS2kyxI3kIysAcqyvDW%2F3x7QshcN0npsZ%2FocogwgmB2SB9ur02a9zI9qH1mbsub5J%2BB9YAsUUwtrggvi8ZY7i5LbpO6VzFO%2FIjghiqzOwQHEs8ht%2BSS%2BCYeGsIKnQZCYvjL9uoHk5V26DTqQNvO7%2FwWBUCRmmB73eDFERvH%2BBHPqWsve5qM%2Ba5FJj%2F4qm7tA9%2Fq8%2F9WOyFLD%2Fqkqshkhj8Aj6dO1ZCqe3qRQEUg2nwnq4JJg1YoPMiVWnzf848EAXNb%2FV%2FcCcrmj5PfdKxUt7aaa3aFGTRj6OxHLTpyiSKlrhjUq%2FiBNZSSr7czvQIwlh8QITjahiU2V5686lXmPPJfrozBhFPT2BkWJRbreWRZiTucYJE%2BGEv48F%2FsMv747XH7CDfdyPu66CyQUigLtCc1vBvjnJgqDPu8ajjtw2fVWC0MidA%2BvraMXjKE13faSwjBIPDzT3FZK23NjFiFop%2FL4MLbEqswGOqUB5yP%2FWrBIOQ%2B9%2BB7WOXN5ULG4OivpwwvG%2Fd3Og9SP6KtT%2B5q5mG4yXqQSDC15powTB6XrscZAbGO9423vLePUO2Tu8Snas1cwKunYwKnJpSKdYw%2F6laSVirB5ISQyIGhTf4j9FW3yFTZJF%2FuJ0GdwbY6zZ%2BZM3ccHhEDvyw1nS%2FIIzbG2VTjhkdee01d%2FqxV2VI%2FAne55C9wK0YnsHFSXoOdjrKyj&X-Amz-Signature=650fc32c4c3bec3035c8610910c751ceb6d042e216c600ce48e3cb4efe77fe0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
