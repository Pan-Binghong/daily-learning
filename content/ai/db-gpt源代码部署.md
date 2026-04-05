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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HITJY4A%2F20260405%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260405T035527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDO3bFyON%2FHCfyM9otnebrCriF55IY3scUMRndccAgb6AiEA1Ue%2BarkCLkx4VgG1v%2BtX6qmlXhfPHmITffzEnLhQTPYqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEA17TP%2BKVU436h%2FZCrcA3sEYf78E9mWAnD2V5HDWZx6KoIG33%2BNx%2Fhalh4qYx7f63pHrpp4%2FspMWWad4IY5Np%2FDtpZOFv%2B2YfrpwSP61NAjITCqtmpdC1wEhUGz3U7XdFApgwnpGFgKpQMHhLsZqg6cppJzAV5pRPl0capNw0lg15AgXIzYHrzyF42ID9L2hpas60x67A2UXFwzxGyTeYo6errPcyb0%2FQvFR7ZFWeijXO%2B8zFPpqB6x%2Bwb2cFrG3jifOXNxWcAiPIUwUEZD4yCGeSe3xEe0l%2BpNNUEW5GD40vyrHj0LIVz1vvy7hQ%2BhbsWBZh3nmXu6xcghASkPXetxo3QUSBHPU2wl0zTvdDK7FZoyEE5QE3%2B5hCejNfYn9wuDaIfZZMqR9S0jA6T8f7TvDbN3wbxisDFPEkc%2BosT0k7FhKk2z2tYfBFEhTNu57bP%2FXnINhyLJMMOLaY8Tc19fKX2Ut9rbVXq%2BmDFtezF1pN5FUZXrbBXE%2FYtkWJDtfi5NLk%2BZ3RIFcdRU4jdHtbhgPL8o54cbK%2B3OjA9iqRjpgscvkS3IyRbCghhNPUQ9XyF6sXLasu6FTpBdrLeR2UsgNYj%2F49eLrQzkBuyyl%2FgTnwInVHt4xL%2BlibsrV4pstUqCK5qy5X1E2sLTMJifx84GOqUBtLyMRRCO5d9vdqvmuGt3DLhijt9jXaYRz1CL72708st9X0oxTlclMeil%2FIJDH2GtcBnslVk9FR7L5rZGoxBxu0nV9aH23VkhNEES5vAx123KF4wGPFjQDZpuGjipysDRj3uvc41IMTAPyOZ66sLgHb%2FRnJbafhe%2BGxArKX7gZLaM9KkaVeyY6TPNWVTubgZ7c6g6O95pigfF3noDhRnY%2B%2FKpgzDx&X-Amz-Signature=03b39147f15fc3298e8e25c842ac686138fc836ba3df6f296b79fdd106ef1d1a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
