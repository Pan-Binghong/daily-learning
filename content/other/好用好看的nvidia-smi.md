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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VH2G73PU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAX%2BlGLaaQ%2FZaI5lCO8f%2FgqnFHjeoSJaG9x1ped1mpAIgKedN9dRv1qFFuCLwgyyK6IMo2%2FAh4mY3NE5QnjPWW7kqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKctaD1F%2F2JJRp3FLircA1EChTuSmkgJYxVoHsZH7Fwm7TueUJwi2XlG5t8nLs3Edw1qQ5k5it7qU2GrPOQ7EDZOXrDjpmLaQ5IsiXqrT95Kt%2BeeD%2B1cx2uFuTD5FL1nD0UzoNKTAknx1S436T5ZEQ9C41v84NRiZ5sPoR90wkXwg7qIrwerX%2FY6xDBC7nAqw%2BxSZt0WCrjKTMIKbM%2B0gu0mjEWpfE%2FWIyj%2FH5mfAIf3WO8ccRvt6BXSzwl4zHoU3nEu9gu2CUJ%2FzYXurfjgUs%2F72sfzhmEWHbd0PfB8HcTdQ6HZWEYFHfNstzxmlQbd8hBzbsJoAXmDUuErzLkVpkImtNy69YtyzyhtRTgDZqLykhAY1gsjBho%2FbGwEa09bscRh961K%2B2g%2BGSHwVifJR2OjIKHJ5lG37miBr3DmT6l%2B2UAH132OZMH%2FmIxE%2BQIX4R2cu7VKYZ1pJuh1Gn%2FQQStBxn9Qon7yOW48A8ZxPx0HyA34hMce7cxYTXWTfTjk2tHuoGPIBxo%2F0XTbY7hJQ%2BAU0MvSwDVPcPlQDiTYBrEFmnqpJypzGWbWwLD31EsHJMCoXSMBtPYEJOnh7GK1yXfr8dadrWSszvl6qxgQpMQljykHMKR7wlLba3n6mSDWWZS%2FTlfhWYJnnDnjMJnwr8gGOqUBY2BOuqEAt1kZCnbDwR3TH7eyt%2BrB62FQsldNAL9rg87dkIwun8BfYPdNXW1zA5M7%2FXMbKmRVz%2BGZoXwMsElJ1IXj9IXgvKlnBV22f5IWOpo2iglTO3ZJDHofT6cCDCbSbC4hKBHtfkVLUeOa9fB%2B9erE0%2BKw8rsAFYzoUSV0Cg3P2hzloJGHZKkHl3NxJkJ5jeQRKfWt1g6xIi8HLEuBIlSCbhR6&X-Amz-Signature=1d3ddbc3f4ae6a3c8bdbfa9d706c16565b40ff7638e0490751087d22e5c5e488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VH2G73PU%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014419Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYAX%2BlGLaaQ%2FZaI5lCO8f%2FgqnFHjeoSJaG9x1ped1mpAIgKedN9dRv1qFFuCLwgyyK6IMo2%2FAh4mY3NE5QnjPWW7kqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKctaD1F%2F2JJRp3FLircA1EChTuSmkgJYxVoHsZH7Fwm7TueUJwi2XlG5t8nLs3Edw1qQ5k5it7qU2GrPOQ7EDZOXrDjpmLaQ5IsiXqrT95Kt%2BeeD%2B1cx2uFuTD5FL1nD0UzoNKTAknx1S436T5ZEQ9C41v84NRiZ5sPoR90wkXwg7qIrwerX%2FY6xDBC7nAqw%2BxSZt0WCrjKTMIKbM%2B0gu0mjEWpfE%2FWIyj%2FH5mfAIf3WO8ccRvt6BXSzwl4zHoU3nEu9gu2CUJ%2FzYXurfjgUs%2F72sfzhmEWHbd0PfB8HcTdQ6HZWEYFHfNstzxmlQbd8hBzbsJoAXmDUuErzLkVpkImtNy69YtyzyhtRTgDZqLykhAY1gsjBho%2FbGwEa09bscRh961K%2B2g%2BGSHwVifJR2OjIKHJ5lG37miBr3DmT6l%2B2UAH132OZMH%2FmIxE%2BQIX4R2cu7VKYZ1pJuh1Gn%2FQQStBxn9Qon7yOW48A8ZxPx0HyA34hMce7cxYTXWTfTjk2tHuoGPIBxo%2F0XTbY7hJQ%2BAU0MvSwDVPcPlQDiTYBrEFmnqpJypzGWbWwLD31EsHJMCoXSMBtPYEJOnh7GK1yXfr8dadrWSszvl6qxgQpMQljykHMKR7wlLba3n6mSDWWZS%2FTlfhWYJnnDnjMJnwr8gGOqUBY2BOuqEAt1kZCnbDwR3TH7eyt%2BrB62FQsldNAL9rg87dkIwun8BfYPdNXW1zA5M7%2FXMbKmRVz%2BGZoXwMsElJ1IXj9IXgvKlnBV22f5IWOpo2iglTO3ZJDHofT6cCDCbSbC4hKBHtfkVLUeOa9fB%2B9erE0%2BKw8rsAFYzoUSV0Cg3P2hzloJGHZKkHl3NxJkJ5jeQRKfWt1g6xIi8HLEuBIlSCbhR6&X-Amz-Signature=b389a585fdf59e62b7352ca801dfac474a1dd80985abc85669ad53ebc11c0c1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









