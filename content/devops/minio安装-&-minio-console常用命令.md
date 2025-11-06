---
title: MiniO安装 & MiniO Console常用命令
date: '2025-10-30T01:44:00.000Z'
lastmod: '2025-11-03T06:08:00.000Z'
draft: false
tags:
- MiniO
- Ubuntu
categories:
- DevOps
---

> 💡 MinIO Client (mc) 是一个强大的命令行工具，用于访问 MinIO 服务器以及其他兼容 S3 API 的存储系统。

---

## 一、MiniO社区版Docker安装

- 拉取源码
- 启动容器
---

## 二、MiniO Client安装

### 2.1 Linux安装

```docker
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
cp mc /usr/local/bin/
```

### 2.2 Windows安装

```docker
curl -o %USERPROFILE%\bin\mc.exe https://dl.min.io/client/mc/release/windows-amd64/mc.exe

# 添加到系统环境变量中
# C:\Users\Administrator\mc.exe
```

### 2.3 验证

```docker
mc --version
```

---

## 三、MiniO Console常用命令

- 添加MiniO服务器
- 列出bucket内容
- 查找文件并批量下载


