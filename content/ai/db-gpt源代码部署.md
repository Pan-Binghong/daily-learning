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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QBDXYAD%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAprwfxgj1JTOvXhaJBW153xp9sUX8xJMCx%2BsFLlL%2BS4AiEA%2BWGzqL6MmSkNARI1KOM97%2F2%2FTli%2BYMzrXKPgoh%2FSVYwq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDHYrHp1bIHHgvJbLtyrcA%2BOrpFTOVj8Zazmg7kpnxBuHRTnAVyVeLWxLpwSp%2BY37mUaTym5ZDt6zxaXtBWbyh9mws24XBpS0NtqSRpqOKDz%2FqymS0GijmBRr17e3KGBzw2PKRtwdIOcE4kvlDVpFyz5S7VhUZ%2BtpkiAIVctgg%2FH2FlUp5HRVVYjVJ%2BfYu56Ni8Zktm8%2Fg5%2BLBvkn%2Bi0hHbTyhiSluPR2W2buVKrDiw30MDDIdGLwtFxEl07LrfCsFVvZu4Yys8eBhYUq3DCmpOjJD2ZhFfptiIDcNTVOu1XzvFH7HKMSaXToDsUOW2lSNhy3%2F1H66TQXebhYzYrNWrfR2%2FRtrFXpnBX5mSp5g611AvMJZ5EbV1iyz9Lqwxd0c44MpJAHbOnEpmjnSqaioYYYEU%2BB%2BYm58BTnmPuiJDRopBgQphy2gbSzvp18JgVfotvtJMdIJ5cPDvFhimGtfhtojc%2FdOhokrP4jZ%2F2%2FdIYBUQPNzXHfqvAUml7JXTNvVOqQUuyE5JjUNnpjoEi8zDM3PhW%2BgX9czhnPsPQ0Zv17e69dtjV1fMb2QDK3PUmuS0wlGQcUSV9FC2WMPMhXF5kCRld30LIybxb689AkDUdYSaC58nJcA9qM50gHsaV283M8exq293KbkPIjMPTmwcoGOqUBGMn1oQ9bf9kNvOIxicE6lU9xD2nglnQJ5yEX5fTtwIG2a08jBXjaZTYirbWULRhP2xDrXUdooV8UtTm51vHnsiUEP1coHgk67rivUeJilayHf356YuX4Xsdn5f33piwfw19vlc8Q58AMqj9D0ByWyGzgh3C3eSLjjJ6y1f61VZbGT%2FbYZlXOUM%2BQe06gv0xt7kAzVMKprlrxK%2FcwN9ERdki%2BTSIH&X-Amz-Signature=0a1d6009af461fb1c0b0d8ff333fe52d9de986fb134fb2cfede1d9a1376e6dcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
