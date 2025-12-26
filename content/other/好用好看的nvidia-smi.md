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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSSP57TL%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTXXhIATD1v80rhSD2KPQLptrv%2B3ZS%2FfU30MxRibmvhAiB6X9DB1MGnzwqjXsnM1Ouw%2BHnDEsNMN0oKRmZbJSaXyCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMo6YQWd3Of1CrI90vKtwDlmbe0qayCh%2BR8kHvU9FNZil1G35N6bqQUiUcQYzKz25f4DQXTFaIZma8HfBw7HmUfX6dp%2B6cjy6eFgpYLQeBig9hUopoLLmCqD8Oi8h5Qw8zN2Kj27RWfJNayfxTqcO%2FmoLWsEXZUZENoRDQp0b0Cji%2Fv7USAXWn%2FsldUlD9cTvWJ2e29otuOIcUbefOt1dmp0mnIYpyd0QZ7U8xKvthHIMMQaJKiwn9yDQo1hjB%2BtMXBAbsQ2H00hdf9gWWmCILcnuZoCO8RNd81dMOsojc5IoQQ0nIpnbNKtrm%2BSxISztRUwpdlF4tWpwUbMxgQQwX%2BZ4B4LPqFLXWJcbseVQF%2FE13P6sUIF49ci%2B9TyO9UCTCK7iqgkeflUQ2jXf1eGBbFiLZ1KdfEeJcKRODC9wHL1R07ozSubkVj8cRUOJJJ%2FWJ6NqIjJ2YUeS7KAaRtGNlCnHz98js4iOXbjEbz5pfm2632jabT%2FRxg7doBoZ3hRnWKCgXt5FZFkKkseZyMNTjkP%2FQ%2ByL5Hq0b9CqlwROOQVeMVriWs7Ocdt4dtpd4pktgAyOdDSrRsT%2Fycw6pLlVpTr0VMCKClafjkg5l8%2B4ZUfHx5pYB2wTJKRRmhvCAMr3AlmXPCz%2F5N%2B7mUgQw%2BdS3ygY6pgGmM717DN7%2Bab5EtojGta1PIMSPDgijERVKuBREux9O0Lkr62x58%2B1DXBc2oWehROnps9Hxtpaz9OBxPb4YaBmWjZgbwOwG%2FyGQfPS4ZqZBNWKv0T1H1FViHj%2FkUtGobqrSXoN6h3qBPqidzzvjHYHYWH%2FQclOAZYnMWvBVfOd7a1JVjnbw4PKXZhzZyfmjzjzoh8uOdtecCVjgbZRWC8P2RmqLwz1m&X-Amz-Signature=fa9f319ab8642fdbba4a5d86d8679b18eb95ce03a96ae07404cf125150fd3a16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSSP57TL%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBTXXhIATD1v80rhSD2KPQLptrv%2B3ZS%2FfU30MxRibmvhAiB6X9DB1MGnzwqjXsnM1Ouw%2BHnDEsNMN0oKRmZbJSaXyCr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIMo6YQWd3Of1CrI90vKtwDlmbe0qayCh%2BR8kHvU9FNZil1G35N6bqQUiUcQYzKz25f4DQXTFaIZma8HfBw7HmUfX6dp%2B6cjy6eFgpYLQeBig9hUopoLLmCqD8Oi8h5Qw8zN2Kj27RWfJNayfxTqcO%2FmoLWsEXZUZENoRDQp0b0Cji%2Fv7USAXWn%2FsldUlD9cTvWJ2e29otuOIcUbefOt1dmp0mnIYpyd0QZ7U8xKvthHIMMQaJKiwn9yDQo1hjB%2BtMXBAbsQ2H00hdf9gWWmCILcnuZoCO8RNd81dMOsojc5IoQQ0nIpnbNKtrm%2BSxISztRUwpdlF4tWpwUbMxgQQwX%2BZ4B4LPqFLXWJcbseVQF%2FE13P6sUIF49ci%2B9TyO9UCTCK7iqgkeflUQ2jXf1eGBbFiLZ1KdfEeJcKRODC9wHL1R07ozSubkVj8cRUOJJJ%2FWJ6NqIjJ2YUeS7KAaRtGNlCnHz98js4iOXbjEbz5pfm2632jabT%2FRxg7doBoZ3hRnWKCgXt5FZFkKkseZyMNTjkP%2FQ%2ByL5Hq0b9CqlwROOQVeMVriWs7Ocdt4dtpd4pktgAyOdDSrRsT%2Fycw6pLlVpTr0VMCKClafjkg5l8%2B4ZUfHx5pYB2wTJKRRmhvCAMr3AlmXPCz%2F5N%2B7mUgQw%2BdS3ygY6pgGmM717DN7%2Bab5EtojGta1PIMSPDgijERVKuBREux9O0Lkr62x58%2B1DXBc2oWehROnps9Hxtpaz9OBxPb4YaBmWjZgbwOwG%2FyGQfPS4ZqZBNWKv0T1H1FViHj%2FkUtGobqrSXoN6h3qBPqidzzvjHYHYWH%2FQclOAZYnMWvBVfOd7a1JVjnbw4PKXZhzZyfmjzjzoh8uOdtecCVjgbZRWC8P2RmqLwz1m&X-Amz-Signature=58d20f207d8821e30b74ebde17cfd9b2180acb9a0ce3657a683899dead6e23b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









