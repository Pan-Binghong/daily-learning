---
title: 多机批量配置Hostname&Hosts
date: '2024-11-29T00:37:00.000Z'
lastmod: '2024-11-29T01:08:00.000Z'
draft: false
tags:
- Linux
categories:
- DevOps
---

> 💡 批量修改 hosts 及 hostname, 使用脚本，并同步到多台服务器内.

---

- 前置条件为：机器hostname设置为h800-01, h800-xx格式。准备service.txt 文件，里面每行保存机器IP或者hostname。
- 脚本
---

