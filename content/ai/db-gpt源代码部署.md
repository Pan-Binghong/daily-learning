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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOGCHHRL%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJGMEQCIHPWbdtOJfSKNI653u713s1iFBrK37BUXbyimvrrGqViAiB8mlvcY4TfZTiqeGhxDtNoDqiL2TDcPoqZ5K3cRucJuSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMbfcDfDIFUy5WpAmyKtwDBrizU3TIXxt%2F3QCemipYBZE5KIyAQq4gV5jJOcPiqbRr%2BN7BXPziStS085vn%2Fl8Yv12iF%2BeCfqij8w34O6e6RkZ%2F36oD2o6gt6PTMzRvp6%2FhzOfPC6Eo8YMFitBpam21USDHYeVaRJH2FEmiqgw8yMnjXFsomr%2FRGCfflSsTG9SGRRg3ew9IDvy0PRUE6IQuD2Y0%2FiGNLzuep1crJ8RpUcP6M661lhnSty1VyLDcQzuS4NH7T6%2F6kI17Ls7Wc0uBeZnMUOaeP06LiAd9JSaENzgXsfBVnli1LASvO8dM%2F%2BYvWSDcksjRtdMrFvDa5jrZ%2BGmnG9HYsSA4OJYlXsRXtFw1iR6j5bvWlfsDuDeBmYW79dSN%2FhUswH1JWsTYnPHUAZ65g4EfCqn3yiqB%2F05YURPANibsyYjCQLcWQErxohSSP3cYvfa9WYb%2B9KWtEThuKqpLE671JBhTTKRacMclHiJZylR8d10QE1dVL88GwacobLKrI%2FRWUY2knAGQmLrkeDQn9LT4v55lPOeoBsBYZJ2eQ8zVUa4EFVuBf7kb98ZouOswakwT1XBIcomP536HiN3EluBz%2FxJ60x%2FKGWBVaowt95t2GQ826n6rTMf6akR3ayEBRPqvTK%2FapPMwqJa%2ByQY6pgHEapkuGn0R2YrUc6bMqJgQzCGduOp%2BiKTwOb%2Be0FhCoUYEH7m1xYn4kAI6S8eMPS9rzsoFNG7EU1gHHe1xNWl%2FYhhLMnyHjgjeYXaC3UWxqDkA3JDv%2FwxzolQh5bzK1bNi4wsyGfjN9GcFMvshm8lih4voguCVCttdbcHcSMAi7%2FQBC6o1qLzRMg9OSTyYSRkdmqLikxbfwV%2BAj4vXgjcrv0deiVba&X-Amz-Signature=3bb1ade0ac0bd4261859c8efa71e4c15ea6bf2ad6c7d6b406d3f1e32abeef34f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
