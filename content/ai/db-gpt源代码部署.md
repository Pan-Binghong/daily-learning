---
title: DB-GPT源代码部署
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-27T13:46:00.000Z'
draft: false
标签:
- LLMs
- DB-GPT
categories:
- AI
---

源代码部署DB-GPT操作流程, 含测试, 部署, 注意事项等。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QP6G6SHC%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095838Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA8kRYU3tpCFrcGARVipu5dhOTB5pIhJhYO6R8F2sp7jAiA%2Fn6JmO2cReyv0Mi%2BrbSt2nVgz66AhohOlg0PHAu5BkyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtbAjpvC3L7A6%2FPi4KtwDCnu6UEq%2FGy6Hj%2BCwhgDbbWYOQLSai1hOO6zNuWpZl98uGrMYcdonxEEilU8G6XYteUiiNk%2FxJGGTfRd%2Bjvk7asgVFHqiaq5EJV%2FRbheDWYQapfQZx%2FNB6%2BMiapu6EQEuAOco%2BDaW1Jnaoa7HEOK1HMXUfllvMnaBPIxZWF0RbkyPbfmjVjioqJXauRR17JEsDyfb9J0%2FmL%2FtxbJnV0nKFBW4a4WgMlCI9wmReWOWSZQ7GzoEk6xAPMw6IdnR%2FSJUbsFMuhTcpJ59eAXoZCEJUwm7jtzzS2gtL3D4AN2rh3QovEo27829RKkbOFeyF7mXBjKmVYEcC89mnCW%2Bm%2FlRoYhxX8A%2B01GqdysdXkAN19Q%2BLtllVXPHzZL92Sy8SAyy5ggCvTsuGVvWEG3JYlCqb1002TDHRgrT7MQx38xmMvcR8rSRvr%2FukJbjxCg%2F997Y3qUNtF8lOm90ONjfJYCvf4c6ErjpKlLzjVvRDuNHKpzQJKwe%2FyERmo5a8UvEzjLRMRzecjr%2FxM6IVpuUeJXF0ZCbkETLDCG%2BwnF7Ve0LsNIwR0N2d%2F13Yzb2%2B6ggduwPrdfleAjrfEP2i0bt%2FSg2Uf1Qg7hHaoxnhC9ZYKUr6YJ%2FJlBLmL2cbZTu0LowpqOsyAY6pgFEMNSBWpK7%2BREvXtRAdL22vMBftzL%2FMGVq1r8Ui6qmZjeztKcHGKSfFhmsdyz%2FgLLOhYpwiBUT6BX%2BIU5He%2BYXbdI8oayGyVgqt%2FpU3L%2BXvmH%2BTmSm2SY1WF3FqKGtXTNmIptJ4duAIueNrOf91xfFFjukuvcg%2B5RZUgyWXgQ4fswJLL5r0RKyNTMg1IWy7hfytfNbkvbOoDDq0CBSrqyH6UP7Fasy&X-Amz-Signature=dea7391b2ebfbc3ca8039230f3a559592af11f3c37f7b9796a121c7aedfc9340&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
