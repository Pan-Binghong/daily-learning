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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674VTNB7F%2F20251218%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251218T025101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYwLd8gYHqIGPbgZUuCRej3I24nW%2B8A5hcIaQD%2B3zUVAiAJOp1%2Bm1So7h%2FW2xBAcYfsXNqAKtrBVvFP4U0dLofUHCqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMyncD%2Bc5jUzUspz5bKtwDNUFlB15T0gVL%2FjKQmqiOvxKvfRFtIPDQqUaTLiSke5MJBr5EE0Tn7AR%2FZsccpUiJj3nyntr%2BiUoYeEkcNaQ%2FJ%2FO7vFejXhp9VV6Bk1OBwxyvCzhF0o1fKEpMKEbJQ7uatt4AhvQ1oKwlBkQBm1%2FqyaXgZ%2FxWIfIVRmXruwNFQrJtJzPk%2F0t%2Fk05f4GfI4mKpuZwc24thompenjcfNRty9DI4Y7QX9YKvUzeW3Co8Nhi4PUsH%2FvPpii5S7ZBOwXr9%2FrYuOYZ0P3Tp84py042eMdjC4QnYMaCoannYWL4d1K%2FasevsFVxuPx7gR4CsS2BHgwIf6QAwJAAOb%2FsRlnbXRQKenR2L90XcKcEGkeMm0EsmpvOCIeFmRmwE5VsSrEWg6fuWuLiLCp1bnitmN9wHDT%2F8cQhJ3iDi26b6iwDSSNMMo7zeX9f7XRYrptliLi2duV5MPOS6E4QYD%2Bp76lbnIRcJ27HSnkT2QeHshNvdaQoefpzQO8cFfgs1DEvajHJBzenXfSnTlq2UBXf0QRe95KZeVXGz%2F41fmILXfyYiVqblHgXF917g2G%2BPb%2FN5V67vvu3fPzkzeDVzYnwlihBk1A0vt8k340y5LsLoez49rmCw51zQrRRLRt65qQ0wn8qNygY6pgFDag3t2LMH04AZTfWPT96nUmxOtNwJOONUt1nqy0A4ZVrmfGXLTfb60sUhOFeNUCjzURwqfDwdtb15tOACdRygh2XgS9fGf8JRuIMaj8VF3VW7%2FucSqTTrvTLRgOFFC1HMuh3IMWHEBC5M8ZhLNEoHhs8tw%2FDZp16aNdt%2Fl6YPdP8ALyLYb0WXKM2ZC2yj2BH9fjEAL3ySZosgoHTJkPhZVcfwLVMk&X-Amz-Signature=661d131bef168d9133f205efccbf9748cfbc3324748d6fcf64c8b5aae049ff53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
