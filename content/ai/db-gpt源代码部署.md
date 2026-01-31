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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSTMG3UD%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T032352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDPVE3Qxu9mikXYE88cz2o%2BkayU6MYsg6HGVZhZKFlKoQIhAMyCoh5xBUuj%2FzwiVvm4p%2B2d3pIermkUJ%2BSQ%2BcKEdzKjKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwn79celrVXbkIQFfQq3ANhflLgrVDq3Tuq3LWcOZLDq91EMLeXmQjVqCcDD%2FbPDusYL4LqIzpd%2BRr65jdTQ%2BMmlfkt9qCEbl55WeGxj926LjdTpnECWIWlizqwlgCZ2p4Bpa9UJpSnbO%2FR6Wf%2FdDITijEuyVPDSa3zNM%2Fp%2FBggk3pZBx%2BXF0270mNgh9I%2Fw8w8J%2FHt%2FWs2wgCLkB6KhGDaDI7Y4cVwBx6TjKS54raFSlB0%2FsnRpUeQo%2BBU%2BE3npH8o2M2f5oV7xpwAg7Kz2dQ5%2BAIV6eKugP%2FquSMLFtaXlsJ49i0lznK%2BjzWN51rcwTqsqjCfJyDoMre9avMoWoAVL%2BtxgJ4GsDsi3lTGh2gqLpy%2F4dImVYxd4lIYgzKj7icawwJ6WzwxFXvSfJYElafBgqCxHRY%2FW%2BpbQBRGzyf0pp5CrtfhnZdxAiezunKlTW1A2ciDQA0y2jNjIbESy6tktwvPbnILdn7oeqKR8lW74sMdOLc4PjxxgxYoeDe1JZwCJBQguz0KjsaRi%2F%2BCRtbc%2F8CNjvaWufyvtu1%2Fy2IanwNW081JMV7Y1Pg4%2FeHl8TImc%2BX8vpoO9TV8IGXbE6tr49PSx3QiTZs2v%2BIS3R%2FLDf0LO774%2BrJmf9uwti7TKVOh05PQIhYPYYHEpTD3y%2FXLBjqkAUqF6vqgp4NatFpOOhYtOH4Ztc%2FgI5vwtgJVFbFJ8YeCn%2BoE4WKclWh74Q0hC4JgFKKW6%2BRB1LfljcoA6K9ZBKe%2B33MusH0DIXHA6BlKGz9dUFyNNkJ8ubOX8xjw0RAHHMuODSgn5xrLSCopfVbxntxjGy3wsmGSN5xYTf03ylKeCYV6Nnx60D4FjhTOJ02xHqnr14VX3fVIK0BW8n7gzp%2FsW87%2F&X-Amz-Signature=3db857c0693a8039e81c5533c7745083554603cdeb8066a133169ccb57703e31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
