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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y2EKN73J%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBaHSjiNig%2BnptwLSbX7Qvv1g%2BvHKAXorUn1p3gx5BvNAiBcFT2HBir7uEtk9%2FuRIfV53BCJudYBhjL%2BppUwQj37bCr%2FAwhNEAAaDDYzNzQyMzE4MzgwNSIMy%2FkTSWfRCwzClVj7KtwDk8uuzis%2FitkY3MNX9Qh3ibeebxmhixVw84sW7gLvDV157yCmVGuJmC8kXWOJc1inIhYd1adI9a9MQcypmiQu7MhDFywokgmLizhClUNdm%2Fst%2B9rgeqPA9AKAWgKJzPtT%2Bo6l725oiFqL0yu%2FvRMoqM9nmbg1J0bk4vyl3Sd%2BlFMh%2FJYNYi1eEIjkIwcmTA9GcIgltNNGzF37UeTulHxLg8%2BBGU8WNKW8HSwYNHk%2BC35XaoCZa71ExXbok%2FyriMtOjuAmi9Scx6QBuISiFrr%2BZ2Y4iTiVXEeVXry7mHfS6nD2TKayvvBa8axPJ0p9gFaRA8fix%2BKAViMu3RuTPolE09OXA9ZycoYNiaTRBhxskNKEOA94MD2s%2Fe8cGdO%2FuQFGhzFS0Ln5FrGGZmU04NmwcVBx24EDy8DZdUbXTQ80aiJStprO9IGdSp%2Bvr8G9MHRd6mdWorGAm5q3Su3pKhLWv27YeBrmTTiTX8ZLVo0qadtS3xcro%2BD%2FEFagqZGxiZxdx5pgC%2BS9ZmtckeWWEM8xQ5%2BMmIScDDGalDRBU6Iy1gtnIvBOFX5O%2FkkFMJIZXhuW3tVtPMancNiZy0b1iw3HHXMUGd%2BY1iYvHwQ1zJ2bij3pxkCdEyyrfqW2L%2Bkw66KyzgY6pgFivL8q%2BKTBzmnaAjji7VN2BNHLR0lIRpuYR20cHAKzG98CkplPsSYGyIeG0SiSJQB6mn4vwvKAAGGJSmLGosuKCfew0A4jG4%2B7ZY3fl4pBLq6MAq%2FFRpUx%2FJzu3D0vtzCB4gEb6iW8EUjC8Td3%2F07F0HAd%2BitIDrn9D9Jayx%2Fefwt9fe6P9kfcK9H%2F6P7w3Y3dUKPK6CZM0ZDPGZCKvjJMQYKpkG9G&X-Amz-Signature=1aa699d73684eb09841302a5ba94aaee2d368cd2baf4e13af82e515c41c67c17&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
