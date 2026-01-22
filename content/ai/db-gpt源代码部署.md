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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2WTAKHQ%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDCztMKUj5LWMPJ%2FfAgpHDOoHbbAWNjc3oiRSLidE1bpAIgCju%2F6BZcD1D%2BcLK%2BrbfCYtNPl0MsCJI9LvfxSqh7gQoqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLwFoPhdUJ75iDdkQyrcAzAKhfDQhUpE%2BZehbS8my4k%2FAsmUoviUKwPbCiP%2FUEfq1VKf1E8yx2p8FNbNnmrWFu83TEgxdPHW7%2BLiP46rquj3xOcYJflvlLduZkfYFjjRx6U3DMFV213nSCp9gZLDuc6S6k1OmbTepF9Z8qTI6KqIquFIFo6wL%2FY6zhDobyOQlUT4kD0fjeVHYuBXCrE5qv09rUtGUXYX70CN199xzUv1zmj73YL2UEFygEnY0i4cy%2BM7G27XtUzvT6UJ6AJdqL1TbRAbSn5G9aVpWP9CEL1ATegroH4cdhGt%2FuOseRc9wxj627ryuhv5ZeF9gsdRJvx7tDJvBvyq8rGgr%2B%2F672mr0RTTGjlyTb1YJImMLRvwfd1Arwk6bYIWr4voPDrCBV1szBl%2BqP0wXwSGdi9cROlvBsdZb0ntgWr%2BmsVl%2BMSKZBWj3aU7XpZh%2FpJGETjZHZ6phXQjQuXpHtPSJTGYOJsaLkkWHD%2FIuJT2camD00UkKbheu7E8kHdB%2BWRMMey49thVuBWoMRqxqqDIE8mgP9DUW932dLLFvfvfXMfbsgr3dl7TneibnGwK%2BDDpOKntjmnVQ869%2BZxGs9zSC4grpf4hPdVqpzXxX3NTDYEErogMrSjJj3VIfIAfyo8gMJLXxcsGOqUB4gBWuGNUR2SyDbKLkv2NuEZ62Bb3KS61QXIM0vt%2B50td73p9yUWExlZ8hlaH667QJJQoUf%2FgbXri8XNfRlgl2VxpThE5vaCTY2X8q6RXE%2Fw%2B94jnMESup2DBoHmSwYj7DgCcYAYDpGNdwmEbTPDtVSHvb2FBc3XH0vLlpwCs%2F8itKGoWsGKynWD1TyUFvttx71mbC1BPWqCRtucbONYpHUTnlQzv&X-Amz-Signature=6c0f18119bbd15f6291fca690ffbbd33bc819657d11f8f5ae8ce5c486b2b3b13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
