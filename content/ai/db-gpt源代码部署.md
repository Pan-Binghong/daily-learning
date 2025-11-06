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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZ5VS22K%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDCctnwEH4tJo2114vJ0fuPfWoM11k2tMEZRbYhtKMGxAIhAKculPOEPIkP4GtNBHB5v%2BsvqFagvOCKRYmB1n5Cgu1lKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJZT8uevW0mwXjITYq3ANrrzSRiISBihtwqGGz7uwurmwW3zKi7wFHJpHVnsQnk%2BlWFEO8zRihRaWjgP%2FvJZRj0i1jymkdeI%2BedK62lxA1RSYXGOKT9MFLfHxFjOlKmw72YZaMF8oHMcd0UM77AOnkaphuMORLotM2%2Bhc1Dw7S6lRnm6G9yL99nN1yPxEpNlyFsYSFwM%2BXn1Q7GwBJIgDpXoScP9WB1F4gBACRPHE2fXtZj2xR7NdHwmwlah6Yw9A4PM1bn6J3px8eloVonteptyl%2F%2BrHzdaQV%2FMtW5LCM8JV5xqPOlhFry3F4fGT0QLszAburgqOCdbaba1pAahSwwZg70Eogh97eJ0XrQDUSMft8%2BEBdHjzXHRwVc7%2Bey645mUmGePB%2B9wJdNUTaO117ATpDPOQfcq6d%2B55hkvhezavGzNL4gc51uNphkaTGY2dzd01ylCgOdhORQMMUV43JwaYAICkOf7mk5l%2BtkXVUoWO9g67VDW5Ri89E0iMPq7VRJjl34GjCcvZy%2F28Kl1Hi5Ihr8kyNw4J7VUvnSGC8NgvKhheMGp27U6%2Fbpo6jZqh7fRhRHxmdddMfe%2FGL3KySxmMfYgi0m0jB%2FHLHfmd6eXWekRm0FutCUtYDAM%2Bl%2F7NOskLBZp7Bct9G0TC48q%2FIBjqkAf02K1y5Ipx4xf%2BNtcACCBfV3b3EPn5QUcCHbAQMAgDRmVlUmLLRhhGEnh2BJZFKdxNhi9PndUyb11d6kCrR6hdcndCECi3QkE5PYZfMJE0%2FtqKd1%2BOX1kLeV8bynQ510d3R%2BNOVHFkFhXOzc%2BVGGmsYEM91su8qGMRQSfBCQU4o6LaraJzeImnvlUMbaGxkAihW1D%2FCJ8WSii7OwMlxklBSYWJ8&X-Amz-Signature=9eef0f06c09a16c86e86b2faec568a6d5192ea2cb0571130b5a36af1b0223a32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
