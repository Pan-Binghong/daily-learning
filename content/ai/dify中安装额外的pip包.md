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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RTQMBGNJ%2F20260104%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260104T031023Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQCsgnmrVcwCuhYLhf%2BiNa6dhXVjQlhhaGeGliO1mut9KQIhAI2VukK6i6ogJ7xOiPBxuC3ShXtaayEzgAwK4ZRud093Kv8DCCMQABoMNjM3NDIzMTgzODA1IgwNolgDwP8XIZJIukwq3APjeK4sGpdzmebruuFwFNYA47PNZHy%2BSro5XSSGwv4%2FelL578PupdXeHlipplHXH1Pmf7m2F0dpZncKeOoNi0egqAv3z9SjGZTPntxQ0f0UfA8ucnVY55%2F9cZQSZR4MaSj5WWPYs9Xrh51wyed7EKi3hW6Qx7Vq9%2FAIwkeUcXZ5U3MXD7cNizQFy9BeOz8qz8w5ENXakNYiYaSCHWzkArPS0XWT6RHSdicjoxiUqVsgKzXoEVCnRPJTpyzgxrhaaFiTES3WJ8h3HmO8VBxI2HiWmfF2JHiXDJTo3gZWeesabPWjikPLZ0OrVStjiKzZgZ2CT91SZdgTXecR3mRJcWvowLF73FrTv7TCYjO%2Ffy1lQm1yS1%2Fs0F90Cbbhn%2BPUDglk3VBQK2J9mytvO4QmvN7shARBRn4nppKZrFZbCoo4ZBcxr%2BilLKinGenV9Ujvjaa3Nw%2BWAw2t2lDSb21q9H7D9YNeLVFq18rQPY11HgI%2B4HkMCkAJKVuopQ9nwu7jaHQX5QeCkDk%2BsQshd1M2zP8A0LXXp9wal%2B0ACuiKv8DjtQflig%2BvTRcpjKBFGtDj%2B4cziZtlUU7cc6B7wamxVwSBpStqa%2BvOO4BE0BzztkT0jVQ3nZJ%2BZLf5CQIncjCxhOfKBjqkAZqZb2GJHFBbeq347Pw45tpJk4B%2BL5EnxDe7N2SXSNgKRlpgEoe6AM6dzlGZgMhty%2B8zZ%2FdCJIe24EGCYLqoilwo27Smx8bgpaz8nBkD8kYuC5QzTbsxTZDFePeHmnm8NntZk0vP1yXctV5s2A%2BcDpaAtpIRbPrxmH9ClLYtJ%2Bh%2FYTGvFi8oHyRkrq02VdMD6H4toWtp7UCBVDba%2Fa43xI2hutGn&X-Amz-Signature=266d407f9e57d7d0b0c016b5b9dc4635a5640a7755d10f5a650cac5be5594f65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

