---
title: DB-GPT源代码部署
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- DB-GPT
categories:
- AI
---

源代码部署DB-GPT操作流程, 含测试, 部署, 注意事项等。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZ65LGXH%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEkC%2FXqn028qq6N3ETc6aqq%2FV54XnDd64jKxeC71xqdgAiBXvsl%2FO9WK8fef9%2B%2Bk%2BoJo2qZakb%2BYG%2Byl0a4DCRaeHyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FWuuwCgVlX68lQjHKtwDjSuRQQSR8xeTxZ6PreltUXGZT6MeO83OQCsKb1d0C1cJbDnEhffyU6cga%2Bgk6XU8eJviibNGd1OUT%2BgXjyg%2FVrM1nzToO57DW7ZWGvV%2B7nJfq7DjMJXNfj2LoQjsuLAUDEmmcg8YsDE5FnbPHcNjZNb2E0p0EJDoGIoUAebCRUtsNSM2GmchqbDKTzyRnkhN%2Bdzi%2F6Kee0AFLe5p%2FyTzKo7Vyr2QmrUVfNIC8Fb37ZfD8d2qYY1AsgAy1KQ8tVgWsvgB1pkwjmrsriIZxU9NPVG7kywj0eC4ywGlQMUC%2Bn%2BzPnDv0%2FLrEwBDpA1zDiBVkANuse%2FdPadWhz0qS1cm0k809Vmup4ttUgnyRSlPUzt2O8GOmvSb%2F95yWGt82AA8KYy7oYf%2F1u7vmr163dqX9RkSVg2K85Ak4RgXoAUZWd6ftmoU2hcVu4rtYpCUum3NMaeBodwt5ABELiQ3dgVLIL6jSn6hNoH1XIRT4RiyEbkDxf6lP1aEF9M3iCwecgQxsMY4uQWMZO8mW6jV1r98p8XK2GTbMvxmfO2Lj9pRj4C06Ingns7oocCFy2pEPj0ewq3yO%2BXfulp8cCxsYU%2BJLr9hSA56oyLrzBzIuXpavvgDRMWSPv%2FWzhRQytMwu6KsyAY6pgFdTgG0IpwMqrFJj699qYefq8rvOzMqtyMySP3%2FFaDTTe0rtNB1xQ%2B%2BjlAK9TRM93KkRINdhEPkOB%2FCiIbUbrVY0bnolsUTAmTSD8iOpaekPM942BD7GQ2jRQBvsDVGF3oGQPqL0icDcKy3kdAkC0ueg%2FJLsY2QMnBprFg72oIFKSsU2Wcx3Wkbdh4QJaow33YY8oBcAjOPKJFlmTDZp4Gh43FuJu5b&X-Amz-Signature=dd8718385ebc31c7aad90f17c7cf5b4d3e767944fbf40c6a42f29d8e3e59bf96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
