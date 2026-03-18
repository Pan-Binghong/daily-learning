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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAN7KUEW%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIFJFSs5kHEDPOqCeyeTW1W7v%2FKMY50cuv49Un2XiAKAjAiEA%2FvZNi3ngzSllThvHkTpNPVxmwfAJPu%2BAmpEBsxRadcwqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL%2F8SKRxvOLOdbeYSyrcA%2Fc8Z6618Abrr0PFUOdKITxGivH01TiB%2FnpvDKSw2Sla4FR1EWHDEgCSjmrJp8oEWQW26BQvqPtL27MKO1Ck%2F09t7h%2Bl66YEghX2tjTr27Sv3%2BgCswKgeNs8w6XnZBbxnDNmEGeosdkfy0N9S%2Fzz5B2wrfp5iKTAkQjY6rNn77%2BzXgNbAPTjTq0StRMGxCIPuZKKoyyy9Zzso159QGAC%2BgqOSqMg%2F9TwwbJ0iWsC5gHFUVo8xY1jFHeYkAvn1LNoXJ9FwlmkCPN1CaBt1SfRT9282nRxSKrKHWzVAgYuPZ5SH61cySBhxqiznt6vnFqNsdkDCfvqng24fMo9C1Liot4qJRAHX3JvtMjtszlp%2FUumi4OakQRNL7YlVKXIOYx1RGEWLVW3TIOLtzDvdFbUqfXV2ixSYpfhKN74ev%2FAXlOY%2FGrceK9zji%2Flth7JCRFIj65VfUypXHjPDvtaGmbpXVW3OcLq7lNfcz%2B5uFTjy3VuIMg%2Bu1MOnJeYTfwLUeCm1NzJ69xkdFrn2u1vykNerLwhy4zprXmhjs5s9lkx4bLr0aGEQh%2BU9suKjdlCOq0d%2FUswGYS6pF5OLZcunPY7yPPObWIi4LHqg7fI5WbwQgXN190Rqup3jHtPA47bMI2n6M0GOqUBRHIojAtP1MmwQ9agMvZz5jFl6AV2GPM6PetU0CD4ATQzQEQiimD4mwEoiElfiixl3iwoTdibuf1zlFM%2B9p45K9V3%2Bd5RZmlsuw9Y2VHkXiqheXjsyALOIwET2rBnqm4sygx0yrD318VUq0CuPWlrI6BqlgQ6UZoyd0dae1gCP37OiNHyYKCMjGs7dZf7Nzg9hSam5FpVM2bZwIajhiwY11W0HWez&X-Amz-Signature=eee5f2907152a2b7c82602dfa6b9aef219ab56a87f79e0b0eda104b4b1d6e95a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
