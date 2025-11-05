---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPGLNMTH%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T095858Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDAJxfYxPJWcDn6zLwfr7Gs%2BppWTeV8I2tazaSc9tyHSQIgMr6yzg38nl034bZP%2BVm5BTOZPckRzPH5MHuiYDudTJUqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFI4kK4z7pAxiDXoeircA1jJTVjqf9NcXzmhOvSk2iAWXgEeizkN7No0bGAztwGsrxUArwOgtdMTYeZXZsAucZRDtIqqYQ0LvETpUOdwmmvc1QtB09JBw%2BcIx7CpVvrwQ2YGeLDEl3nebpMWJOv1%2FSX%2F%2FNhS%2BqPMX9IG%2Fh9eASZPPktDk%2B2l%2F%2F0nKHAcQ0wHGaCp2Qk0mj6%2FQRRZ6RruXuGvzlxHfQVPjkTWPEmW9vWMYi9Pm7oZbmTb4M5WnxIX0j%2B7p51TRO5ybWnDRfuZPZtewykM9I23%2B9GOKQzR5bc5QEA5WuPQ%2BDtA4bqfkU25jnrLnQwxl7SR79%2FbGSNEcy5SoMunuLZQj2PMyBF3F8BqHvU2ZKnF%2FZncn44N7Q0jmd9MY5BTQ2lVaWS75VsuTosqDxf%2Bb0eSD3gaeK9Ox2c8JrSNBwKV8GHPhvD58r4ZVLHq3hZsMLli8DJ0%2FylZhs8pzeanOCZi5bkZ6arySFGvjCreIU%2BRiymOQA2Q6uE1EcjQisLRjn78ecYiZWUe0rVlpuqU6p1NkkQbU%2F%2FNwho9L7KtmFjsOKMfaYNBmrS5yk5CUXJoCpgHCYacZe7yqQsUJQvQHI6KsD0jxeg%2FlHMJQy1%2FKU3UjJStrk7WrulC61zR1aR6nCLboX4KMO%2BirMgGOqUBxgKouRVeV%2BZp2C8gEek2alt4OQYt%2FSmP3yU7MrnxFd2NsksbjdDpXOeNzACPNjFc4f3xKp%2FCWHNEGGVebCqv2R%2BZ3iFWgBUAgHUUuqbdmLOTco0i2NyTwT%2FYMlEAaBus6SAFliDiCahParAKIGKAXD9IamUCR4sl1o1wDMY51u%2Fhy8j2NtEPaH6BnKPV8C0sawFz512l7OOcH1luBJnvoSrFzTq8&X-Amz-Signature=847e15fb23d9352b79e66e3b8a78aa5980f4acbdbf36dabd0aa39e7692151b76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

