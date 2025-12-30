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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVBJ25XC%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T025710Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B8Laju2S63pkAkV62j4yZVCt5mPkarIn7Mg2bnFRXIgIhAN13FL%2FBmLYed0akilsx6RhX3K1eeH5qI5pHZckBIu2JKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrdKRWOO1iVuaeclsq3AM%2BcSnqAbowZwIMIk19ejT%2FszkOYGqeH3Pfmo5FOYl79EX%2Bdzk05DnqkIR4vmv5U35aIExIXhO4viVqEBclz0BDZJgibZm%2Bqb4jFU6fHXQYImJYWc5%2FIZLUXGJR%2FubS9d7vVMC2DH7LbWR394gd8yvx8Fe0829Z92tiLs0%2BdW%2Bpp9Lk7RhIp3WneYi5ScJ32yoccL%2FabKoQZ7NeZg6rxgGrUOMUAvZTylzYgwu%2B8aAIutSq%2BeVygxVkwonauKsT7mLjeE7yKuAI%2BZT%2FBOemgmm3th4yx3nh%2F1MjxS08E6Z%2BpXb4jNPrDDHEY4QwvTW8%2F5aBl9DeWpzimujztJpXnl55M7acTvro2DwepeGN12yFEMcs8gqg7Rx4Mls1b4nptgIN4JdPO1vtdnLs%2BJNURNkBBwMAfwdnnD8qR6P9%2FZvvSAdZAIp0WsAlah8vdEi1GXcfX%2F77U%2FbbI702IFLPHVIVOwXM5rSCzAwoMbgxkdO%2BfBD4XHo62QrumMoeED%2BygXYlEoLh7C6TOr6fFhDSICFc6%2B%2BT67rTmtcnG8RKxN%2FaKBwnfVuK0zY%2FlYmvIDzXyJrDJyWL61QHESqoAAbGg8sXKLHBI24Oqip%2FLbkkxlsAFGWty9egRlKDH6FfxzDI1MzKBjqkAaE72CxUS3zU%2FOIz%2B911YMaK2ETAeEQ23fhEIhG8Nv%2FDjdnf3m5CXmbeq5zTbKHyTUacYNaR2tnEED%2FVzC99GGFt98ljt0uX%2FBtGLWZkkNFa8NikKl71gHHZQe3eES14q2CImubulVaQBdnkxzmRnF1aYFVO3uIAuiyAFcQx3aHpzcldZh%2FM%2FXUZJIrJqWPqRbqGlQidh%2FhBMgU%2FHFaACJjcOkV%2F&X-Amz-Signature=642bcb253136e8b222c19f27d5c4e6cec58fd6dae291d30ba041153058b648a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
