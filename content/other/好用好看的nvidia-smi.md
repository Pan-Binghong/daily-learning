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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635F6CIUO%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQD7B6As0C0p4rn6Bk%2FGFGzzPIu8uG68lcgF9yE74GUN7wIgekbtAXhiSuAdnZSHO4PsycTays%2FGR6p1lN3tqGJ8DL8qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnW7K7tpZ48zjWseSrcA0AJHy3D43wkiuF4GoFEZwDGm4CmOXGWocO6JdS9XWPCQ0LYXSXuxfM0c%2Ffb%2BOr8piy%2Ftyayj1poYcZivScnwJVvtwg2XzT5P9gyBfDzUgEhZtA8bkOm09o0pumg4gtdz3TNYD2G78bgty2CgZ307%2BTe%2BHn5AX9xpPGl2C5Nk4uhOxiFzOteicOC9V6TPHya3Qr0jcnhQMPIMjEh8Kdo8vjx3QVrc1rzu8%2BSGs6Zhu%2BZSHOkSWf8ay4K1vsLrHJxyZX2ZdYuPO%2BuppLgnFFPkg%2BGydXiUkQkiJ%2FuRfJgVvS7j%2FNvyJztBGvAoLnu68Sc%2FqEed0dfRiO5HOMYe2a3AOm%2Fu%2B2iJL1DCtTb%2FCRAu6BRvpfTyUskudxkRabCTK7Y4sxnGs%2Bt4hmEDpIwhUpVK%2BDz4DXJHyYzkWCn7qJVSwo%2BTglY4x8OH3PFSkNprLA5ptOVl%2BLOXq5bCjzSrBWymSLI1jt8YwOnvLa5InIlKmSuU1ksHdqCTZTH0VQSRDjEp4VIcC60oKZLYb5mQh4l6BXm9wx0W1ioIDYxmCI%2FQ9ycOnD%2BXQPm2S%2BsBB7Kr9Wk53tN17Z%2FysqAhFjpdLVANVckDwlxMT99qpulNCPSpcP%2B3bFHj5OhLI%2BLy5ZmMNe3s8kGOqUBfOeDXMiWltcyp4zmpbG8uRDzm9SvGfut25lXAPeS293dN5Lxpv%2FKl1yzbCZ8w5LoOuNl4jx%2FClZoSoJrumvk2rNyWjalYkvwN0lwZj3w3%2FMaA5pPmBgSJyc4wrpdbqUQltE2VW8ilO7BePMxnjIcCiVlbGo0hF9qP%2BFT1LbVd5FT7Wmb%2FJwfBEpQ6OJogaAJDZ7FC9lZPRXKhH825a329r8nDDJt&X-Amz-Signature=d95959d5e09a4df8d8ef97d66afed2a2ac67c53457b3bea0160924a9da8c3333&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635F6CIUO%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T031133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQD7B6As0C0p4rn6Bk%2FGFGzzPIu8uG68lcgF9yE74GUN7wIgekbtAXhiSuAdnZSHO4PsycTays%2FGR6p1lN3tqGJ8DL8qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBnW7K7tpZ48zjWseSrcA0AJHy3D43wkiuF4GoFEZwDGm4CmOXGWocO6JdS9XWPCQ0LYXSXuxfM0c%2Ffb%2BOr8piy%2Ftyayj1poYcZivScnwJVvtwg2XzT5P9gyBfDzUgEhZtA8bkOm09o0pumg4gtdz3TNYD2G78bgty2CgZ307%2BTe%2BHn5AX9xpPGl2C5Nk4uhOxiFzOteicOC9V6TPHya3Qr0jcnhQMPIMjEh8Kdo8vjx3QVrc1rzu8%2BSGs6Zhu%2BZSHOkSWf8ay4K1vsLrHJxyZX2ZdYuPO%2BuppLgnFFPkg%2BGydXiUkQkiJ%2FuRfJgVvS7j%2FNvyJztBGvAoLnu68Sc%2FqEed0dfRiO5HOMYe2a3AOm%2Fu%2B2iJL1DCtTb%2FCRAu6BRvpfTyUskudxkRabCTK7Y4sxnGs%2Bt4hmEDpIwhUpVK%2BDz4DXJHyYzkWCn7qJVSwo%2BTglY4x8OH3PFSkNprLA5ptOVl%2BLOXq5bCjzSrBWymSLI1jt8YwOnvLa5InIlKmSuU1ksHdqCTZTH0VQSRDjEp4VIcC60oKZLYb5mQh4l6BXm9wx0W1ioIDYxmCI%2FQ9ycOnD%2BXQPm2S%2BsBB7Kr9Wk53tN17Z%2FysqAhFjpdLVANVckDwlxMT99qpulNCPSpcP%2B3bFHj5OhLI%2BLy5ZmMNe3s8kGOqUBfOeDXMiWltcyp4zmpbG8uRDzm9SvGfut25lXAPeS293dN5Lxpv%2FKl1yzbCZ8w5LoOuNl4jx%2FClZoSoJrumvk2rNyWjalYkvwN0lwZj3w3%2FMaA5pPmBgSJyc4wrpdbqUQltE2VW8ilO7BePMxnjIcCiVlbGo0hF9qP%2BFT1LbVd5FT7Wmb%2FJwfBEpQ6OJogaAJDZ7FC9lZPRXKhH825a329r8nDDJt&X-Amz-Signature=99d4ee395598e03ec222272c52196c34eefd1ecb92bd2a325589e47c1085a591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









