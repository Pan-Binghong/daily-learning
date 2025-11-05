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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TN6ONEOF%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICByf6ORZDNOPKiZWY%2BMd5uCI0yTm0UWz0z1Eq2athx8AiEAsfo99nALQZUOdWrs38stV6yNHMabhZG4ygU%2FokMC4KkqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgdwoLZtxyggwzTFSrcA%2ByAZCmPdMAFatV3JQkRfwHFCMBoX4kGLCvEva0aOJipMSONnrUv8l4xmZ2kSyV3cDB7tbTjsn%2BZqR%2FBCF20y%2Fnv%2BEJfpStpL3NmoMiuX7Y2jmwicapvZ%2B9QjXseAPog9IosH3Krtqqup6EMUB%2Bt5sx%2B0TWp2ooBCS51JL9U9eoRqKHtIQxLxB1CRuZAmoJ3rd0ZxfvGNCNYtquYlRMMeGWSOV08njWOREHl7syFcddswRrPL8OdDp7x8KpdW3C6giFyASeqbtpch3XJyMl9RCvE4fpRE0JELSaRI9xmrEJg2T3J4WQz5kRQPBMFIA5PiW0KDqT65k5Q%2BcZjPnJCVLs6SAQHrEddpFBAcWKyLA3i889yALKKtfmL6e%2F%2Bgfam%2FprZhmrDpakl1mPr%2FQPy9pr3ZxsWTWxM%2FNPVLjJMzmdTszR03C3bH8Gp6h4RTRCY28wuPHdB9%2BIBXWVZ0%2FoC7wsw%2F4C4wHfHHmRB5rnFYDOfQD7kve%2B0hgEd1To9CRyXB76oJ8JULy7sxkPA3sJaDmtKkdYG8s2dMfee4G1NCss6lsqJYw2al3%2FojoAIvXikIXv6mjkVuI6MkGYSdK6CRnKncZKo5PQCQMrbQjPZoq3QDVeacF%2Fe%2F0KeUXJDMPSirMgGOqUBLxbN1NoZByUNIMOhttwAa%2BJrabcsEEnBPqmWD6gmRMUfddVCCDFyege%2BSFBx%2FofKV2NhxRJTwm74ApcmO0hlaa6lWXi2ynKddUKkSCsMgtHZUtIaFQj5tpTGpBsWylI72jcn9%2BHU4LL0pcJzAknGFqwZ5harn7AtUnC9Csa9oITsUR8deddi2gjMKNzFLv1ti0kekd3IiAz6M5EYZy652kpOevUI&X-Amz-Signature=be1f6d796dadb203b1756b6b6224b55d0bf3e9197300c0a905a50641dc0347a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
