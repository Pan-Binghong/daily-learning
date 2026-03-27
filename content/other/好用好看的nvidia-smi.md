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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2BABD63%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIB%2FVdRq%2BpGTvkfIr%2Ff0ZS06Dj8ZtpzRRLfKju%2Bbd8EdLAiEAuuMfhkqKx3%2FfAPlHy6Kk8UtB%2FLV35FrxVhRNUHTf7uYqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BMKxNCPTk6xjeeISrcAyH5RjHEU08CVrq3oL8yHFiYOPCw0TCgF2vWqRvba7wmH5pntse07e7XjFDkn58W6K7cvqdKJDK7MtKuwe9o%2BVnr8Auuy44VvHfOeYPjCOgvTOROFVasW8nagHUxcXrMWvOhHxuddJpudA6pq0SbnV3eZ4kOmkRbzBLjyn3eRJSZdGqlwLNvWEvKRJTIw9J%2BuLmM3RCgxODJ%2F0FwZjvw5T1xkAhNYj8Rgrxz1slsPWUeR3LkPPIEE%2B5wjsyjNqpkdku46mEKtsvz4FR4gD7cGSqXoe%2FempI%2BQdcue1p3eT0se6B0NBGhyEKRJ1PukLns1lqCCKubTWeBy%2BNv3YnGogGmhwlSv6fpBd7Ks8v1UMhiIfHOaip7%2FXgNp2l0apfI%2FfiliJfNvyK%2BWmnW8r9jOD%2BatvrD%2FZb1L2bshJIqdvcoA8K5HDGmOzOePo2R0B9HsGJWKDL2qXp6yStG8%2Fa2FF76rkDdpTpL8yOWh0CZfJGbtWiLTxcGvJG7vVU8IsgyGksSgFReM9A42B%2BCaGMnR2l1DfsrRdO%2BjK3UbnaEvJs6S1wgrPvsxcu4gd%2FskUy2j71b%2BSVg3%2BjXtA%2FZ1sXY0iVL7j%2BRv5a5lI6BgET9YE%2BKzZ%2FB0ptdyJg5aIbbMNLnls4GOqUBDwJjh%2FyvFLOlfhIttmmio9VByz5CoFT8LIE1Hgp%2BU04MqA2VjIXZTJOk6AeybTDEnIzohbHGHJz75s67wUCuDn0oWFlpfCzI3eIjmypPOtze%2BhR2N4BVWlMdMmO1%2FpcKJV%2BS9VBhH1VHaIFnWDE8PQ2yMs3B%2B0XJ3xX4GhnQmSICDbcGYQ8oRmKm7E7UgboLu9Ow7ogeBLbs%2B9eKK8Tt4qxO9h9U&X-Amz-Signature=5d056273cc711db83b41ec6824fa3f5a26f2b2db542c354709c8291bcbbcba21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2BABD63%2F20260327%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260327T035335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIB%2FVdRq%2BpGTvkfIr%2Ff0ZS06Dj8ZtpzRRLfKju%2Bbd8EdLAiEAuuMfhkqKx3%2FfAPlHy6Kk8UtB%2FLV35FrxVhRNUHTf7uYqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG%2BMKxNCPTk6xjeeISrcAyH5RjHEU08CVrq3oL8yHFiYOPCw0TCgF2vWqRvba7wmH5pntse07e7XjFDkn58W6K7cvqdKJDK7MtKuwe9o%2BVnr8Auuy44VvHfOeYPjCOgvTOROFVasW8nagHUxcXrMWvOhHxuddJpudA6pq0SbnV3eZ4kOmkRbzBLjyn3eRJSZdGqlwLNvWEvKRJTIw9J%2BuLmM3RCgxODJ%2F0FwZjvw5T1xkAhNYj8Rgrxz1slsPWUeR3LkPPIEE%2B5wjsyjNqpkdku46mEKtsvz4FR4gD7cGSqXoe%2FempI%2BQdcue1p3eT0se6B0NBGhyEKRJ1PukLns1lqCCKubTWeBy%2BNv3YnGogGmhwlSv6fpBd7Ks8v1UMhiIfHOaip7%2FXgNp2l0apfI%2FfiliJfNvyK%2BWmnW8r9jOD%2BatvrD%2FZb1L2bshJIqdvcoA8K5HDGmOzOePo2R0B9HsGJWKDL2qXp6yStG8%2Fa2FF76rkDdpTpL8yOWh0CZfJGbtWiLTxcGvJG7vVU8IsgyGksSgFReM9A42B%2BCaGMnR2l1DfsrRdO%2BjK3UbnaEvJs6S1wgrPvsxcu4gd%2FskUy2j71b%2BSVg3%2BjXtA%2FZ1sXY0iVL7j%2BRv5a5lI6BgET9YE%2BKzZ%2FB0ptdyJg5aIbbMNLnls4GOqUBDwJjh%2FyvFLOlfhIttmmio9VByz5CoFT8LIE1Hgp%2BU04MqA2VjIXZTJOk6AeybTDEnIzohbHGHJz75s67wUCuDn0oWFlpfCzI3eIjmypPOtze%2BhR2N4BVWlMdMmO1%2FpcKJV%2BS9VBhH1VHaIFnWDE8PQ2yMs3B%2B0XJ3xX4GhnQmSICDbcGYQ8oRmKm7E7UgboLu9Ow7ogeBLbs%2B9eKK8Tt4qxO9h9U&X-Amz-Signature=400ad52eac67af091c7a3b3dafa8f806bce4466482d5c94dbfae23b936f607cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









