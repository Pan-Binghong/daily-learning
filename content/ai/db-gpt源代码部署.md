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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46667SI5Y5L%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCrzTVBoQs%2BvtL8rGhiRIlAurbUfmc8E1eo%2FC2QwPhWXgIgZYl5fo6wOBeSGaYXjw4umSFDOJroUFh50KQXsV5JRlwqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIu7nQ%2BhuGv3c16Y7CrcA1zygL2K6tQJHZAHtXM2ej67IvqVVgn8snP%2B94YrNH65RGfxnQr%2BSiThTkJQyMd8Ou48ZoBvi1t8mo2gTSv6mzeZTD63bqa%2BWAH10LfnTJtZhDbAFn%2B2KRKfqDfNTgXKn6SSxC8pAJdwfniYuQ0vfFFRzwqc0qEgMcS5BZkDzH%2F0xB%2BJtearLuMa35rac%2FBKKefnh2At792s9udu%2Bz5ewWxw872j5AXyFVbSv3iEsAyRs5zN1ee41vpGu4O7yVUYyWQDNoGyyrtbfQpWz21YUuwlDB0KTm8atxPKzlWztOVXE92%2FhZ%2FJBpPhgmgPlEi0FKBaTnObQP0zjHsqoHVCplOS6GQTqOlQ92dWzLAiI2YmtYuY0WYjCur2a%2BeU%2FJCh0o9GkzL3QMgXYqkeMOtgv%2BhAzyfNmkeLXDZvdCGpCfwbM66as%2Fa8ejL3v7cGHl8dFHqJRd8DgnsR1OrZuGdBQwryxRIFvD9xgYihr2zzUFx5FCzG%2BEPhBKCTBsMiRGeu7qs9erAAOvCBEzSj4BPV6b3qFIV8ry%2FLhnz3oENt4WGCORpwHT7KYXiRUUh2whgDa9g%2Ft%2FPVYc%2FnP2lwd42bROFzMU79cKigFGNPUDeVz3Ud3uRoXILrK%2FvWobJ0MILXrckGOqUB%2BA9PMGj9h37FuMl8yKO2zURMRKKrpG7Ytwx7LP09MojMxKgo8FyhYGqExPcnDm8HXq0GoJHVlcNclkjEXkC5JTDzx0aAFTc2TE224NigGDB22oiLIsQxls7c46cimnMGZQMKI3SF0wK6%2BLNnAAeQQqMH9c30Vpm7kDlPHaP7rTtjBJdl3Yqgoz93%2BOKW%2BgK4kNF0WSkq2vv%2BgPPcgIbZeQzwZTVg&X-Amz-Signature=492090836e1b6df64c513129b7901857c91f6d6b64b626903b325e0273dd8de6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
