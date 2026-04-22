---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CMLYIN2%2F20260422%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260422T040941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJGMEQCIFSFocPEd4F3bQ%2BQB1CP%2FtLQQkrxpeqt%2BTHzRbCfd13gAiAk5T6ZmngQGYFcOLac6GwLC3LhBAtiMSkg5K6A4fghDyr%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM0q%2BaF1vbYuvq8VkBKtwDY454oIrWBqkW4BLrWJLdMjOkfQLQjYbQZRPr9a704ei6ymX1njXaU0SSquoFSV5BwzDrWl%2BcVQ1ivdIJ0WC3GoTR999SO%2FffJl%2BZCaA5qQJLZRtXOxhEAryyiSLune0QPQprdnYAH9RB%2FWopMjXpM5HAtLVOZ6Qovaze9%2B3%2FOOcl0SWfY2tdVGbmXAFyRvZMVrFRl0gLc4StOswgEWaMj7M1nnzxyAD01Mi6SFH4kO%2BG0DhvzWwr%2B0uOfymQSOhCUyqkQSWR%2FY4HezEo5iNXd7tJrYOlEJKDHRaW72sRqKFbwmrxHcNcWADnBg%2FBk6rx1sXT7QAwluX1MQfGhaXJOBvUcr9sdnLoTS%2Bl4uXxNzNybBk26clOscthmrpbqoDpxJllCiPVIVvGCKO6Q6VrP8LCUubxY%2Bf6hmJFqDV5Ph7dEUbU%2BLlE2vSxoSWkB0RjgGc06bIlYvDKknCeWVRw14Gxx8UkboJ93aKgSH2y8CTnG67gDGp4Cdx%2FpOiYQduukHMN%2FCfJ43vSXBAKNXdg99ZcrA1Y84iLk7GH5ICaIb5dHhJbIKH%2FtdjRpXpKqnZ%2F0Ahy5TlTlKfEFoe19OxKXZmYpNWkRHXLtHfHjIwCS59OTErncM%2BPLKTe7kow1fmgzwY6pgEMgn9G7aJ9%2FjE3sgoDyM7eEDr9VN5NDllmCa37kHkdkXk5JrFcNGLxEiaz6geS1tds%2BVl32QQ8YRMMg1gzc3iKHXjs3qlHdE%2BUfil4qDNN5yB%2Bmz8bUCmaFqKXzwQ63aUfxZvg9Mrw61cyI7WM8baFjbTnj37ZtzDz%2BA0iidxtuYfdiduUWm0%2FtdilIPqs4U53H9FgtUQ8rbveco6ZmiSsn3iN%2FoEF&X-Amz-Signature=c1393f5368697abe90302f0b91b47fe72b7d1ee150d5e1f594e651cb47f56e0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

