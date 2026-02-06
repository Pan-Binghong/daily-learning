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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ATBP3IM%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIGlezaQ32UBixki5Bffl2SGb7t6RRx7kSXgQA6ESaSK6AiEA4ASKY%2F4Mm%2BEPR2HU3dA41fOgNWy8jlAsq0Ntc6Kp4RIq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDFX05qfJYeI9ZTpnqyrcA2N2%2B6pnNyiVBJBpAp0WMKGJLoXmugkykPkYY4BGBFS7tIP%2BZRFgoI7dhtBAdmNjrDgsDVL2pUQK8JWBUbBGl1ExqSU3g8bRqvBkTqu1nyD2tZzN03rw%2Bo3KoPsIyToMyXkwpFg2f4h6ZOaDmJ%2BlSxDSKpdUBJiqbsl8yTFpUHGKKVmM2ee2sY5Jo%2BEZUag2Jx9NTVElXCT%2FViBO3Yz8gcJqj71uPIDnLlSK9pdS3pVF2pJ8e4bpvhTGVRkdE%2BO%2BuOyv74N22qIvx2Tbl%2F6jAqmgYd6EdKJXQGrqDPcEYftQ4VN0pyGeFbFiBiHSRDZ%2Fd3qgQyeOCCwPAOT3kiH%2Bis8pUFSRidQsit4I7cIgaw9FrUHTI94S3HlQwnWi395WBVZ1oRidtnCZG7gEswyOe6MfhuSQ%2FO%2BTSrdiZKY42ytH3j5D%2BQt26BJOAHKFlLGs5Cu4g9wfe8%2FmATvAzHKUD2gntoZ0Lwud8fgLC8NuUG7LVomfodP81u3FJfX%2Bo9D4%2BsdHIZjOKAK4bMXahm32O9M6%2FW5mil5FI1%2FWitjHF2Azlh9s9vqsO2flWJxuM3Et2YjGZ48FUNfV34orNSbSt0shQBgAS%2FGRSqdvFA4oPIKU7LnpXb1L60mbk%2B2DMMu6lcwGOqUBBV0ht9X%2BMTA%2FMm1l6c%2BvzDVm8pVAp0WvblSPkCljOMZ6YX26wSwysuo5vk38sRR%2Bro%2FOl3w8l2HTMMkZyvQKNHnQEKWW5jnOcDgfl9TMoYEr1sulXV5nvc3fVrB1EQXGn8a0uJijznLgPFJKbQRA9wqortN23GWDK1nM54JKjSty1FVHeHxymWuJpsuiRXOvCx2LC%2BZw5ogQxoKs9sFfxTmB5Tgr&X-Amz-Signature=1f5b608c41667fa53a55c68df24cff4066f746efa9120419ebe769293dae51b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
