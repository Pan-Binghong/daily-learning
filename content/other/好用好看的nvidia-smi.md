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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMPP2XVL%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdJBT14O2UbvcZ8spO286P%2BFAaWN3lDXwV3kwsoPHkgAIgNU11rdpwPoAoblFge2WWTgSNeqXXTGhdUc4BOj2iRcIqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMOeJq3EXuOMwiOLCrcA2lVNNkMPUz6lWrUhTek%2BOnMg%2Bj9EmLx8YHbeIGwNP4NhER3pCNMAroXPHdy2Zc87ctZAJlhaaP5HvDLTjRex670cwWHcWvELsnRfSslgt%2F2IruwinGrYirnoul2JUZolW1RYWsvuhmBBl0NX8MKGtPSmhc8dGE4JKFqn%2BAg86wfeEvPHUekB9jBh4LbZ9XRBwiKEqkpFwhGRcRqxEyQdfL7whpswry4QvI4ThI6cUER9Xjl6s1kl7PXzbMdd1LJhb7uX1HJ26%2FdQq0Ndv%2BEGYDnQAXYwB2EsmspLol45eFRTBxLK5Z3vcJAg7tIU0ZoSBTpUrjMO8jGh0JS2QwhrMrKZvzjUyMwuc6Vi0fosk6TRm4NXBcYBitg2QaIuPmIGr1L4S4FEbPCrrNaSi5JPJtEuPHW7oG9En%2BeiQRtNX%2FxVNkT9YVrJHAqeRoIunxZSQzDm1%2F%2F6rmVzdUSmwpE1iUoq6ruic1N%2BuaEbJulFuHCfVVl1vof%2FLKlkAcns24yaGEQa8u3Zu3IRdmFnATXUnNQH2mTWVVNbsPvXozdBgcJ32lxzgNjqYCoE0%2BMsN3W1gi%2Bzwno2PAVa6t3p7kYdEc04dOWxDBLH%2FW0wIwE5PW%2Bovsegp9n8FA5OmvXMOKV%2FM4GOqUBjgR%2BSAvKmCNEd61ioPzy0vwZJvZgD3l75%2FxVGUh4SSeYMYX%2BR0tkOhKsV0hjdEq5CONOO4ctWg2ZXLPz89f1yS7%2B2xC3xrXxjHs%2BeehgBxbSokjFzGLb67kNTwiVOslPbVNaUWvNAEswCgnK2novz8VmccGIHpy3XlZGYNpjn3UjRw8tDap3NW%2Bl%2BIycjrBWqoZob6n%2B%2FXmr2BMmPoTRns4uQ0yM&X-Amz-Signature=e3745653ffd22f33cc68face6647360868aea52862860542407e0834bf56c10d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMPP2XVL%2F20260415%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260415T041113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdJBT14O2UbvcZ8spO286P%2BFAaWN3lDXwV3kwsoPHkgAIgNU11rdpwPoAoblFge2WWTgSNeqXXTGhdUc4BOj2iRcIqiAQInf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCMOeJq3EXuOMwiOLCrcA2lVNNkMPUz6lWrUhTek%2BOnMg%2Bj9EmLx8YHbeIGwNP4NhER3pCNMAroXPHdy2Zc87ctZAJlhaaP5HvDLTjRex670cwWHcWvELsnRfSslgt%2F2IruwinGrYirnoul2JUZolW1RYWsvuhmBBl0NX8MKGtPSmhc8dGE4JKFqn%2BAg86wfeEvPHUekB9jBh4LbZ9XRBwiKEqkpFwhGRcRqxEyQdfL7whpswry4QvI4ThI6cUER9Xjl6s1kl7PXzbMdd1LJhb7uX1HJ26%2FdQq0Ndv%2BEGYDnQAXYwB2EsmspLol45eFRTBxLK5Z3vcJAg7tIU0ZoSBTpUrjMO8jGh0JS2QwhrMrKZvzjUyMwuc6Vi0fosk6TRm4NXBcYBitg2QaIuPmIGr1L4S4FEbPCrrNaSi5JPJtEuPHW7oG9En%2BeiQRtNX%2FxVNkT9YVrJHAqeRoIunxZSQzDm1%2F%2F6rmVzdUSmwpE1iUoq6ruic1N%2BuaEbJulFuHCfVVl1vof%2FLKlkAcns24yaGEQa8u3Zu3IRdmFnATXUnNQH2mTWVVNbsPvXozdBgcJ32lxzgNjqYCoE0%2BMsN3W1gi%2Bzwno2PAVa6t3p7kYdEc04dOWxDBLH%2FW0wIwE5PW%2Bovsegp9n8FA5OmvXMOKV%2FM4GOqUBjgR%2BSAvKmCNEd61ioPzy0vwZJvZgD3l75%2FxVGUh4SSeYMYX%2BR0tkOhKsV0hjdEq5CONOO4ctWg2ZXLPz89f1yS7%2B2xC3xrXxjHs%2BeehgBxbSokjFzGLb67kNTwiVOslPbVNaUWvNAEswCgnK2novz8VmccGIHpy3XlZGYNpjn3UjRw8tDap3NW%2Bl%2BIycjrBWqoZob6n%2B%2FXmr2BMmPoTRns4uQ0yM&X-Amz-Signature=13a930aef55cf89a422e6ce62880d9a77b07a1e5a03acb5ee060dbaa815efba3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









