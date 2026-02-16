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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWKE77P4%2F20260216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260216T034304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQC4QoNkBImiExmuNyggv%2Biu4tRnlh6vTGDqExBbCTVKNAIgKiNUHadeB69wt6JdKBgW0JY12whPrq5XxY4Qpq25hEQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDLV3sXuE2cjS4wb7GCrcAyoXAdqeCq3veymN9AgLkd7pwuBdtkmOfKrDHldiolS7y%2B61K4k6xFLOX26DN3WzLq02R5PIsd%2BIUnuALaVD%2Bt6p7QVcs0QS088M8QigApCzoDCrE1%2Bt8o1YYLRCluchI2TYh5yuoTiQGYYs2nMSrkkHcohFVD52SWnGDfoTLxEc7NPdzGsWZPz76X6NPi1ovExH2A1FdXT%2BUnlkmprmg9R2d7ogFqbL6e06YmmCwD3nJyLX9qhi6aTTJHZH7Bcv1G36MTxck8AhPvwMyXbDI5ui9DPSUZAuBnojC9s5O9O4tmNLBPuXGkr4Ilml2AIW0xPZBtJJ8kyD864JB%2FNUMBwbdkC72zlupfWsXCzYgeVepMxXCEtXinSCIr%2FzB%2BolThjwe1pmQR31Xr9bpzJwknlq%2F8GjPE4DNaFdXfPqYhO0B6Fbdg0MSbQs91WHQiwJJ5ieuDCHT%2FnkqStvL%2BvLfIjMaH0vVl1Iscn%2BNK0IHwgJPqb0U5TQSdRKl8K7Qn6tbKqz9CxPIuU0GAlh3VC3L%2FSHWztBOQcDc0hvLigPogSklp39lVx%2F%2BmbmPePIJM0jlPnjOIYb9XL6%2FVhnjq1CBQzyrQjvKfxrJwuqDJqojLum5%2FYSrZe28sXg9dkSMPqUyswGOqUBXa%2B2GVZysJfYwD1%2BDfNRLEvKmCHbr7BkDfcLpSwzY6BDgnkmZ%2FnC86M6daVcIiFkoJSTXOYOoKjY9ZklOmtE8wvez4Xr7x0%2BGCIZ3SB8eJhm3hP%2Bpm3B7BS7rvABsnpifI3QtUBwgo%2BCrp0zO3X4kFgQGq70wjP%2FL7XR4InymWLfvHRNrWQl8LJtWHjk0CMD0i5ll2n1AX9%2BmkPy0mcdWf%2F6yXLH&X-Amz-Signature=9f3ba4ec718688c7ca5e66e22486bf24d64225a931d79a688580dd5edd5d5f19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
