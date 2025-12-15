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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GP7DGUI%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T025943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJIMEYCIQDP7s%2FLOf58XnAJa7%2B8iJSftBXMZsKBfYFO9WdbK2GVoQIhAJA3bWJQob%2BTmo6TD8%2FCkFnNZmsOnadJNY%2BL2e%2FskVg%2BKv8DCD8QABoMNjM3NDIzMTgzODA1IgxtDvA4%2Bc5%2FWNTIHGwq3APz0HW9fGYtrUPgg51rIOevJIToB9lTkebhVjraRDoHwjpqTOqBa2IhpLhCQBdrtAt%2B2d7jT8sZYxDN3utmUISSHppuyuCVMzbxPyAzFfI1ZpJJwTWNpwKBUbstliTmIpp7t1HbrLUiGIYdJKDfCaGpOXW46aoGvzPrkL6CGNnCn%2FSaZKUxWJPtM7AKa1aA6dRqBKgZWL%2BmQu0SBYy9IyJx1psHfNKJWJ%2BgPvJiVy145EfFzxwSiqTABfgqjVvDEnKG3iHLSwS4qZRrRaWWDukSBTXXEEkijciLspeYBqUQrs3HMf627f%2Fps01Odtc8u%2FIzDF6OXmFOkKGj66gRwUuX5M056fz6C42L68Q5jFcqgm7%2BmvnJJRI8lBhqvyBbgqBN5tx3URpuAL%2F687mGcwFCClsh56AWo6LBV%2BAgQ4tKrrWUX51%2BnmlchJEGWn17H9PDERcV%2F2213ixzY7swwDzWj2Y50K0%2BydMSNWyqGvpE4t5%2FZ4Rrn4%2BWbfoqQtriVfIY31RJvDQcQZfOcpsKW69sWSIflAnyMXXIllRbdRfdoUI6k%2F4DrNbVBjQfl0jVDmfgmNN9qGGFdrGZqcaVnudXCotUj%2BfmGZePt1nEQjPjwgrkVstcNcCnGoqBJTDt2vzJBjqkAUmwTdDLJHfcYqpldMlNluH2%2FSfpcLcajQHE3ldZNeqPyhVt6SgHepUH6hlT9P%2B0rmkYqLCDduGoV0oqAYp0bQjQLo3DVV9PVa7qXCjmNPucS2RgfGhHXzq5taBtraIPH%2BFI2DmioG0Hw0NyRKNnpZwK%2F9%2FS7Hb8jS7WtMk4d6i8Rm8WvH6n4mb%2BV%2FhlsM3FVVMXbarHWyAogzyZavs2SOidopbr&X-Amz-Signature=f5ba778ba357079452712e09e83bad2982563dce20296d29faf88ef4fe1061fe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
