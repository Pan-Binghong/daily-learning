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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJYGZQAS%2F20260221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260221T032442Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChiyRk%2BsK%2BojWd%2FBkTXFpMKOTATLb7TVnb7%2BKIvZcJVAIgAwn8B3c5XJaA5YeAkCcNg8RQJB3IpQBEuJz92H83zk8qiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNqDpLLyqAzdSEEDkyrcAx%2F0pmDpdUe38pTKTNaYPiM4YhDKT5ZkjOI8wM5k%2BFKvC9p0k1CnkFlOjU67GnAEXyHthshQTLlai5L2lmLlArnsO%2FtLyuwJjylFli0MlLqbgxNaYrMGwoP6mCCrh%2BM9vxAooztUdOlwW7DbpXdENn6SRMUVMl4aVI7wx6qXcKfeq2f6qth3o%2FXTOPk38pj%2F6V01KZyGPip8qK8UI6x8yEzGzE6gvSelsZ35ip4%2FhPoGO4xDIEXGmBIB4EaZWwAkBtD86djjQ7fKrSJzW5uS%2BWUiIW%2FHLDHTRTTEVga0s3UP2e4UW%2FkKyJl%2FzRiKWFZ0ZQyU9QGbLmQ%2FfhvAFetobIUlRmZH9fyYmoiN06MpRMt9Pflb0LFl4Y4T4yEoGa7xGEsa%2Bw7zGgOTqechSn1Ne8xqTXK%2BKCXWwKA9oPU5a4pSYKzbnVL2%2FDrC5hWjNFT0NwIpFUJ%2B5S2m23ajuduN4ulm7nYqphRxkIbPmtBdw6Kn4%2BF7e%2Fa4SBZtv9qh3kGPoBCdHEMKsl3TCUELO%2BBMGL85ayfHgXr6EZVKMWWzhM%2FcKoIWwxzag0Iil5zjNhVnFtaSIbm7d8OIpS7S7a91fq5ZeFBJFy2%2BT%2B8CoC0yv074sK1GR3%2FBQPXgCiufMLi95MwGOqUBOkfIYyGvawSQRqskLcJ8mfPFJkZdb1qnR35lRK5qnWEnwEDMLCivH6WDkiGTmTzMuzdFUCZ4uymV0ZhX%2B4KHScQYtyQVG9P6miJIRXUXHTWTMIAz0onRq4Izi7JUfxvs6xnQF8HsA2zmkqZCEGQEHyJTu7fF%2FxaAAmreUZ0Jf0%2F1A8Yqar3jiV%2FCoFCPQshuVQCNlx%2BXA3P6fswEqp%2B%2BHbKktNe2&X-Amz-Signature=cc7e3f4c2fa21f3049819079e5c8bc6ca09c3f0fc4cd7f3bf33f3cfdbd223a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
