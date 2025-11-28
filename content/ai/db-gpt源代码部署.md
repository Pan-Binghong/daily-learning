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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFI7ZHMZ%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBIgCuku4qoj9fuqJXYG3rRlbY3wRQpXlL%2BXLcBzwNOUAiEAmLnQPZtoQAQcEwy0LqpUdE%2F6oxkicHevk5QOmdCWnj4qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE0RV39mfzO2t2AeTyrcA%2B33MINqjvhcZVuVLu0Degsix9pDsMCzghWDUG05XI8rrFUNrTWJAPHCR9XkOC96fR9NRvofOD7seMRmHR7DNX7B9FF8cponAetx7eFd5%2BUEPisTGGOiL2lAlSTICP9WhlcE0Mr8ppaP9lKgHLOrgLYofyjgnRzSwMMhKX%2FwDarNnlZgiL2pM4OSGL%2FFZC3u9J5g4Y%2B3%2B92olfR%2BeP8%2B2FrPAsVudkBeMwob5h6Jv2ydCJ9HSwbfu3DLk8vxFVwPsaTc1z7HihOyViLRLAcseFitc5iMq5wRBeBR%2FPQQFzWloaniMthag%2FJsG0Bv8L62RQ0Dk%2Fb086qzaRlqhn1kqjuo8rfc07My9pp8yyzxDg5F9q9xWJjL5B%2BK3e2AboePP%2BFg2qkaJ1gRyZzYus8fvz5Zg4j0FyHZFD81yamuNIzVI3dUAv9kg7bgnxNs6L8zEcA6YA6RXqzTUPuwtmGITXsj8ne%2BZuVERdGyiuKw1SivS2VUxZtH5mKbahlpkDUwYXzRyukpQIONxXr%2BYmzWaBCZPlcAi0I%2FwIWe9Olq4tJ4rnVY%2BdKqCtOGCnp5ffhYVgHAK0cJVbi32pUvWeSGAtT3NiBciN1SB5nTCLKtsMhRre2t5kDl%2FTLn4Hi0MO75o8kGOqUBcI7rbGbIc2xbo6IXQ%2BIaxjD4vtz0mByt6kecqQYhWuQnYjBkKsVWpoIMgpwemCIGPbIUf53YioAZrtsO0kG6ydeJA3cohmzmN16LVb025ioxzwKkxLBqnkmbTl2TtenJZloMHwpqh6HS4QN3G5bxAoE%2Bn0l9ju8z%2BHsWTgz8NUoHZn9CXeUaq8G1ZssCumnfO1V9RSL104GAHi%2BDehEWe5U%2BOPUC&X-Amz-Signature=a89d6b4e037c2334ad43626d29a74cb03a38666d1566fcf578a42662734f1eed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
