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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466475TA7TR%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICEH9HNFrWKd69gIU2X%2F6UqKxv80pOECPrPsIFyZfDEsAiEA3%2BfgU40bjJrWmdre0UOLN0ESmePhp0gMuwzvsCMtBIQqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEy9dV%2FtYwiO4J0uDCrcAz3XU2Yk04L8%2BPXQtR9GzCTu2dHSBX5FI%2F9HclZTYJ9cL9NLNRItL95QiNPtdBaKMyuV5l0HdqO2Dk51YiGjdWvAj2G%2Bhbg%2F2yQyYF%2Bli6IwIVIR9%2FJlQpIBmc4wC40U%2Fz9bWvhj%2F4EgNXRioSiUuYFlfuEIT2nc6bmevFp6BiLz5gsZMfOrCkn5eQ5H9mksK0fmPjq4Pu6fK5V7H0XtFRXCRoVoBv9yYH%2Bpv5rEsqQOY4%2BY9L9ECkhtiMBSy4m%2F0LSUGvV5srwXX0o%2Fylx%2B5XADqRxExOTNO86rNlEe3A9MHVenD2OAEvTVDOHtcAux9LilbQWQRFs%2BGUq6kKr6Raa7grNEDGFuM%2FQlw5CCUSssALs7zoFxRnHjl%2BSPpVbu2K7fthtLPO5AotCnZkU3MUk79heG9x4xLRYhkEMvbGZQme5pL8X%2Fzd0%2FVSMXFZO5q4UnGBmGhTxpE%2BmWO6EhSFqhazAnvKsIWD1H5boupuRFeZ%2FvOUUaLd9iusFPUfNPVd2iFKEfgN2fNOIyylQemFtkHoNWyLWlSO1F3CP9Wd%2BIu71rMuMx3tnw%2BOZO7rRw1HQrycYDuF6IBkyWfmCdDhYc04FY5zieIO8W8QHc4FlKp2lziy0PIfBYBWzRMMj5hssGOqUBHBmtj4AFzcSEvk95h5fMBy28MIiDOZE9rN1iZA8lH98qKvJk7PCrhz98MAV20ee%2BNhkIoQR3GLZlLh%2F1VWQevssgHteFRK%2Fpt48Lqhq0T25YMm1A2yDQBBTSIkzFOIXWPLo%2B2LFbsYQvziI4cCOstV64hWZ4wCKaVXip6mUeycOl0MtNn5EwmNoHmPE3xUGMcoHZll%2FtgCnAHZtErdm142%2BjpkGA&X-Amz-Signature=1a1d27f44df17772a6b475d168ca4ee2d72166c26e196b53c4b7ba6cf897fd3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
