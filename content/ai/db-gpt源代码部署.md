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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G2THWUS%2F20260426%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260426T042427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwlvBZ81qFJxBj%2FTe2%2BL2Kz%2FeJROydXfEzY%2FTbuRA2ogIhAKNQxRJBNuoRSpR91qe234%2F7ljsSye0IFkz1V25%2Ft134KogECKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzcUQbU%2BievZaOkq3sq3AM%2F7nMtuWePhL3lcCEvGO1k%2FurremIAJpGWNqWmTP200lFqOQ3BuOSQIzmRLWlNZFBUO0QIjwxQM5%2BaPJOgMfgxzaLwS3fcDaEwyIdlfdqntHyM6e%2BddoX4HIxtz31An4PPiDE0fHj8%2BJUTTKcEn7g2YrowWfKpDwTHYIg97H9%2F20SyIuYNvL%2FBWK%2FNu3MjJLiwcldYURcxC9Rpmm1cDixWxFqkezbp1wTN72TVhBvzsT4Yl9My%2Fh3siZaGcbOLB%2BCabqKTW9Qb1IkFur%2FzOJ0izUWWo5J5qWmtu%2BGg2BeIpklHbMKAOKl9SgS9%2FmN0LnNvJm6quIdWxLSPq2ok6IVfcpC16I5XV4fLV0vHR2UB4wUZ4sVuPjrXNAehrNfFxrPW3CJk6Uepc4wcn3Tip5H8S1LSNKiwvPPgr%2FzxFyjEV1JLEbg2gIafAhYqARviy60UQA82qV9yLtCFUTyXJWDXwrfMSvICBAuzwio2QZq4Nj%2BNAgtnYwRAdhtUyf4SW1fQsoQ0UezoOKwiiSmqu1C%2BelBv3Ts%2B1vPbOAsd2Eo7t8mNuJT7S5azUi70VpmRHsG0kG20%2F2VHmcAXysERqFWmlyf7ETAmQVRWFoiUvEtKYK6yKUEcbLh2h8m43DCwj7bPBjqkAfqMO8PncR8Kcqb1jX1T%2BiDQjYfHmP67YE4OyIC5CucDZJdoBVIAHH30%2BPp98GQYC%2FwC9mfd%2F%2FCV0TR9NjPQ8fcw3zhUJfsutmyZ7tLZCleaHyOZ9zUxR3bK9dgI%2F%2BOgfbDj7qPgSwrfzINwkZiLGH7bZ2JRsoa6njUUY1DJ2NvL7D8mGkSWhHwxNgXNTxV%2BBMMcKYlctTlYtl2dhEWvZgMZ1IYc&X-Amz-Signature=1ab9a6cfe108f02aa6011ea2834a0ba4681352f903e83e70225ea4cb8a47026a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
