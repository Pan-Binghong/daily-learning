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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VDRDTBH%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T025950Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQDboptTNjKeFREc1PowjjE8zUpSQM9HXHXvjKck2oFwzQIhAMTGJy22fjf17hyraCKGx9C3dcIathBUmX%2Bi2%2FitUfS7Kv8DCCsQABoMNjM3NDIzMTgzODA1IgwnTEDLZj6OqCR0mkoq3AOBCmN1gjAyvtVvZO4g0VEeda1fVqUl8pR%2FnWqmv44YQdoho8lfi%2Ba7BH%2B%2BS76xIQ%2B6%2BePSdNq%2BUuCYqqIyiecuFVUaCE5OQBfNqK1NyVVWhRdThLaOzzqtgb0wzqVRQrNpDv8gq%2FFQN3RLqMthPBSJ8piYimoTUUzYM2wxaz7oTLejGiYTrif5%2Fw7nq%2B4tfOu%2BtGAAnyrR9WAXRBiKtZoU3VFbk0xURsxTQZVxzFfcR5LlpvE5V2dw3pnfiv51MRbVdBZu5lhDLwGqgUdLe1Gd2qRJA4y8aUGUN7Yqa8Sv0g0VEPDR1w4FwmRQnB42ZvtkpbIE0ZCfooPyLQ9J40fS0xcLHfMABXo4Lk12Iwm3GC21anh3FdECIjvN3Jx2L%2FAt8FeOV1CDMSo6FIj9I2OMVA4zlcDDY6UqowFSJwY5c6ZofGsedGwfInRFH8BbshEN7CryPVpsEvJ%2FljZRB%2B36MbH16nK2EnN6rluDUcc65yVdhrPSvA5CvadBVhaHH%2Fz0HoeQsVKA8E1r5gKScKyRNjXDo5Y5Z5cRyNhAF4Dg5A2aPmWWhcPRLx8wNQRuUj%2FGqFdhISQbJUoRrZ2VU2iHSXJRPgnitR5bvWU4QOttQ0A39U1ObSD%2Fn5oLeDDWmqHLBjqkAesx4gThLffAvekmCPi%2FQ5BnUUGkB5aC9hFM2U9%2FBpP23encdXaoprDMkwUTjZpGsQNWi3Y%2F3XWOYrMQ2G6me0vGBAaD4k7VhKFkxp38ctXItTlPhe3svOTLLgfGBlq7FJyNrvf%2FHjxzsyEI5ZpHeI2BdMBGn6teshc%2Bj6b6%2BPficfmRFu2XI2o5qXVlURV9Ey8CgHAFcMwFjNDxHiWyPb%2FvlSww&X-Amz-Signature=ae76c60bb811d259c3b4255ad44c4c50a023f8f062e03409c865523ba8202a55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
