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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJHFO3U5%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGKdI9TCIhreP04eOGQVFpv95dknB2wmWimnX2OUaoB%2BAiEAnnzyb%2FcQt0l09%2FzzeREbpWUvoltkE3ILvy8hcD%2FSYQwq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDCmfG0V%2Bygp7hh0SlCrcAyEZrEy2op%2B3wogQ52Y3YTfQnr9dwSOG2ZcnmTeWOgF5zgp5kaELrYM4%2BCPJrQqzuVHpdrpgigRwxaVnP8youNgbllsQ0k46%2B4vrAT4kaGXNfRIhjYVSEqjeYMyO85vpsK4qnZMvtGplPB5ThbjOCgHRNIN81LXDn4beBL%2Fw26Ajs05KQDz1Ca2oy5OAmNqPyr5FKmx2%2F1hDMDMpVX0oZGKwqKmb%2Fgmrs90wS1fR%2FM4a3ehftL6D5w2OIKPq55fLJYPizTPCZ0rBtanDBDW5%2BjsG%2FKMThoWHBKEC1T%2B1VJyaEFE16Z4SW36Fi727zM7lRTcy2RTCGcvgrvsXqcCzcaiy0YsifpcIPcvW3EsWsl5yDmKMAAYC%2B10oxJmzG2T7V8ucOUK1Rs8zUVl0iIRzJ1d4jjhevtE3oLORjnYCuAFzBm5L1tBxP0tS9hWJnj3V2pY1011jnjp6yF2bifhr0PGc%2BLcO%2Bs0be3zqyJ1bbMC%2BGPiI6XcfvG50yEZZU4R9uG0NOVsr548ew8GRzKGaz1UccRPE0X1V9LZIIKTs9SYzqqhGSfbFa7eBo6MfcnJRchmMtl5s8CU4RxG2BcK%2B6VVOCNgW8sKcVfdNwCOXCidWdiurX%2Bo7SepfHxb7MKjk8coGOqUBcrehdBUX9Qam8N6o0HRZykJ8jdTLc9YEKiDtPoGzssU6OwR3zL3KTyff4HPAhmUFQLQMdp7kakIkwgB3uq4XvghKIZ76uFwv6Iw%2FyRJy7Hrvnq2nSmZkAkJztBbDUGBpQvh%2BznBzgrZdxmynIFu6f2oc1C5BC14D5ScmXvwxxT%2BzjwQVf8ot7iyouXTSU6KQlMFWssxzP4JwYACCE5Z0bCcH37u4&X-Amz-Signature=2a80f210cb61381738344131877fbe3b2cd3a2255ebdf95d646473fcc5cf5190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
