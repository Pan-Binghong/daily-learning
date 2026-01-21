---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P2UZZZ5%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeKAABBkA6J4APlD2wlbSSKeyLOtt3Xb7Lu75UNwo9jwIhAP%2F%2FI3AUccGjbTKnJRgICJ3JBX8D61kGym3vEfdjqYvRKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzo90bVt%2FXW7QaQdaIq3AMSwWkYfOcjWAiZOIzcr8EM4bRweDGHub0CgJmLCSB%2BYDMf%2B6HvvKyaUtvGOx6OyqVOwmczeKjgmurtBZ5Fm2ojHwIsvfU3atpY8KQ9XSgYNFtcY1gMtN9GrfNfsK6yiLiZOYkjXbPAE5GMKLzFOwL4gGTf0%2BeHOp0dMSkBwQgAEItrtvFc8RdWeAzFVBUxM%2FJZavunjqnyVFCQKDI%2B%2BgYhb5guXvUWpu0MYhzVus0MuZmcAQ4iO9bcfGZFTGK4qpRbW5c1tQ1cj2iM0ghv%2BAezSwwIonfR5Cejn1ON2q8F65j6j8iILBZoOXO7VRPQ6OcvJLKRCTemI37ZbnMLQ0%2BXP6KZOv%2Bt5%2BJh4UQEa75ggD%2B%2BbXcdaUYI6m8EKGdX0EDYRgCTPCOoosd4hUbGIS488fFO6bPy2eRGQFUSfBvClXyYYyu7G%2Buys%2Frhq0tCOUVRCGbc3pSkdr3GLQ7yrp3opHTn7P%2Bi1ov1D9ek1oEJhuGykm13m%2BQL0E1hj25zGjL49PfH4upqTGAAOcJAgj4PSDujYwVZzGdvCOTitnvaaMOq1trmSlFTulqh%2FQvyTRFt4oThJ%2F2Ru7KgSdVN1SV9aAg8tTJvSFIf6tV4ejkFTC%2FVwfyyj15HRT0Y%2FzCU2cDLBjqkASqA0J1PHqx7C0CefrqaDD%2Fm0al8%2Bu5XOM3g%2FQBnA5WP5PGObCkUtvFvHdslZw55h%2B8ii17m%2BvOgVuUbpqB2nIz8rnj%2FYgFn1xrQZkKstv3pYEGhKxM64N0NQ%2B045O5AG6lThx0LOlNISuuYjqbovlIN7YIPuyZfNTi9mWNyc3UfP%2B%2Bm7pRoaYDkHrr1kIx6nSXAcQB6TiAQjKxm5I2Gg2136hnk&X-Amz-Signature=1a22959a621d8c883e15362e06d96470808d2c14957cf2cc7d8b31de00cff0f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665P2UZZZ5%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCeKAABBkA6J4APlD2wlbSSKeyLOtt3Xb7Lu75UNwo9jwIhAP%2F%2FI3AUccGjbTKnJRgICJ3JBX8D61kGym3vEfdjqYvRKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzo90bVt%2FXW7QaQdaIq3AMSwWkYfOcjWAiZOIzcr8EM4bRweDGHub0CgJmLCSB%2BYDMf%2B6HvvKyaUtvGOx6OyqVOwmczeKjgmurtBZ5Fm2ojHwIsvfU3atpY8KQ9XSgYNFtcY1gMtN9GrfNfsK6yiLiZOYkjXbPAE5GMKLzFOwL4gGTf0%2BeHOp0dMSkBwQgAEItrtvFc8RdWeAzFVBUxM%2FJZavunjqnyVFCQKDI%2B%2BgYhb5guXvUWpu0MYhzVus0MuZmcAQ4iO9bcfGZFTGK4qpRbW5c1tQ1cj2iM0ghv%2BAezSwwIonfR5Cejn1ON2q8F65j6j8iILBZoOXO7VRPQ6OcvJLKRCTemI37ZbnMLQ0%2BXP6KZOv%2Bt5%2BJh4UQEa75ggD%2B%2BbXcdaUYI6m8EKGdX0EDYRgCTPCOoosd4hUbGIS488fFO6bPy2eRGQFUSfBvClXyYYyu7G%2Buys%2Frhq0tCOUVRCGbc3pSkdr3GLQ7yrp3opHTn7P%2Bi1ov1D9ek1oEJhuGykm13m%2BQL0E1hj25zGjL49PfH4upqTGAAOcJAgj4PSDujYwVZzGdvCOTitnvaaMOq1trmSlFTulqh%2FQvyTRFt4oThJ%2F2Ru7KgSdVN1SV9aAg8tTJvSFIf6tV4ejkFTC%2FVwfyyj15HRT0Y%2FzCU2cDLBjqkASqA0J1PHqx7C0CefrqaDD%2Fm0al8%2Bu5XOM3g%2FQBnA5WP5PGObCkUtvFvHdslZw55h%2B8ii17m%2BvOgVuUbpqB2nIz8rnj%2FYgFn1xrQZkKstv3pYEGhKxM64N0NQ%2B045O5AG6lThx0LOlNISuuYjqbovlIN7YIPuyZfNTi9mWNyc3UfP%2B%2Bm7pRoaYDkHrr1kIx6nSXAcQB6TiAQjKxm5I2Gg2136hnk&X-Amz-Signature=38f6bb39aaf55afafcb0318206f00937353150af2162488681b49b881415d2ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









