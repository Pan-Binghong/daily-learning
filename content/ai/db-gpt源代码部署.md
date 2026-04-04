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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5FGZLUM%2F20260404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260404T033519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdGsijJVAL128AcscoRfkwy2Wrjbikrfn0sBYtDXbo5wIgW1qmwnwUW8gR9AxfCGWbGByt%2FRwzBdmBCivvu2CU4u0qiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDr2emiWPWEgm8LiircA7fJssMb7r6v18pnGzCfPlN%2F16pNwd0f2MDNIIkbJr4%2BRhtJOaSgtFQWxCp36FMsUJNeLPEnLaSK9%2BJHMixa6pbQzPVVUR3nvq76NnNpzOhS0qlM0PNfrzgzTdHh0M%2B2Kd5VFdb39OL6b%2FnB1zX1FHCybkSe6ucBVlHmcad6zRxTMDOy4Ib8w06t%2BkaJT1gHKtOtjqaY1KPjQjg8uPehfWPOB6Y%2B9UqmlkgqMvQfMu64eZoE4MR8E4VZfu%2BuUjvwYyUF24Y%2FWGAI8dqOTjt5lkEFpEep6i1zsOpZJe%2B3VzIgPrE%2BA3kVB%2FBWlpsidqljq5sutXuE%2FvdKjIueBXvObI0gzEw0UhHFmrORsi%2FLe%2FxRm0jYIqnBgvv2ej0iw%2FTRvCrtWt0PI%2BZgCOloZKGebmhGQCgZphe0C9ZkPht1YIHf5RNX7YkVAHzorX%2B7X5kgB7dAIzzcfMgF6DIVt2xjLKpVBeKzTnuh1hiE%2FAhdLGBSm6IXclJWyhTwMZ%2B3Ot8MWFq7yP7dvK3Jrbwv%2BXZ4299W%2FKAz4VdeYK0VSET%2BYrspdgbQI3otWQpVeRzML23bsgyXZF%2BGSGrgJGgEhSRwwXGU%2Br6xPvuar%2BvwH3PMrrE%2FRRXLs%2FOfIvr4uhjQMJTkwc4GOqUBnv3rFASFCaIo%2BrzpUa38IN0gugqi7yFX709IRGarkOIb8GOU9eAFEAvYiBQdxEqkEMFjt8Qf%2B94C38ezncMFR%2FK%2B9igAg%2FiUpDNf6ymEzYNE9mPACugPWzoJQJKaiU2gFYW9JbBlubvKvOrVLKqDVn9AbJIJJ7bPyftfSKyl8GfSKLrF%2FyVhvUDTpzUEzr5GdBHjOpeKjgQ2Yr8sgLtszlfH5lQv&X-Amz-Signature=bd523fe22176b2e799711d0b5fc8c64e160410a4e1875f1afeff1156a2b38cb1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
