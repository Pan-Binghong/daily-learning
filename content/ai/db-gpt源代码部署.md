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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWDJNNFY%2F20260315%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260315T035148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6ITDGfwiTczw2970e5I%2Fy5Kmbm%2BprzaWY3zIkmdrJCAIgbp9Mbl%2B3sgUu99wDiRFEduJ%2FflwcO1%2BzVTtY1YNOTqUqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIAcvRq55Hn6NBY%2BSrcA9OmIaCCryoTgweTGndqyQDptkIrzz72ng%2F9AyUdhJcKddptRPeacenw5wFNVc4LpDZv5L3qnKlK5dY6CBCmlozv4DD4Txfp6T6A9omJitcXrcpepSPolAvk1kFhKzmfI%2FNFdmdfFT6ks%2FBdCrOmuNmPphVOzHcixhbJMoER7pMTaPyaS4zQA5wZTaKKj9c6ppzAaAuGjUEwDm6CgZ7%2B9hUSRkXshzRPgK9K18fxbbzlIlSRHKqhCoa8AyJ5%2Fla7sg4Zr23%2Bw2ISX%2BH9eHiVaXZGlAaf6pPR6iphMVu7S5x2mHBydq7iZgeDT7%2F1lvFQFxPmXHubAXQUhSWpWo4noFATmzL4yJ51NeyWhc3v6lJxcCMon73qGmNvAsxOeNzo5Ha3SP1ZWAOKg9FQu0ZbBTa6wfUumycsNBi51SKRyLxY0x0ozI1fsX4erbOP%2FwqtrzvYooanJqha40nzLVU69MFoVQ7jhaqWx2SgsG%2BFefR2CaXHXb0T6vG2CzmfdXsLk0MrMq9m0uX38uvbute929barE838hhPwVbqnORLCl5xSzRiKRH0i8jE%2Fbpr8zRagLXhcwcQVN5Vxb4gfThp4CfZy5G93Ke0ktoFe3aIftEIlOKsllyyBPeWs5lmMNqP2M0GOqUB4Fl4%2BSSIzqKZSce7f4UIJWn9snCzmoYg9AR2P4sWTqz7MUrtoSC0T78yudgGgBhvNzZ4kGaHzGrp8ANOmeymzoxM1TVLbSn6sO3IgsuscbJIM%2BdqZYa18FUwH4AjtppOzl1yHs1f7swg2nCizNl8hVPmTbRRQUsXHvuCvp7e4kTVqCILIvEf7ehZ5HHdJBFTX8jBLSC%2B997OdVExAMRMC7jkr1D5&X-Amz-Signature=9949de5f451d324350f078423a13fb8b1d05a2adcbc7cd13e1cdc1a5976f4420&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
