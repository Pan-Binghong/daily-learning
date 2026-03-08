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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HXDIAGT%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJGMEQCIFx6ZDSGzpVdF8SNx8%2FPnz8%2BAw416yPHMNGDchaY9PPqAiARNO964tZbAQGFz1gH5jpmhUjAz1pB0ZqhNLXMJ%2Fh8uCr%2FAwgMEAAaDDYzNzQyMzE4MzgwNSIMsjX5%2BFGkVcr6CsXYKtwDX09Ta4MDN2olfw4XrNfBgcTpB5l7RWdFNb0FpVQzupT1c2d09aSVIKTHDeC2KrmLD9X%2FGIbIqCGFxEFgjPqtdSqSuhbRZmP0n9jRmRxNrF6VoLUJaOjaPghU2FFtzPkRkJMWbAvZ%2F8maSCuaQFoRKDRroRy%2FG9m%2Bgnpu5ZWHCuUZPh7Wpq%2Bp2f1EWOuCz%2FzfK%2B%2Fe6ME7b3Ytrnd6zfNSWldJK3tOmLP6bRfi1bc22BkII969%2FCXwP3o0JDMbeWzuypW7R5PODiAaQlOz5RsGEveHg0MGGEKCQrn1x5Wn1G%2Fe3pmj3WcCkb%2Fw8It9yIH1ghdJwGX2rTfYTb%2BhQ%2FMYvl1QD3%2BvVvLNl9gg8rFRU8DgSCYSjp1Ah1zJgobEv2DFeFBq%2B62p5WoyVvje9Ru7ldmTm%2B%2FbyziWh9N5gjl8EIoPBhiH8nJ4Ea6eU1hZUHCxXwDqBkdrbsxJy6xwMGxIEVKKDzGEI8GuEJ1dfMKsYueQ29t458SlBs4PJ65LCt9%2B0S7BGFLBTvn9PREMYYWZN6pcxMldUSBU1mh51Mro6y7pRBPHFSKIfQ859ZdJ7TuXIJICM6pYgganVauRywHmTHIZur%2FduKHdU5ZEBuvAH2oxuiHmn68EGiLNgYAw%2FcKzzQY6pgG30c9wz9ERdfauq6YxfcOJzPVYsuINih3MfJ3w%2BksOiHNdlBDhfWHajGN4kiilJiHd9qMT%2BV3hu04ry57en7Yb70nuvaY%2FNlQ947UbumUMqkN9MxOi27rG6fcr2RNVuyk40Q2VrF1Z9EKLBWpTJnriBRwXhdyzET94xDpCug5Ai9Vx%2Bkh7xzUNENmAvW5JX%2Bt%2FUXcVdfePrZvwpT90I1%2BCHwNpYeVb&X-Amz-Signature=b3241d8a35902ca42286aa821126cf47fad1c4d5f671088c0f67d39b56478c34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
