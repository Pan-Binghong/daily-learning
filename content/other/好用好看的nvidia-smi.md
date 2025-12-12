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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466264GMLUG%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIB6KW9kKPmRhvsPLkpIIIhz57ksyXimkml7gG6oIoPW5AiEA9pIlRSkvVAx%2B%2FQLNnOuHEGyZd%2BTC8Lg33t%2FGZCUz1%2BQqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9TCOnELdSOrM0fAyrcA7%2FwH3MxXpDll2oBMzCXlFKkQs9%2FtPdKWQIBSyVW9D6kXyyRvK72d7g0%2FgPGdhXh2m4I5QBw%2F8kf%2FSVOKgL94xRVb23iSVPvAFZsE6HyLilk7A4qcLtCuRsjjDSDDAZhZNzy2PPhHc7LD%2BS5tT8TaJEsIBIvMnqVFLo36n2ENdfF1GZAoUGnrllWkWx0VOXTWYhm%2FeRzLuhAgFPVBOKEEen4K8deFEmrOSNGW%2FdImAPWhKhXCjQ6OMt9Xzfjoki9paanzce80mh8F401azLDrTYeK1uMKroWBACBNCCSiZauGd47u%2BDBZCyskgo29nYbtwC0IPSZvbtKNqGbJT%2FXxu24bmqCd%2F99DAgF68%2Bz%2BnhA0PtwLe%2BibkoiRADDOBIcpQXs0FY5eueDXaoG2nEKgtDHzEg5x1q5d3UHefuVkQiglYEYqG77Vd9GAOGbiIVrvbKdv82uvzwYwzLU0Kf9h0byCeLJZJxLk0LEL2RUC3R32aUloYQksRMjwrFanjkX4YKJNtlQFppnfWrgMdJQ4qR6FJ13jlrYxcWJ6lrVeq54aHOb0wFVPFm4YxLQuGo1Et8Ec2K8MMO7A61P3hgTWbne2C99O%2FTXBrg1YhsVaUcAlvBkJ%2FY17l60bfvqMPrU7ckGOqUBPuCoqNwKhjouz%2FyLUI7jNwPhOf2o61mcMbjlq3Oa8guT9OXTUJnZjCTMJgSHJMJHYFi7Qvd9H%2B75GqoaEOWnlduzmtwB4CIZKbkHmAtGyivUe3PWrNbva4NORWTddOTrqVIsXLJ0phI4GpgAIP6nrxD7LwZ17h51Buwx9pf3UNrdqrLT7fE1b8DUF%2F8EmfTcsuRBojrKR%2BmmlzR%2F785DGKAf9MJH&X-Amz-Signature=77f90c7da27b1d82f8954c0304d998f8b5feb03e9ec9099edb50429ddaa402b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466264GMLUG%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T025519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIB6KW9kKPmRhvsPLkpIIIhz57ksyXimkml7gG6oIoPW5AiEA9pIlRSkvVAx%2B%2FQLNnOuHEGyZd%2BTC8Lg33t%2FGZCUz1%2BQqiAQI%2Bv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH9TCOnELdSOrM0fAyrcA7%2FwH3MxXpDll2oBMzCXlFKkQs9%2FtPdKWQIBSyVW9D6kXyyRvK72d7g0%2FgPGdhXh2m4I5QBw%2F8kf%2FSVOKgL94xRVb23iSVPvAFZsE6HyLilk7A4qcLtCuRsjjDSDDAZhZNzy2PPhHc7LD%2BS5tT8TaJEsIBIvMnqVFLo36n2ENdfF1GZAoUGnrllWkWx0VOXTWYhm%2FeRzLuhAgFPVBOKEEen4K8deFEmrOSNGW%2FdImAPWhKhXCjQ6OMt9Xzfjoki9paanzce80mh8F401azLDrTYeK1uMKroWBACBNCCSiZauGd47u%2BDBZCyskgo29nYbtwC0IPSZvbtKNqGbJT%2FXxu24bmqCd%2F99DAgF68%2Bz%2BnhA0PtwLe%2BibkoiRADDOBIcpQXs0FY5eueDXaoG2nEKgtDHzEg5x1q5d3UHefuVkQiglYEYqG77Vd9GAOGbiIVrvbKdv82uvzwYwzLU0Kf9h0byCeLJZJxLk0LEL2RUC3R32aUloYQksRMjwrFanjkX4YKJNtlQFppnfWrgMdJQ4qR6FJ13jlrYxcWJ6lrVeq54aHOb0wFVPFm4YxLQuGo1Et8Ec2K8MMO7A61P3hgTWbne2C99O%2FTXBrg1YhsVaUcAlvBkJ%2FY17l60bfvqMPrU7ckGOqUBPuCoqNwKhjouz%2FyLUI7jNwPhOf2o61mcMbjlq3Oa8guT9OXTUJnZjCTMJgSHJMJHYFi7Qvd9H%2B75GqoaEOWnlduzmtwB4CIZKbkHmAtGyivUe3PWrNbva4NORWTddOTrqVIsXLJ0phI4GpgAIP6nrxD7LwZ17h51Buwx9pf3UNrdqrLT7fE1b8DUF%2F8EmfTcsuRBojrKR%2BmmlzR%2F785DGKAf9MJH&X-Amz-Signature=b2e710af32efaa7b5b808bdaa34f256679aed91a4c1fa39bd1516dd6f376aa08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









