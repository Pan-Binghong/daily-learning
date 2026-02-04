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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJJ6AKKK%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIFkpX5RZosPZ7GlrIkDbay6ORWIfm1gReRwQc2jN2zhWAiEA30MEJTv%2FCdOyJk0LZMtC3x5R0EXHwNXSb9ZgHov1Gp4q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBjvTMS8yjFm5T9m8yrcA3vUls5V1NqopiOr2Kqqg%2B5gmRCsk9DvW6LqAPIlmYOFhhYwPodbJhFsSeNRn%2BSjekk8krKifVNWJM4sBI4QfsIihKhhznm5ityTEDJwzI6jCf3gQDj9GB%2Fcdn7H1PMwdulD5ZrCAqI85BzsVTfR%2BadBWJstRiB44IbYWPD8ZsDZXCAxQ3VLOhpvhA7aLV1p5TE1xo%2FcsQDU0Cp93fg3E8ta5INwGEw5qHXq1sWI4NYTwALX0RTe6P0T%2FmAqRRLYWPIX172JCVC3BzQYZt%2Fsmoub0MBCyvrksR0%2Fij4aFQtlEOiUEPaNE7R2Gmb1jQn8iuXbWPCoe5QzJLamvn0G7qyLPeQiivwM%2FzEmUhfufWSI2JiDA%2FQO9cAgoe%2BGSGEOhuiItPRP1tzRDDhiu67xfobJfidajRNc3SW%2FoVVmv%2B%2Fq5HEXi%2Fb7HmnTw2gJwTomvO5if5DgUWMnecSp4JbKOHGAmIIrcGdA6gX56ZK51cqnshqXUcdb7F3HBPf9%2FILKZrH9IM%2Be26VNkAXBAXCx%2F0lUe7Hh1EfyGAa8KQH2Bhk%2FmqfhBU2Y7622h03XBCcXxAkCXatZ0nH9uXGM2GldbBrNeeZ9MgqkgY6fsPfAiRhVZv%2FPaNRRp9dH6F%2FfMKfpiswGOqUB0DVZwlWxlfOjyVaBzZeFkwtM3ErCgcI%2FB7CZrETcvNeEAqNWC2v7Wa7f%2FyUPmZjlx2ZISxheBvmIe5ix8Go8QWSJ%2BH%2BJHC1ST0Cgg2%2FiY4%2ByE7f2F3Jovyxwug2I3z6w73p5OlmCmBIzuqXfT%2FDRbXF6XKPFEMnoQxmDRVxtzjnA1IZVqzUPdmhDo7DxUghg3QDuzzeD6%2FRR4q%2B5EYjqzFCjybuV&X-Amz-Signature=d9a7a5ed903799cb787069a36af0f8589fca64377afaaa26cb319a89c9295602&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
