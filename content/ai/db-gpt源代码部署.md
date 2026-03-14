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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOYH47WO%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T032818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEVRyOWT43EMkPeRRRXO8NbqyPa1BlzGYjp5V3SNmbpgAiEAifl8A9xesHhPdc%2BRGYHdiFvArYZSNKj30N0%2By1fXXwwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFs%2FLw9BlbM4kOQG3ircA%2FxIPq5VkVu77JJJmudT5sHE1kFCgY%2F92r7dBWJdZTD3BHcD2v2jsZQcF2N1le3JlHvVm8s%2Foq37h%2Fvp20Jdy9lbjhkRuK0gFTuS0qQ8Bi83yaTKTN0Ab58SQBDr%2FrigZig9RDlOnxwnuOhKv3DurtzGVcL8rX9xd9tej4dD2g8i5SRMCUQ2iuWi3Q5hYv1239Kv4jKZHdNR3sxE8qJxJzyIdQwxIEyMZ8hMtyzpsTNgYin2WyBpK2hbhjsh0rifP%2FAG03FGe8jUAU7JugW2SkYngkHgk9mzhS6cixzzZaCHQxub94WyY5PUBeK76CvBFBjQF7hX6p47zrziWll54xVEq6qsoi7udtlaKUGgXSNP6Usp3DfL7qaQdUFgs96KH%2FqniUSnGDrQkyslwWPG3Kqwk2LDddDuDJe%2B6NVgLtvi00WqsNb1VCLj0nPewetdHaNYBZGH0jGc4F4nzb8z%2FE8SGN0Pf8FiDy0trJiBe83I%2BURjltGkNVUo3%2BJtwp0jJ%2FPcMq1C4%2BH%2Fab9V%2B74Jz5Nbd2P%2FhWNzBwiyv0BN3mjQGiUuhByVaZs7yD%2FzXRQ89mWieDQbRS8zAuy28B7VaYQn%2BykeQhRFY6EW0wu2PIYHlM%2BUzE8DIAGvMKHvMNuC080GOqUBCbFEU1uAQZeEwvWNCWnfQyDsVB4oLLXPvpSdPIamdGqrpsIil5J0y16F4gNRfTKeuxPr5ZXpGjn5u%2B8SP4rVndp68K8nxTPLICCLDokjevCl1%2FboJ96XBvsCevGDAvznSLuutuW9ZNOXrC8IwHPqdt1mU6dC5lp3C1yYS3f5hbqgmKNHmzNHIsUTXgJV2sNUUEUVfpRWwbW3wJNddGIFURj6bU1%2B&X-Amz-Signature=4eb4013a75455ba71b7043739780d3d52dd2b06b2a88b22ab42ae74f4714ba09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
