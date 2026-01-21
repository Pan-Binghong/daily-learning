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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SRUMEB7%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030111Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHlCSeG520R2%2FCpLyWQUrAtdfCBGJLhgL38jaKJdbDCmAiBUS2sgNzuaA5CkWgLNNiDtoSygg2jaQdtf2o1UnOctmiqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMFBG4IHi0gAVihNPOKtwDUR66bzDVTbJ%2F%2Bh4uCj91xUciQ6GOpjZQHh5AOhe4rC%2F%2BjYgtHK13hcgeT4nUorksscX8IcW6TCW0V5YSho6USR56pXM3zgB6aEVaykXgUu86YbS0%2BlJH3le77TNcrGxsztX529fSL5bg5uYrb3gtbAMUpRh%2BYuuFgjcUpy04hi54aOWx0QEz6V6mRImO5WFdBjZkE2EEbD2UUs3fY1Qgw0DFXvpFgIevBYedx57KEo0PFuqpUvDWWWMAi2tK2kD13tx7fp5ya%2FT3wyG5MH1s9kjYJUuIxucVVWY5Q8axVu%2BQjBG4WRqvkRtDDL6UvgwVtVvtXylXjjUUKkvWjitvbmrygJStS%2BXMlDpzYiGTRe0gCrRDTaxyGu%2B4p%2FzuSWd6IXhCUduZGo4eq6s%2BGFhGyzIoepZkky%2FzvZakvwhqQSG%2FWIH%2Fzrb%2FzLLFsvs%2F%2FDBjTYl%2F01wtwpRaf8H%2BkcorO3Wu3MxPsqKGiubgU8%2BmedN7jXqlMaNVJ3YIDNgrL2zPmaEcpcyRuYmSb74Li31rC9BInCVGQb65WNFax00ZEZKb5eqYCe3%2F%2BYznXVqLtNK0lMFw4%2BNSJ1fMs1ffPB2U4Lk2cTi5YZ%2Ft%2F4saxDcPFPi3NsM9os6aRHTnlTkwpdjAywY6pgF6XkZJ%2F%2BrSC7Q351tSQqlvExaOH5LvXB4gbavqweFR0oJyDVRVVJXyQbu7TlG7KifOxk%2FVni2gW8P5uAsiLqJSc9JSUkhoAZw36EP1W0Imk%2BKeiL6HlEYYE0TSFLnloG%2FrsZxY7L9HMpcDMgyhr7debzWuqP5FJpAwc3UOhv4nrSVNB9c7FgubpJoqMHzhIFmozUueBeENery0pDEzXpxkcujlogzI&X-Amz-Signature=cadd794139320dc11b8b322388ac384445c93c90cab848e8c7c6ab62e4768174&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
