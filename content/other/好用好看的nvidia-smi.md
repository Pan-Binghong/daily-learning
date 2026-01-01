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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOICBVHC%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDPdElwJ6k4zE63V6cRaEyc0LsPlsedewXXiU%2BGMVovcwIhAP4eQpMpbHa48F3W18bEmMH9xjl4qe7YtG0yX4jyCDguKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym3sXdiMhGRpoUilEq3AP2%2Bc27brA3IynBwHfhdpZEGRbauuL%2Fc4UDmWFFU5LmUpe9wjLHruOPMY%2BqN%2FXE24z%2B8Sz%2FFfPlw6dmZ2ukcxBfot2tZ71K0YhZ6pbtzqD%2FGQN%2BJayCuaQlRL5A98WcuHEGFCeTSGSL7ie4e6zGCzVBNnXSEjBlR5Ddc2s%2B0Yx9rFplucJhQVAvpa2gcZulIYlTpjyZGfO%2FSmYOB4m1ERO8NvmhuuD3aaYKueHA5i8mPonQTVCCJgKH0g9FYGUzijscP0lpVzGA2Yf6g%2Bc%2Fo1zuUvm10gA5Zm7Qt%2B4TUnpiPI8ERz%2BYyuLxJ4%2FKu3l1JuKpa2x0dF0ObYORkmuHcTXA7z180H6CgUnbA6lyER1OHNSqX0EgoMhVJ%2FYX6LnWnJ7yM0FCp2oCk2%2B0LgWxThfOTRqGozusj6hwFvQ9QjH9OLl73V%2BqFmNKsd%2Bf9MHPmWyJXyu%2BHuICRV2bz2cap8KtCcDxCJs9qL02g%2BgUUvxiY4PY1UxjYFpBo2cfMgnTKAazXHTSMkdbgKRBs%2F9Dot6NvFQMKV420VG7Hg9Yi3sCL1RVRWjc8bUKaIpeIDzB9dgr2I2kEN%2F5UGvn9t1dLNKg%2BTo1uznN2aUReTh1f%2Fr9b4%2FfYxgAccHpWbgRszC2otfKBjqkAfYfQDhByNsCagzeMd7qNPt79pYWCzUBGFbYxP0VpRaQeWT%2Fyd3xofSgpte7iahVwkLC8Y0VY8rsycxhqx36ZZ%2BklL1%2Bvr9uNj35lnDilxNpwDc5OHB8LnUsyUIARUNQljwwPrOZUb9UKq4M2XS1TW2hc1oG3PuCqm5s%2F%2FqOkGDQ1ztTwNsLqDrpklrMAUyixerxftUsmb6ELyeLRhu5kLIIslrt&X-Amz-Signature=9a670494f47c7f4df8f33a2b6c2fbfa8cffd74d977a26ad868ada4f843574872&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOICBVHC%2F20260101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260101T031124Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJIMEYCIQDPdElwJ6k4zE63V6cRaEyc0LsPlsedewXXiU%2BGMVovcwIhAP4eQpMpbHa48F3W18bEmMH9xjl4qe7YtG0yX4jyCDguKogECNv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igym3sXdiMhGRpoUilEq3AP2%2Bc27brA3IynBwHfhdpZEGRbauuL%2Fc4UDmWFFU5LmUpe9wjLHruOPMY%2BqN%2FXE24z%2B8Sz%2FFfPlw6dmZ2ukcxBfot2tZ71K0YhZ6pbtzqD%2FGQN%2BJayCuaQlRL5A98WcuHEGFCeTSGSL7ie4e6zGCzVBNnXSEjBlR5Ddc2s%2B0Yx9rFplucJhQVAvpa2gcZulIYlTpjyZGfO%2FSmYOB4m1ERO8NvmhuuD3aaYKueHA5i8mPonQTVCCJgKH0g9FYGUzijscP0lpVzGA2Yf6g%2Bc%2Fo1zuUvm10gA5Zm7Qt%2B4TUnpiPI8ERz%2BYyuLxJ4%2FKu3l1JuKpa2x0dF0ObYORkmuHcTXA7z180H6CgUnbA6lyER1OHNSqX0EgoMhVJ%2FYX6LnWnJ7yM0FCp2oCk2%2B0LgWxThfOTRqGozusj6hwFvQ9QjH9OLl73V%2BqFmNKsd%2Bf9MHPmWyJXyu%2BHuICRV2bz2cap8KtCcDxCJs9qL02g%2BgUUvxiY4PY1UxjYFpBo2cfMgnTKAazXHTSMkdbgKRBs%2F9Dot6NvFQMKV420VG7Hg9Yi3sCL1RVRWjc8bUKaIpeIDzB9dgr2I2kEN%2F5UGvn9t1dLNKg%2BTo1uznN2aUReTh1f%2Fr9b4%2FfYxgAccHpWbgRszC2otfKBjqkAfYfQDhByNsCagzeMd7qNPt79pYWCzUBGFbYxP0VpRaQeWT%2Fyd3xofSgpte7iahVwkLC8Y0VY8rsycxhqx36ZZ%2BklL1%2Bvr9uNj35lnDilxNpwDc5OHB8LnUsyUIARUNQljwwPrOZUb9UKq4M2XS1TW2hc1oG3PuCqm5s%2F%2FqOkGDQ1ztTwNsLqDrpklrMAUyixerxftUsmb6ELyeLRhu5kLIIslrt&X-Amz-Signature=bf946c9c3a5257ae25bcc15c041ebeb5f272d64ce8f21fe444d119016269bfd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









