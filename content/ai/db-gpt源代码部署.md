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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPVZ7T5%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAjnlOn%2FgcE%2BW%2BUZVgP15YrjcB2J3EbQ27ukXpPNI4VWAiEA%2FYVyfoBrGzpOLtqa%2BKPo9k84dG5drVfj7SfHopNh%2BhQq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDPxJpLpZDkblApA0YCrcA5hWb4Rt2v3NtVoqM0RV27SFZCR7tw5lFVyxg7z%2Fdopgx7CYBlR2p9JGBDmG2v9mTwOJHoC7eoIfhcmWxb737hucaO2TjwOSFHlAUA9VU%2Fpbpg6W8Qrdqxpujklhk7sxY5Mf3tjBY%2Flur1gRYsb7j0Qp0ySL5rPDs2I33exGIF2RGqf8SKlnDoR4rVBCoEpJ8aukMkmkstDzb5tj%2BT8qDT67Y9MbDF57bKLQm7srF41B%2BcGjs2CDBJoVQgeY1ca8EvEcslClMqkvFl6%2FkenDcva5pTVjE%2BzDirxMmCke%2FSYeP1V69JFLlvwf9v3ld1Vrw2d%2FLmByWrNoq7DDdBCdctUzr42xnWCyHCjDpx%2BEFZtMGrgNfZQm3ofHZOZ552hqczkvWygJrO3L2IWhiUQ85ra5W%2FbGGM4wPOGbeytwDERXAqbjRUKVUVl4PvW6pv%2FoYt7iKWbT1OO11TPGdnQ4h%2Fug9MO%2BAQJYCx8fYsqB%2BYrs37nQYr6MuUFgD6op1N3kZzzf6K5Iw7BoSJtuM2SMTRTbbREan0rYLhMfFjdkCJbK9CK2B7lf%2FnwSD%2FxIvOxOQWvglxDjCTb%2BRJ0LZZjt6DuLmadwL3MFj6v%2B%2FVwySSq4Rv7pD7Nu%2BdEk3BLcMM3kvMoGOqUB3TqjYob90LG3s8iMw%2BRH%2FHI61ybzden8nOzk2u1RDxZbd4mHGamMHPpgESpavPK4xx62qiobychAHkYBHjBhDVpLdbIbZ%2FtQcGRCT9t6IClaNP1fKh1E%2BAoCJIkkXeDkvsls8H0fY1Wtsobzhj0zCpFEK%2Bs9DKbWuxlAHOJVJ9Jc6TZZkFgCs8Z9QoBYSJh9Gs1BapJVTUAQ%2B0GmieCXGuOtYbem&X-Amz-Signature=cff78a0dbe02fa337629f7405b8d62e2c0cc65117f912a535202730a17d23993&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
