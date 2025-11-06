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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MIM3TP%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBng1M4JvadTTqFtwGXveqlG8UrxlPMpdPxF2RmvbcNhAiAjlRJUKOeDl76dL98hdYrVyNgKhz2gfZ5K6DPrtCBMvSqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRRBFFV%2FcB3LewXjGKtwD7IDlph3t8dz9%2Bfzfn8vgaHnATL5XjKK6TJqV1xC8Mf7MxxzjvAm%2Fv83lUxiR2PjwT27tDwWDDjEHE24wj0DNZdxJjBg%2B7ziX%2BuHZ%2FUDJlL1wrkpqGhdDzlDv6oUj5zPQt37pLU63tPS6bEmU8SG6eq0Md5xqBzcmAfjZPKhELDXKicnoU2mwM%2F%2FK4XjU4VDz0D2%2BdK8yYvciTsJtWHTIpsx4dT1WZCciwr85G%2BkLNIZEmkzSvRBdz9m9UrMnHP80ixd8aRVKDidH08ASuHWKEA0ENaP3M5o69QvLzSCOlTyhXrgmOmmiIV3B4pAcaIcbggAU4ZT0QUNakeGwdyUPhk2EGyc93ogAUiMU8NGAJnlOm8mg4rVjBiE2OnhJS%2F8WqVeWy487cqAe4bOqktIUdq73Jo%2B1ZvfOeRdZqxKrruhVadviKfZ7rWw1%2FWPEEHXCfz1Yy4wxDMnv1qS%2FyqbcZ02OUtDbr%2FUmjiPX37gVSyJ3XPcnCpQKp2fGcD3xHnhYiBC6WdWdsvTdQkI349IUwAsfzXsrWly3m5VoaAUE11cwmblM2%2BqtWdvwcSc7I6EB0X4hgvsZ5BP4xP4uTwCe8JXnyiFcP3M1acTFox4yttQVFZpbUgaFX9BnY0kw%2B%2FGvyAY6pgF79vMb5QirDoZ3v7CZfdZ%2FjTMSb2VSi96O1DQx3ka15dl2eb4SmoLwf3FtQLluQcVb0Rd6s1A7gUnNLU%2FcXnT4IK3M5Fj4MNbnLnjRp4AZ1zDUl%2FqO8ZxD6U7CLnyADQlc2zCBg%2BfHnRoRtZn1Jlq5fosjU5EAMMri2Pt%2BkSCV2OUXyu3QR6Z%2F4aZX3vD8EvxSu%2F8HLXE8GgEkHkQFfTax2b%2BF4V3N&X-Amz-Signature=e1ad76eb93ac8476ea548e2be6fd4c7ea2cdb5e0ebe37cb9c5da626455ee60d6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
