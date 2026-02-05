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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VFCI6QT%2F20260205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260205T033410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQDy%2BrJY0l9JZN5G5qX%2FDBUaKoO1yr7G9tSFOM7HfOWRxgIhAJNMfhJsyLQB%2BCuwejcGJ%2BXw1aKrSXoyDDbVGZuoianYKv8DCCQQABoMNjM3NDIzMTgzODA1Igxnm7Fql6JYkldkit0q3AMaQY7ZUlUg8fvFU%2BW%2ByYQ7G%2FNlQY%2Fmmke1NwR1dC96hoEL%2B3%2B8WC3pZC6%2ByXU3IrBHoekra4LVE%2F4Nytc8oIFH%2FF7TNS97xQI2z1YOE9Di5cLLjacLifAGTBRNcrukVYiP6Wqu1KYDow5g4ZbD8GvOXjl%2FZ07LFsv6WNSu6FA38FP9Zq%2F7eSU2cuP%2BbllpQpP1VmliYWwU0h%2FMVOb9PKcGVtrywffUS9gzqzDVwqBzwqUsi8Rfakttrqf%2Bj8OLcwbO%2B0dlINJKJjI809r%2BGlRxU0Fn0PXQvwcxV%2FRkqNTmUdCwPv%2FI9AR2aaS29XaBZTAQ4T2vpvR2ARzsf2PFD2hatYHi9lvmReXYIV%2BrdZzR80iZcz4GAivfoJnO4QcL7js4Z5ZYUxxxiE451xCIFcDHWwkkYqYkjq6ACnxYR2GHTFZ2kFFAGYP6RWkCo6iFDxnV%2FCuKO2TgOJamracZaqsE9McMTLy2X4Z5AVqnxURpmKWpnx5Y9RAw6bVvGaY6oJ1nfgYceNHcuki9oFBSRnbSx66udXcFACZX1vgQTcwI%2BzUJD2mXaJ2ypeJGkZIb7c%2BvKKfwn2Ey8xUpvgFWsdjF5%2BXau4s6lFKzEtwPixsCu%2Br9nuv%2FINppvPBfOTDGlJDMBjqkAWTWeggYmVEh2RAPkoLN1JUy7OFT9tcn20mjz9p5afko0T7Vgj4Asd3XjnQotLCsLpMThqypPuwc934XG10m9fC5Rhr0Yz1AfHsZuTXGDxbycEve%2FpwrqPSjajbE7hqrmGu%2BtcoT9wvqqL02S7Dk3dl4DOIcbo07m9ZhRTqcaBocHMxTHKuCtJwJtoZH9FuuQgUYbKheBqnCTNTP84oXf7AtSPRG&X-Amz-Signature=84c5356337641809149aee0d6ac82925a80a5d265fe778f503a4d56a0e7c2d0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
