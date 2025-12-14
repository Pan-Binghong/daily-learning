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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI32DX4U%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T025926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDxfuROrSEgdV8QXlsvmbFYs493SDm0K21zvhQaWDbveQIgBe3n0SJCLg%2FG9q%2FpykqOBZYIMkgtH6v9Me062RkqOOwq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN89RIn15zjiIRABkCrcA%2FqOnQB2jZ%2BILrGp%2BoHXmUFJ27NK5XGmrAVRdUkAganBZVqJlfGPmlXBQ025DRXBzJdNlo63qt%2Fj4CIAJAABmC%2BnjtkmkDTnXsRHpP4VHDVUO0gSLytJglssruAV60BjnPMcHg%2FF36xpumdIys6Y7%2F4MrQjmPlm4CaSCu7O%2F0z41SF3yJkpAI8UkIDLKKJY8CsMeQfGiYLDA1wk8BTDF7Z3y6iBt%2FVQ8nWcizq1b703e7sAciTwbM5EAXBpztdzg6SU5YPyPmOfSFDKZa%2FW3rX3lJi4IuroxRDSvz6dQGtPQpuUkehKYyttZkzd%2B%2B6iGA%2FKHgcEGNq3PJM3ekcRxDK%2BSS0zrP6LHjZnzLaI2Frjv%2BlRGzPi2B6raAx5PsDiT2ZsSyDRLJIAEDQe1r8A3iYpUcIskwhXPTcuBmyBeIt19Q93iwH8qxFzb2JRMd3la6At5TW0UAPyBQl6Rp5eEDrncIpYTHAVFSAlKq6kKuMoSZ4qDMh%2Bcyl9BEDiK9L1xOVuKZvPyDoQ1ihN36VrbXgOmZV59yLG2rxqr%2B1dT0UALqhWfwtcFzZWoFoXWsgzW6scsI%2FgZDRGInVqu7iwfW5iOdUOBmzIvgEmlB5OpJIYOp4ywCRGfT9myIgr3MN2v%2BMkGOqUBKkOSkwj%2FYFCgCiO3LPAcMmsEdKUWTDuF2fbfen9I4xqC3PJZ8IjpXaAfYQWN4C%2Bzvh%2B%2FO6bZZgZnN1Hvx3A3dteVeb6BQJr4zTK0WL4AlthUiAEys7o7fbtv5gGnvh69RBV%2BRosoBDd0GKuxN8%2FhjgN%2F5PxPINDI1dV5pq242bI5RJW2LI3tq35NepNYoWN4GdGlS1rp2WDm%2FlI9HVI18cH0j13T&X-Amz-Signature=7aa2799a5e3a5d597eaa78b0c560ce4ffd6056655d794cebb3ec489f1f1bf7b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
