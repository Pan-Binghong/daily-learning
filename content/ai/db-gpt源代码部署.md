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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KRXM3VY%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIDbZ0iVq7241CCl6API6a8%2F6lklN8J7cEcQPufFfUddjAiEAhPJELSIfmUemduVq11rXvGQQbJvdf0EZuQJ0eUJMOCsq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDP63dYL4JbrCTcKHnSrcA1j5eq%2F%2FphEmCaFIH17YczhOfUEiHeMccBFdOzXNvN7WxtKC9WQVHfJRuId8yqQxXuxL7PLGIvl4aIxV05DdYXXgMHSrb8ug3eHDO3Xr2sbOUnd9chPruHJjXcDtuTAt7siqJL0c2P%2FdnTH3kLuJ7UGK9Hiqbds4KHv%2Bv9fraBkdyCMKNmASEnNAZYE8arjOP97TgmEpNb6a%2FMMuOGji0CxVwlNgbJbbcQR9k0GWyChoQDIjvFprYvHj0o9NQZjLB0vyeuH22Hb2FCvUYOt8z1zNrS3pB%2FZtnuFazI78duHC5YuDzfgTXvBE3rIvgNwgj6mKClYqn0KQmNncgY8JZF%2FAqzq0mLqbQDTNEi0soGQU64lMQoclKRVk5REK%2FwdWcAQgRQffeUDoqcVaDiUgxNEH%2Bv5c%2BokcB0euxwXGUDmhA6trbwYIr3BnVBRVa6qzLMveuGsx8B2JXXGrpFsSkB9Ac1N0OUosNDizc2m4IMrjlv8pDtKI%2F4WXnF5Pw%2BoaXwhyMemGi03jnqDIGPiAmQY0djTndi4FFiYKG5nQfrtJ9%2Bf26%2BamMyRyLVao1uhvQTAOOLKOYx84HgGTRdcDn%2BoFishjDaFlBhnzZeGVHNgyu367tsDR4IVDfTjpMMbr5s4GOqUB%2Fhn33MGnKdV%2Fo2%2BJU2YISR7U2dtk6k0Eq6pYWaOdz1YJo5zh2PsayaN%2FkGRG9s9K%2FWCQ%2BDaHp7GAhcb%2Bu5Jtbltol2FlWKsl6OayQ1I%2BcPR6pAMjQv2W5CHv7%2BDs7mocslZc2oati9TmJyo9RoPiCwlcrKJlG%2FBaax2I%2Fqk2aSq9NeKET9Ln4aHd7U%2B27PD1NSn1%2BOKW2dVoPQZ%2Ba7I6p%2FWCnjeF&X-Amz-Signature=4d633d950ba1c2ecb191c9d4372770ee8e11b2a2373e99a07218fe83fb0ca830&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
