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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWCWBEWW%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T034853Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQD9zBYBo8AHscdOj005gflZmwYYsLuvyBkxaj4m2k19JQIgYeV2e%2BB7clSreyPRR4UPE2a88QzzckZi%2FERVLEc5groq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDBisDtRGTIqhJkk8%2BircAw22YaXfJzBNECcWWrUBjcIRt2ZNVMWmuB50zwAOn6FtZv1t6dXJ1t3KLB%2FHrh029lM0%2BJ849u4EocO1gQvob%2FJnOHSvjxTxKQNIdGzRPiVE8bbQklJos1bSBU7KQGIXE%2BDRrEMJPwuV9ekoSB1ZpNkwawvwtb8PsOhKiYlWdOCTB6ScL6bpu5OIVYfTSZAgqzq4CLFdQTAPzlO9vB8lYNVmdMLqMEvC3O8yIYFeMfec0RPHHtmYDxYKpfU8g7lYWS6axQHKjLbXa3%2BeV4pdnjzbE9qi26%2BAoeGB33DoUZJ6jPTWdyD55mbstY6VzNw0rnsYE1AIa7zpf9BuIDnbc5wKiECpUw0mt6s0%2BjXBC42oAPWoLC1xZb91td%2Bd72ISz%2B6LHxGrJ8cjPTp5J%2Fv06dSSl7YNcxFhCx2BYjiCJO17zYoV8g3R3w3ijIGknM9m7O70KeeShY%2FEjZ6r2JBhB2KWiBS8x3dMe%2FYlRnkWcBl4Feubquz814HMlfQoqkwWPlWvIrsO8VlFk1PLExevEQkyqqk3Wdsmt%2Fmu%2FsWP8cPWHC1KZXzmTBbo3WZg2PiZH0K5%2BTgRijk7HcaPjNFYj80kK4L1tQdoShK%2BRbzn7W9MUyMgsBrt2wJbe4%2FIMPyy3M4GOqUBKI3Wgzp9ENL2LnfYKZuilFBUzzOyodUUJmbadXT01XmXUFJAMxXCj3PYy2hs4sxiFa3%2BtIEO5rO0bdmj3ojeKa%2BfgQTYdV7FtlI0t5sAwdx%2BbyeQBizam0exF32f5RSiPKOhT%2FyRTgGk%2BicUpY3HX1mSE9YCsbSoCF9BI9jPp4MG7OQYUqelpSrTmc9Hx7zppyz4LufKG%2BFhSxrByAczwH3TBCS6&X-Amz-Signature=8dcc86c6e992d03c204c988d5751ec1ae100c51493335768f51d5cfd3417f074&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
