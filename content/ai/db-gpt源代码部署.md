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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/257103ae-75a0-4053-9c33-fdc2fab837d6/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HHHBF37%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032634Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEmXPo1Mb4pbcICAMFSUbsI3Mj%2BgmI2zfy3plB9WuWXyAiEAnw0lBSbFHibQnV9oOWb2jXLTw86J8P1nfebijKqJTx4q%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDIhfHCLzsW6FMvXs3SrcAxRPzmuCRqIqlg7XYw%2BhkY8l3HfgfISh6JR8saIvk0cLkGsiXEHYfvF2paKYijy3TFWh1tp3I26CuwZ9hBdnbvlM1mClH72rYyyFQ%2B2h3Dvz2MkNpO7luFHvsifjt4aB7x2tdIUoHhh7Hjjfgc8Zw4hm9q81YC4vtqD8rFS9QetCv0r%2FOct1YPvLpmUd12jbvxDZ44wOHk%2FtGZjg6gad5OTexmpeuNIUBi49%2ByaBjryxxknccwQvkiXQ2JF4oFoMe7pgSCWvPwxEW07hddoN3U8xxMsQIEgerW6gNcRytLSqdcjNQML4GKjVOFEVlOdt0gXE5HDCxhKM7g4uPUe%2B%2BsYlB6VbrJIkSe%2FSlG7xjZEBkEsKqZF5Mt%2BR%2BA60Peb41xU%2Fi3Xy1Or6FCjHzqgWtkOKachw3Vb8lW2lf2mA34RLjffiZY5vW0YuE%2FoLi%2BgpuzGsNA%2BZ%2B9hFHGIe9TQBCq%2BLXVHw8BzaEfxiXOv%2BLyZRsSa3cJ4CFKl8%2FCNZzNmOxSOkGCfC%2FR8a8PoRApoPXlIy5PY6zDxzF1OYOSxQQ8VHxmkwfdeVWmLv3%2BQM28bI%2B50a38gUnuYXJY1J5AVTUzt%2FaEc6rgS664w%2BJ%2B5Fqtnp3AnK7Yu1N0rooLjsMObEmswGOqUBsyRGKbTBoaeupYH1yLkgTZvAf79PEax3GTljx0a28lozYyPveZMytnw2Er%2FztE5sgkbm5G%2Fj0tKu1nJRDDJjahyOE1rN5d2BC7ZTiqKIaFkyMVlo7socs%2FoWdYgeIO6JGrLN9ktrsLx3zGJlNj8EiCLI0Rop%2BAdvkI8HThLntFVP6tccDjnA0fgP3hYcbMRovnADDAk8JhfIlSol%2FfzAWQD%2BpqNp&X-Amz-Signature=56b0023bd431fa7aee7af4d3c4b224ce86a47c7b0e68b7bb5e09cbc17609fb7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
