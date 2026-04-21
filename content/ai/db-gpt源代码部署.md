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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZUVADP7%2F20260421%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260421T041322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIB4ilaja7L1LqeWQ0vKEA88rDeV1kVwbncIKvRdhx7VbAiEAkisOrNmZStF%2B2ljMdVX7kqeIZHQe7pCju5RW8YDv9iIq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDPhgaRc1GisPgvwB5CrcA10fqSm1XUTX2VsiqzmOq2XCXH1ckTMg4CjFGjxseeThEFVRsi9x4alXrMLC0j3fzYPWV%2FLGegVPw86rFZ3HiNiollY2ES6EIq3Zwe0puaI%2Bw6hQLPvRzITl4wc0YZEShpKTZLtbFaS1Tm7zOLkr2VT7o2rsVrKxR0jxHEUS84radFnFe1XAzjCjKXXRUbEZFGcHeSI6rlpyXEHhCBCUmMAUv3faM93A0ItWB%2B0Phdtc%2FVKPF9RlSTyrWVhLhmsf8aWlQs7OzV4XxTA%2FNcJq5S8YUA9kaGTiKU8Ke4ng7pHYFdKF0zHL9wn9GxUkYJUppMUl3%2FCgGQNY0Pm1mlwXN1Lcnx7XEYvLhctGBFv23BXi3APfbdyTx6SssXQ5RgLzek%2BsHjsDPsbHfubbZ4VrcW1%2Bl5pM33XKufAhBrt6GHRub6o2CaeCbrb%2BenOcKN4QutUocfmX91bgje81NdQmUAsQtADV7xXoNK7t93i2LsFEoH1rwMbEhAfKmK5cwvUFO8hZ5Tl0mYCsnq%2BA9zf8Ep5%2Fjd8zqdGkDal8GlrfHWpDrX92DAZNSD4mYF8O%2FC2LuuJPxQUTvn3pMX57rxoX1cpYEHx7D8V7gIFUEUD9KsSN4bMGN5ZsKZsINcZdMPPVm88GOqUBFG05duKp2n1W8R9C2hjwvfE%2FrbFdTv7RlJ6hQJGi%2FpqY4jGgFmK9md5Y6A7OE65NWhlUV5Df6dOlss1OZ2fs8saUERxCeakyf6aHXa4183TLxjA1PbTfmlZ%2BHEIkUuMTMq0zFfe5TnlJM%2BjZQPsNf8Ct0h9tlotUSdMcMDM2lE7uA3EqbNGP5PbFyWv6Oda4IsPPbFGlxNhJDbgyXhpSg%2B2xAerV&X-Amz-Signature=e2346363ad0701f114fc6e1fb8fdc92e94a44f7088a1bca6d946b3ad0259bced&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
