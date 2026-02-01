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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OXWOCRT%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T034944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC3N8JHsjizDfVwx95%2F1gWfMiG90dwYxHUnZPpdhqPAQIgWMiLIRO7jEnHN3rvo%2B4BHFrHMXnZggq4otw2wCIQIPIqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJXn4%2FfNV2ktM21ASircA%2F6QXx3b8sYs2qvj39tHWUj86a2qJKpQZ%2FrRTqxK1ocIJQM0%2FIWE64mUcA8GPU%2FvtohIMaFBYyI5y1xH1NVy5%2BI%2BBmkL8RdIbF3zkwNLfSEVw%2BkZCjFrrVTn%2FuamZi9tTQthdAaq4xi8LNYhn6OltFIo5RmpSMDsRV9Qm8G7iDLzGARbPfTNBTzYMCY5CrIrl1TRdtDLKSA4xSOe8CfVZ8b3DWxHgfkOyEMVs0IX0GvoqpQCvI4r2MNyqOEJapm9ALHcNl0EiIY9%2ByzgALbIg%2FqYcZI6Mat5w93NRH2l3qCbuwAoOQBfl48jUz8Hsb8uyNr8saArkKGknM5Ih1y692mp6I4x1LSmdaPB46dfLW%2BJBV63tdJQuWWg3jBsm2Agzc%2Fb2ExxYK1O21RPNpS5v9Ix3Rq6Zvjeqg0xBquqgjg7nU7hW7tgfcOWZDjtbGnO1F%2BAuRh8plb8rx69G2eDMrIffk2jtXJFeTD1z4VmNY8MqkExL2UVTX2%2FIixwW6OKEq1mIo8Z5tsw8Zzf%2BY8gzEpeVvQYACPFE4S8aJboXE%2B6okXIXuGnVjKh6vg5PQ%2FwywcYAvHi4iIaFezBBC%2FnpHQFRdNbrqYFVAxDdpHSU81vKIIy%2B5uBQbad3bvFMOiU%2B8sGOqUBTbvZ%2B9XwM3rKU%2FPq2m9vnGF1yL0AVZvvRtdbJ8WVxFk5OsHrirb%2B0LU8pl8XiE5xmzoQL9CYe9TkIIx6ANp6QcLoJ1yG0%2BMg7P%2FwtqhIFicVZj6ivMbHS3mIbGDGS0ZXTN8yUSzMdh3QWtkT2KmBf7hjNCxqweukH8n19h2bFsZ2FqrhNi1b%2FxJTmW5FEmEBNhNUxKlCEz1P2lEHliv2%2Bv59IvrU&X-Amz-Signature=7ed55e7b46106462d6b8d3a6e7b9737642509878f1ffec2490df9d8a4eeccf3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
