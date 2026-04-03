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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YGQGK45%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCWurNZJLVkE9OPdVqLDytg9KW6k2oiHM2tnUqDTAljRQIhAJ1hqCOgSy%2FBRFw4KJTJbcYx30C3hIFN95uikWjWdQNLKv8DCH8QABoMNjM3NDIzMTgzODA1Igy89YRxMO2xYbp7nIoq3ANvUVQHE5%2BApucDiHfMklzLupMnbamsuUPEfm69dMQhmoPefj%2B5QcW82kaC2LCvPDo5y67nrMYHw8VOt%2BMo7m8%2B7M2mmZRVdNFtzS%2BXFW2ap35WcX9QMAxl9WrrhXaMvDWEoTqltKkgQeLUlnefLSwPwgK0iHxxIYd%2BffA1tHYAvAHiZrQMokyFFjct3mp0%2BJ7YsxO7A1GxD6A0x95qwrUqdho6U0GpntaA4yc1aLad%2BIFWcVE00zolGse1MfRrgrfqB7kaydn%2FsbowhsDIdDkSWMLvRfuRxEcD2wZZ3%2B1tpp6cQO7eGM7xBS1LTyWBTnLOzOXwCBOP08zH4%2BDRStoG7kWFM4WSHOnrZMXnmt5ROym6aHRxHRMHA02A8LSCO4CDVZpqDphSWHiRQR%2B%2FEFouOQwZUjATponBSlxLRhCoSUdjJWylKM5ZpZ6GiakigdL9iDMWajR30Rpl%2FKXItH8YhbSO9MuJnoPYDtuEwoeAiIs6LWyNsgcTpGNkN8i6Hc%2B5YTjt5SyeeqlpNe3Fu%2BTjHRn%2FA4gQH9QMVMvQqM9KaV%2FOciEKT%2FeAUtA2ZlF%2F%2FLeZhHf6E4n1oNdxFNiSvpcqTDBVDkD3anJ7pGGjHm%2BIvCGZmDHxbs83nIaqlDDCrb3OBjqkAQ28t7RLlVA6HOpPxyc98vr2tCQ%2BPkBxKASktAmAvy%2Bb%2B%2Fqu1DgpLFf%2BPGL9sfKx4%2BRi43F%2BEelGDmrADbu%2FES0oVyFChj61qKxz3VCy%2FjF6snu9g4f6Wt2LArOiOVl9gYJ2NhAmSF93anavubdbLrxQgpL88w31Vmss%2BSKqJkhd%2FvStu65poILnsfKvR%2Film0aCIh2NPkzRfLwW9XVWNeYljIde&X-Amz-Signature=a2090841464ca455e7ee0ababe8bdb0b50c12908ce24db497b0c969055f930cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
