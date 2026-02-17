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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4AH5CGS%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJHMEUCIAObUGSQcNsoQFTZ7m9d8PsS6gd7Yq%2BV8PA7SK5FkXimAiEAjZ3oT0tZtGeIXW72WfDEUhmUOI8NAS%2FbHw9fltM9EDUq%2FwMIRRAAGgw2Mzc0MjMxODM4MDUiDFTSWm1fcrglJZDGdircA9WVfQfIucDjuJbs%2BUmy0Zpceqc6RBItH1He93t2McvoBhaclD67my1qDX69mfTJl8bv0PQlyTAVntxEPRKKJlJw%2B3NFFGwDeZK6UYK%2FtvJAzlWGZmQdqInCgmDBsq1156c7REdiKdzfAhIm1cipRcy82%2FA3Lbwlm9IwYRPlsHpQJt8I2q%2BC%2BUeLkIpVUeMBwf6RpqBJRsbSwwtexP%2Ba5TRA9%2BM4LqbL5QcoF8zbfaivupipIWVRZnL1mSSh19kIva8nbzoKosSxoGUFpgadqj2oaY5%2FR%2FeSWCzaRo%2F6U5p80cHDgPPliuI%2BHxP0jjZeoZVHT%2FNIISuglAsm8MpwmUsDAAR%2B8CnhXV7%2FRkx%2Bvl52i01JEhbCaacZLYphs2ScUoLafpCekRLLfEnhx22kPSzuQ4C9CJsPYvb9GDCpJm7%2FTN1sOKUxvQ2CCVU%2FEOXBsYC0R32cumQTMMk5mKEFdh3LCXhDZWOEyhysvqd4usEwXhNxacC61YjCowmSgTwNhK%2Fcyzh8Miu6IIbjpse5EtSTi0DrAoX23t%2BzJg9qY1lGbOXwQmVa6gm%2FNUXP1O2j%2BprwEOQjaaYdKd4bzQGqqpaGw36eerN8Tama%2BzHrrvqTvAz6i3PQaC8hJMGMMO6%2Fz8wGOqUBHvLdVBZ8K6%2BYCXay2gtRMuKs%2BuOh%2FAH7zVaagPPoo375DCCNqpgZhb0U%2FCvNOu9%2BJZwXgFKhCNmbMTMYFY7YLI1%2BpXuSkD0vKk6tAKw0DPnlXqCW%2FwL9SWa0AR4p7iWd23cmqn8H%2Bazgj6rIyoga5iGFiPVzCxLqWkz4zSLAvThwRuG7NjWcPv3VQbwH9FEK355b2O6Mvx6JPjhfzBYm%2BOMlFHRf&X-Amz-Signature=17412091323d22a52369b80a831dcb1e0d45fa4efe2476d3ce742006bec0b0c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
