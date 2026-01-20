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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXOA3LEP%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030243Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE%2ByjUzAgXBNtkodjrKDvd8xI6VQMkjK9eElnRu%2FEeJiAiARs00pC4ENP17jLBuvCB6FT0yp9Og9zy1xV4CvqqqoiCqIBAig%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMafeDjri%2FWExWBZcLKtwDU4U%2BC9grev4rhMQCmRi%2FADc2Ct%2F34wSn9xEfLhLAaJ8lFI2MYTImQslfeZ1RFAIjk8xlPSGG52QjHwHU%2BpW9Z9mjL7Ax3v3DmG6RS5qGom43u1Zor1hZK5uKC5lD2Js5NozZMDXl%2BBqedijkCQHJiMmoQQkD5MHqdtJUzT3aLroZnTHJ06KEuzYyf3VO156aZe3PGnpxW3HjKBosWWXkDCZoogX5lYVgWK6nP5q82LCmIZVXD0X1GNV06UuveNW4EN0QCsdUGJZRZxZvrgd7AXjwnKqUQRCM5YI2vyQ0ywIstk56y6UMqxB40LJobQbjhkAhqbBvrMtw1s2EaJlV2z6YQNEw0m9hC0%2BBNiyV%2FZ4T9FwIE%2FSYUNmgLeAC2wh4Twr%2FrqEi8VDSRDF1mLbPX%2FjfG2GChC%2FtrT%2FwswazzlKIP2nDOyr1uqIbvQP0UCF8JRDwSxaqWPGGDegA1AW9z9x9aaUu15h91Tuzjwd4meSF3QZvvph%2B0LTsQREIkElu0O6GinsKQsFYeIhWW93i5Da5ctXMy6kF1KymLNPhS8iKlXmqPh8mIJtDIe3PnY2njswQwC5M4%2BuspW%2FkD7v%2BxEtPmA%2FCnyf2RzGt6lZcmRXbq1JOMD967LY%2Bu%2Bows%2FW6ywY6pgGdfUBhVluI4duBECegkUPt9L1Jd9NyU8mAL5lAqgaksp3bmTvRawx955ZjpwRJFDEi4sKk25aINHAIn7DuNAOdVsZKDKpF%2Fg7PQjeD1QB27LQWTOeH%2BmooyScqgSqHEGh6mf5huF81wBjYZkUI3LUZxnhzbibFwhg7FvhLhkgfh092lDO5UMCUjN9vA0%2FfCgV2yU%2BUqtOdgGW1HNKmFz%2Bh6G4ntxYY&X-Amz-Signature=9e19fa5823a54f0c3a1faf18a4ee1537dc61d1464ae41fac2d7c71b72d314175&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
