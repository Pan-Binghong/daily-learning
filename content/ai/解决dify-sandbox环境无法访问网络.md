---
title: 解决Dify Sandbox环境无法访问网络
date: '2025-08-28T09:20:00.000Z'
lastmod: '2025-08-28T09:39:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 想要在Dify中实现，上传xlsx文件或者csv文件，最终通过代码执行节点，将文件写入到远程数据库内。踩坑记录。

---

## 解决步骤

1. 编辑squid.conf文件
1. 增加以下内容
1. 在Sandbox中增加PySQL等依赖
1. 重启项目
1. 额外操作
---

