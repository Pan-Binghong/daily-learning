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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IHRT44E%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJGMEQCIDvdwgYWq9uMNfX6LV%2FnR%2BUmbrubgNygGjcIUNm2FSIEAiBZzkywfQw78g4VC%2BRikPUZB85yQm2hmxvL1YNwCtAKcCr%2FAwhDEAAaDDYzNzQyMzE4MzgwNSIMLGityGosuvaHEDZzKtwDfkfVYULI9tA7hFT3u1L35b9GTyu2ZArjMHa5YkJ%2FQRgHAGkueBOv3oAdTR1AijK5U6v0bxk3EDHvTWVw5GHQ1zv%2Bn0cCxrGVkWyIb5CWPCjvlLRax2Z7eCMhXktseTZTtqOOhViEv0L3YhBUx1muRbSIXMher%2B2jVdCCDuNmcfEYnJe5LRwzN84J%2BP87xv2TD%2BUdafN%2BhvtsTie1ho%2BYlP0YuOGC6fgjZ4QriYRrzRJlsIt7vkUtrf4WQh24or%2FBi9rW6h14QpPDue7P4p1koRTJGXHpNi3kVCMIjyZ7qUGP%2B7fJVRxQRYBf5Mu9nOnMp8%2FggtB46DOuFnYcUb5LUjYnQHCHZr6lbAs85YPSF51Pv0pw%2B5ePy5G%2FGQ7Y5mk51wLGP8%2BqBqyWke0XMe3rLy%2FTtu2uL6J4iFQDLEqLHizI2iv7W9XgkN9foyLnMq4J%2BU1KY6OUYrU5GUshTb9fmRujT%2Byk6l9sdAVsz%2FFctjHLkwHKXf8lj4kNbnAwsBtGQd8ihaHINgMl0ragZHieFE7KCpLKbU4K5WdhBC%2FTMVd%2BF63UnkPrQ%2FU26SfM2Tzz4V6SDQHtRGtFbiYFyHjCGE25v1xASmus4lJU13REfF1ufQSQqjKfc0D6feUw1vDUyAY6pgH1ZtXlqXsSO8z4uIrRSh5FyhdrKKl%2BINLsA%2FCH9SjaZQepdTUuqg9q6D0MLsWPmLzluQhiJgetzJ%2BI13vP4rnCcD3lspWavW7JL4M9JZkU0GrW7vC46jwaO7V%2FC8%2FpAS6TMiTjQ%2FqHoAH0p7giqTp4k2goa51An1zT5ztmtxKLwiP6mBJ17veVOIeNW38UJs1arQs%2BDP%2FJ3SNC85IcQyg3vER%2F5GFP&X-Amz-Signature=af9be82ac5da066cec9f3b54e0466ac3643163ff043f9736257ed9444fafb573&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
