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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OJFTDNQ%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZrMkVh%2BzxTqrjbsqG0kv%2FRvi%2B4dTtTlIzCCyNaR0TrAiB7Kfeofpn5Dj92%2Bhh2x2DtPoY%2FMHpu741Us5R6X%2BltsyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPXRc3NhAW19uowBNKtwDuUGGBSJS4CQf2YhrcgUGr3OmB7X%2Fd2GYUH52pMfNxeVW5xn0mIwagQNuIGCd9b9Xq1C3NDi2K%2FFFRNJMlV1YSZqONk%2FOwa2qo%2Fax1wav6jtMx6Z4Z7TOv0uSGe3dZd7BpdJoGe8CrdAnWZYdsa671lHAUUr%2BO14bkMX%2FtaC4%2BtxWP7xDPVFnFW01dzEr5PxhMx9YZUyQ1iIxkUY9GwqOhjKcl3%2Be70vjpL3Lemw8gpGNsqRGO8BDit5e1X%2BKJGxk6WtByIZmqkX7kShXzyH9AOYJOnTBDYt2jRy4k2uW2OFLOHd%2Ft1eani8UXtrIRIChhpYo%2FMguCiXPsGMoOk%2Bflx8vzZdxEFLzcrHes9b%2BgXPwocPu7WqTlmpT2wIYqARfiv75AY5dWEhLEdp5BVR%2FQfntAozlN%2F4vxWJ1bQbIeSV%2Fsmly40il10G97%2FnrzVuQ4l8fBHfwEPjQsqtB21eMbaQMAyoYqQ%2BKZTQXRrk40wVC2qMMAFbTCx9Jts5O8cZF9faTW5TDafiNPqfIGEVnuRazbhN3yPfDclhS7nL1ytNHA%2F%2BzI%2FEbGzAGyIOnQewMndxOluJ2tIwT1ktsyGBsV3%2BKbLFsl%2BN8iqEkLxsHR8yEghuPgsBG2n6P98Qwp4aYygY6pgGxbVCGdJY7v5OVnMugoNct1tlflXEY4%2FvmZbHoz1y2zuCmJTkY4Uj1d%2BYvkXJhLyDYyqhqjSZZKG3iI7lHoTBdCudDX2ZMJLnPTDC37R0Fo%2BCVFwBkTbyL3C%2BVuNWVuOHe%2FPUb1zJJ4gKxiZMz7%2BRrvGOvQT3pl%2BnKvbq14pQv2ARXSvQ%2FROjLp5cLmCevhmU%2BmBvV8fl3JWk3vInS0vIE01oegtXk&X-Amz-Signature=b7ef0a9b603c1ce68b2cdeab0510b444b3079394114813f1088361ad096b75ce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OJFTDNQ%2F20251220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251220T024653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZrMkVh%2BzxTqrjbsqG0kv%2FRvi%2B4dTtTlIzCCyNaR0TrAiB7Kfeofpn5Dj92%2Bhh2x2DtPoY%2FMHpu741Us5R6X%2BltsyqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPXRc3NhAW19uowBNKtwDuUGGBSJS4CQf2YhrcgUGr3OmB7X%2Fd2GYUH52pMfNxeVW5xn0mIwagQNuIGCd9b9Xq1C3NDi2K%2FFFRNJMlV1YSZqONk%2FOwa2qo%2Fax1wav6jtMx6Z4Z7TOv0uSGe3dZd7BpdJoGe8CrdAnWZYdsa671lHAUUr%2BO14bkMX%2FtaC4%2BtxWP7xDPVFnFW01dzEr5PxhMx9YZUyQ1iIxkUY9GwqOhjKcl3%2Be70vjpL3Lemw8gpGNsqRGO8BDit5e1X%2BKJGxk6WtByIZmqkX7kShXzyH9AOYJOnTBDYt2jRy4k2uW2OFLOHd%2Ft1eani8UXtrIRIChhpYo%2FMguCiXPsGMoOk%2Bflx8vzZdxEFLzcrHes9b%2BgXPwocPu7WqTlmpT2wIYqARfiv75AY5dWEhLEdp5BVR%2FQfntAozlN%2F4vxWJ1bQbIeSV%2Fsmly40il10G97%2FnrzVuQ4l8fBHfwEPjQsqtB21eMbaQMAyoYqQ%2BKZTQXRrk40wVC2qMMAFbTCx9Jts5O8cZF9faTW5TDafiNPqfIGEVnuRazbhN3yPfDclhS7nL1ytNHA%2F%2BzI%2FEbGzAGyIOnQewMndxOluJ2tIwT1ktsyGBsV3%2BKbLFsl%2BN8iqEkLxsHR8yEghuPgsBG2n6P98Qwp4aYygY6pgGxbVCGdJY7v5OVnMugoNct1tlflXEY4%2FvmZbHoz1y2zuCmJTkY4Uj1d%2BYvkXJhLyDYyqhqjSZZKG3iI7lHoTBdCudDX2ZMJLnPTDC37R0Fo%2BCVFwBkTbyL3C%2BVuNWVuOHe%2FPUb1zJJ4gKxiZMz7%2BRrvGOvQT3pl%2BnKvbq14pQv2ARXSvQ%2FROjLp5cLmCevhmU%2BmBvV8fl3JWk3vInS0vIE01oegtXk&X-Amz-Signature=44a324c7f0936d4f33a6cd503887392dfeb3c0ce7bae5832035ce32c7f890cd1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









