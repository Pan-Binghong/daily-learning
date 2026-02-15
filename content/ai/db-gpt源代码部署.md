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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YEWC66UL%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIBoeI1FIDvTxAVVrDKNWF8MjJMye2tlw8Chj33z7ws55AiEA46ciLWlSxNqoGs909f2FQkBa%2BVPGVCAvthvzeLD66o8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDDXjjlMRy9cU4gaQNyrcAyXyGReepLkdZsKtqyGGqsTHdHlv7laUJwC2OJRYuMCW2z4CwICZ1NKTSBADj5AXL2QRDbPFaJmp8W13nPihRAi1i31BFW27D%2FMXka27CvDawKtk36J3CDc63xQvRn5RWUqBOONQvzOnSPeW%2FdyFMJKwIa9dXmuuILzEKMAHah6BDh32EZI8Y7J3EqRUE6fPy4Zs6KsCYgg5z88lK%2FFiYb1qU43PHeFLeQkhshJxOgsKPyS55Ob04ZEz2PBuBB0NqOCJSZ4PrQiqnvZXH3bN81E2FYhiZcNZ%2B%2BX15VZHBy0vwz6JrSDen4rU3tYUYJPT0TttyXtCsqV87fe99jBkoMEFWwZVaJ8My8diT4JulY%2FR%2FjCuhCzHaP4CpUJHZIWqH29HMnnsJ7q%2BFugmSVAC5RPoKVyUmW1SdPTkhu4YJdhi3x97KxCGMJmZXSt2Of6tOqzBNDsVGgyqobgGEX7PpCR3tNbwBHA%2F1S0kl26IxssDSGWvulPsmS9UKeAN03MdSThhiLWQff5PjnqaulB6QBUgffZg23pwLMitBooQuECUr1fx1SOAl5DEFInnREMCn2xJfnsfxwzQPd97PnTACadE2TXcaAKDnsxQV0zO5gzVUY%2F1GLpDZmy6dGpfMMWexMwGOqUBqAZebkbispCyg%2FmADrV53u%2BDVONHUiePHsYHgRFKmX5jDR0SyyzCpLasATRqxTFoXXidYsfz6x7x5yf5JM%2BBT%2B3xl002dNJYTeJ1Gt0YudXRvXO9PS4QAVsqoAUVOz5uQAmRx3AnBxiJ%2FxYzR5Pe4wkJ0CjUHAG8zwwib2egFEpEwih5W8%2BLKaKRzXgywGdVaZJrZs9gK4h9I%2F7bHgX6uc9FSas8&X-Amz-Signature=abd0e523e3c26a14b03f38dfaf42a3cf5d042a7a395ca1d3380929034eb3bc6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
