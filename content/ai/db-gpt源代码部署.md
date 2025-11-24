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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYDAB6YX%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCja2Fj6%2FWLQKR0EynZiKPNIExq%2F4jyAXOuOzm6YwNuWgIhAIUDtkiiLYIpOJFWQTjt5pKlnGP%2B%2BN4exQ9jSytR7DxXKv8DCEoQABoMNjM3NDIzMTgzODA1IgynWf1Z%2Bx6m4BzbZ7sq3ANi8LWLwy5Le4WkyTHvZ0c4LRDpHTNvzXlsNTryjfifSR1vSr1PAuoXx8dx3JEANaUzAVn0lJ7utycZh%2F67aLPCri1QFu9bhm7V1QDU%2Fzm3Qla7SDEuJ%2B9dVOWd7elgZioI4qJXolXbzPy6mo70mDqLtCnpjsRQ0sN7nUOdAvpe778fppkGq2Ya44ZrCFBZat9LM7l0dekhpl20m7kN2utCe7xu1pnZtifUB81CemQ9Lfb%2BlOO1B5YwM9Q4ux56PRkSEmQkdys7Ki8rHpRuXcCFR8f6eQTfbD8Jdb0K8WSscUd8OF9ipdTu83BtTm56jd1Vwh1bEHTiKF5%2BuE7RaVL%2FynenWNAN8aHOhHPLQAV%2FanXUUMS2teJIpB1tj2DNkQqJnsth%2FxX%2FdMZdXeaEAQ%2Br0PfZ8yxdccGEu8Nf64KOcfhwjAU4fZ2icE4HPpImQwuYF6ufNFzN5I1PNwOKij6%2FmrU975hHn9bjlOxczgaxAF9PWAWWq34Xtq9fRhKrpn%2F3kq8M41RpJ%2FPYwLdH%2Bhj1ouawqobDmocAFIXEgFT%2FsPqFdQ0CLFITQzy%2F4NpDyOPrPT6YYD5g8iDWmewRjfkr9J1zGl%2BeLALFbg1EjxS%2BBL0urw1MGHVKJkgQITCZ3Y7JBjqkAYK3sox6126zAkZq9sNSbJbKzdxUX9TtpoN8fDDOBYrBH59nnXKSGFh3fF8cYn56qftLATzWkT9D9Uqx5wDCAbY6X4eGinQz0NopNe6sxZPYagJKlrEM%2BLbKOVQ%2BwFj5drsLucwQsDAZWonbEhq00poS%2FGoNOUc3P3%2BjmKqFgpZTcLKIJxLvpmbyUJL0yyuOi2ykwsml2upVGY4uj6A4Lcnvooq3&X-Amz-Signature=ad4c0e31aaafea8cc93b2d202bb7cae5f1233db10e46deb1c59ff71190434fd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
