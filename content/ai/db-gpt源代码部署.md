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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZAYXXOI%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIAIHL6KzynBX65lZc9GN5vkiEazLqri4kdwJqu6kBXtNAiEA6vBz0Dxc4XiD3S9lduOIVsG99gyqG7tpDDcLvOoawXsqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ070fAl5RfNhS52iircAwQqWGRitFY8WA%2B3%2B1ewaJ%2BlKsrr5%2BwKrS43%2B0BV4kV%2FJXS7QLBEMKBtbGolDRwT1XLm%2FT0pjNxuV4qTl44oNcqveVcj1NTS1Fx63WfvVrSN%2BHP83BBbz0M2Hd3INtPDi8rVfLeOD%2FdakWSZz1t4U0tL5naCxD6v6Iy1VgQslXshNSiIdvDu74AJry%2FLZ%2FT2UFQHlbQnMa8A74%2BE2lVrLJXlTIZQuTY%2BVwponWKYsiL1NKVPsbkRMDAG%2Fue654GjevhaCXZcybkyrNdd7pWKjB2fXZd9V8br1MX%2F%2BSOdbLX418J7V7FFF5qHhAkG%2B7mD4Pn7dnr5UTzmLSd3AeVWMN0xMT2Jrm%2B5wv%2BLzqjwDygyFde7HONbRYiueGfYhu0gIxHKm7gMOiMGGitmgyeZgsNabjwNKTqt5%2Fv%2BpJd%2Fvq0S5VBo5yuCanYCnAgLNVzokvgfDsUsT297U0ilLWzw%2F0SWzOtGb4ZsZYZrqV%2FdgAxOMD2oVcCdurEJ7qKOzgXIppx4LJKloazLzUXbtBB2DXPsVGP2Do8Kp4NMNljs6aKaXdpHEPIqUI8uRSX9xt5Fbm%2F9ln4x5K6N4U2cJrM3OOb9ts8JErM6IaMtKRskRHMWr%2B%2BlnhiWtSImeku8MI%2FW7ckGOqUBjQZR73R8rCmEasLD2XSdlLro%2B7LjlwshB8dXDlfldjs8jhga95py0PkW2OtlrpKbVkXGKbeF0Yn4GB%2FI7k4tvbXOmckPOo%2Ba36p4wLsVgioVTEAhe9vcuBx6E40jSrCzGikScia5CaMaYrQF6%2FpygDtbLp1BxWio7K1NbPqTf4%2BDInulLmg9yMj4MfMkxxa7Xx6lNL6rz2CeUga%2B7Oxr3PKZF4%2F%2B&X-Amz-Signature=7e79a77ac5d885bb2b9cae4d59b0747c5ab9e9cdc6e0bbfe7ef4e251db0bcdb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
