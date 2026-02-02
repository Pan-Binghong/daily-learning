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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAVQTCLY%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034236Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDscRqH2GaVLWELkYOKlpRndvImoebt77g5eh7DKmbEDAIhAN7V8sSdsw0mLoibQKv7iQEj4VMxXSc%2BZCkiIv8y3OBsKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxX3RyMTKVQXvw0Ztwq3AOcw3erCqKm6eXFFJ2Y3TE344Cut7Ka0HJiNJQS%2FpNVpA%2F34lthrjSr%2BIsaDIAPOm612dzNM%2B8D6%2BHiR8Qx4m2udnvzGl3s6dfXy5Z2X%2FgujaoUqLeSH0HXfD%2Bv0BbGawvA1N2xy9No2rwZZaRXGFmuWnxTxak2KTwq3A2u9b%2FFYun6m2gCMtineep1h9xajT8yMWuzlDFJTX51nK2%2BPwL2d70tBgHlvH0J93n07zMegibcGS639lVVnVsjDRO7vl6DLEXXTki1raQFONiiF2tB3ZF2Zl%2B9xzmeqjQ4aEeAExoSPtvXxmBPFfjvJwTV61ia4MJUJG4fL5G1ULCgNCfpWQhqGkJ%2Bv1KMPXm95dsWKWwWbS0ql1a0fKGu39uDKh7PFDp0RFnLUnZ%2BM%2B8Fg0jafgTjDxO6PEFU0hL%2F3YC35PJNNjZAHoOuIhiMD6BGfQ3FH61YzNqtiXm9Z3KnQldPlKf4nrtP2L8xC3YNW8SK7LRhlfwEaCkDQxkowkiCXw4RZMwokVkiWuOSXVyK38KY3q28Ho80NraNo8Y3Nwk3eSNCBCHnKx8tbXKGXnD%2FYdlyhn8DzL0%2Ba3Eu4fiZKqSJimO1WXu3CZRvetWobYOhs2tDePJIBJvz9TwrtzDNhoDMBjqkATvmDAp4JzX2zEN4UOhDPlgH%2BgMT4eEQsY8LRcxffvo1sG7THiAYgbJY%2B02yzSu9%2BN6AEZiGtdz2x%2FAOfFdZkNA4fL1yr%2FTJuU1zCMg8KvofnkTguuMUZInMOed56ce2y0drmHuircMmeO0QqEc4PV9mwNIzrX%2FFEkLBcricqm92Ns4rgGvQrhoAD2eYRRwGVdInhTukS%2FKQQE7r7A1XrnqoTKbG&X-Amz-Signature=5fc573791c11e0b36cd40aa7b378032ef3a0f7e2783bb5835dbcbb7b3e957a77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
