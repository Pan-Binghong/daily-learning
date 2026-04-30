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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA3NBPS2%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJIMEYCIQDJOw5K4Vw53GqygF1Ef4fPnNKXozeSpcgiGcCT6rDAaQIhAK7RPJZAAvVbz8busbBukIrzXLyVxlr8lVOx2K5AQhagKv8DCAUQABoMNjM3NDIzMTgzODA1IgzaYA1rKsYnbb9ujy4q3AMmkj7r22qc1yJsyqr4EWEaNBQQwtk1Dhejn8aDHNJ5XqvzcjZVU2UiYvFmjkQD4n77kgiGJOHT%2FNHjaM6vHzTQ37184J27YLiyvs1eNSsz6QuBqiXA2Q%2B6dGBmH%2Fatg6bNJL9OYJ9eTdYykHLcP7yxlt%2F1m28GtvMLIBG1sxFe3ouhQPv6IMUKPpdfPkdu4r2KO3wh%2FezJ6nhAcLpVhm1Bw3sd%2F78uYJxQDWpGn2iS370AZyqrwf6QfKhMXLFr4QEXcd4VfN7hXKuQPyPPwEaWR1tJINbB0%2FXC8K%2BgCmyxcJE7LYfLePifo79ygx%2FPWCj13gJbhMVzKTKwKDIZxgxktCJi3JK79KfpahdVWLXiRkUnEHk3xF2k9L3Keyq0QJwWdNu9FcYj5zs%2BAsq6OuMLaWFwuBqV6HnTCidihjh%2Fht4xFYTvMIjGGFp%2FSu6ZRjeFIQ0Wtk7ZqZHoxLbLQL0iYaok%2FF52hXK2cTv67QRWIQWoe1zDsKMq%2Boy1dNdRJqY5qpaTO8yeIuwPjJX18W2tBHK2Ep44XXgLZlE9X%2BQTDilwp5DJYsF838tPbs2dpIxx7yvuZGWwjvcBkQhaF8f3RHwZ%2F9Kg43cf99a1CsUXhRAJugcnegY%2FVCtUoTCxssvPBjqkAbBz2GVqdKMhce52MHm2JxrDtF3kP1BsBexvjo18%2BkFnJ1NyKwSx8jqATUKsKAN59gKqhacNomMjI1JuQMkVRxbromr0pjRlsnooz6zrxTh5dLY%2F7bQOAXJuygzEg3KyWUsXClI5TaC9Ttb2eXwOC5ugf2myimhq9hmjI97xrpsDhESR4DuKuZt%2FbhFodtXi2uxw1Qh%2Fm7AhcUj6AaZAwfejPrb2&X-Amz-Signature=56843a9794463bc045fbd728309979e717dac9b665c76cc213c98eecf31ec064&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
