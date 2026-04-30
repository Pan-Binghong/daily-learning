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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLZDZZNT%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T084818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIHwI1iYhLbiXq%2BZPnCpwDcDNJxKtI013WftufrMplYdoAiEAgl%2FRPvNVGHnco76JRlB6NGdR9OnAJgMcC5RvuqLATtkq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDKlfcBTWUFBope25PircA3x%2BbK9MzGhIs06eff8sTRKI%2B2V5zqX5dV%2Bniimy4w%2FvbAFxzgiPZBDf54CgIhI8q19sC3Rsty19HBiVWfJWjWrA20WVz%2FMo2m9YdaJNRiGOJuBqfy987gUYJPxqqVm1so1oxNAbgu9JDvBgmHZ4ZNFh6k8MINuZWOUHU%2BlSRLi%2BoM9uhUUKJ%2BAgZCthO%2F%2B9NKiETQpquGCkM38%2BX12X0y2srTvoCWJjI60FrJdJYtSRMZhqRkhQDwqQspRb2MFqQlq6o%2BYlqBB0eKkX4Pkmdn30Msk9iwOBL1fC1nzGrjfXvSMeF4fCBHzEs%2BWWG0OgN3UAzrygQGorTWoouNa5eN2cq9MWSimu42IFJo%2F9GTyDshWgz2GGeW0A4PVEPWRw4uKSEFWMnOp0FmZGrwni%2BQ8xHNGyFo9xj902pIXm7AuKn7LM41q%2BiYa%2BbztKLzHyc%2F9TxjL8Rp%2F%2BCrKudSkSVRCHHGwRejGY%2FpcXlVQYyfSYEZIhAx1Gje2FZmyew1BwEOch%2BI%2BIP8NmVpTycbwyLg1OU4ByTPTk%2F5erf1JNPWAnKPXFUrFE18GP5VScUrBYPuKPWF1jokIe4kZxsuBI%2FQk5fIAOmIA84PSU0DNua3cgLFmzHen8z1VpOQ4WMIeszM8GOqUB%2FnRirSWtGSObcmWhDA6jsHF4Zq%2BQpX%2Brg9uh5sNTd%2BJVqktuaGcJ4Xh7DZHK%2FOiUmtl0Ey0StjD%2B4mV0UC%2F94S0Co%2B6gK9apvsW2CdkdokGK%2FZEsfvRpZPLOvDB%2BjuLaP6Y8xl9v%2FyGEoy3vUOwx9JFtv93E82pOw%2Bcab%2F%2B54iv4boDmam4Xluni0QIhA%2BK2T%2FSo4RbbsvbXhsTkhbVsn4yIuRL7&X-Amz-Signature=86e08b42b55d0de0caff39618319b341898d1545d88a50133d65654efb4a722e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
