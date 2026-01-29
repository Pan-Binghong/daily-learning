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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7AMITXJ%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T032800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFOlMmSmOVi8lCSH%2BCka2bsBqyiagwOpq80dgml04xa3AiEAuNwp2fZ26PYdqeP16pw0y7qu0iQmkmfzpogYE6o0YLEq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDI88QUstKEKczlRJAyrcA%2BIKly%2BGYIJohsdV0T3uYlsEc0qz3YKceZyi9%2FfevCD63rWdt9JMJKOo28PQyjrpcjJbI4gkiB2vhBYgu%2B6rsA2CyOttU%2FPOfYJJwxi6ntgAzk8t%2BE06Ikxskw7z2kSfm9PBS9%2FEJ3qujMmojzFE%2B21U90eSO6Myayzw96hV6Q4CqYW6GTTQRSmv3u0SoU0wFg6bHPuR4VrpY3e%2ByXT%2F63W%2BcL7C1%2By1nkgc6MqQFWW0KRFk4FX3uBiVPL8kVz8AM7hPNWWTUZexYG157nnMzWvluRBrejYk1hI3U6OCmuZd%2FwF3%2BPrFsYtrWB7GIq8d%2BfBGwxLoUSXji3ZJ2tkL1Su%2FGDLUwGhCFSf%2FoAwLA6K4iaoCQKSHkDkW0b1En56APvOwbl4BJXjuPwFs99rA5GQBK7C2CKv2u1eRKEMVAYOZgQ67cB13qaDfUpPWBvq16v%2FnPbY1TXaGP%2BU8vcah4BgqyRX1VjMLU7l5oiBUsTME%2F%2BhGGwA5EbAZvMltu8f5%2Fuypm3n4dtb1OenHnlKo1v3%2B2TG8F0m9m4BTBdPjiM6ahoYVPTqoC4qvoUQbWCu64gOjpSelwaJpHxuQerns20sdxU70LJw%2BV7t%2F6ZKjRBLPg%2FkCzIzs3Sk5P22%2FMN%2Bh68sGOqUBYImY9AfxgRM3BQqqc%2FZvM85m1b6qj604FPGdYe7LF6%2BQRdwKPsnjt5V33CcK24HxXfD2fvJBpWtZo8jRlePjiMz%2FhrOcPmgRVl3jL2yF1OquQmVjKhw9wVDP5luMCVBoyLcOU1Dn8OfMKN%2Fu5JKt72KWrCBZFVstOykIYIdP%2BkTJZsWFIzGi1rsmOR23XEQfeFC5T%2BlrbgQdWNpRtOptPGBGU7fB&X-Amz-Signature=f919f451471c8fea3ccfc98843795df5e16f1a561956746d6e4f55d8949fb8a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
