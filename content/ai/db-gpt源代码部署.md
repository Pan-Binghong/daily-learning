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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZBSCD5Z4%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T033833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIEETQhMhswj1JNPPVnyTu6TMZ5i9SXC7YbUCGWhh3KCZAiBHrBKSiVT7x8e29NO%2BzewqSve0fpx4EYv009iY1%2Fm9NSqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUtZ5jE1M461Toj0MKtwDVsLfnJ%2Fv6nCo%2FcUomwSN%2Fh4RwwB4%2BpbPn5gPzroNslG%2FkfOcSjewxQ6%2FwMZDNATaC783%2Fm3t9j1WeKdrqaoo9JcyEWGXxzLz9y8fKudw1JiZBvSOe0Hdiwf94RGLnnJhFsVLZX7jBzCkTyxS05oTjuhN2T02wg3%2BgVvIShWhJZTYed3dSFTBuQjgIOKBDXBBnQ54UhAbxiN9Z7Jdbfb3kBiRnu41e%2FDWZ%2B1%2BnQWOsc8BISG%2BB9arFKbQQrBowKGf4mS5Bsm8e4riqs23h0Afi7y5yhZz9jyR%2FOotF0NN9P%2FoJucl8nIP2BQUnKPil3xyG9l1czPNeYhH238UmEXt4sRUD7LxBpJEF%2BUMJqy6txK0DG21IYRLCw5APw%2Boak4ekv3nX8179F%2BGXIZmKVxqlMbUjdr%2FPW5qkSiD6JRjutJqwf7oS1b93JTsEsrX2Ax%2F%2BYA9NNzj%2BhYpVPp0Pl8XrhtMP9lTrBYSuX84fwj3yQrSNT0CafcOoaH4xGqucANT0XXizO2befNIWdzOGmlaDz7I1qXBr7JNLvJ%2BUvt1bSdQaQGeqlvwtEa1GpHTyq%2Fyl1KeBAJg4ek91U4PcYHo21nl21Wipoc465kRoU7hfc4M28D1WbWzlTgWHFYwhe6czgY6pgEb9iTYt824dXmTxDq9JjKvcrij5J%2FmRYB%2FlMdmdKuJb%2BQwXY8b4VTyu4J1bVlBun1vU2I3LoAV433NbFXKVevtKzoqc0xzeYkLDpavQq9JepIYyoGmi4TNYcE4fN52HMwI7kOZxAIGERQ30%2FtjwIF6ci%2FImEdUU1bcLauFCvEV53iQpQ66pRID7hN%2Bxc%2Bxpg5f11UfPorXGStsdOZVWzgxfJzZEng3&X-Amz-Signature=0228d257c2c27d37c031bd74551e1b487c8447a99f62e352bf71ccd2b7bafd80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
