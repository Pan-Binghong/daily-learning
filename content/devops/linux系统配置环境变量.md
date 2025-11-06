---
title: Linux系统配置环境变量
date: '2024-10-29T01:52:00.000Z'
lastmod: '2024-11-20T03:10:00.000Z'
draft: false
tags:
- Linux
categories:
- DevOps
---

要将一个目录添加到 $PATH 环境变量中，以便在任何位置都能调用该目录下的可执行文件，你可以按照以下步骤操作：

```bash
export PATH=$PATH:/your/directory/path
如
export PATH=$PATH:/usr/local/bin
```

使用export命令只是临时设置环境变量。这个设置只在当前终端会话中有效，当你关闭终端或者注销登录时，设置的环境变量会消失。
如果你希望环境变量在每次登录时都自动设置，你需要修改相应的配置文件。不同的Shell有不同的配置文件：

- 对于bash shell（大多数Linux发行版默认的shell），你可以修改~/.bashrc或~/.bash_profile文件。对于系统级别的环境变量，可以修改/etc/profile或/etc/environment。
- 如：
```bash
echo 'export PATH=$PATH:/your/directory/path' >> ~/.bashrc
```

然后，为了让修改立即生效，你可以运行：

```bash
source ~/.bashrc
```



