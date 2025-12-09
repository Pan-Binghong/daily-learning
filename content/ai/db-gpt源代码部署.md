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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBYXEGG7%2F20251209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251209T024924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDSE8x1mGst9Tu%2FNsyDrOT%2FsiNi6k%2BADR2aY3tgN88l8wIgNIDOK5VKHdSB%2Bsq%2BZst6eXU4KB%2B%2FiwbQh3iVIcxz15QqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEUKTfaB1Ndnr373XircA3p%2F362ruYsaDD9BfOR8O5yUpCSFkB4kLfImkiDelGOLBqefu%2FhefVvGM7teusxQtlZVrfbyfY02ctqFqYlqfxmtCBTS8W6lxszvec%2F8QIE3G0eaCy2LngA3sE0V3blNBnXslI7rzWByldpR%2FqxtjyVct7ctCgP%2B7vCTx7%2ForMG5yIev53AStvI459jIKmBh9cFnJEXXwd7AlAY5RgxIge7q1%2BQRk0LDQhyvz7csdV6rM0XTlFsT8GYbHzq3IBPdvMj%2B%2FD554ZbVd35VwAcoJl%2FCbDrYVkIxxk1LVSL1K6qHYyeuKg0RExGV2ZtMcFASzvqYz07U7nEZVmnn7VywN0PtJ2d9%2BYBoZlsl15oMNpaovQ4NgDIED65GtMWPFfd%2F4RWG38axmjlFgVLJCI6bBeVjyiw3Eon79OXurCERhaQQ39qPmyH8DjngRLe08GVvcsKQmu0gonVFtj5%2BIPOmJzeoIeKNLc5qE%2FgKZbUmSpesgvQQLmT1EoPBYt8L7f%2B1WysODC1mgf4cpu4nFa4jqbFUvOVfsBOZcACXtwzGca1OteoQhdlO47HnffhJvWdipINzgj8eAaK4qWAflREuGbZu8Pi7bYsMdxvFE0AMyI0VpjBsGGZxbahEB3OeMKaO3skGOqUBTwyP0nyHNWpXpMDsiFQnAysc0eSN4kpDD%2B1ag7hYaSiBAnAh4xlC2GTcI%2FwVfaazgyAZANeYL6xRK47f5OldEMJjAIpHTZP9fiylij28sR43lmqfSYdYLvuTLdlcAhnd%2FTbp5TTcp%2F86HqyCje8%2BCgq1fmYAoaAdVcPGiuWx4c0PpblCjVp9b4%2BT17KXhDUnGAKZMgpnpwUHweZ%2BL5DdxSOQuRVG&X-Amz-Signature=f55e546e5933f149c37286eb2683999fc6be3832a60463143d51464994df6b78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
