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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOOMFKRU%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCMUJi7aHeGShYZM7XE3N0EfUdRcOc5YOipGbkW3WRIIwIfFq0THIYbAApgA9dF7ibK40kxJ49Zr%2BS%2Fbvpa7jqA%2FCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6BxuusSOmkEkU1QtKtwD28G2qx0mz147z1FejtkWuT1e1DjhWZEdb2qO0Ulsifza6Qxu8mPbz0Vhw6%2Fe6UqUNUNmw7dmIGwcJo5Y3l6psWsaDxoeYMoE8U3M%2BLjw6%2FML246Q6jhHGmP2Z4nF%2BDRmRzHtEvcilQEXYrWW7K4rvgBmg1kDmIlDUF72dl4DZ9WMgrBA3YbC9VcKYPTA8FPXJB2voVHeWj2BMxebsrmmUs9OngOxmguuU%2B6Kaf0LkzBVaq5sucLj9DKp%2BfDBRamQkkWJJ5ecitacQOvR7UtU28PMANOyTS%2FpHn2O0JPaxhtIA0bJaKR6YlALpj0aXfNZKDLzHpkopuwBzjHvufijsvwqObglgT5qEjfLn0ArkE3w6fV6kMBehi9UrpMvbBNTtJAWak6aQ5B3jytQfYnHW55juQgdAs%2BS2RynR%2BE6eHCSJiX0QZe5HjO1mYoJ49An5ln4faSK1f1dkXgxPnHW1BbVD%2FtHrOOMjmD%2FFHUvWMP6SwLGOWYcds%2BW6U1T7WAxcXeXN0%2Bo2RNfA4P8EBbgig2GuPVfaHrHRZQR4TEkFTyO9bOU3xvdyw2gE%2BtWiZda5cN21Vpwndo08RSPx9VjHcuS9ORQgoF4MLorssjV%2FbxF8V1g%2FuVy8sLIMH0ws7aYzQY6pgG5EdJQgzDTFG0n0KTEvCHnG9t4iW%2BaAsSdaVNkpSz3%2F8WI%2BlT%2BEz0oSuuZWHJat4T2Klu2XUg3mcgp1tx150YWAHszYxUVdonJpzW57ogrhGI0Np9nl0S4157MPOePnwllQRG3WSYQY4aPk9F%2FKUIlTkis3Sfg0qwl4rxxs7bju5%2BZV79z%2Bmwba2ivsJMXt5yKVW5fZstV%2Bk5cvnB9JPzkeXD8hANF&X-Amz-Signature=a8e34782adf080214342bb8eec8b22f1b8d27e0f33adefc0b8516583fc601623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOOMFKRU%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T033900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIQCMUJi7aHeGShYZM7XE3N0EfUdRcOc5YOipGbkW3WRIIwIfFq0THIYbAApgA9dF7ibK40kxJ49Zr%2BS%2Fbvpa7jqA%2FCqIBAiQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6BxuusSOmkEkU1QtKtwD28G2qx0mz147z1FejtkWuT1e1DjhWZEdb2qO0Ulsifza6Qxu8mPbz0Vhw6%2Fe6UqUNUNmw7dmIGwcJo5Y3l6psWsaDxoeYMoE8U3M%2BLjw6%2FML246Q6jhHGmP2Z4nF%2BDRmRzHtEvcilQEXYrWW7K4rvgBmg1kDmIlDUF72dl4DZ9WMgrBA3YbC9VcKYPTA8FPXJB2voVHeWj2BMxebsrmmUs9OngOxmguuU%2B6Kaf0LkzBVaq5sucLj9DKp%2BfDBRamQkkWJJ5ecitacQOvR7UtU28PMANOyTS%2FpHn2O0JPaxhtIA0bJaKR6YlALpj0aXfNZKDLzHpkopuwBzjHvufijsvwqObglgT5qEjfLn0ArkE3w6fV6kMBehi9UrpMvbBNTtJAWak6aQ5B3jytQfYnHW55juQgdAs%2BS2RynR%2BE6eHCSJiX0QZe5HjO1mYoJ49An5ln4faSK1f1dkXgxPnHW1BbVD%2FtHrOOMjmD%2FFHUvWMP6SwLGOWYcds%2BW6U1T7WAxcXeXN0%2Bo2RNfA4P8EBbgig2GuPVfaHrHRZQR4TEkFTyO9bOU3xvdyw2gE%2BtWiZda5cN21Vpwndo08RSPx9VjHcuS9ORQgoF4MLorssjV%2FbxF8V1g%2FuVy8sLIMH0ws7aYzQY6pgG5EdJQgzDTFG0n0KTEvCHnG9t4iW%2BaAsSdaVNkpSz3%2F8WI%2BlT%2BEz0oSuuZWHJat4T2Klu2XUg3mcgp1tx150YWAHszYxUVdonJpzW57ogrhGI0Np9nl0S4157MPOePnwllQRG3WSYQY4aPk9F%2FKUIlTkis3Sfg0qwl4rxxs7bju5%2BZV79z%2Bmwba2ivsJMXt5yKVW5fZstV%2Bk5cvnB9JPzkeXD8hANF&X-Amz-Signature=77dfa76f0b99bcd303a6d18522823a87f156ac75f381cb197c6b2d613bcbdd46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









