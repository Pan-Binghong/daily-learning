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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX7SHEW3%2F20260223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260223T034234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJIMEYCIQD9SoKpNWAOWZy9uqYpXfmOOuO%2BCM3y3CdiT6oJm57txwIhAOEw3IRMCkOywYfULSHEIh%2BfC3t7wT%2FtuGFUWLlljsA1KogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzg64gTUoGZwp8SrB4q3AMnrrZzt2MDZ5cG9OF84rAAlKAIDSCTFqKydi%2BQ%2Fs%2BhidAqiT0hlWuKIfNvCAPOGBgXwElES0dLiylBwOZnit%2F1Pv4jfxEanoyRUqQDR9j4B82FbYvU0JgKcy2UZL35R9hhzkMYgW8yDH9%2FgHspITy6geYSJfw1c%2FgWAW%2Fw6nBxzndZi4%2Bi7qcLcSMZ%2FTWxzoYIjvWOhoyztQHX0dxc1PVM6Am7WQIXk%2FEgboMgNXKue2csra5ovmLyFdC4mAo8kBP9eofVsCLw7ZhRyLG2SQgICx1pKUkTqYM1jRvHGX9ugXfr8XG3MuaekfetNXe3ARSl8mJJwv4uxrO0cqiDJGpQ%2F01QNkGis4h3SDfhzZLAx5MlfBz%2FfZAXoewj7%2F5iLLpBKCkJuXykCvqID8oNtlzI0jt%2FchBnGerJm%2F25T9mV8Y4PrqVPtIyylRHZMmI2NQWtojIg%2F%2Fak%2BygRmgNyFceoA7TVEjSUjoucvC6OP8vUA1mUcEZ%2BcFz6Ph7V0ipxPIWtwfHuxUpKEDf7TSy8mk0rdL%2FEylkt9urQExgs%2FCbIkdkpnzNxo8YBHTX5do5wWu8%2BmBAsafyRGBZvRqebhZ2PS4ldakMyA5SOs77RYJ%2FgaIyQcnxmDX9DvIlyojD1k%2B%2FMBjqkAaPTHh6HBYCMorIMb9%2BAsSBw85CFlVDZ1F0%2BN3vQl27Zzkc%2FJUkxSSRuHGigxJQkaCKid9e%2B0cMiPvFwvoA43QvHyNfS7SXRW4Dw3TWMul%2B80Kid5StLo8UX9YjG4H%2Fl4IlbDgImUM3zxYMNPGwcWF07eyys%2BHIOaJSQeqr%2BA27bkpFpSxl9zYsToinxwp8U4lzHZGO39bY%2BtbToZX9YdfB%2Bev3i&X-Amz-Signature=458a141f735adf89bf168a5ba6f72ff7954db837c263a80498d1d3784d04412f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

