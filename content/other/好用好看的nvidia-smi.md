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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QW4SCXU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T025007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCqOA3G3xVUIjU4KhWZJ2yWhJqSVG%2Bxu3ds8QXzRvod%2FQIhAJIPzJmRCfoCqJG4hOp2u1uYBxvHi3nHe%2B7xMVTVOhsBKv8DCCIQABoMNjM3NDIzMTgzODA1IgyN4J%2BWDkEr3Tlqy4Eq3AO5FYY%2Fr94iwEnfGkoP%2Fd1I%2BEsKfJfu%2FlTrhRFso0lUmLhEAYiCo61%2BQkAzoR39EWWYHt9Lax%2B0rRejHa2x4Lm1DV7bBRpCyJ3CRT0oVewCcxHOj8JR%2FPLaqvTEsQG67H32ziTBCZAMpbR7t4MiBJ%2F8tAva%2FAJnZ9GpDGSBJIE%2BP%2Fm79ynMq9Njdhdca0FTnmJ5NN5wdRvel6igCG4ndSak24G%2BIqHWgc1A18PIHIa8otEHdTMRPCjxtrpRgn4V3VrzyL12%2FPQ00mU2v%2BwUcGoPIM7tJqbUQMkdtgtU2k765vjs8NVcYO0H2iKylJ%2FTuDIC0FavbCLn3vFHwyXFS6yhdzpeBF5jPDOcDOriE0uo4F%2Bga1ECESOSW8Cxykipa1E%2FsllQMTAk0Pj%2FbITZWe04kHg1N%2BZjttYsqNH60XCmZ31MUDwGg9iYVY2vf5HzefVBlW3pJih%2FQzE495iLh5oNKRM1kmj3x3sGzFbqJgqykm34WhsTnucCalEUZnWbzAk7GxnoOow7l2rTCkDu46dRw1a3CM4IqrqOE0t%2Fn4QMh8Rul4WsgiKTbYp%2FJKju7yt2plMXlPFywit6r0dNOpFsPeusSm2Dt9rWIkJ48yozviyE6fMxc4dAQXTc6jDBlL7JBjqkAdhAc%2FqMK5PgrUhfeJ1gMVFeNVIZVFoSjKgNWRmRhCenSfx4t3xZS76Z4qiUzmMK%2BfOVnFMnFTaRIfnjKqt%2FqJZdaCGHx6C5do9o6v56ouUn9rzWgHwLiuH%2B2SmaPiw5MuwYR7tx5V1ekFFnjSrOheaJXQeqFCL52DfR264TRogWaIzTVGqp4iz9mFZUQQRKBDlGJzRJUCkFr6F1%2BIe2jFS3jDE8&X-Amz-Signature=1de67a2121511f838606efa1fd27716f83c3637c8ebe6cddf9abc0e08e6f3e07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QW4SCXU%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T025007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQCqOA3G3xVUIjU4KhWZJ2yWhJqSVG%2Bxu3ds8QXzRvod%2FQIhAJIPzJmRCfoCqJG4hOp2u1uYBxvHi3nHe%2B7xMVTVOhsBKv8DCCIQABoMNjM3NDIzMTgzODA1IgyN4J%2BWDkEr3Tlqy4Eq3AO5FYY%2Fr94iwEnfGkoP%2Fd1I%2BEsKfJfu%2FlTrhRFso0lUmLhEAYiCo61%2BQkAzoR39EWWYHt9Lax%2B0rRejHa2x4Lm1DV7bBRpCyJ3CRT0oVewCcxHOj8JR%2FPLaqvTEsQG67H32ziTBCZAMpbR7t4MiBJ%2F8tAva%2FAJnZ9GpDGSBJIE%2BP%2Fm79ynMq9Njdhdca0FTnmJ5NN5wdRvel6igCG4ndSak24G%2BIqHWgc1A18PIHIa8otEHdTMRPCjxtrpRgn4V3VrzyL12%2FPQ00mU2v%2BwUcGoPIM7tJqbUQMkdtgtU2k765vjs8NVcYO0H2iKylJ%2FTuDIC0FavbCLn3vFHwyXFS6yhdzpeBF5jPDOcDOriE0uo4F%2Bga1ECESOSW8Cxykipa1E%2FsllQMTAk0Pj%2FbITZWe04kHg1N%2BZjttYsqNH60XCmZ31MUDwGg9iYVY2vf5HzefVBlW3pJih%2FQzE495iLh5oNKRM1kmj3x3sGzFbqJgqykm34WhsTnucCalEUZnWbzAk7GxnoOow7l2rTCkDu46dRw1a3CM4IqrqOE0t%2Fn4QMh8Rul4WsgiKTbYp%2FJKju7yt2plMXlPFywit6r0dNOpFsPeusSm2Dt9rWIkJ48yozviyE6fMxc4dAQXTc6jDBlL7JBjqkAdhAc%2FqMK5PgrUhfeJ1gMVFeNVIZVFoSjKgNWRmRhCenSfx4t3xZS76Z4qiUzmMK%2BfOVnFMnFTaRIfnjKqt%2FqJZdaCGHx6C5do9o6v56ouUn9rzWgHwLiuH%2B2SmaPiw5MuwYR7tx5V1ekFFnjSrOheaJXQeqFCL52DfR264TRogWaIzTVGqp4iz9mFZUQQRKBDlGJzRJUCkFr6F1%2BIe2jFS3jDE8&X-Amz-Signature=ece281886810e126873982c5db2152ea07c59aac1b589d40004caae03444392f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









