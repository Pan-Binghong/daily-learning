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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ4HAEIA%2F20260113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260113T025800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIQDyybM1aNC9VEtVoXUu8%2Fy8SsB0LzdOlXmpDqm9LfUMkAIgN7KbIfZHTvGwN18YoCfdKnyUSS5qht5v0HRSjl7oXuwqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEk7p5QLL84dMcNhVSrcA3VQSylFaV6sWJ2b%2F%2FdplZKm51h1yjoVs6zORyKTIfC1%2B4sNnABpqBVxRFetzpppm4fvlZ87VoD0rzoOVrGx0eFK%2Bs0yWbd12HHbhuejvgyIln7w8AHPVcmlZlnDsMZqR1I3l4%2FtjXVfw5Vog%2BZZ3YkvF1qTdceg7epA2FegDDzZMDBgoU7Keits6o1q%2B8%2Fqb2y0%2BhGx1wvJ%2BnQPbeN5Ly0sf%2FcXOTVJWUEmmCZ8G%2BudQB%2BzznlYWMayPYwgNxxYDr39GuYVU2y8mbUhV%2FpyWPgvZGESAwUVhtFePXsbLkEs8RaWp4zeltKHdTGIKvpjL0cK5NeEtTKgbCirl9WNdEEiD6HWmjdWdYe6L2kpx15fBIedlDc0Ae45prnPOiRXJOtoa%2BOqXE3tKpbJhIwMZs%2FwH0IfHeif9%2FdIhRirhw9WYDtQhY88P14Xcm5PupdbhONqgO8omOFZu5LMD5K6pIrzxYUhREt3bkvH6R2NDXHjALCRBA8pQ%2BLtlU2tobAjPFVGvtqVLXnOREFPS1bpUUTELNFWaqMhpXVZECFBsKGiUkpxEECbNJpUZIhUEPSqiAJDJW%2Bes7UfgX7O3mp2pqS18mXWuROqHdL0K1QClIcNNDhIGUfSWJiq0Ps%2BMO3mlssGOqUBHaNzohv2SL%2B0yy5h8pC%2FPcG9jXGcQ4H%2Bz1FQb8YJQhZYBRefdkm1DQBA%2FEZWwp2PTkSWBhEbqmRp1Zh31Uz%2BAHdqaarsLOMV1x6iPb8gswjgikrQ%2BvOOm1RJFUPHiXzLdfYdhEEKEttC8I6wWH8W%2BHqFsBD%2Fsc9r1rTrAoSPqwPlFaZNpoUOqI9dbVWNqJPwCXHJPOIHhVyZrvID1zfLrC7aYazi&X-Amz-Signature=0b39bb7696e3fdec28e6f08f4426788ef3b33463a732b46d78488bc17ad183f5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
