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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TC6APWSU%2F20260320%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260320T033151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIBRWj%2B14tEBSgHtwzXKNG%2Bziq%2FUweaiebItMirxTe847AiEAp9AEvj%2FWXuyHvWaY3YoKsF%2FXvm%2FHBaYLq8%2BS11DOEGgq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDNqr%2Fi6BEcDeVh8dkyrcAxQzU9U8YX9eAET839OaPBsCSUTcZtRTA82Sx8R5VEoUTbtSUno7%2B0aty%2F2tZSRwJVWapWE6e8t4nut4wrCtB0pEMzJmTLXTmiTRL%2BZcQQTFgQtk0U2R8QUi8TcxQqqHsisMXtiDdEfs0Iab3u4SmNohIXjWh7LgmVtYzseFMLxmtZ3mDZy0oT5yhrTK3HkiKY9aj3HxO5bXXvpaUTl9mCtOcsapIVt25XRVB2mY3sxgfBME%2FsfFZapaVGAc6LsKE85USiY2SMk4Te7hWazYMM3RFjN39L%2Fbvb%2BcHIUIB45BYIVwloJXuMFIrM7hdLLhmBr95oUeDv0AYaJxL9cUm74v0bMx8i3nM3VKYRplu9se6a4EUQdcoB%2B1qkvYYsUxp%2FpbLBG3MgweATHwQ47%2FkDWGN1K0XAGgUmIhb6cSFk193wTppQG%2F1S8p5NU5gcL1%2FkCHNgXZyl0kjvyp3fRuE8t2JGl30etvXBlDOXkp0T9etzReya%2Bi80A7tS8OJ5HrUKW%2FACTunbmMR6Nnah8Q7JLlqV3Kq%2Bj76z%2Fnj%2FTs8%2BqVVXjpBRajwkNpUAPwKjEifyqS9%2Fp06ieDUqdBCATp43Sit2aR9ypLRFDegVqjZzIz3MzE%2Fj0t0Il4NVMxMM648s0GOqUB%2FRi5MswcNCfMNJrivUoxgPe%2Bz%2B5nl%2BLDadl%2BgBoOeTflw6cj0SO6qbLP1%2Fk2FUoM1sQrEYANcfDQB%2BxmEzatMYGxLLyCz3Btn5%2BS%2BMjc4lbD0Qyw2r7F3GfRA%2FejEN7Rf3nXhTCEfrqwLJcVPIok8pCnp7KidkCUFZrVR0xO9oi3uDTJ9sQcZTEH6pi5e31yptXgzTLic8UWa25XWF3EwipuQYgX&X-Amz-Signature=6bc1fa658721c7e38cfa257a2b55f5002456236385fd39752d183868c7ddc203&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
