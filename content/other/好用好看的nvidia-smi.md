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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY7GGTZH%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDP5BN%2FVVWDOpG9wmAYP%2Bj%2FZ4qfjKTl832XsTlHwov5TAiA6CbpymcvJlyTs8dGacwAPSdn3e1J5yGT3Mh2JL3Zd8ir%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMDyn28wcNCrWUFOHGKtwDPUnZL8KqjDx3Rpkgc%2BZqtkfk6BimJQGFkUrfRRI90glQEXiIJlWf8wRrxnVZSCnj%2F15cvj6%2F1Dvqvq4si67F2kolcZgNo1BDRx19Rd6PetkKlocJsEs6a7u%2FFWYXTJPBq4lWJQCQGbgNyndkupK3s%2BHJ9bdcKGzl1q03%2FioSjH4xokNF92x2U7uO0VgAPns0Z8GXMelcTEALwcY65BOcoHvci4M390hOZSEjEvhdRLjdNUJT28gxIXUIk66kDbuAuH2TTh2XYyPyaDAThAoDi2q8v23eQL6TUKeujzCACMORjcqd1IuqDIdgPTdcVrUlj%2BYT5QB4qEEetZiAS16%2FNqdesz59o%2Fhe8VZn%2BNg1hgtxlifAUlqTE%2B5ysjtqy5gtvy%2BTyB5qr3Ap8iG7pWVf6fWn20BIutfdmYcyCxSD90jopIKywiHPfvwqHdaIraZqt4W5vzd6UqvgRZJfOoiK%2F1JzKuTwtY6IRq2PS%2FhIqBHo663dOVbjguRj8JdCz9XCzjtQ2Kf6aRt5dwIaf%2BbQ3Xp%2F8nZWRnJuL%2FThHQdWPqkZqWyWRo63FHWvlrS5cAZJJg%2FK2Dws6QBiRrioRJLXtarZ%2F%2BzoHWMRxp2wOhoUqcuzq6y1wAgwUwgwa1UwgKjOyQY6pgE3B2Vf%2B9RpwGIsC7W7Zd9tDL1HCkOGKExIdNTBosVXrv1v1bR0QL0jWgsmA9y0nDeiHNSTIXkar6h9hwGn13Qc0N%2FxvCGaJdOgIgiz2dyYamv2POkuoKcyMfzyHsXlRsus%2F2JM6On0RBTiV846yFj0n3ypLMpblZNi4Xn%2BSvAy4jZmf51gkOd3wPhfL0HrrioKO7MU2%2B%2FMk6cDRKhXwWuGQ7hkxMl3&X-Amz-Signature=58e7305f87f68a8bde530798c76ecf055a8bea0b18918080af661936b45c0452&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XY7GGTZH%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDP5BN%2FVVWDOpG9wmAYP%2Bj%2FZ4qfjKTl832XsTlHwov5TAiA6CbpymcvJlyTs8dGacwAPSdn3e1J5yGT3Mh2JL3Zd8ir%2FAwhsEAAaDDYzNzQyMzE4MzgwNSIMDyn28wcNCrWUFOHGKtwDPUnZL8KqjDx3Rpkgc%2BZqtkfk6BimJQGFkUrfRRI90glQEXiIJlWf8wRrxnVZSCnj%2F15cvj6%2F1Dvqvq4si67F2kolcZgNo1BDRx19Rd6PetkKlocJsEs6a7u%2FFWYXTJPBq4lWJQCQGbgNyndkupK3s%2BHJ9bdcKGzl1q03%2FioSjH4xokNF92x2U7uO0VgAPns0Z8GXMelcTEALwcY65BOcoHvci4M390hOZSEjEvhdRLjdNUJT28gxIXUIk66kDbuAuH2TTh2XYyPyaDAThAoDi2q8v23eQL6TUKeujzCACMORjcqd1IuqDIdgPTdcVrUlj%2BYT5QB4qEEetZiAS16%2FNqdesz59o%2Fhe8VZn%2BNg1hgtxlifAUlqTE%2B5ysjtqy5gtvy%2BTyB5qr3Ap8iG7pWVf6fWn20BIutfdmYcyCxSD90jopIKywiHPfvwqHdaIraZqt4W5vzd6UqvgRZJfOoiK%2F1JzKuTwtY6IRq2PS%2FhIqBHo663dOVbjguRj8JdCz9XCzjtQ2Kf6aRt5dwIaf%2BbQ3Xp%2F8nZWRnJuL%2FThHQdWPqkZqWyWRo63FHWvlrS5cAZJJg%2FK2Dws6QBiRrioRJLXtarZ%2F%2BzoHWMRxp2wOhoUqcuzq6y1wAgwUwgwa1UwgKjOyQY6pgE3B2Vf%2B9RpwGIsC7W7Zd9tDL1HCkOGKExIdNTBosVXrv1v1bR0QL0jWgsmA9y0nDeiHNSTIXkar6h9hwGn13Qc0N%2FxvCGaJdOgIgiz2dyYamv2POkuoKcyMfzyHsXlRsus%2F2JM6On0RBTiV846yFj0n3ypLMpblZNi4Xn%2BSvAy4jZmf51gkOd3wPhfL0HrrioKO7MU2%2B%2FMk6cDRKhXwWuGQ7hkxMl3&X-Amz-Signature=542696dc585e3bbde901e90668a82cf1cc5a26b6ad2a986223d0848832fb954c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









