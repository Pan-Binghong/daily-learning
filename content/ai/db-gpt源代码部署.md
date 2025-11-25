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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662CUZVUJ%2F20251125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251125T024632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbT6xMt2uzXi0%2F%2F%2BOAgD8q3l%2BlhjhR6aIeNa0gy5ZOLAIgeDuQyU1FVE%2FeawFNvCOGt5Iqay8iy2pdprR9pHQVzJ0q%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDP15Q5nc5YaBKkpn7CrcA3T%2Bj31u3RlPTHN%2BDpW7hQBrxrU7VDGbSNefBR0hVHqucX%2FTgv1523onCM8Fz5GEfTThdde88UxXSUWw%2BtkUc%2FP0yfKLWqOO9Qs73gX%2Bf%2Bwr6%2F7Xv2vmUMJ9z6xyQ5y1%2F0qnZO5nbr5poDWduzjFukQeYks9WVhara6T55FkVS1%2FqdeyJmLfhmvtTnC70yZp7xrHIuIp%2BiRu2ngYLRzFXEABvONaYB2ZDL135xzycVld7A5Kd8V%2FMJ5d2HFo64oH3K7OrShgQor5E4xy%2BYhS6J41GZx0MMzAKpWX1lut0IiUb%2BIYCqzA8aX66WtApzsZD%2Bef2ggcp1EDXDS8L5pZX099Kinf0Y7cWOrv1iVOGdDT5jQ4ZN%2B4R%2FHNO80UV%2BucMWafc%2FwKqsrs7T3vufe9SHd44SXV96HqjyP8I6WdTQ4vPaTjR9KgiIL7K10Kze%2BA%2BXkw6fFoFPh%2Bn1FxDQovIn581XhqvTjog6EzvOJOgTbhs86j0OQBtzbme3UVKnuTO52kXi7JaKEnonfGBIFGLGDfweXcEsN3GOrF%2B6tORaFNQZTWpBt9shRrO%2Fapza282StOz6vHOL5rIUd7us1ZNctStc4ek23WEe767Dc1P1e3UPhcS7BcDw0gzQC0MK%2BulMkGOqUBSP%2BFntcHOGSjYiSsn81VX6ShgvuMz75QpV6PCMxL27EIKgAjWUVhFbc%2FVW1mMsiCd4SyV8GJC4HAUtSngGTAfmvWj3u0bn0tTh%2B7MJuF35PpL%2BCNGRYfen2SqouMSwf9K%2BFc8%2Bi%2BrC4%2BdupNbHFjdeBTDb5eYI73dWsILZdr639SZu%2FPy7YlamhhWRdK0rfoVtcrre5wGD%2FkBPrYPMnEJKo9PQg2&X-Amz-Signature=e0e176302e645efbec9c9f3d5bbc1b7018800bdbaa0ed6dd7a326145c72b52ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
