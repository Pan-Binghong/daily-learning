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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXP56PTP%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T025941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDS0BZjiy3cZEBaQ9zugqdDUHdxZUrRqIOg81w9ZduZoAIgLZk9cpkvkLkU97wcoe70%2BA9X%2FE1XkIMWB6mhgSl%2BTiAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIeIdvu%2BMZgRhSpnbCrcAwF53fmcQYd6DST4lCcKyQyDBBs5QCHk1isDEiHmEEAObHOXmHac3Pb3YoHq5un%2BTLKjaibQq89sskmyXaKTviDuRvMHUzR%2F0Fyt8gdeFtcXXMNzxfZFelMe4xHZpT5YdsQT4OSqfGBxOXNypzdmAS9X9ABmivRe81xLQ4aTex5OVaLslv2IyC46tD9Ted3ERvz9NrwcJBDMQNOVm2gYRcDNQPJDqyPbdxQs2B1aaMs6Vw5tKbTZ1vVFLPersfx5%2FTTaaJFKcRDhEmVhtx2tk5Y4JxhtsSaSvU3tOhoux%2BWcFRyeTztehxLBAzlqgPAhYAkeFa0IIXAIeSXEBwNhLxJbiJ%2BQZhsqPm81lasCCsXxy4wOAmXFYz%2FlawbL%2BtUqldX2KxU7F%2BimXAA2AkGuvsSJ5MbqjAYhWaz45rVpSK9WiTObls1%2F%2BqIOXPlG%2B5FaOygeJS3to3Bu6s45LWwlbtAfs2iX7OjHgpwtd%2BxMk3vfi65vntoLuQ2Jb01BSUIcimRyOj97SW4gAAEoNqaq509FzYQPOltadKsV3FgYhdKo5vnmb3gDlqie2CCoJT5MQ5Xf%2BUEMrH0vhWgPs9OuiHYhqls7pGEYLi6glmR0AEsBlEGgBcBqMH5v9s1zMIL4nMoGOqUBVO18uU24qDoU3NAhNJTv1R2CKuqYsbQov9hDt0bfh6xVByPMW2GRyg5lD6VGT%2F5KquEOCJKUVXH%2Btofx1RW%2BNPm%2B%2F1ZFJWaU6nPsxiiPFVft4xaJ1hs8iZYkCY9C4zMS8V6aZdpUfp8yBXhMDRQdJiT6sD%2FhPnP4kb5sOBuw3fB4gLcHjbYli6WIp8jpOL9a8WngnHhCUEAGR%2FfklVqMT7NppgGz&X-Amz-Signature=15bcbcb65f41f4b4415c1ef9cc41ea22f4090d4e70f60f413dda9ca05f1a66a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
