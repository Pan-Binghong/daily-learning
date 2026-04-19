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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VA4HO7D%2F20260419%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260419T041627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIH4JZCM8SApSmBBRaQB5puBco1go8bOYyI%2BGv6daFVA5AiEAtM0M8oDdUcdtVrPbvFYadrMwFvRWiH6zm54v59TYtxoqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHTWQofSWDqM5TcuJyrcA9RwjVWkctz84GxEinUQu1jy9hqBMsCPA6fRV5%2BR0U6usAcAod1HvPp3UMGIuXr%2BYgU92GzXJDQHMciVRO7P128W9mRO8Rto7t9Wyx5Zrw8PajpD7rcXBqgBebgJyMHWaqR6kKjazOSUGx5CtfoClMf0eGe%2BIry4xsx5rDao6lzaIYGtrPSPTk8rKIYoN0P3LrkWouK3Lgv7dcMd98p4s4fk%2F5pe8%2FGynpR77V00hb0pldcv%2FdEmDTNkK0okJ18OSv40ckAwhfdMAlNcUFOT1TFH28vL0LJcXbgHfC5pPtZqxYGvi4rYxF%2BBicCRmI3hkbk%2FM9gjS0t1ZHwg6o6sFu5nQ3AyUa93SrEPYO1DSou6X0SxHTuMw4UD4AnZ5GPtUegLb40YTTnB%2BBqZC7vga%2BdcAjz345Wz7eGjTK5WIG2X5R5qACZkjV5aS%2BGbKmu2j2mRiqgLCiOMtdXzHTt4uqb9t8LYN8jAA%2FRO84XEZgSJxGWEUeJeMaEWuwTsPHNP5UnusjEwMXImtPCEyQGSV3Xt47o5SZpjaBH3SGEIZVDNzJ1t%2FX8pNHAIT2FZCnvE0hnDrFd7KqNqybyliKk0NohoPvL5MmHzORR5K3f4jLZkYGObGD5hJS8UZcB7MPPckM8GOqUBghteduuzSajFJwLvak2eCAp3u7lxgw6HeVxHCjRrLtQPWlYBsrovh66JZIRoTbEBnDzqvoRcyPrEnPIU6nCjaZ7cLZAlrWjhG3wVAjg0DwQ3Gg%2ByxEorF5BAV5cYjcSoCIehyJmO0nq9EiOetHbJEy%2FnDWo7s0vkgCd8bfDwt1bOE3ouaEVRTRjT5zgab0c1m%2Fx0GrzpikDu7CkjLkZccdI9tuHp&X-Amz-Signature=8645c93ad0a24dfc4e48c87303f43e71681b3bb4e2eb83b8c6d5135eb10a3cc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

