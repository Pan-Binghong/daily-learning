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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IAGILZV%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T030914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQD%2F%2BEDzYTgaww33oFUWe3gqYBDixIH9Dmj0zBQj39w2UQIhAMtRL1XER9LNl6KgOgNw2agSjHuAUOM3DIGOOqUQwV0kKogECNr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxKtkKBa3ISLMH6mwsq3AP7fXDf9hK8wPPWgjLYI9jomxEwffGhsKH85usftDemERfka7cQZK2hr70jCalVxJBqkADFuF3eaho0Cx%2Bc3nqJ1Z8r%2Bz4bK6ZAFrTHkHKohwXoJO3oCcxYG1zw9XQcX7bG7CifcSgdWi69Ik4V3A2lrrD5%2FIrY0GgRUSbi7VYsKg3b4Ag8P6MZ0dUPeL8mcNqHD1vr65sH1sAEcSC9oQPCY%2FFelPs6le4fGdBo7JD7ryqnPWIQq7mhVSO9SfcdxHOFnETlVDkcIRG9WMNrVeEMPDhMDSvxn%2BfBN16VaAZrQzgnCVoVnPmuSYLXyCVCk6Au9oPlZmDrZYeOHVT8UH4ykhPvEBZ21UqdLw0R19gH4VLGyaVFlE2%2FM9uQpedgIHOdR4RUQd%2B9A3TlTq7hTiP3k4hgZLoQ3xS%2FLjobj9H2soBD%2FiDzKpcxfNS7bhtTS7dPZ5Xtqz58Ei%2BOsKhvLpe%2FTC9DE%2B%2FgZ90DEXdJRiQPgHbKrm84i6rEXmGDiNcIu7OUzONF8CfAwqWfffk2DlPetP%2FphAj0oB3lXtnUu6JMTZS8c9KHYnI3jQuYUKOKDv0hAJ40kRFJBSQ%2FajVSfQms5oyVojuIPB6rPxI8KooiHlUnnFULzAhyzYjuWjCLmNfKBjqkAfsn0aUDOrAhgMGo6nZ4tXnyGdxcz2SFLgYrIoWYdqESrvKfulJX%2FZpEpJWsQQxu0MhphBpfCzZ%2FXwmfiGUy77evIWbLAyAKqcbQjdH%2BiDbICzT1RklHNB5p4QRU4I4r72IGNuJ4y1xeRC1FIAT75IZDnEUsxNPQmvZhUWp8%2FJAe6wQG8hA5meYtHqEy1UT3klZWtm69kpxeXzjXkJWFbWUNfhmt&X-Amz-Signature=cb5fc331f3ea04194eb5f21f77878c6b5d03d49af893c6b5961113f19c8d9dd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
