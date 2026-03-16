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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SODVY5H3%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCbqFSQt1HbK7Bsqiofe4IgIrKJIljXzPVt9pT%2FnVXyLAIhAM%2FYiYFySpdwsxcJ%2Fj5DHtTR5%2FULqxmdtziqfsLswb7KKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzvYY9r%2FEZr%2BvY7Rhoq3AMEv44Bg24bOYV45%2Bq8KKwFaFnOo7Bn04UE%2Fs2Av5vtmeCDIgh634hVEFMWt5jZIhI%2BcQOy5QgSzmwYdb90zvMsQ07xymNGl60oP30ni6N0TRnZ0et4bNo0LsyvumlAcKVYR%2BWx93MGwtN%2BRLJVEqlvq7y77j9O3ISz3YESFVJum2K4IICf0c4ygis3v15OCBLowKQ2tvJ4JmbKa19zoajs1hzp0lDoiYttrlFKziFjfecIf0JGG0IZidxQaDLYcbgHp581xwHxOROPClshxbykkML8atWedgeD1Ont2AAJX%2B9hESSRrfnfnxvU6a%2BQ5xhgHDjh4lXI1r0X4hOMF4wemXnVFSjm5srRwmpKbxnoxpEoD6C%2BB90%2BDB%2FpFuRQNymlXXTZOcjAMUB6yWT5wLqN7EumRanOeXhId65ad6N03M%2BThH1LOBEPDEGJJ2LqGxt4V0o8KlUfnKWf1zzA1iw6EDIY56AXVXB%2FnzTGSAA2i4Ts1gQVDYwztf%2FngrHaZZmOMSYZt6rkW19PfaH1HZ%2BDJL%2F3Zm%2F27MzHfhsdLpxtu9xrZ2w8zTte%2B%2BduKPPNNBvNNoVcIQgUYTxm%2Fix%2BFwWNp7nEJPr38WQsvvDxQEVOVj9Mya6fmXM0DMaVgDDLvt3NBjqkAXn83oes0cFgEDLKJz7tlSqIZMY6%2Bf6MphkTZ2tG3Aj35qhsg2UM2n99FLG5NnOy4PC0Ab0jdPb%2F%2BMnDnrvMoL2F6oRH3JRp%2FIB3J0Pafs4%2F2T%2FhFW5S4wYMPzrvUUhwumuksYdJxsZsMlFg2A5KQCof8P1Rah4FFNJoeXvi19bIXsMjSwWcOs6GZuYte%2FFn9J3p%2BNrxKL6WiSoFvM%2B3nMH4pc2c&X-Amz-Signature=087022794f8d1f4d1bf285d4cabdac4cc86dded7ed6f4f92e34178310fb59646&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SODVY5H3%2F20260316%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260316T035828Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCbqFSQt1HbK7Bsqiofe4IgIrKJIljXzPVt9pT%2FnVXyLAIhAM%2FYiYFySpdwsxcJ%2Fj5DHtTR5%2FULqxmdtziqfsLswb7KKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzvYY9r%2FEZr%2BvY7Rhoq3AMEv44Bg24bOYV45%2Bq8KKwFaFnOo7Bn04UE%2Fs2Av5vtmeCDIgh634hVEFMWt5jZIhI%2BcQOy5QgSzmwYdb90zvMsQ07xymNGl60oP30ni6N0TRnZ0et4bNo0LsyvumlAcKVYR%2BWx93MGwtN%2BRLJVEqlvq7y77j9O3ISz3YESFVJum2K4IICf0c4ygis3v15OCBLowKQ2tvJ4JmbKa19zoajs1hzp0lDoiYttrlFKziFjfecIf0JGG0IZidxQaDLYcbgHp581xwHxOROPClshxbykkML8atWedgeD1Ont2AAJX%2B9hESSRrfnfnxvU6a%2BQ5xhgHDjh4lXI1r0X4hOMF4wemXnVFSjm5srRwmpKbxnoxpEoD6C%2BB90%2BDB%2FpFuRQNymlXXTZOcjAMUB6yWT5wLqN7EumRanOeXhId65ad6N03M%2BThH1LOBEPDEGJJ2LqGxt4V0o8KlUfnKWf1zzA1iw6EDIY56AXVXB%2FnzTGSAA2i4Ts1gQVDYwztf%2FngrHaZZmOMSYZt6rkW19PfaH1HZ%2BDJL%2F3Zm%2F27MzHfhsdLpxtu9xrZ2w8zTte%2B%2BduKPPNNBvNNoVcIQgUYTxm%2Fix%2BFwWNp7nEJPr38WQsvvDxQEVOVj9Mya6fmXM0DMaVgDDLvt3NBjqkAXn83oes0cFgEDLKJz7tlSqIZMY6%2Bf6MphkTZ2tG3Aj35qhsg2UM2n99FLG5NnOy4PC0Ab0jdPb%2F%2BMnDnrvMoL2F6oRH3JRp%2FIB3J0Pafs4%2F2T%2FhFW5S4wYMPzrvUUhwumuksYdJxsZsMlFg2A5KQCof8P1Rah4FFNJoeXvi19bIXsMjSwWcOs6GZuYte%2FFn9J3p%2BNrxKL6WiSoFvM%2B3nMH4pc2c&X-Amz-Signature=81cc91b98b7e0a658f27ff8c698610918c337baaa34fb8f9d333d713ff4d86aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









