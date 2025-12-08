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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMCYTBRO%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDOswACCb%2F220zitX%2FWs%2Fn37jk3lxoAqQKINnRymLXcGgIgO7AK7wWXssRatF4s%2BCM9W90j8MTQ9e0ZHETH%2FgkbDVwqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBJIKOZ39h5W0H2veSrcAw2p8LjAWo3bXjLcEOP37xIfSAV1QNau4KPgZBOS81uJ5z26jQOgS%2BV9nG3CDwVNCxw5aO5XXwOHMU7kCtWfNjyBMMTJTCCAdjpz9DCn1SMsyE9lVNk9opEY8QIFqQGc%2FY6lngCPQNF8k%2FH4BINo1JUtwPH5Sx2KZRl1kV%2Befpj6KaIUKdM8eBlPp1arngMQ8NCKy0znzNXMiJB2adYArEbSNeImCug2gfBTm857rLM2J5OWXlA1vUPnGVAMBd9WKBdBdQbWAW0BVgAGIUGxocbZ8raoAyalGeL2MwDUVwCkAUOY0SCYvtV%2BJXXb7oh%2BFm0S1FgHTAEZmcuZTxVT6Qrc0a0Z8WywIG60uijBa7gvDW2igdIpg7uTkjzZQ4LkMg8a2XnDYO4VKHk88nti052BmZ%2F%2Fje2jgRViEKViR56BF07JYCLGt0gagSFuLWtKrCDtKyHicZIKBVVjrrZqLFtUZdrbYX%2Fg9v5hCkRi4a%2BXQDnnCAOLPDDxrAoWtmnz5RwGBfnooj8ufukWfN76mjR%2FT87HrQizmKpuPO8XJofY16%2Bp4mU5sr9kgel%2Bs4i%2FjWQ6BQpViebm%2FQ8eGr3R7h0gC873AtPvg8IhLh1u%2B2x4HYbb6b8Ev1xSLEXYMKDv2MkGOqUBOoKLYCflCsT7GtWjcpIVoa9LeHVIUJYRHWlKWfOlBh2Pbvk1VfhOaL%2Basmt3sGE6zsVqD2z3nzs4LmL9Q51PRWRttkLowKTgh8AOF4Qfi5yKFV4PwB7reTpSbcak3h3ed8K%2FkH1CYk4MLA%2B1pFB4DihRoddAaHqzEgxu9ee9PNtf0BcMFO%2FJpOFHR%2Fa4%2FozsOij2GIQ2hk2bN36CJRddiKJLRu6t&X-Amz-Signature=4d13478d54f8c776225328091df15463a71a14e5c5d340957330030ada072667&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
