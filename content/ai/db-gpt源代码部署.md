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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXSRN3XD%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2B0dPpn187dEW%2B2UpS5SdVD3xnRy3us%2FThWtNi6Q2bVAiEAlBo0SH8ASR2v3m3lCESaXiJEvVNUVXrV4h%2BM6KLmsWYqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA0eGnqHx8bY%2B%2BD4LircA9bX9g2XRAB3OpilWY8BcCTsJ1bdcyAeSp9rhY6EyXV8gFQsB7WVBFpNRSmY0%2B8Wn8a1YuEOjv7FfdING781TKCFqRTxhzybRrz1Sbv3fd79bzOE5tc9EvrzJTWgCZeliWnoD0e18JW7yaBsAzsdOZmDbPO062qQDxfgMIo3Wx2nju%2FaTzOXHk%2BiMJwNFmTx1oRuMS%2F0iyq5cCFmHonM4VCXTkLsWUwQ1DqZHH6I7jmXajhgFrH286ThOgV2R2LxCtIywO6rNuuXyWjUKzO4kUAM0sxqBnkJdK%2B49zemiFZ8%2FkFR72SKUD7yGCwsvG6n1H0KBcppCp9%2BfMa9a5bTk%2Fm%2BN6nDhgt2OV9qnQEHOR%2BI%2B4SLAPRJeOBXJNvLJ0iS0uHxZqQJtfxRhMUcZyC6ZQVZ3%2FezW%2BujC2amnrMM5Q1WuWYjXH9eWQT8iWcVcTiEy89GwwKVP4evg0ghFaX1K7EQJz8Y5CjDg%2F%2FXZfJjYkUyjvDQoRJDhfG5n7pTuNedxETF3zMPc8GJ1FcgDaUE20T%2BNbwTTOceuZei8yNSgFOyMG%2BMkxH9cdF85P7IN%2FSogw%2F9k%2FAqhLhw0gUwhKjj%2FiEj81DZ0H28WMe9ugulZSl825Z0x%2Fr6RwsNvr%2BDMP%2B1mM0GOqUBdRHRr7QR3Cns6OayXaiLkGWtHhzzBYerOG7m6nKGiKbr2Tn99fc7TQDBDx7aPyjpyepkns4SPwUcksAdalnKRnojvmyt50vlmrBjKLcAYxhHuHnp5Cowo87v%2FLLjEYxMUO0HgbS1N2kM5XJDeCenvSJod%2FyNnEuv42tkm%2FrkB5XIn4cnAGRuAss9V4eTBklPAB6TCeXnkmBUq1HshYKtPy0rkLxX&X-Amz-Signature=1fbf1fa50bb85dc3cb9ea9ace0a88806e771b3054745717db5b4d1864e7ef4de&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
