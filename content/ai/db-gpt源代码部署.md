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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AWEHOTU%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIFGhIono9hxVvmlU7rzj7vp5C8AMJyU0QBjTyBYinBcBAiA47O273WEPcJ%2F4elqqyZ%2F7F1X95yoSNCrW255K1bq3IiqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2B3ncciVW7Q%2Bue%2BuuKtwDKITat9RIAgJITdjQmamQK7D%2FErfejquXUZL5hsGegF0%2BIbl4Uj5HHmHTtB%2Bo%2Bl9Zf4fRDc%2FYV2uLX%2Bvi%2Bs2Unqapmfh5g%2FSdLt2gCpdAReDjruYYrGLbQEpeeNrsANJWEcY%2BpztwwQRP2ZAGIDqgpY2iuIJaykosDdDooAcBYcNkWtocuzVoX13SzfXuYVWcvghjKfxQNJ6cJZa4%2BXjUaBaHFs9uqUSsZzEgRsFQsRRh69KHDRKLUhRiEj%2FJ8%2FxCitG%2FDkWHTxdctzlUrPWu8sZ1kXoPHiO%2BfzkzMr9dm18bBH0X%2FVX%2B8zvfbPRFxsOaugYggDJfpO9bfKDsZKLu0iE%2BwZWpy%2FcTOeUlb9GgXxYekBqVlt0taOft02DejHcUevYqSyACJVOg2Nxjd3yFk4NfMxR0Yvel1huDNU0iO60PfY7Lht4M80okCacLVFGKSc5DxSRSQkY2S5zHdQir61UEaOUEzclUhlZ%2FO3AtfNwAJiaFAWFA3BeSDNf54nEH5K0ZaOvGWIQ%2BZjxP4vZqNT2vLzHmcDqKGpH5gYD0bKUpT9nLSq5cx1hmyMRv7%2FktB8Ypi60PhCRTUZxbVOHVlfovLWTPCKHfpt2FxHZJ4fFrPrOi1KnkcZIgzpcw0rToyQY6pgGbCxx2P8uLx1TxZGEi69RYZWcSwaI0acAwbahzspUKFwvMDbZV4JbGCWtmLYHezVnTpZ2mIF%2FPKhWMD0qAiUgWjD8QlDdiuF638A1cUPxA7hgcYHs9f1rqqySGsm2WtcqhUrANw%2BDiMZ7KKhev3cPfqMP8nINOzh1G%2FWLuIV5thvjS1hjWs%2B5RWaP8DnmRWciljHXKlZcEvl%2BEK%2FH%2F%2Fe6mlq3%2Fsx2t&X-Amz-Signature=6b53fcceac25a181f5c88382d280aa26ed284ebda9d034ef688f9aee5f2231bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
