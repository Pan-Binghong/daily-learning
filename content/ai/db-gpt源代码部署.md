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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642H436BW%2F20260321%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260321T032325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQDAN8h16bde%2F03FJ2rr9apwsswmbYGboNijdW1U0ypC6AIhAMvEOKWjSrNqoegRyBYXFMt0sqwdvjaGJn39BtUEY8NeKv8DCEQQABoMNjM3NDIzMTgzODA1Igys0ZyHFVoBvFLcSQ8q3APXYTO8jY6oE%2BV7CafHxfEMCbu9Oq4VliAkhtz%2FwVxSfqapS%2FHnS07lcjEL%2BPRf7nH8ngA0kx5pxuUAjk0m2gxQmnPPYMvduiBepc5RgJp6maQBNeH5iqhyZGc0Anbd6Ozw7KwIW%2FvWswUIWnBaOuqwYkF7bCaQoWQBTdvmf4W8J6fAieKj5WbxoHEFtUCv7VGeY4g87DtGvFneGRXE51HNp70AOjqBuwfATTgtKl49%2BcL4WFY7BtlPuO%2FPmYE10kcvt7l6s2JRuKltE8UbNueRDlTNuhpEZuweGNZgi808trvsvPxHRb%2F3h7jy2MlkBpk1cKq5axBUxU%2BxE8UPLUoBrpbZk0%2FL7c0gYcvEyylNdEroFXx5NPTi4SXH0bqtyHWrBmMIJ5t8YSMDrigBs%2BE4lDNOzPgLHurKItt2CqAzUrV6XZntGViCOsl80DxAA8XyFv3Nu%2F6vMqNjEX1U826UG3jnXMbFofWZH7WQgcBvUqVnDWDJ7tgyNqLBtzQ7XhOW4sX6PowNwuMgWe54ANmYLv91Ux1gXsCuCpbvgHl82W9%2BNeZ1sl9lA%2BqEnKsLnXt7aL5OxcrFRMgDS6w%2By1qfjGkq5vlAuzOPEfy0BgcxcrFu1RO5Z%2Fw%2FMG5CkDDyj%2FjNBjqkAQX1hkCRsrL1E3jQt4Qx2KStxwOo%2F0pTs5MT5cFKhTeqV2rK7koZtrcZinb5KHZrCPhs896SAphxWEPJspyAUNfd0dS0UBB%2F61%2Fa6HAQYH%2BdSTS%2BnsqhxuVY%2B0NZiuErRGQpkHvYzmmbruqkmtzffE4hWx6BnoUzneeIQ6LC%2FEzs6Lj6B53rvSG10fmAmOCZ2Z63mHvwRkNyMPT2rREoaNRE%2FL3a&X-Amz-Signature=1427ced99d393928c7203c384537d1c22da5752e37710854bff1c18be903a859&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
