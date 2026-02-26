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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664AZAVM73%2F20260226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260226T033425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDntoXTpCQKjeYdsKcXlOCe0tAvZ09%2B3dQUSgHGq%2FdQOwIhAKHCXuKrPWBG1rniQggbpujoEhXC%2FIg0fpoYqxH%2BT9S1Kv8DCBwQABoMNjM3NDIzMTgzODA1Igzi25B8kXII7iQG4bsq3ANrg3ijio5mVG6ya8oQltSyp3kygnjAHy4nQW2rU9iDYxhdPueF4Y%2B3ZXAbDo%2BOkGKQiu5w%2FtEsf1cR8pzIzB0RabD7sOWiw0lEjMxBCUOj2RDYAWclN5kTFyjTThEoWlrqN1JOClzcB9duXiBTH10YPqOrAUisMKzqjLWDe4kqBcifGoi4Nlcfi5X0uCJEIQkkLGmbwE3lVccAZQtHj4Fgx4L80rMYAq%2Fuxosr7abaMJw9hF65RsrFBscFXrja55jesuOlvNs72hGeuya2E%2BI4ps7bHRdBYJxp4iPM3f3BEapgyV4newAaaA%2Bvnu5F60i%2BonVStAxxHXJqXO%2FzJt77n8gYhbKVYyuzC2IDwrdwwdDIVOYwpoVmG9Mp4wB7%2FQSytqbs1XNlG6aPkxWOm21eCg74EMaxZ0dVdRjD20jbsdjRAEMsBGTHokZsNytUif48lzGLbFGmoN3HQmNKsGhNUl3TpMdKDI2PNTQK%2Bhc4a0fKoVr9r6UM0PwGKRh3CZ5Idgxx0LknHKhHr8iPraW2CYgaENszFRLBVyNtS8XJBXV2aKf%2B4UJhUziLWJYtRBjNh6NTdZlHW4c7NFkmJyj0LA%2Bf6PslVzEmdA00sMRgWXwWBe4x02AuU2NxOzCc9f7MBjqkAQJIhOp6p6iiPZtf98tWFV9fcn9pgy%2BAF52KPruPKAH1fyXO4jc2zgtpMLOuDnWxy82pF%2BmizKMSGcm%2BsX6Ld1EdkN8M4YpvOvIoV5brI3qnVdpbFVnRwhQvELrzz%2FLKnEcc9DVTAAknvgf0ea2FRHWFkZVF%2FdtqMVMJK4v6hHEQ4PUNq7TcP0xUTvNsydwel1ApeEyI%2Bwqxr11ajPwfOBXOuFPp&X-Amz-Signature=423329596e1fd78ff469080648a9c89b5386f04ff94779338c39f18349130f16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
