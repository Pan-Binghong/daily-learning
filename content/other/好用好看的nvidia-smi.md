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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OYHCDZ5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYnh8%2FysOJXBt6M4Vi6yhV6u7XM4wXMAxufXVdAGmj5AIgfKlu1%2FT4CGwlzDXy47aS6gk%2B4vKt7AVBEoksqYahVB0qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtNAR4D2Qle8A25ICrcA%2BqJywb06dQM2WeiofH6TSPN3myuLk%2BZxM9fq0P92aBHpPsS0a6%2FP87UnJrF6yt4FQj87C9C%2BF0AojKOiMufYtsWsMRWebHtZe5Q%2F0pc0qTYJGkJypMFVCwqrRcxCMZh3RPWrxBY2Yv3vwMeHLtI7LhbZGfM0ckniyTSmlY7jBGTy4SCpMwnSweqtA9jlcDvdxgdYKoByMY4Yx8Gn%2FyEupW7qDx7%2BqzCacP2TuWJmpXD5%2BUXzHfTL4I8TDwMSs6zl%2FoFjSlNB62aPnlWmv%2B68wOd3RS%2Fw%2FlTKLdvpmFau38wY2ft14UcHWAnB%2FcXEOozIj9ptVi9FPUMRycqbhldtAy8s1TJj412YkVElLP4YcmcmfISafXwFAUHt8Jo6LlvgibadEhvL7aJbUmyZk%2FK9DxRGh%2FNNmoi44Vv8x8THAq2lIteW6nakHdRNtibIoBh0MX%2BF1rLJnk7n3Bk7J8HNtXFLk9KTjOmB%2FiSaT4ZNLoHTCIASL4HkqkCOLVZCjA61QKlrYb8sS8p0GYzS6GfOSfS0kqK5zZjaiOZ3blO7dU2CwxC5QtD4zfFFkp1TsqjLTvQ4sFBUhr5S%2BiYs45ZMcL330h7XQnGtfxawIynvlVrpE7PyKbxX%2BZ7x0MdMMrx0coGOqUBR0woWdJadV3edfHAE%2BREyPg7V8xhKnmtRIOs4BjgGOZ%2FZ29ywHdSqhZ2Dc5ti4wTwr5odTjqY7yHAzpaslD5EYeB%2BCFZ74i8H%2F0%2FMqT9QJAMHljxmTslffmwaSyaqiMJqKM1RY53pzYInHJzky1gwWyw9S8RS2s6wLUPtpN5RGLa4%2BWDHBwlK%2FyY2Na%2Fgn1gPgzwssIRBop6HAUsrBfCB1m%2BBKah&X-Amz-Signature=bf15896aac53ee28fc6573330ff889b4767807c2aeba5533426247d62bba9dfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662OYHCDZ5%2F20251231%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251231T025829Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYnh8%2FysOJXBt6M4Vi6yhV6u7XM4wXMAxufXVdAGmj5AIgfKlu1%2FT4CGwlzDXy47aS6gk%2B4vKt7AVBEoksqYahVB0qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMtNAR4D2Qle8A25ICrcA%2BqJywb06dQM2WeiofH6TSPN3myuLk%2BZxM9fq0P92aBHpPsS0a6%2FP87UnJrF6yt4FQj87C9C%2BF0AojKOiMufYtsWsMRWebHtZe5Q%2F0pc0qTYJGkJypMFVCwqrRcxCMZh3RPWrxBY2Yv3vwMeHLtI7LhbZGfM0ckniyTSmlY7jBGTy4SCpMwnSweqtA9jlcDvdxgdYKoByMY4Yx8Gn%2FyEupW7qDx7%2BqzCacP2TuWJmpXD5%2BUXzHfTL4I8TDwMSs6zl%2FoFjSlNB62aPnlWmv%2B68wOd3RS%2Fw%2FlTKLdvpmFau38wY2ft14UcHWAnB%2FcXEOozIj9ptVi9FPUMRycqbhldtAy8s1TJj412YkVElLP4YcmcmfISafXwFAUHt8Jo6LlvgibadEhvL7aJbUmyZk%2FK9DxRGh%2FNNmoi44Vv8x8THAq2lIteW6nakHdRNtibIoBh0MX%2BF1rLJnk7n3Bk7J8HNtXFLk9KTjOmB%2FiSaT4ZNLoHTCIASL4HkqkCOLVZCjA61QKlrYb8sS8p0GYzS6GfOSfS0kqK5zZjaiOZ3blO7dU2CwxC5QtD4zfFFkp1TsqjLTvQ4sFBUhr5S%2BiYs45ZMcL330h7XQnGtfxawIynvlVrpE7PyKbxX%2BZ7x0MdMMrx0coGOqUBR0woWdJadV3edfHAE%2BREyPg7V8xhKnmtRIOs4BjgGOZ%2FZ29ywHdSqhZ2Dc5ti4wTwr5odTjqY7yHAzpaslD5EYeB%2BCFZ74i8H%2F0%2FMqT9QJAMHljxmTslffmwaSyaqiMJqKM1RY53pzYInHJzky1gwWyw9S8RS2s6wLUPtpN5RGLa4%2BWDHBwlK%2FyY2Na%2Fgn1gPgzwssIRBop6HAUsrBfCB1m%2BBKah&X-Amz-Signature=70239e6f869e5bdfd223abc262981ba95ece028c809b815f1eb85ddbe1a47f8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









