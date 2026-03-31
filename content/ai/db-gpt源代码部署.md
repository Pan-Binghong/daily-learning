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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662A33ETSK%2F20260331%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260331T035124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIFSgmMvTGFkd6%2BgB7g1D%2BTOGeuBaSUaGqUHLyg%2FvpTBJAiEA0xGduMNGPhMHGx3tbw4ZQSSGJy3VxJD5IZU1oCeW6gYq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDPujIHL8nnff4qC%2FWSrcA2ZMnTqIcE%2F9mo2mEC%2FJWDf1dk0adtCEpiTAIBEwK2iiqBJulehoKpNHtBiD7kJMg8Wzl9aTG7QOLXS2j8lt3uB21sEhs%2Bhy60j5ymoniPNJoll6fNSB%2FEtDObPX2pTqOqM0ab6fdh8BCLwUYrW39yQ%2FMOL3dYzehDKK0jiVLkbiRic%2BoyWxhO9m8witcJbhxrMWjFfW7LHWRJ3EMbmLbPT9djm48nMA9yg0Wine5a6qxp0KE6Hq55ZJPGIejV%2F0JXpsCHjUhFGsO4CHp4Dh67rtbnhoNLlvtgyck0ylejBqcT4RzmxIfOnBQrP2Qu1vSDrhcKEvQ8j%2FSTDbzo%2FkF7%2BeN9XZVYXVrJ5415vm6NA%2BBaxTBKqUxtjbCu8ZY9cHNutHGjFcVVCW9RmZdcbJ0omMpQIzmspsE2cbWNfbvjCsQxj7ZFOoiJQwEyyja%2BEClTzqftrYJbnhrYNnQYJY%2B1G1Al4CjF0ITD%2BOXk0CxZZc0viPBVahIGUfV89N58jchv37MfaIjZUnpZ6YdKXpH7pCct2m17D2QEjuv0lV16kJe3ceQZDqsBRkS%2Brt11E%2FV4vHRoYXjDiGmxkIusJroPAkR1GfjiWYV5S1DuBIHSivFClNyZ3IOZRaHVXPMIfwrM4GOqUB%2FBn0IDmuoySCehMEviDihohp75KSM7MdkAIo4er4ktTB56YtYeD3NxCQCVBDZQdaZseCVVjsauYhZd26NS1HA4GPZ4QiNGhqQCfdyvn2wt6VnH%2FjqPeqpzSz7kFP59zuLZmIBFzTHeZJNl%2BmE%2FmAVHT291AtRYTQg3Wxnj57IIiEy3z6nLl0M%2BPInvq5Tx7HVKVphZ6gFzjRyPgimeqko1ZXuOgG&X-Amz-Signature=4861f52b7a24ad19be2c3b1c27987b933d1428d8cf2f7e4270adca7c1cc911b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
