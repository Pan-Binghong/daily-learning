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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIAMAYM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGocIOJykj%2Bql1Ed%2FU2clyX1wW8hibPPDeHDj657%2Fvl3AiANsJIzua9ct66IWC5Q7OGn5GFk644X3NTXTBLddzC%2BByr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMaWYjgqk4Oc335AiZKtwDc8%2FIGqWvGX77IcMmhxlZDxTgJsM02Dj1TZweTiSd8VkxZDTr0F%2FO2CE8Zn1tYx5%2FzM6n3IF6VMEyE8gdYimgtqp%2BpmngAeXPb%2BwuI323k50%2BbffIo%2BNOhOzy16DkRbiOmDVzkLR4NT2XkH%2FwZkXhgT9PC0izXwTFozAiZiUj%2B3dg49UkedzhwNw8RNSb4KnN%2FLUY4eLSNdzC8hY6pm%2FS%2FxFC8Kd9BsIXMOcgx8fp9Tx9UabGDCKXULAedevPIR9xrQF71H61LmxM5Te%2FAvZI05xfdtBYZWmTp3nzkI6R4q2zfOvxEsTyCp4RJrbGITbF62UFw0X7od59SYpvmSlHlKQKZEuzv3%2FUYgFpQK3Md2M7qywVPJL3JWpxWfgpkSG%2BgsVmoPh73vGg%2FPrG2fs5Z94PDR02eZUwpkJfcQoyDIiBxIrh4LTdhXjZWLUwHwn%2FXdZXGLSpodvehDg2IMKTlsAqYSrOWjfkr%2B%2Btm5CI91EnSu5yyFcyhFB1WRzoNYwnnJiwN9ik2dWlfujX6M3xNVV8Ror%2B2PsYq6nf9hkKzDbIK%2Fya4LCra0gC9jS1Fp00nE7hHZviiF5ppHpMYvHAhVdDMj%2F84o7Q4qS6f5%2FobiA3f4ovQ0tnyriCHDMwieq8zgY6pgHZAeapnfPn0qRziPWQGCYjKqqHVNmH3OW8G0e%2Bp54P%2Bqi%2F3fbORAYqjj%2F4ZILLiPFJajMbdD5EAgA53Sqcwm2ndeUDabvTuXwbROSRGc2%2BxZE4e%2F7U6M%2FsS%2BrNbiMXVxlrwqZhBCdhYnjIe%2F8kR2fdzxLMEBNjRX1lh53v6anFFDis%2FHH%2FYioAENNni9xbwXxaJf2jUSy%2FHLCLAVVknQ9eoSOVHVGK&X-Amz-Signature=bf784fbeb5d4f915682b5663fa334d3d1f9487d3e50e9578f28f94bf7d030afb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
