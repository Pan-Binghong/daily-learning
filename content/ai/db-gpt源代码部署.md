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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXQBA5C7%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCICKJtpY3Z9mXFBnoQTpWY4BxodSUBppqjgv2fGL1V%2BfKAiEAjRkZLwm9QFrZwiZa6pCpujFX8lruvzP5e5HkjBYXasQqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA2fyKW3Sq4UlhDROyrcA%2F8Kf1JJfX3L6E%2FPKmDghOlAw2g1OqNLDYsVaB%2F7ECFggwST4hxnedSKvlnmkEr0vsx7LgjF7F1YXY60Yb%2Box8jnT%2Bh%2Bi%2FOGnLEuNq2SR8z5ArTB37Jo8NMf9SiJgk4tPc3CuDaH1oLXKOUrgGq%2Bi2nX6YSjxSKKQ8QUL7KY4XzqQQ7eh0hMl%2FUbvH%2BSeU9%2B8iG7OECGn0LmdavSkI1vxE%2BAbrcDf6sjU03f5D8g%2F4T%2BjPsdDUhN%2FRjdT7yaaXB4flYhMG4yiadHLNkrbHKXwfJHiTI48xZ2%2BnSNZrwWMMoxPabHBlt9xuHuuZ5LvQ9ZLZgtTq%2BNGpES7TVlZ8WZwkH9E82piGGETRQpc%2F2mTJMnaVRutWKuUr5sbTbdeLvSrKF4zjPAOSAOEuhB9t4uQVqfYpptZ4Cbe90JKb6zub85CWcSM%2F0GlneWxDjrFLGm3J41GU%2FNwZuvgBdYYSjACkLljBIrNZNSfApXe3psiD7rULECLQZSTb7Fxv2moqBfbJBQ3hJqUqE7ycrTFveeACFS4FVdWzsNGJAu7i%2BzpY2rcb1u64KOdX2hTxcJ%2BzrkQ50wIMHvLADiN8NsMIUshbR47t57iVSx6uB28sY3VDkqKr5Ke1N%2BXFMOg38uMK%2FYhcwGOqUB1bxTdEy2LGCaXW1JzCbSGCOgFhdXjQDG5vJg3W3lqLSxw0ZG1AoreIxEpTnBYvShbKNY0P1RaB1yNSTCdE3ZXpYWoKNbf3wfsqqPiatobqj50VHZvvQrzoRYYD11MVtxnvy%2FcGnjuq0lItwq9xN4%2FvQ4BPXg8cVeAE6Fm%2BGm6iB9t2%2FzE0ddhkn%2BLZ58yD%2BfwN1ZCZX%2Br0OQ%2FU%2FJLFErEt7%2B7GZn&X-Amz-Signature=105d26dfe8d0dffe405dceb5903e0a2ae8a1f2a90c3ec84545f5121e49d75fa6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
