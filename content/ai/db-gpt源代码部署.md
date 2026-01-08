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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662V6YWZUP%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T025852Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCroSkF93YCO9AtAaepAl4Hiva3%2BFODKDNFS9qvO0hJmgIhAMtn1OQFlXCvKswQ2eFKfwmUi08vfk8cBc47CCJj3xNcKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyttox2D51DVKunTdkq3APb3AO6ulTipi4daK53f4%2BjXHs2m8kJ480S66QYpjtUY0W%2FqE5EM4e3SFFGBnDwUKeBVqJWAT%2BQB%2BojQ92t%2BFhXM3VcDywJb%2BYH38U6XDfDpSI2VNVRMXnTHSVhkSlHbI9vPvSUkXEMvN7JKFF3k3QESbphxKGFZi%2B6Kvk30rCPOFC9s4H%2B7vhw6WVR81FL1%2FahWqX1E9kyVaByP5Abga%2FqzmZLbcsAVeyad%2B3N3Us7OIP%2FDic6pJP9QbCyzVvx8PoqpzEDDrKvFRrPDd8sb7ziZmZBH8nB7%2B5bTPtg5e7KyGbHWI%2F4qaGjqjbOt5F4fHatgW4PzU%2Bn%2BdpntPqkAtd%2Bp8u80ZuLhJ5WSsSRsdYbPSJZHxTFf7p4poyYqY3l%2Fj%2Fui%2BejTvWnM2BRjmT3l8tFIk8YKe8HufqYV5zfGTFqdV2I1h3I8pG62QYNiPv10aqVl%2BqYh2qBFR6wzFr9TzEu1UaAiBWW%2FYmeWlag8F3Vi1u6ar0fObVIBCwBNXJAcYQvynQ2Lsekfj5%2BCm2ceQH%2B0TKLLFvHmXa6WJhmKPp%2BCur4aHKVVn%2F9MGaR8xtJPjmTQfnWV%2F9djXH%2Faho1h%2FL1anYez4XiqkDgeeU%2FjGZtTOwh9YKPFVnMBD5bYjCiqvzKBjqkAZ%2FzkpjDbGL9SL6DUHzSvbq34Tq0INlnkOf%2BOcvyEOAKYDC%2FvMdF5eKInRILAgBSjz2N%2FxYeCued8dvxYkuIcs55tUUXSY40wwyo3whp5eaPMkAZE0jZqmgEdyQpkJur6hQiStkRIxOdGHVXaUAgO3FGfOeYOjh7Uw1tpfgq2NZ6iYlvS3%2FVi88u94Vei%2BIMxe6O8nRkMRpcjI13zqIT1Nho4mmz&X-Amz-Signature=a3eaa67484c43cfc056efba9bf62aae5444be5364ac7109023cc2f7f64928410&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
