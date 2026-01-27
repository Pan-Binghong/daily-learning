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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XV3JQY46%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDN6kQQDU2HSUTnZTsLm8SH9UPNEIwHLQpWBSH6VywssAIgXzKSFCWn8fyPAYvkSlg3WVbmqZDWpz7AexH%2BYOwfiJgq%2FwMITBAAGgw2Mzc0MjMxODM4MDUiDJDeK8EPptm2pN%2B%2BlircA7e%2Bx0Dm1h8Av1vGBYfDKDvQZmxpDt8qAHwrd7qyi0MDHx%2FD8fEG35hGbZnGVXUy%2F8KHmSWKNhJ32D0nq0IzRGpbazA5xd1SO2etMIKhdqP03REKLgnnIP9UukiT9Dxd9wIhfcidzVvKJimG5CCXLGx1oB866V72U5zaFQXoOnK0E9dlyz%2FW5xB0TYnZatmWEm1BjLMVXd1W0DqtAoSQGxg%2BCwqEJwkoS%2BF%2FXoCvdEAHrMe0RCOzVGKuEr3cfI%2B2og1QS%2FqLUCFl7kn1BXcn2bgvEwQRx70GJlkiLLHcYx3DGGaxh1QUn2QEZ2bu1e%2BsYCFZMPZ5Z0UQYT7LVTduOswD6nFS1xYBrLjxv7l4YFJc5rhvnj%2BgjYKKyot%2FOcswTEFOyd3DySXbNJpjoXolAbxHtkRf8rD%2F0s%2FpjV0iisEn9KPDOylT8q4F2WWprcXn8neZwH39CUpRV4FXAbG6Dq3LBaB28g4yWMPhg2%2FltP9azQR6yTZv%2BmWHrJ3M%2B8pGWfggYIUVSxjRHHVZ8lxJBgg0u5wn8UsFMH0kUnlgYEWwLb45TxMChdBhXb2RFZcQDEtYJvfWgtPhdPJKiX0N7%2FlMULA7LBXBZOPzScnKlmG%2FiShCB5x%2BrPKwcLhHMK7T4MsGOqUBUEGIpcOFGlhjf%2B3WB9Z4e5tjHmJqwFdrm57uOMlA%2FQ%2BBMwx0HyenxKWa6288YPRxeVhgQKxguJh5SH%2FQiu0qqG7ffVfLGek2TPIfkV95WPhV3ywR4o4t6EoDabL7dyXtyyIIcLp6d1Snb8Z6vnmOTD3EVIWwt7sAKkjoxVubS6ThUMYeTjYMrIBPK0JyKowGlYktJWDDuX5k0hAFeCSKTWx1057o&X-Amz-Signature=3ecd2838e72e7d86613b0519c220d4e1e52520990f6b87e174a07c91544085f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
