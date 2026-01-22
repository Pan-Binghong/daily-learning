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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAJ2R3BR%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIDv5YJQDAhXF8z5%2FypFY6lRxoImacPje2M9rMSjDLAOFAiBQE3Mmq34Df%2FSbce92A6FcGc5aCGG%2BkSVN618dzjjWKSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3B66ylcZhpPobDHFKtwDJ2OPanbFZhisz4HkCjHOm7yRISrlRLi17CmTT3RSFd8MRp1lUPOJ3n6xycXDlrU18nLyWJPXXATwrgNv3qoe%2FEl06TJ03noyRQPjfI3at9ZjWJaOjGbTxODHvyb6ATmvfcLYsux3DL2NEra9HgiFXLz%2BblCid8uV%2FEcezdfAB3t1hb%2BTjLYqawxhDCaPGLeoQhOEx6pAsxzVV6%2FrY7QVP%2B5y8pFWxQkbhho5pa7JL9wHJjjPj1O8NyRQ987Qy7HZgvXixORqNqURe47dzK90qVdWCJW7Yvz5kxj79qAdvzpAMfQMISJd1ZfDOjvSwo%2BMWIe1lT5%2FU3SSsgX5ymVf%2FGoLw8HXop43aV3Uz6TEYq07%2Bj1tLQSsA5yQZlAlvdTnIwc7ea9XuqBAmsMK%2FQufbq57H%2B0pokehUrsVvaZ6L1UHjNraIvYUTtEv6RPkcWhnQAV1r85yfnRX9Vblt3mlaN7JpaiDrEOOcmgR4TeatN%2Fv3w84hbZ3Kth0aNzg8%2BnD2%2FurAMPxxPBaYNXkS6Ku21%2FOT0%2FmyAlqJdaFzmzTnJl71%2BFk0ddItPRhO%2Bp2cVRKS25tI%2Fj1nbwj5rvErjaV4Wrq0sg%2BPVjV%2Frn%2B%2FIRv2qSBwUwJHkSA3GNzuMYw5NfFywY6pgES6CpPzm0F8vbEEZCD75wS4x%2FxoxHOCsERZBIW7GoR%2FneSgiNrWexrWTn0mZN%2Ffd3wBmGkIRkoho91phep61h4h0sVyu33ivjZVeFWaHnj9ampPFjmt%2B2fJPhGlqdpW68%2Fq3kTMdJVotUvOUlbAn%2Fs0LdEJqZaBxkTns%2FdVus4PaCDeT8HpFNg01ujNmITn%2BuRqZxbmZdktiu3vJIgq%2F3py5Ysox3K&X-Amz-Signature=45ee583ca234fa9ac91f0a1160750a7156060167eb69ccfd4726bfa81573d0a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAJ2R3BR%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIDv5YJQDAhXF8z5%2FypFY6lRxoImacPje2M9rMSjDLAOFAiBQE3Mmq34Df%2FSbce92A6FcGc5aCGG%2BkSVN618dzjjWKSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3B66ylcZhpPobDHFKtwDJ2OPanbFZhisz4HkCjHOm7yRISrlRLi17CmTT3RSFd8MRp1lUPOJ3n6xycXDlrU18nLyWJPXXATwrgNv3qoe%2FEl06TJ03noyRQPjfI3at9ZjWJaOjGbTxODHvyb6ATmvfcLYsux3DL2NEra9HgiFXLz%2BblCid8uV%2FEcezdfAB3t1hb%2BTjLYqawxhDCaPGLeoQhOEx6pAsxzVV6%2FrY7QVP%2B5y8pFWxQkbhho5pa7JL9wHJjjPj1O8NyRQ987Qy7HZgvXixORqNqURe47dzK90qVdWCJW7Yvz5kxj79qAdvzpAMfQMISJd1ZfDOjvSwo%2BMWIe1lT5%2FU3SSsgX5ymVf%2FGoLw8HXop43aV3Uz6TEYq07%2Bj1tLQSsA5yQZlAlvdTnIwc7ea9XuqBAmsMK%2FQufbq57H%2B0pokehUrsVvaZ6L1UHjNraIvYUTtEv6RPkcWhnQAV1r85yfnRX9Vblt3mlaN7JpaiDrEOOcmgR4TeatN%2Fv3w84hbZ3Kth0aNzg8%2BnD2%2FurAMPxxPBaYNXkS6Ku21%2FOT0%2FmyAlqJdaFzmzTnJl71%2BFk0ddItPRhO%2Bp2cVRKS25tI%2Fj1nbwj5rvErjaV4Wrq0sg%2BPVjV%2Frn%2B%2FIRv2qSBwUwJHkSA3GNzuMYw5NfFywY6pgES6CpPzm0F8vbEEZCD75wS4x%2FxoxHOCsERZBIW7GoR%2FneSgiNrWexrWTn0mZN%2Ffd3wBmGkIRkoho91phep61h4h0sVyu33ivjZVeFWaHnj9ampPFjmt%2B2fJPhGlqdpW68%2Fq3kTMdJVotUvOUlbAn%2Fs0LdEJqZaBxkTns%2FdVus4PaCDeT8HpFNg01ujNmITn%2BuRqZxbmZdktiu3vJIgq%2F3py5Ysox3K&X-Amz-Signature=b8c213c3f0effd74351ac8be4a5537a105ca1378b6807a91a35e97868ec6007d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









