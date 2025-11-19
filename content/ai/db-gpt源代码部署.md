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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAYSL6DE%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJIMEYCIQDHOWiMe7SQG4P%2FV8E3NNRFtcG9uB3denUxoOhgHxSOhQIhANLv5DVzxcLsvNPu0%2Bhw%2Bkrf%2B03C%2FiuO6CXGyqt42ctWKogECNP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx%2Bq%2B7lTA8E5lWDVe0q3APXSRPT7ItTdewP%2Buo8wTq%2BAQP0vkgATNzm6GibGJakfgbjpi72eWrNbcY2heLPl8FU7KsJWESjLXunHLLpqDYBdA6Owxt8Le02%2F0KXrUbhwm4hAT3P48AHe0KuHgxhCswWFQI10uLvDR72p40zdZ%2Fie6IW%2BfLnnrjcWmSnEQg7k49FNEc8ac%2BW8pfHHhGM6hNAOBPI6GR9aXijyNAIer9mLdGeJb4ijha3jSqFXLC3j4BfTJc5lM%2FknCdLu9Gja8Q8nEp3zy16MwtYrU%2BkvkeMBoM8DGNbvc0xoTiLrnrIlbCbO7LazIEHMK3B5Kl4WVoFFPH%2Bnbh0nzNWBnRJuM75t67GD3uL%2FHXZU%2BvMzpIbVBc%2BR3IxxnQCAoE9dLhTH3qS2LgAj6UMpe394dLDRMqG1Q30W9xKsvMMWjmhHDRd3YVibU38vUp3GIbxneVkxA1O%2FySaq1%2FbGqRBX5R6F5iPkXuuCQezea2S1I5MID9dBr7PSSnqk8%2B0AseaHUICbbOBJUM72eAQdvbXnovB%2FXSmR8leZHBR1YWyPquUddRdx8fY45fRjoHPFHac8uuo1iYxkd7PAsYyZ4TkKI2AAxZlnkrKugaHoAoWTX5%2F8GrO0pYdvoRVT2aFT1FrljDtyvTIBjqkAZ7guXDs3H%2FG2ODhDUWmBl230tOMGpDcgU4wLuVeKekE2Iz5%2BgAjBGH31JAcCOGyofTJ95kqSUstyzbUKy2S4ESNLnyxymVJ10Sf6EbTUtBck8trLVPA%2FI55KohNj%2FwAJwAE29oZgq5ow4gonPCJGpcqd7pqYS8bgsvqipMNa2GERZjtLUkY9qjo3CEM6ejhXOxEmMn7IHje5zkKghBmKkV1IMTf&X-Amz-Signature=b40190480e01c49a2a44d69178ed24f4bbd6b840a7b6f2dfc753bbed9481d1e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
