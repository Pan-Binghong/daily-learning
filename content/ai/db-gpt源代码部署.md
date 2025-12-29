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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TA7UXGKN%2F20251229%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251229T030726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD5fX7U8TFCSa2z5RcO7nE1Bmk1Z8v08%2F7g3wCn7ylmHwIgRSVZUxiJ8LsB9A0yxhpSieJSXbvcj%2BAf4TRcxXaeKCQqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGdaQh9hfkuz6k12UircA7vs64FB3kUzUWWMLO0k06Dj4%2FPUyrzSj9QiWpgjGZrcfWwUjB43WQX%2F%2Faf6h9JK35g2sYultdSHU8pwAvBijPTs9Kaj38LBAoxTHmc3KEpn8zKcTSjEzsVfD%2F9NgQpfcAb%2BCGAqymF%2BeTdJI4BApZNWrDf8x9MfjxRZEHjRXDDC7V3rOkTpTikeCjG1HqMFGF%2F3X0owosb7sh8wvaTnUGJ5blB1faLIIghb%2FQf3irA5TxMI%2FLDkdqlq0cdXRBLn3gvbc92PaTj%2F3e75JSXsOQkAEJjgLb3xNMOBpNJP2BmTfI2plQUI%2FPORpLGyoyaUADFYnrWCaretKa1N6xq5MPtN0AEbAVWIkcssj%2FZKvnz50ycqfaycAJROmtx9eOLIsJmrBgFhF5GVNM%2Bn378cN4Co5MFB8oqy8kjwfzpb6ugng6BV6K%2BaT87WO3ev6c1esq7wvoLIYHK6MvcQcEWTyVVD1mvgvprDw9pMkMBTvHu%2Fe%2F27vo%2FKRMPQ45n65z3j%2Bg%2BFq%2B1SkP0IYute1apj7baCMogHHM8YOKcbEBgz9vHZEkpBNv9igQqWO6oJ8bug5MwxXVQpnL%2FyV%2B%2BBNiB1NYcme51Ud5RI9cALTReRPsl5OftwszRM6XJjuXcnMNihx8oGOqUBdQhMQuMXEjni3fhIFhp0y8DYqEghu66%2BsITOEIXY6U%2FMnYbJ%2BA1D9VTjjj5e%2B6oFOYUitKUftzaJiFQDRkCO1y9lngMwnQfWBfUwMqG4xcPwKw5FLGH8ETeajnG2OD0UhAiHiCRELi%2Bl9Yvc1HMwgCB%2Bo6YXHNG%2F7suLyY%2BWT70SW7%2FtptwedbtuYh8iXZtynsJFb%2BSVP4SFAXNomMrA3UR%2Bmkl6&X-Amz-Signature=214cc82a8235b8953bc759ad4f595a4b0d94b6f00e18a445d52de8f19d71d47a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
