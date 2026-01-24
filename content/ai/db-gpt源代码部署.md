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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUU2QCDU%2F20260124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260124T025600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCCvT9%2BdEq1I9iTAlE5ioAJ2K7UIkbtoyfeSnh2bUtaqwIgQjWvTA6iR4uPYStsl9V60w1F2%2BOfPhNxpWFACZU%2FgnAq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDPihzS7HyNCvd5%2FOsyrcAxRTueM68tr0mtuW96MCFY4yi5gO5K%2FaIVuF24slUwRw1C%2F6Ds6%2F%2FqCpGvHOx2x%2BrsoozAxaFhGAguFAJFIiQJ%2FQelkTX%2FwaxRjGdyYa1dOphCkWOvX2%2BOU5hPSyY3oWeTRsFvJcr4FiX%2Bc2b8LlFqcjSWeoljL22A0XyrFP%2Boq5Mte9bA3FKy3ZLeWxgrDa8pQWqLGQhU61Yd%2Fvn1a6J8mS%2FqiFufl2AP%2FB09vb5GOgi%2BbJcstTdfyLJlIy74z8gdHjjQ3FI77aqjKRKZS4pOWuex%2FSEGWwD0AKVH1eLCJ36OPb%2FnqPzbEpQst7ryXbPqcYaS8xMflCGvU%2BwFqKOKn1E7N3%2FX4sugYecVPW96w099oJgXdX9x5TLXNSL39WdZ7a5BFPMauyzRMVO%2F9N%2FjcOFl50%2BkQ2bkZRLNjOan%2B1gYB8t57GH8FFIkfCq0dvgMmOFSvIP1OY%2B72H5RGpmdBHEbpLSMYph3FX8vTRpdfQzLraLSC4ecpPAksQTrGW1lv648aqbSezkV%2F%2BSr098kZMZEK2HamSiSLSO3hZO%2FGELH1d7tzDndC%2FWdYqH6bDSriel8bt64vBFqs0S2LW6TmCb9qZaaluMNARk6iFhO0h%2FXSTr81je6J%2FGBOxMPvN0MsGOqUBvjWYWB9hkPQjClHzaFdySdwvpEww%2FVok5j1YroOtm4ueXAJDuAXZUS1SaLZuxvRCeDDD2kkNyZ1wI47BdGsGyXHSIzHszS1OLoV%2BtCZcLqDtfVhmoYnm2VZYbIHzg2E6Bkfc5cW54nEPaV9BwwHW5HbAqlxyyC4DGj81t6W33bu6JEDQD8bqN8qSaShjUm0dyLiGFM0ELxk%2FNyh2FFWjbEMKvoRw&X-Amz-Signature=4cbd882f917af3bb806abd51dfdc97d0964b264fe1a690ccd5d48af3c6d6ed7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
