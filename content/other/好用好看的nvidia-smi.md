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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3T7SHMR%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhQriU4rTYf8NsRd2t0pgr6%2FvkhIzpihel221wIhFi3AiBu75HsfPKSiAubp15eRb%2BV%2FNp0%2FuSuMWmGJrc%2Bel3%2FmSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM183efXszVhU0DUQmKtwDq0w3Qf2JKxbSd1j66tS0bbufABJPSaG0T7Kli4NEmZs5SMUxetZzYLVOF6ycr5ut0QlwH1guOArUmxAEySF2p1c6z7A%2BGlsvX2y28llyJzyvfBvgrkf6G8BJDjsm5J16OW5yZBByczeQCVYLNTLF%2B3NQbG2PgIv0UVBJfk5Wb3uKYgL1rHG%2Fteh6E0z6iZOI%2FLGSwYDnGoIy4%2FFFkNhycLDIleAgFnWLVHfHlGP2mVA6FhGsdmU8fwELZApnks47vuIw34oVZaJnefFlMWH84WZaYGP%2FXItwhoadt8E1SqGdkUQeG2S4ww0%2BQcCrMFkS9CkCF49gXabBURd3CawNl8nuZHDH07CRvhMNmqrhcvFJNNquChUGSipp1GoRaZ6lxzpq0gto9ohTFiyrec7ZpX9rVgIfWSAMfINw7dxHo47lwsCE09cSLEVKcPI99%2BT7%2Bb%2FmL7NpoMSLCm2WpGXKNz98cyxOv6hkPBRKrs5aDEbBdpmYpf3L7G1mBxWBMnBTFvludwGsgsHP%2BCrqLb0RK9IfW9efwvXjYfF1V59F8o8rQgozKxB%2Fkwt4xBIppUm8nPI7m6lrYiUbZV8mHrbdq%2BYTVDpiNtpYYU20HTFfv2xryWrmXXtt%2BqQtCaEw89%2BjzQY6pgH8WEbSVuMxsDAeUwAQqyl18tPDCKd8%2Fl4y3c0f8Z9jGZ0%2BRWa2RzwhlK0jFNmyMmSrzr3LrsUIUOAJcMZdrey%2Fpr2%2BJZswgTjNwsoLXNICQxN11TYAJerVUvzDCcqO%2F%2Bmsk3b9pdy1VGPyqrjRBY6BNQVS1ErsLiOXFTQVGsOiTniI4K0KpymKLm0RSt44tO5kMaugF87PsZF34aVozd4qeLCw%2Fx%2Bc&X-Amz-Signature=9b504d73232de10c4c3d0da5ac60aca21cc129c478e78d77d8b7a38522811231&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3T7SHMR%2F20260305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260305T033259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHhQriU4rTYf8NsRd2t0pgr6%2FvkhIzpihel221wIhFi3AiBu75HsfPKSiAubp15eRb%2BV%2FNp0%2FuSuMWmGJrc%2Bel3%2FmSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM183efXszVhU0DUQmKtwDq0w3Qf2JKxbSd1j66tS0bbufABJPSaG0T7Kli4NEmZs5SMUxetZzYLVOF6ycr5ut0QlwH1guOArUmxAEySF2p1c6z7A%2BGlsvX2y28llyJzyvfBvgrkf6G8BJDjsm5J16OW5yZBByczeQCVYLNTLF%2B3NQbG2PgIv0UVBJfk5Wb3uKYgL1rHG%2Fteh6E0z6iZOI%2FLGSwYDnGoIy4%2FFFkNhycLDIleAgFnWLVHfHlGP2mVA6FhGsdmU8fwELZApnks47vuIw34oVZaJnefFlMWH84WZaYGP%2FXItwhoadt8E1SqGdkUQeG2S4ww0%2BQcCrMFkS9CkCF49gXabBURd3CawNl8nuZHDH07CRvhMNmqrhcvFJNNquChUGSipp1GoRaZ6lxzpq0gto9ohTFiyrec7ZpX9rVgIfWSAMfINw7dxHo47lwsCE09cSLEVKcPI99%2BT7%2Bb%2FmL7NpoMSLCm2WpGXKNz98cyxOv6hkPBRKrs5aDEbBdpmYpf3L7G1mBxWBMnBTFvludwGsgsHP%2BCrqLb0RK9IfW9efwvXjYfF1V59F8o8rQgozKxB%2Fkwt4xBIppUm8nPI7m6lrYiUbZV8mHrbdq%2BYTVDpiNtpYYU20HTFfv2xryWrmXXtt%2BqQtCaEw89%2BjzQY6pgH8WEbSVuMxsDAeUwAQqyl18tPDCKd8%2Fl4y3c0f8Z9jGZ0%2BRWa2RzwhlK0jFNmyMmSrzr3LrsUIUOAJcMZdrey%2Fpr2%2BJZswgTjNwsoLXNICQxN11TYAJerVUvzDCcqO%2F%2Bmsk3b9pdy1VGPyqrjRBY6BNQVS1ErsLiOXFTQVGsOiTniI4K0KpymKLm0RSt44tO5kMaugF87PsZF34aVozd4qeLCw%2Fx%2Bc&X-Amz-Signature=28b17d9f08d9ad102b74546421e73a6c73f59d8c7abe2a3532e3362c65e044c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









