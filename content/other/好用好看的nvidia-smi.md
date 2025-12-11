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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHUSEFVY%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIC7hszjvPriHug61AE0Z8AFIP2Mp1clrNrzpohAlty5AAiA5nv3xCJs5v0Z81bHgPHGaTrWU06QZOhEPrwkqyKYD8iqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoENTgPHecVjzbgj%2BKtwDNSkG1YbHX9BEofa3ps2M%2FIN8ink3x5jYCs1eZ0evoL4LCFIbjDed77sasLB6c8JhQ2wSy0wljKJhghIdOhUC1Ye9OQTIypslGW996%2F%2FNE9jdcSdrFTxPSmye8OEus2FUZylvpRgsPiFrMZd7quqI5Ku1GTbVy6mI4bdC72oC2o%2BNImo21YtPY1cRieqcDOJKjB0f4BtHfda4QYOsWM3YsWdAABap6xnNeErgo4AaRd61rj4%2Bi4EBsTb9ViXKGZhdTbZdUKwak54kpSKXB8Be52DUzmSska99857xtnk20Rvc7bWbOFWW84jhKjTGhPKlOR%2Be111TGas4BfUL89106PI%2FenUbP9WgqdaFE5a5uYGs5ok1FvyUBdkIXwsGgBuGr8dhJ6r0Jy8%2FAAH9PsY6jb7k6Zc7fGtZSSmNMjIdo8xFAChJcRrUu4CsFXwETzZai9AkU4QRvySKatluVdE7PnL8AvO2zP2Sjg0Wl4e2Iykb0%2Fj6h1j%2F6CT6DN8wTnp%2Ff49JSuojTQAwvV4QrJEvyLZ%2BE5r9LgHUlqZ8RxrAK9s6KoCTw340l7%2BHrnDNC4GCVZcZvTABGbNomZLPSGjR4T49NoMvPdj9mxaV%2FMzrKAVcURU%2FZdz4xaNB1cUwwrXoyQY6pgFXQyYJhb8Z3x8gkSN01umK032fuZUtyjBjJYy5sNr4DK2U%2F89c0%2FdKBCqRjn88l8cxJvyoaU0JtZUUyTIQhgmETOoYbkW%2BlJlTWl6dVz%2B6wZurjj5MRnE8zKX9bfXZeatLqtL%2FcfzMBfzlqx2FYxZHtdsBSTdJ6zSR%2F9eipsRdFCI8bKGZvL3VFdKa1VtLO3a9APzvNwniwhsi3aoWpTMMicMn9EuC&X-Amz-Signature=70a4865dae3500c726bf2f17c15230f5ddaeabdb2e27f2e9e4ab59835bc54db8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHUSEFVY%2F20251211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251211T025749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJGMEQCIC7hszjvPriHug61AE0Z8AFIP2Mp1clrNrzpohAlty5AAiA5nv3xCJs5v0Z81bHgPHGaTrWU06QZOhEPrwkqyKYD8iqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoENTgPHecVjzbgj%2BKtwDNSkG1YbHX9BEofa3ps2M%2FIN8ink3x5jYCs1eZ0evoL4LCFIbjDed77sasLB6c8JhQ2wSy0wljKJhghIdOhUC1Ye9OQTIypslGW996%2F%2FNE9jdcSdrFTxPSmye8OEus2FUZylvpRgsPiFrMZd7quqI5Ku1GTbVy6mI4bdC72oC2o%2BNImo21YtPY1cRieqcDOJKjB0f4BtHfda4QYOsWM3YsWdAABap6xnNeErgo4AaRd61rj4%2Bi4EBsTb9ViXKGZhdTbZdUKwak54kpSKXB8Be52DUzmSska99857xtnk20Rvc7bWbOFWW84jhKjTGhPKlOR%2Be111TGas4BfUL89106PI%2FenUbP9WgqdaFE5a5uYGs5ok1FvyUBdkIXwsGgBuGr8dhJ6r0Jy8%2FAAH9PsY6jb7k6Zc7fGtZSSmNMjIdo8xFAChJcRrUu4CsFXwETzZai9AkU4QRvySKatluVdE7PnL8AvO2zP2Sjg0Wl4e2Iykb0%2Fj6h1j%2F6CT6DN8wTnp%2Ff49JSuojTQAwvV4QrJEvyLZ%2BE5r9LgHUlqZ8RxrAK9s6KoCTw340l7%2BHrnDNC4GCVZcZvTABGbNomZLPSGjR4T49NoMvPdj9mxaV%2FMzrKAVcURU%2FZdz4xaNB1cUwwrXoyQY6pgFXQyYJhb8Z3x8gkSN01umK032fuZUtyjBjJYy5sNr4DK2U%2F89c0%2FdKBCqRjn88l8cxJvyoaU0JtZUUyTIQhgmETOoYbkW%2BlJlTWl6dVz%2B6wZurjj5MRnE8zKX9bfXZeatLqtL%2FcfzMBfzlqx2FYxZHtdsBSTdJ6zSR%2F9eipsRdFCI8bKGZvL3VFdKa1VtLO3a9APzvNwniwhsi3aoWpTMMicMn9EuC&X-Amz-Signature=74b6fa9fa2672e0f2135cda13eb9b8d236bd719dff223772d1eda51b9e3c5388&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









