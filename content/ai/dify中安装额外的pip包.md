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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAH3UHNJ%2F20260107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260107T025943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBeXoNLieVzU2f2nxA%2BKBgCvy8HkjOWuDrbiVyL6DxGYAiBvJLrOzDD3C%2FE%2BODrUjkQ8eNUY7mHmmk1cYrAXweeGUyr%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMYl35H2DObHZx%2BZ5qKtwDSjSI9iHg2KZ7GFXEknbXWc%2Bf6T5kijh7vMLzn1cciAaIMaoaQpkvTR%2FddtsQ%2BD4CVBbt%2FqTsh020Z9dWKRBjBS2DHZgzVOS8hS%2B6cUOuxyEw2LQfxixaxjrsgtJJXGypCNOe2m1IdT71mfNShqgKhLO9ZCqhyObnPc%2BdzZHzRmXKDuRMEmntpaG9Yce3KR%2Bwx17J6J9MG8j2UHbTOCDr2cTtcZ2xrKpHgcD19T456%2BjbgaBrmdr%2Fq1s253TLjTbxhCuMOSgteKaRIqhsucMKK%2B5i2ToX0hL9FJ%2FENEkkQrSbqmjjdRJrPrv%2FgVJcyjNswHJoRrfT359LbL3D%2BwQW7uek52m4ok9ryv%2F74lhsI8Tb24Cy72qTS4G7LGgRqlwDh5DhXBsMImdXp%2BW4z%2BF6OrZCm3QxvU4n73unW8GXJkT3uf%2B6Yz6S9mQDkP766VvFZuPXBKdWoJxiXD4KeOJBDQ410psmHQDTa11EGey8hIS8h0G6coHVXaua0VdL7x0jv%2FJLKBpVt7l4XjjTySfpKAzCbq%2BDLWf1YyCXrH7lYzkT8nwSOkWDM9rLvGYo0m9hp6VoUz2TXOMG39RJfPt1jtxPK9CyG5H56mx%2BO79qZcoQdhn2F3i4dE3y4YwwsI73ygY6pgHg3bpb6IjuOAiMaEXFoljN%2BSxCWTPiGG8nIiouHW0%2FfgFmiFd3aYsTRupQ67PrAzZ9e8S3p%2Bduild%2Bd%2FAxfVMOvgGjhanc%2FI65wBoeWB9xM%2BS8G51RQzXjqQBnDCr5r%2BvxMbBicy1mFoncqSJSn2fjGvAYWGxA%2BAZnML4MDNCpuQYNHsQFZOAcGlpWlKfk7%2F3SO84I%2F4NVIgiViPlDT3%2F6DFgkBTwI&X-Amz-Signature=ff77fd3ffc569cb37b5a56caa217b9516122ed09c950415151bf481ceb24c257&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

