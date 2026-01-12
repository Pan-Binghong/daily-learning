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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SYRW3LM%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCIG7SDlVMRlNMSizkDHdCu0mcmUzCw7Vo3F8S%2BKIo1TuIAiEAiZPudNc9ClYnpsh77qCF7FG%2BdLPxYbXzfQKWyVmS9ukqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGZ7TvAiqUvrrbF9DyrcA2aghzy7bX23DXYTeBfOoUv9sgJK72lMIcQ9XMKYS%2BbcPH6A91Xrcz8i3Cv16wS%2F8Xc8puOAGNmrzoJGB1RNvlJwworHqHzZML17ox3f8pxowRdwGCwzYh3Y0T7oL3mNxJZ3ULEodNCZvjNye7%2BnzFcLo0dDxxwPPS%2FP%2Fm1bxyhT6V1lkmHlULYp428P9vjalAqz0cT%2BNrmxapmgvA7DSFgqTIz8cZrqQXopp0n9xyWsi0%2Bi2ZaRIqJby4yuc28NN4Yaep2AfeR5vUw0WdxX%2BudjO6LCq4Rswz5jF%2BRwMecriRsRCvA7ZgSZrITFmRUUHOCtgksi%2Fa6heiyiJUv4%2FHk%2FuhZCSRVvoC2GpXUnyvy%2FEhLI2sXYIREeLBYQdsZniINLndgHUEqLtVHekY7JCwbjYNycScY1qGLaV%2FehI%2F9ske5g2orOMm1fvOhQ0Uc5LBU1S3UEzhNZPaOF8ZO%2FTrM3SkJuw7kijQWoxDrzgGbqp35SCvS2wEBL2jHbfixZhrtzacqhBRCjd7gkhykcO7gy%2B57eAQ9T9nmF2lvMDPTSYslgPwqf1sgPg9wpq2wh%2BTEmX50rQ0iL%2Bp%2FMn%2FoO3QHIVi1kps%2BC%2Bq%2BuIlYsdqJROffbxyM%2FfAdDww8BMMX3kMsGOqUBJK9sRqisBHa8O%2BAUyH%2BSVGz99aFTs7iZlPTMTIjc1izmheiZ4B%2BxKZfDY%2BUXDP6%2F1bYPoaaZxgwMDq5suyZR4LBs1vIGAuTE3IyY2e5koF0nr1TMonDEul%2FwsOEYfR1KGk%2FgqFpAtN5C2uc3XFeioqUT9t8xpaBD1ca9kjEWKep5lqnzqBgmnVMqHewuswD2b2Ks8wSQNP0vFUfucckErkB%2BADob&X-Amz-Signature=b0aabd46d5a3b7741283cb471512f82ae15cc1b2bdbbe8789fcaf8cc6a853793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
