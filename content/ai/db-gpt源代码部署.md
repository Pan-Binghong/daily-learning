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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUL6JJOO%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T024344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDf9qWmcTQSjoZd1PIA0U2slvblrl7L%2FDkkJjfKuAsOiwIhAJerfSm4WoYBpxaMCQ5XNzJd5ip%2Fng7mp1AKzV4GZ8CAKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzb7sd5yCRBN3KttOUq3AORhqfQRwasbyOWUaXs4I%2BxZ6rUY1kzRCWwzMn1m8oZCElUtUcc0DqUp%2F40kumviAsSgjE7dk%2FElveuf85cbDFDF2Kx5jxUMOzMvzR12luxu6moNw1WGtp8A92syGumCDasccBjr%2BoVNdnYQiGOFwIrBXGnJHMwGVoiiEb5wIpwNdXu46U73rH%2BnXe%2FxFZJdGOfluVDfbKEMjlvNMsArvO4cDhu%2Bs399Kg9GqRwmjupm2DzKRgzo7e5tIbGqWn1Ut2khozHEJa9EsWGvElR8qXeVRIjKk4Yf40hY53LCynj7uDEaVG0k%2BErd2Y3Y5n3NgfhazxMbEv6CqYNntNhLq%2Fu%2BqMwzjsUiV7cosscnTRrrDCr7pH4r5AOAl6MvcWPjdv%2B8O15zofNiRZO35%2FVGjtcnCvL3ZNFruGxkoPWszvhAztHxhhcUGEMJa7GUEIlIZb%2BRwD%2BGu%2BcrlUXjlU1WjBItAaLXVX3edrMmXac0XGcyL5Hf7C20aouDxVw6V0XmtnReReR%2BwOFw%2FhxZqvT4vMf7U6T%2FMgGedlzLiru98nmKdnhOcpzhRbdqcGt2ZdqYJFSros%2BZ2VMTK1HlJlUq9VeIypEeAI17ong6i4%2BMM%2BCLxKK2k7T84uH6%2FKjLjCamO%2FIBjqkAWdvceswTFK4Sv74pkrMd7ij9Lp%2F3%2FqfRrke4uQJi66XMdpeKWLUc6UW3gGIm61S3ZDFXs4fbysUZI79rX%2Bb4qtEJeKstZWFLjwvSE0ZDMR0k1iXeIYiU4N13M6OF4EUBEggqIhzIOWnXqo9r6mPZbWz%2FGvhF9RYlKaM5kGQxNeEknSI1wZOACWSXN8zxG0e63CZqa8x%2F9dQq8dEENaCIrUnTlZ9&X-Amz-Signature=7d8650ad07b948761e0e45b40458fba8e3ab36105b01933ffde56302cf655bac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
