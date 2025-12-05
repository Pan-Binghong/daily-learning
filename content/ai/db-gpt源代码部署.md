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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYGGIULR%2F20251205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251205T024944Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE%2F5WZWnvvHgs9svaLBl3ClVu88buP7Svpz7xRdppW%2BEAiEAlXYCQyPtmRPcKXZ6LJj3u7yHt0RC%2FAxGn1a2GcwJ%2Be4q%2FwMITxAAGgw2Mzc0MjMxODM4MDUiDJH1dbfi8NCawsyrvircA%2FwSfmngKs2Sk7TRFsGSirm3F4lEWXibcrGp0g1nrRjYVm3fPZ7SmC2EgKG%2FzCI61%2Fk%2FlEaBi2DPI8GACvQHS01Cj1p7FLeBGEoys08nn4GUHQZHJIFsuPNp1l2dUvRMf7UutY5fGmJsx5yDIyjhyA0g6PNdTLFVlJEhe6lJcA11EyvMII7J%2Fs0ERDkTB%2FC9uuwPHKPpwuzOcYo4XpiIP%2FD%2BpT8GlD3lsFPzoUD8%2F1zu2V5v4NL29ybK4bwVO4eAI2r03Xp7OeZVUlB92ql0cADW9%2FWXwE5ReERJGWIHITKMsdKZ945JNtZFBXeMfJkdv5aPLIPBavoavVcN%2B8POcSDULiiXMF8Orx6TurHdIBZb0kcE4ii72Q8xJAINVDysFbbCO6dlpqO%2BdsipYefWXR5dKZ5GU1TIAmgDXvr1V%2F6Uk8J%2Bs%2F%2Bklp4Yi1Zbee6qI4VfwZKfaN%2B%2F3KZJFEy4xznbR7TPdGbFtXEboKJ%2FpI6550RAWklkotgyguVWw%2FzNdwUV7vdi201qnMnQ%2FqxinONKycc0%2Bg55k2SP%2FRAm7YHDPey0toHmDrZKOqV6Zn%2FXdcffjhU%2BSRSFVeD8uMq0zXLryojO50%2F5uz2Ew9MLT5TiAZA5YzHJ2LYrdz0yMIaNyMkGOqUBjG75MJ0AoOj%2FGzaY5O94T0unsG35lKlwkrFU0oCPCOFr%2Fb4uvp4B3%2Fb6Nx6idMs528P12nkkpue9M0NhSCOpjqDqRH4zleKeNkLybJDHMpLwKv2lXh0Zc4GyY3E2bxtVFWOkAMY5%2ByRMs28wdy10vrA1INjOcxVprtwZl%2FvtgW0yifXILbPzKsH%2Ff%2B1HS1SVtEdJvBACXyzanAn7Xoc%2F%2F2OQUeGF&X-Amz-Signature=4a944700d1e53bfb5a5c69962167ae84303adaec4b416f1abd25d2f72b9eb09f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
