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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBDIVWPR%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQC%2FhU7Ym47EiG73539ogByiUuW4%2BtcpQBhBNBFQtFPRHwIgRxlXnXc4xoAh3vW2iFj4D%2BalA3qxxubhLHs8R3%2FU5IQqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGrkAhu%2BP%2FDn0vt85CrcA0zrJQxc0vAQMUIWmTyWgKXHdyOP2E35yAuAdqAyFn1AAmif1%2FVTGBRwY%2BJZ1LawT9kC58JVGZSIhMegK5eEfWSuo%2FrrWBUkYIPrnZAJKQ6M9DyY5vsAf8rH%2B3dGrEWvnr8d%2FjzqFD6swk8pu67rwSVj7J1yAsVyHp9jDzEKHFTkncDAdH8mfyN3kHaK7k8W%2BYJ7Tso2A%2Bcs0ZWukZhuDaguyrZqvtou9BBZ0FC18qQJm%2BrEEQVdrG194fTechx3T4GlMTHgD0D0hOHmnesPDeFdU3MuZHRRhYxsonCcffraG5ks4AX0FkOwrKOZT1ZSHpT6CSkGyDv7IhGcT6o3PSR3uTolfYJ83ZmyqaGk9iEPxE1y3pGKa%2FK33cDrKI6Hp2hrcXPyOgkjgxW1HaDSThkf0bRywe2wslMm0V9z2SP64HfDaWfeOZQ6h3CUAusJS4gc2E6OdGuiRdMcE7eKQKB1xjSFWL1eyS1Qb0V5pFCYBFNm5Qjag5QRBdNvJzXsaQ8%2FniwG4N%2FHh%2BUaM9IhZ6A%2BVs2ICpn4OyXR%2FCl3jChsyT%2FZW0uJ%2FuS03S9UEUHCpxBTiKPvkAFpMSSxe0zk7JFSItHazCpa2MpBXXNCeZa8ArojlnRbKQpdVvk8MP3q%2BcgGOqUBqC73cXQPQR5GgimUl7ROECekopWsXMTuGoV5%2F%2BeJUmYTXiV7ioQj5S0idMDCVxl3nGDAf2hK13B8O32SekoV3xMgWhpxtznK8AVeIa7Ug1JPS0qo0kK%2FtVz2Sdwn8qpX8W%2Fz0b5OAnPmixAuLrBXJ2%2B02T7OIvTJNtYnxOUXqixvGEKBddgooLLx0nHRh1S2J2tj5G%2B0mdR%2BORCjrVa1UZuJ7XHH&X-Amz-Signature=af8089f0974bcd047898a8ee658b320638ef1a952f9af79078cad963acdde76d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
