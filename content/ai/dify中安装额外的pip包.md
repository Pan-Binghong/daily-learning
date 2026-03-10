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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646DC4NIW%2F20260310%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260310T032804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIQCULvkDFmDM0rVIu2Xs6G%2FCtsIoMkyI7DbKyNZFyUkpfwIgN%2FTArKYSJVWrxZAubbcLiNmuFyjSB54H8QFEmrmYt%2B8q%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDOct9wkpI9Vebwp2RCrcAwkx7V3hvUR5SZ8HVT5BEarbjAT7mvr%2Fh1OIHpwP69wiaucAnM4L8j%2FgI%2Fo2klYYman29AcnNCOI839on3ClWjMxvy8Gs%2FN%2BVcCIM1sfvhepaaCLnwwcGd2bdgZ3Iw0%2BXcxbx0AR0YStHVuBskWVgNGS%2FQUlFicIAoPLQvfb3V%2Bzqh3nySIREiqtTELRxFqQTi7wN5nLlEpOnRpxbk%2BIA4blD0f%2FzgKWd7GmXzHvFyC9lWL32uhyM52SkR1mvn48t%2FIjTcP90UAZlGk%2BA3FmO43qvL1H1EenHWVzBE5VsJbLvkV6Xp9DdI1KyrabfMsWFZ9uje7mmfG5WXVanBfC50LuqYWo9ePC8XG53URI8otvdA9HEvLdopPsNKP25pST5RTCKPJ1D0bP2gaLZbA2ktEiREbJzfFKWupTZRqwUm9VRGVSIxbaPv5BEgzGu2SbMWUytGZ%2B1mk8ZLbm0fINIpL6B%2FAfcs9nAImdFWISsxOMO1ShZdKBad1ChjeDYP2JqMamJFqPH0q1I4MNbdJiL54IHelulAQ6tYuIawQPdsOJpdgnwgyk0EgDwqgHkpNrL1NvOtILdO%2ByQFSNna2avFbJ2sepGU9S0Tz%2FjvpMzvCW7Aqaj0YoP4Kpcs7JMO%2BQvs0GOqUBd4hGTZQpW1vRWnGWaCeQmVQBduMoGzS07xuA455hpOSxGRWybrk0Mc5jaEvymoy7jmZhUG0RxIQcf4yyseoPtB36xltDzJeRpgyCaswQ%2B4NMy8V92z6QF6aaDglOigJ%2B9L1bbxTO86YsenrRlLNLYvAdu0Ee8gZsJETivKvCXkxq%2BD3Wxe0H1%2FafljgpkOGJvI9gFhbYD%2FFTIs8oQmbfDa%2FzCXgr&X-Amz-Signature=76af15c90711138915c766217311809b121868429ac0f65fbe99941d1072c32f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

