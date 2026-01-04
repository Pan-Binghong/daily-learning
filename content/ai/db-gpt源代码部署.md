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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4NCG6DL%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T030955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIGKQFli2bsLGbXTyX3BIJsplIlkrG%2FNLd%2B3Q10I8jYTSAiEA0c00mszODUA1YQf4MaBHKY5fjhtoIcBimmcfrpuTNbcq%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDBZ8%2FgzkUsPMSmG9yircA0uZktUyceMmZMiq0gO7B48ZOExo4pByibe12ISZXfpiuuA697zLh6Lo5TCTlQeThGCMkKqIvKHt8Hk8ulW5AR7H3P22ez1ZDDBg7B%2BNiTEsZ4b4eUCMc%2F5Au1ODobuc57Xc9mA28EhGtnoCIunm3cUpIBTJTyYBStRlzWGhCLDvZG1koSM5waYvwk7IqyFWXhMF5NDgtO1WY0d4oLJwF7hMZvIAKrlIZhiQmNwUYHwFtuqbn6neVDTdjcIdIEd5etmFNUupM9a9JpQCtvSQBLYKCp8%2FhsVG96f78z4GwceSR0WKbXMxj43fM58krbrEwIUmykGbriHB4dcQdEPDwpWpUNYfbOznBFy8vnQ6EiV7J1LcgfpeLbmhlcXZ57jKC5EZXfhPM0%2BFl8Ho5eLwG8PghBUUZa6rj3Ew1RiOqQJlCFXLegyf2b2%2BxBrS6hR%2BqaAzulCZVbIkJhexAnXkTVq3LtpxL5%2Fo60%2BIDwHcRRDvhS9jmZP3QPVzGuPC9DBDw6hCMDI7jMuAeDW5GP8xfdMORudTAa%2FYe6eTS5XMSpPYQCj5Ok33dGMPKr6o3WNd5Lq8b2VJ76LrOHPMsFpCatuR%2Bcs0PW4cpfauT%2BG3zXn%2FWwcIZoeusX8Yql8NMIiX5soGOqUBhXQTwKJP8SD9sPGOC6F7%2B7r9gd0FrYL70VfLgDk7roD0rJ%2FYM8UF9VE0Ssxl3KyuHdDurEI3hZtW6%2BSaKn1DskwGe4YC%2FEJMzMfwFaRgHm8x8cQ7zoE36fw6LyihDlls%2Fe5zOEQFgsBTTxAWKn%2FuALJR3Sx0uDWTS324fSWUYlsZKGM1q8Fzu%2FoXq4SkYpqMj8tUHNst%2B2w%2FBbuVZp2QkR4YUIYJ&X-Amz-Signature=02daed8458e80e118083603ebfc01510251b5c8d62e072ad8e4514869f4116b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
