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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R3FX5Q7%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCm%2BdjRr%2BU2Nict4IwcEUuZPWEInw7QpEynX%2BJhuttsFwIgXpA6y3AennWLCYPUUmx0NCqu8tz5rG3uFdyX%2B9As4QAq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDDeRItXQHIJYhl4quircAz%2FNvi2jZZOdnaOH1MWY8p50ZEIwMxcWxex0fl4s7aPau6k0aOCUMYECwuoQ%2FbfjyisFE%2F5t3A%2BvYYh1pK%2FzjgPFwuQ%2BO1bVytYzY4V%2BuJ29NoFR%2BCmJ35Dwa5fMRqnfQtsAXyu8u7Hl7%2ByNwzXy4yDP3EE4o0C%2FdS0SlLp7%2FOIgKAXuGD%2FapmAPWHXjEF0RrOzZddKELiJ15Ez32BIHwsKRIIcgqSpsJ0Vnpu1zbBI4K03Nqxb%2FfJpkgr1ND%2FEXvFFq7w6S0nKYXZeJcjrUOEhU%2F6CJJjZyH2%2Bvb8WQKIhdpLwiy8BavxS%2BcSdwnphT%2BCS%2FU%2BkSi3FJevB7YmyCpHSZHSTuQW3wTqt4OFE%2FWucPw2W4Ipi9Th82PDFa4UzqXF3QYMRVr2v4w966La9mV7q3Y9%2FncrvKGorqjxt8uK4J16usFADCUzCuQPQX9lrKtCD4Sr5o2Kh%2BMjraw%2FJqNVMEBxVYqp7nBpsDNqEyf0YmLbongk6z2gzJvcVhqjzf8I%2BMbNPX1dRP0adZGdCrJGJnHUKjhJJ%2FlsJfMl7%2BR3iYUVAjYBpOoMogbtgJrtLWSCmtql5vf4ni%2FClju2UAiVJyOVpBXyfFgYKrCMbcjba08etXK3qZUPe0w2IXMI6xickGOqUBvD6kg7cxZsfuB18O2i3%2FqRLYaURbiHHi56WQIU7judQQcU2f91wJtzZkjP9tFP951aOzfwC%2FQHWGiVd2yYq9xwEwgPWTDSDEq2AQTdcd8XkWSMTuZCU6PIQl9RcBXwxA8zzp5uaZYRZotTQRKtM1IdjPJUtMk%2BW77sLGKyRy5IdrQ61LG9dc0GEslN2yu%2BDrF16yL86tdTOqvIiCtrYdU18pdqN%2F&X-Amz-Signature=3e9edbb90b8303c901228384b40b9ad23689c01546916659a980fd9ed2a9e7df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662R3FX5Q7%2F20251123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251123T025943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIQCm%2BdjRr%2BU2Nict4IwcEUuZPWEInw7QpEynX%2BJhuttsFwIgXpA6y3AennWLCYPUUmx0NCqu8tz5rG3uFdyX%2B9As4QAq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDDeRItXQHIJYhl4quircAz%2FNvi2jZZOdnaOH1MWY8p50ZEIwMxcWxex0fl4s7aPau6k0aOCUMYECwuoQ%2FbfjyisFE%2F5t3A%2BvYYh1pK%2FzjgPFwuQ%2BO1bVytYzY4V%2BuJ29NoFR%2BCmJ35Dwa5fMRqnfQtsAXyu8u7Hl7%2ByNwzXy4yDP3EE4o0C%2FdS0SlLp7%2FOIgKAXuGD%2FapmAPWHXjEF0RrOzZddKELiJ15Ez32BIHwsKRIIcgqSpsJ0Vnpu1zbBI4K03Nqxb%2FfJpkgr1ND%2FEXvFFq7w6S0nKYXZeJcjrUOEhU%2F6CJJjZyH2%2Bvb8WQKIhdpLwiy8BavxS%2BcSdwnphT%2BCS%2FU%2BkSi3FJevB7YmyCpHSZHSTuQW3wTqt4OFE%2FWucPw2W4Ipi9Th82PDFa4UzqXF3QYMRVr2v4w966La9mV7q3Y9%2FncrvKGorqjxt8uK4J16usFADCUzCuQPQX9lrKtCD4Sr5o2Kh%2BMjraw%2FJqNVMEBxVYqp7nBpsDNqEyf0YmLbongk6z2gzJvcVhqjzf8I%2BMbNPX1dRP0adZGdCrJGJnHUKjhJJ%2FlsJfMl7%2BR3iYUVAjYBpOoMogbtgJrtLWSCmtql5vf4ni%2FClju2UAiVJyOVpBXyfFgYKrCMbcjba08etXK3qZUPe0w2IXMI6xickGOqUBvD6kg7cxZsfuB18O2i3%2FqRLYaURbiHHi56WQIU7judQQcU2f91wJtzZkjP9tFP951aOzfwC%2FQHWGiVd2yYq9xwEwgPWTDSDEq2AQTdcd8XkWSMTuZCU6PIQl9RcBXwxA8zzp5uaZYRZotTQRKtM1IdjPJUtMk%2BW77sLGKyRy5IdrQ61LG9dc0GEslN2yu%2BDrF16yL86tdTOqvIiCtrYdU18pdqN%2F&X-Amz-Signature=a1c07d4932b86b597945ed6a177398eac848f7bebf0a0910eb56b16b57369ead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









