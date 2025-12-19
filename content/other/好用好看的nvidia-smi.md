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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKB5BZQE%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMJ2L2PkGKxvMthGogIAZnovEhWbnzqZqfUApZgPEZcwIhAMFcTteiS2wws0mxbGjphq45mzMocy8s4Ak99bMZ5iBuKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyfs9f3PIdsLGRRnPoq3AMWTVFAplqdlwqFz6IFcHeL%2Bmt2D0wkyjrqdbTTsJmx6LlzaVuEAIgrrxTKoe0HMDHT8j2kU%2F2hDA3TRrfImYYJjCArE%2F92Ve%2FABErS5mh8IHvfMe9p55UN%2B1o%2F6mAd1St0sBt2NgdspipdW69YlUSqER9LTmIbKJfzesgnI8BOfYaUQLogZ9Ql8R4VOd3c8T%2FEWsnJCpPHH0qcdBVZhxl7n9NFdpmKmWF%2BzK9MBzAyyTjOaOl4PhXCDKtQOwh6I8A6gbh%2Fi81x%2FFZx1G5VH3svgA1ejdpVrSXQcKeViXi4HCRdn4CgcRtSepNybl3xhWijGKDGLpWjW5ihziasyP0GPH0V1p2YjtVv1FWwvurQRLvr1%2FgwQWVbHHByKoSmfhFen9e1UNY6u3iVHNXRIk8Gy7qUTYmvGmcDiEeYUkTemu3cOu77o68iWiTkRtyn%2FgVLwvbU%2BW3%2F8Nbw6roUjCl0RjaTJ2ZztoTWkY6G99WSg1TpTVvJWKDfqysBYsa4ZjX1w%2BHdz4KRiY%2BMQoFXwUZhclJ7hxLVUcVUiykK10RAlLxvZFthtYTQbu0yDoAmnl4DB4QBP%2Fa%2BLDyW6VnV5W7fZMNB%2FTsA95DYcLJje5HqksY8bYEk3LdSVYSyfDDE4ZLKBjqkAdhKQP%2FVzc2QqnMdicyHfWeQxNuhRp7%2FRNbr42YvcZMu2QyyuYC8toJHsnDgOeHlTkfhuAP1bGm%2F%2FTLgT2ARuF963SBl8OFeyJat1HQxHwrmtg9mrtgCuGnLvUR4GRlcvXE0Uck5i66AbWUte9CV4XDN%2FIOVl0cF1SB4j%2BBudMKl3okpld5tQDBUciGNH9oliwfMVs70mpTnQk4XKThYJ0iaxZx7&X-Amz-Signature=cfdff05e8d18ba957ee342e775846ec5f9c77866f939eb80ee60ebe77f64a1ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKB5BZQE%2F20251219%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251219T025627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMJ2L2PkGKxvMthGogIAZnovEhWbnzqZqfUApZgPEZcwIhAMFcTteiS2wws0mxbGjphq45mzMocy8s4Ak99bMZ5iBuKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyfs9f3PIdsLGRRnPoq3AMWTVFAplqdlwqFz6IFcHeL%2Bmt2D0wkyjrqdbTTsJmx6LlzaVuEAIgrrxTKoe0HMDHT8j2kU%2F2hDA3TRrfImYYJjCArE%2F92Ve%2FABErS5mh8IHvfMe9p55UN%2B1o%2F6mAd1St0sBt2NgdspipdW69YlUSqER9LTmIbKJfzesgnI8BOfYaUQLogZ9Ql8R4VOd3c8T%2FEWsnJCpPHH0qcdBVZhxl7n9NFdpmKmWF%2BzK9MBzAyyTjOaOl4PhXCDKtQOwh6I8A6gbh%2Fi81x%2FFZx1G5VH3svgA1ejdpVrSXQcKeViXi4HCRdn4CgcRtSepNybl3xhWijGKDGLpWjW5ihziasyP0GPH0V1p2YjtVv1FWwvurQRLvr1%2FgwQWVbHHByKoSmfhFen9e1UNY6u3iVHNXRIk8Gy7qUTYmvGmcDiEeYUkTemu3cOu77o68iWiTkRtyn%2FgVLwvbU%2BW3%2F8Nbw6roUjCl0RjaTJ2ZztoTWkY6G99WSg1TpTVvJWKDfqysBYsa4ZjX1w%2BHdz4KRiY%2BMQoFXwUZhclJ7hxLVUcVUiykK10RAlLxvZFthtYTQbu0yDoAmnl4DB4QBP%2Fa%2BLDyW6VnV5W7fZMNB%2FTsA95DYcLJje5HqksY8bYEk3LdSVYSyfDDE4ZLKBjqkAdhKQP%2FVzc2QqnMdicyHfWeQxNuhRp7%2FRNbr42YvcZMu2QyyuYC8toJHsnDgOeHlTkfhuAP1bGm%2F%2FTLgT2ARuF963SBl8OFeyJat1HQxHwrmtg9mrtgCuGnLvUR4GRlcvXE0Uck5i66AbWUte9CV4XDN%2FIOVl0cF1SB4j%2BBudMKl3okpld5tQDBUciGNH9oliwfMVs70mpTnQk4XKThYJ0iaxZx7&X-Amz-Signature=115cb4bca5bccd5389fd463772601fac573bb97317fc49f9d0e96271c7fd7526&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









