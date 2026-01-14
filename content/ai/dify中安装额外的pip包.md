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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TP43R7C%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQC%2BPeRQfL0DHZpMc%2BHuHlvAYY9smEdCPqTlGnQw6ypfEQIhAIyOIUB9bucqtbosyTVbcpWvh%2FPeJ0Pk7%2BB83tVd3zKhKv8DCBQQABoMNjM3NDIzMTgzODA1Igw7ZGRh%2FlseE%2Fa7Hzoq3APAIdkgRY7Wwf8XOGRwn60uroX8B%2FaazBThEY%2BXPyZvmg7dII78z8n27r5gynIPrraz2m4043P0BYJA5ghtdKWC4obwkvKk8F132FIapupEag5Lc0YPV%2FID9kYzPzOiBU3FraWTziXWqYMAFvFGHCS5ZBC333PkKVkvvEtRJtbFb9Qp1AeGDUp9ltEXww8ZSzCpsi2FiOjcwG1fxMLHRQDNA80xPNyik15vOGvP6BN%2Ff4uHhjI77gKd1Hu3jSS0K%2B5mAarRrDjTzdkQ2tC6cnKzcvqV8XFoo1v9dPvEWIl5rSc2JLh1Eqevh6WhDAkfiuRX%2FAsvPf6q530qdTnmRe8wWFAdAUIZA3SE4dve3kSM37%2FauiVAfO72syoDiEBnDeKNvLQfUlavJKuTLbxSb6Tgo1CHsUnEs14uUA9zBTLRSkwsr3c4ceIm%2F%2FL3qzj7V9o2TwDkriLkDFQEUDoSvd6y3ztdFr8dIxp5AlMfST4InLDkN%2BAXPrqMfRVDEDrstok9Kt7QyYoE6BohNJ2Z2voTyhxsmAN0VL87oPGERWwN4fUe9MmYpsb2UZAgxY64Hk%2BdTboxxjeL6UqHym6N45Ek1OGM90NavyswoQG8rNLAOE%2Bo1uofnIMMoVbYBDDFj5zLBjqkAWbf7%2FUh7UhPOZhM8qfQN1MjCd%2Bv%2FwJVfM1xhA%2FYA3oXfiYYYT7QyzbaJnoqYZrnzWDz6RNhUaI2xfhirDqI36xMdH%2FfyWHg%2FZ3NVxabDYd3pq%2B1S9P4uitwNvx2HVJQXyNJoeRXDPxHeI5MDhgwLTpU%2Fe5v5%2F%2Bn1K%2FanH7Muyt1TDpb6eosYJGNl8zCbvX81p1LEK6IAw%2F6nmPFJgopgKYUyDYu&X-Amz-Signature=44854172dc39cce89631c07ba38fdd02552466ad781d6f6a034bc579b39c1b14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

