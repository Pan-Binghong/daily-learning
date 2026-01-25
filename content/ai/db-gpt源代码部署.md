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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6BDCE3N%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIFWfMALscQRxIgj2PlYT%2BMy18v58CQdRc7QMGkVU4KtnAiBxk9NvnGfL8KnDj1TYlN9ZYJL9SiZhCRH59RJVQ0nTLyr%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIMVuN2db0nmtxujb%2F8KtwDKmQK8zjtjYNOHChx6o58bmkhUVDq55K9Kc0YWRGeWlUhzfAl6%2FM%2FKTDb3vQt1MrQA99MIfRJcvRhghLoUqtDDWTy34BTb84%2Br%2F7hQZjvLU2t4AnR9hLF6v8Su5CMvf6QoX%2BVAoc6uPToJdBhdPDO8jnTOmyWz%2FovJJDFxW2nF92LGX1U3QZQn0tcVoCJulT5L5P4X88BZQQPNqbTYpdrSv2u6aJQ3u%2FU67IzXk4EPeayaUrZXalZ76IgaUsAT4XB8psZiKw5KNkGgMEecNzIv2hjVlLggOjhVW5d9YwT5NLRAYllPCH7k4B%2FYOe8GElMJ%2Fpguyasgwdt%2BQlfSIr8%2FjMZOMSlXSokX74g8Tb61KMsc8zSOyCgCOxhuSSTPMj8Okn1q5gJGypLJijktSmkQE3YCZuWg6eW8CkTPnX%2FTo20RSRM4GwRbSbUDRjnVjKJa%2FbIZacwcsmm5AJNKlvvCEnzfvLApKrCUbKbgzyl3dYZv7ypzelYg6QvolbrkU9BEoPDE37PE2dTFRrSkyLSjsPRf2GWeeqTigK7fqCx5O1nYuIUQiTUzCLiRKNZW9Fx8gLcqX0D%2FsGLDgt5ZF8ahzhyTNOr6hGJ2azU8lrWYbt4LjnEiDPCbs780C8w3YXWywY6pgHIuRj2qLCaeMTxFDkl8lFB8myM%2Fzz95sXtMaja8FWPILlER%2F%2F7p8MpykDOjlscbxzIyfhKUN2HNLQTfBAzZX6itbdEsTURm3oafSLBQDhRg4jyct32q3msZiiCR9rlUXLGgxF0IuelDOI99SY1MbhvXMd9OqpOQZcqI03QK5biFp4MrUlEUHnnF35iR3%2FQtlWcOQMtUfh3pou%2FlojP8a9hFjkN6MDx&X-Amz-Signature=9b2de4fe73a8081f2f022f7082c2c67192a057a0fc9242cfddaaa35a0640b4ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
