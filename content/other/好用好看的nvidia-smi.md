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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWPM4C5A%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDab3FppJSUw4xN209%2B%2FYZb0IEplemck8h2%2FjPoT1iaqgIgIGlswSP5lvuGdLJ6oRMbW6noTGUerMA6EdqB%2FVunmlcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDe7Kbs13fC5mAedEyrcAz66zRDPQ5xlVWCBCjEg6%2B0QDLIAbFuEkylHJCzjSn5Sg0ckzjNSujJYMF4VukaFL70MsqiiwK9GaZ1FTpjruh6T4k7ZCyqnZ6h%2FUFy4kYV923DcB5QBQMONtV4rbvA%2FiWStLuLFxAcYtvzo9gdsDgWMFcL0tWsULQA7kkTitpnoQCUSqKZICKUo%2BmOknYivvBFB5AEqrEBdC%2F9cmztx9sKm7F30OXEtEit7Q%2BCJVqej0D%2F22J8NSCZYxVU2%2FgOFSLtMwRWkpATFFCR6ELiaSSxu0Z%2BgXDZ7c6dBgWngOrw2yYHSLn3NKH48aMVbVOr0vC1omx%2FswXSahY3RidKG1wHwxh0zyQNAq2txiPKrTZCEdvp%2B53zisT1xyRgEC53kAFnlJ%2B8QiudtvtYwrEzuKaa6%2FiTHawbCi74MHZ%2BIL%2Fj%2B%2FqIoAtv0frrMxAhPj9oKchEW0BiRDflWnqSNqU3Tn%2Fz2e%2BH%2Bwen4bX7gYSNeG5JopR681VDt%2BvzvfojKE0jkQt2vNJXe00GgwXZ6H3sfMyK8d4GoNgypMFFHnXSygAb68lrNSVhmH9eul5aFLPrGq0pmXDLKE0CkXuIZuigvYT8YvPhnjzOdK99QflJyH0ho4eIx6xBdlK%2BS5VJmMPK%2F48kGOqUBstUOWXUuYJl%2B8PIR8AB%2BxreNfvPdW8hpGMn51VmymgR%2FtrP234Gq1strvsGMzT9D2nGCbQKCOEYilbORevo%2FtK6jfmelMV02xn0mu0qv8qGl2dr%2BTUl43G%2FZcZjPgaTufxvR0qOj2ZCu993AfvjlQ18cNFLmb8%2BGwZgs7GMVAZaCW10Vis87GWiMOrki8noVHOnBlHh0b7L6eoQnML7NymO9fDfD&X-Amz-Signature=a14b92cf91a2a51f7162eaf6e56a95b51678ca839bd676b8c4aecaebbb6af71e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWPM4C5A%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025435Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQDab3FppJSUw4xN209%2B%2FYZb0IEplemck8h2%2FjPoT1iaqgIgIGlswSP5lvuGdLJ6oRMbW6noTGUerMA6EdqB%2FVunmlcqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDe7Kbs13fC5mAedEyrcAz66zRDPQ5xlVWCBCjEg6%2B0QDLIAbFuEkylHJCzjSn5Sg0ckzjNSujJYMF4VukaFL70MsqiiwK9GaZ1FTpjruh6T4k7ZCyqnZ6h%2FUFy4kYV923DcB5QBQMONtV4rbvA%2FiWStLuLFxAcYtvzo9gdsDgWMFcL0tWsULQA7kkTitpnoQCUSqKZICKUo%2BmOknYivvBFB5AEqrEBdC%2F9cmztx9sKm7F30OXEtEit7Q%2BCJVqej0D%2F22J8NSCZYxVU2%2FgOFSLtMwRWkpATFFCR6ELiaSSxu0Z%2BgXDZ7c6dBgWngOrw2yYHSLn3NKH48aMVbVOr0vC1omx%2FswXSahY3RidKG1wHwxh0zyQNAq2txiPKrTZCEdvp%2B53zisT1xyRgEC53kAFnlJ%2B8QiudtvtYwrEzuKaa6%2FiTHawbCi74MHZ%2BIL%2Fj%2B%2FqIoAtv0frrMxAhPj9oKchEW0BiRDflWnqSNqU3Tn%2Fz2e%2BH%2Bwen4bX7gYSNeG5JopR681VDt%2BvzvfojKE0jkQt2vNJXe00GgwXZ6H3sfMyK8d4GoNgypMFFHnXSygAb68lrNSVhmH9eul5aFLPrGq0pmXDLKE0CkXuIZuigvYT8YvPhnjzOdK99QflJyH0ho4eIx6xBdlK%2BS5VJmMPK%2F48kGOqUBstUOWXUuYJl%2B8PIR8AB%2BxreNfvPdW8hpGMn51VmymgR%2FtrP234Gq1strvsGMzT9D2nGCbQKCOEYilbORevo%2FtK6jfmelMV02xn0mu0qv8qGl2dr%2BTUl43G%2FZcZjPgaTufxvR0qOj2ZCu993AfvjlQ18cNFLmb8%2BGwZgs7GMVAZaCW10Vis87GWiMOrki8noVHOnBlHh0b7L6eoQnML7NymO9fDfD&X-Amz-Signature=162bec9cac6bc2104c717b0e2cccccc9a07c84c812fe7b642b3602abc3eac82a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









