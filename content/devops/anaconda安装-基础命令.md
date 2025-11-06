---
title: Anaconda安装 | 基础命令
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-29T11:42:00.000Z'
draft: false
tags:
- Conda
categories:
- DevOps
---

> 💡 记录Anaconda相关操作，主要涉及：下载，操作，配置清华源等。

### 安装Anconda

1. 下载安装包
```json
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
```

1. 安装
```json
bash Anaconda3-2024.10-1-Linux-x86_64.sh
```

1. 配置环境变量
```json
export PATH="$HOME/anaconda3/bin:$PATH"
```

---

### 常用命令

---

### 配置conda清华源

1. 查看 conda 配置文件的位置：whereis conda
1. 编辑配置文件：vim /root/.condarc
1. 将配置文件中的内容替换为：
1. 运行 conda clean -i 清除索引缓存
1. 创建新环境conda create -n myenv python==3.10验证 conda 源是否配置成功
---

> References





