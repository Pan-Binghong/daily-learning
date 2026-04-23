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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Q5CPBOZ%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T041402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRd9S8jxRagVy1%2BF23MwFZuKCHx6daq9uJHFSU1Nfe%2FQIhAN6ObFm1YsjFeIo4YiI4A2GwoB9zQ%2Bg13rd5D0taH7tfKv8DCF0QABoMNjM3NDIzMTgzODA1Igzouyweg%2FD4O5X34v4q3AODYT4mGgGnzDQongBXR2aVNHstN8Wsy%2FQuF7q6lePU78DlgvyUMp1omdiPLC3xeja%2FEMh4f0iSgv4ZF3s8P7%2F1vLIVbCHoqycOzAtWYjcM6lSTzy%2BRDE1U0xvU8M4rAI1mdYfM2%2B8MOGpsg0eqFO%2B5LkSl7NzkW1ou2FlvAV4N0V%2BZqXFd7BaUSVK%2BK2R2EeYYle1quqXEwFobYjKELauWnJL0JcJomNwLPLWy%2F008YHXlUTBtKuvSQgoPS4Mv6yDB%2BV6u0%2FqsINhigU5Fjxu1KiJyqA%2BBlL8WcCItdB1VbBAZQC1%2ByjeL2mWyMj4Iclbaa88Z3P%2Bajmuh2Dv3jYmZmFDiy6o6HUQPpQK1NTZO9kscnPBO%2Fne3PwHWBOBsBM6PYOn1KxJ4qEZDsPMyCA7cDHDoaAyb9EBA5AVKK8IyOC14VaZoQDFpYgjsD%2FIHZZ6cfrroVBpJJL%2FJbifRqjA%2BP1BUW0viB%2FvoptBFdhU42Hm4pATiCuu540oOK%2BTy%2FgIHc6LD2o3NbumRPEhXqUvLyJphBVpYxwBt7pSicwf8S2EQPOXiaEbEokWTFPLTgxbdo%2FmIoJ1pLf%2FfMSSdYz8KNOTjFrlBP7sfW%2F52BQ4ZI17aXmChuERtl20Q8DCvoqbPBjqkARGVLLxVV24i3Ud2KdrXmBnRJACNJam7kFZuw8ZMIh3PAc7G1aDNiJCLTS7Pu6tYVnCd%2BSQG9kAsTG0lUFabZd7GmoutJ1z48Cp9t1GI%2FwYYKu08yVqvthHoVnHZr%2BZz8qhpPAOkugVHnikEDaRfA3iR%2FYO15Lvj77D3RtmS9mvvLvG8SI6jz6IhgouD%2Bm4i2Kcm5seSVTR7pyQUStOgwDYb55tw&X-Amz-Signature=7e36ba306f62e61cf40158f769f20428fd5800c10f2ab989f9ae5f745271fd25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
