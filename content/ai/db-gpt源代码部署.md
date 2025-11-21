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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RB6STBTJ%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIHpweSPGa8fTVUjgPxz83g3mIrchoZrQp5x%2B6c5bUsXDAiEAy3FlA7pBWt%2B0PMvBMZd5pshz6DY%2BlWlRHB2g2X2rXsgq%2FwMIBBAAGgw2Mzc0MjMxODM4MDUiDKqp3hxRCXIGkoO3ISrcA2j7jI1cVzGglF%2FZswmsA9DoG09%2F8M12vr43dkzVImbYXJ%2BU6dXpKnAjdEB3K91p84xI6sK2AvFPRWRZg9p4ORiYaKKlpLgyjdrCnISQ08ZmWkoNinP8vI3jKeZlkH6Sk8UuSahH2YDFUU0STTHW0Lffy4%2BBwDofPStMF%2BpVes2BEjYm8rqicbY7UYHbNsOdjeaE3ymUcWWr4ij%2BJib6yJHjwKw5F1CK07pOW1facnjcPU4oRhsgXiRYs9an%2BSCX92PA6VzI6BtSQU0kH0X%2FdWB6eaC0S6aQWzYVIBl7%2B%2BS2LDV7PP0JX9oGkPWXqgnjFyX9F7ESQHhR94mRyrcsU16BJzBTJP91ketVubPjmpjNqcfM0WDSmyRaX%2BuNqgMKhG8VP%2FhFB9kcPd2ogIwbiqTkjRwKOu9Sa5RyrXK2ElHUTWmYGL8ov6NeVreCEZhNhYQ1kNWBC5o9rtBk%2F%2F2WE6B9X5bH5DqKZdDK4dpqyKM%2B77%2Fc2AxFQDIjwCgfhBQL2E8rUYDAuuJpT0DOLorX7e1%2FlY8Pyq1uoSxVNhheeE0dohidYhMaMA6bYwwtQrWXLqi9xMZKACH%2FW%2F6TG6QMj1FWN2mSe6Cvp3FUuM%2FghoCvsFY9R9cbso5o%2FfkJMJCe%2F8gGOqUBU8h5BYITC3W7Nuz5PvChVSzKhZnPxQcs2YuJzudRJldz8uJPoIyfkuw4rHSzIOv3XM%2F%2BkxlSMuy1TU19IrTb%2FPwejxhzRR4MUdYlUpJ7k%2BMc8ONPHmmSGLcc3DVoamMQBRVkHMt8Jen6ue3R6HP4HVDCGLdYYCqNwB1XzCNxY9GTP8f3eCYQ5G0LfbEqjNypoQA%2BLtyHAXCvSMiu8WPElsgDalVH&X-Amz-Signature=93d419bc8832f078f6f9def313405d19182bb46b1cc6155f997330eb8ccae1e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
