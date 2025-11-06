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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUL2AMEB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHhA%2BvhFzi%2BjPOz1olWDbP9F51pH6RQ1cw1AQfaWHZXCAiEAkUhtqfhQDubP8BXYtglRVDh%2BwTQgmYLB8yISR%2B54uckqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJUXOSj1Ar%2FCJbr9TSrcA9L5JqiAbqt2EFOKWEXWzUtjdQHtc2hLqDtFbe5v7KOfQ0f%2F5iAjf9gokjySyQk3W6hoUTcRajw7atR7ek6nN4kzW%2FpjMhE6AdWcvDzSeEVw8tj%2FWyJhneoFpP7SbV6Rr%2FQzErSlBpD7YVzlpRicuVdCh%2Fgk96g70wizOBQziTZ35fuLD%2FTt8EnyKQKLLqXnMvO6nkzBFRT7Zcfj29BbbWvfoaeN2ScSArNUyCAgUGorhO4jMXV3QRozqR%2BQ9is17V7c5xCIKkSjY%2BYmpSGaGaeEpd6ssKl2crMLtpJXzlaaBQFq448PSuVeJeTCjDtLBO3Ckmu7%2BCdYmZs2mSWpwQWrkq08sMVzZRXNIOM%2B10b4baK8P2T%2BcZuukw55BQEgDndTLFfiliThy8CeCHsvqY8w8Y%2B6aFqrm5HKloW8yz%2BOeHqukkDr2bmjMvxuMexb09R28YiG7dNYX8iYym6%2FRjDRJ9FKNDH3Agc0f4n12Vs%2BY7gJvktbDHReG1E4rptrNVLDlPJUR%2B7CIeaJWZm6UMFSXWsHVM%2F%2BaBTZdFBJ8BriZVSw3IpZH78HMOv0hOBn3XbhIlblKel6MR8jmFD5r2E1NSXOYis63ocpc92EoRciPYmTqCCp2QicbPT7MNrwr8gGOqUBao4wHBZpbfm%2FzTF2TBb5r137KgDQPmc25Qr6YjhJvCpQByMdq%2F68JVrduJWHYE2EyaxmJJmuEuoJIJ%2FPg5ccvHG2YMrhvPmIr87AKlQ%2BRS%2BP4iVK6Xb%2FqlMxu2GzSwLtOPpYnxFney5STZGlGWA%2BGB%2Bxo24uqYuEsomf7E68dCqxXJUyHI%2FHyQ03hH5UPQbRhNu5KRm4fzoEmh258o6Xjgs3gK30&X-Amz-Signature=7009f05bc42c4564a751e31b5a99428dc787c037db39eca19daf7da67c4b51da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
