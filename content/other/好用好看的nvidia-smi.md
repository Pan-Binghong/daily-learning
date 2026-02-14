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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNNJ7N6%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIBjbji3ccvA%2Bkh2Ka8nn42G0tRir3jW8d5fF5J0FnOT4AiEAjUF5quQJbWOe1QTExPsQhMMGx9rMhQZ68EQD6BpXsdsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2FcaM0FaOnd%2BT2UWircAzTXeOQjvYJWbyyVzpP5YbWuqcRZ74AGx145qVDtPohSUmmS4KwAbzLk1nL2OGxxvSEZuTyrp2%2FTbdmO1%2FLpP5eNUauJgIRBoVhbvn0s5m%2F%2FFyxI4SMf10p2j6ROfgKYm7PjZXWWYujnCbB%2FF%2FQr%2FmXTC6MTld70Mj2O%2BKEaDKamqFWkvTVoheM9GAnR%2BSacYVCJ%2BPT19mcCgSV7K%2Fi2nEflvDbk%2FqpucP8RLQhKmnrPSZS%2BG99Ftgqm6E6%2B%2FVDs5F67PY43Nx5BdSh1exJBJoX5Pre3M1pDvlGb3coE0S9xd7wsNxRAQ6zvkyoGwHDzjBo3sWHzscVblL8a%2FQzgKS7%2FUGy3%2FqJUhJ32S2L1oKnGjjOounZboxgREoFpwQXGvVCX3A%2BBfy1LJezPmJ%2FJ%2Bo1AQ2o8DdBmAoCkv7J2klF9ocU0tWd1sFDnJHt8VAONDow1ZZ2xGIirGvjDFx4rZB3sn%2FbCt1DjFVOes0aj7ZghOvB5hCK6rzLETlPup1f1X6W%2FP7Q%2B90wgkKg4t32b4Ci33zvEMUXPJbTCYu4M%2FxUbU%2FEDglPqkua6DqKJW98%2Bo8cQoYLT5cBhkCrQnWJ9LHNIKeLiVTPO16EuygjV%2BqT5AWbMG7vMxY18hLiVMLjAv8wGOqUBsb76HI4ruiW%2BNtbWXcsn%2FYoCuuksnwOVDZletcQfC2%2BAULkle1SXbbFw27%2FG%2FGFPltQIHTZyqxnpZjdnXJMSFIObRllEJJECxAyyc0otry1rSea7j5yL7FQYlzlxpUlsXRb6AdhBxIOExPZxWhFw0BBLNx2sQxG9dQK0RCXDpcVlbjEUBaUPfv8lReQ6rFRh6F0nWxaDTm64lxbzcxvXpif0q5VW&X-Amz-Signature=1359e1daf08899144f78b1352a22493aba52ea1248f162c4c9d01bec8bd8aee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WNNJ7N6%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIBjbji3ccvA%2Bkh2Ka8nn42G0tRir3jW8d5fF5J0FnOT4AiEAjUF5quQJbWOe1QTExPsQhMMGx9rMhQZ68EQD6BpXsdsqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK%2FcaM0FaOnd%2BT2UWircAzTXeOQjvYJWbyyVzpP5YbWuqcRZ74AGx145qVDtPohSUmmS4KwAbzLk1nL2OGxxvSEZuTyrp2%2FTbdmO1%2FLpP5eNUauJgIRBoVhbvn0s5m%2F%2FFyxI4SMf10p2j6ROfgKYm7PjZXWWYujnCbB%2FF%2FQr%2FmXTC6MTld70Mj2O%2BKEaDKamqFWkvTVoheM9GAnR%2BSacYVCJ%2BPT19mcCgSV7K%2Fi2nEflvDbk%2FqpucP8RLQhKmnrPSZS%2BG99Ftgqm6E6%2B%2FVDs5F67PY43Nx5BdSh1exJBJoX5Pre3M1pDvlGb3coE0S9xd7wsNxRAQ6zvkyoGwHDzjBo3sWHzscVblL8a%2FQzgKS7%2FUGy3%2FqJUhJ32S2L1oKnGjjOounZboxgREoFpwQXGvVCX3A%2BBfy1LJezPmJ%2FJ%2Bo1AQ2o8DdBmAoCkv7J2klF9ocU0tWd1sFDnJHt8VAONDow1ZZ2xGIirGvjDFx4rZB3sn%2FbCt1DjFVOes0aj7ZghOvB5hCK6rzLETlPup1f1X6W%2FP7Q%2B90wgkKg4t32b4Ci33zvEMUXPJbTCYu4M%2FxUbU%2FEDglPqkua6DqKJW98%2Bo8cQoYLT5cBhkCrQnWJ9LHNIKeLiVTPO16EuygjV%2BqT5AWbMG7vMxY18hLiVMLjAv8wGOqUBsb76HI4ruiW%2BNtbWXcsn%2FYoCuuksnwOVDZletcQfC2%2BAULkle1SXbbFw27%2FG%2FGFPltQIHTZyqxnpZjdnXJMSFIObRllEJJECxAyyc0otry1rSea7j5yL7FQYlzlxpUlsXRb6AdhBxIOExPZxWhFw0BBLNx2sQxG9dQK0RCXDpcVlbjEUBaUPfv8lReQ6rFRh6F0nWxaDTm64lxbzcxvXpif0q5VW&X-Amz-Signature=2a13e8a00d073b699c459e709c914520d896443bb5161481e0baa334c81b37b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









