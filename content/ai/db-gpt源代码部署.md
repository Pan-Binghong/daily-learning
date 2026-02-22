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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRMVUFA6%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDppQaNPu3l4TPX94xN1rKoP3pu465t9E4DGRxnOTG5wgIhAMsD4Pd%2FEM9cnSpgahb8xMRxKRILNwU9ff7ABkAARHknKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3U%2BVnvSYdPwAbXsAq3ANDMx%2BW84xUWuYGNWxPhDdXK06ROkhTLC1EGDV%2FBovhBL557iSvaHdA5BGMBe5V2a7nTTq%2FxgUwbuhlY5MbHep3w9oapbCxl6sD56V0Jz7Q3MHnJTlFPquotEF7L53unNn18FCPM5v7npI8qy%2BaAwXz0ZiPVGjzYPKebvAdpEfUeaVhp3RwZEVfA36n8PyNyDRyQu%2Fg1GWavxBFwMpiqqQBehObFYlQ99P4x7RBB54eyXrR3RXHwdxgyff0dt7%2BYJ1ym4wMc3LlXXeC2riXxchkNWPso6H7M5tk4r%2B8vZEQC55Gd00TVdpeVwfcAjcXAU75B98zhUfMbT1YU3UOd0qZwxAb4RA0EB7uX0PYKc30BSwXCZBiHfxIqAgI8DYnfDGm5CHRp3yAbddCKTWH03%2Bcea12GKsotPmFWE2vQ60zIM%2FGVWwjazwGQ4mzd%2F%2F9n2MqfzBrNlX0uyK%2FmMdasxmFEGY59bcG9G9AIaqmZlmaQzf5AIZaArQAL4bHxhwtE%2FVT6CoI6DQzVh5wmwqeZp88qk0QXKXYsCJ8AP6Wa6tWVfHLMdAUnPz3lh1%2F5mWmbb%2BoMbcLxpWwURgVjF%2BUUfXAvQfhaI9r3Bk99VsVJ02qYHx9wVxSNB3dF7YcLTCnzOnMBjqkAb6%2FryYcMguJuh66xRLwNH6%2BLTn3IlahPxwCjzx5fOtSzOTllqjJrgpUrdeccpfx5vI1UOwtKq66McxxJFlVsRfKgHJHz3m8pgWHFZxcUKy%2Ffv6UkkKq79V4tGLWljhVvSHg1DLWwvDzioszYhlYOvtu8wHHp49eQnxJQdBysrDNa8ylQRAXS%2F%2BaOHG503c4wDKyvxh1SGI1KEroEjo2ib7n6d2m&X-Amz-Signature=4c4bf56b6c79ec9de374c3663101ad9ebe5551c9a551203bb29392876e9fba0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
