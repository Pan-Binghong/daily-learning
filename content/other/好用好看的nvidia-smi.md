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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JK2S2MV%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAd6rKteNaZd2UUeSernRY0ixEmX0Mu002UQsZyhvbmIAiAZgB578mfzsJRJLQpdy%2FDrcQs9lHkpUyP%2FAsXDj6vdPiqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCXOyk44ajJq%2FF8k8KtwDsUlmWQnkwyP6z5DhHqKt5ew8%2BQrgSq3BqSmY1nRTwbJt%2FmDeQt5xB0E5YskRuf18r0fVdHsmGEVuen68bx%2BVAgUmiZD5mHa5uuJhe42N%2BE%2FQqtNUOKYTTfetvE6ewz%2B8rnuo6NBXcZq024Hv2uBjgocPTbDOvhNEmEpzWVfYmFyoDLbBAnJDaSoswW8dYQUnXCUBTw2dWUfNo%2B0odYNr2i974TzD4fShDk4Btw5if%2FIH5UvHQftKxnvwTUt5RV3DAXgF3WMKuvxP2VcwCuDmzgjsbSKuktyC0i37WO2YNQWl5FKkXyqOt1Zua6SVX%2F1g244i6PnY1xcp4ILP7bHSuM58iVbv6fKrawLvSD5exL1HyNxOGlx7r2sDGZF%2B79ng4EMdp%2F16j%2BLCVDS6Oy2gfCfirDQM7UuVk7Z6IS8d3LFTRbG%2BJDxslN9lt%2FJXjzO8ZplCGrhy5%2Fb882FJ2h0PjaIm6Ztc%2FIFOa0RdpZZLhomEXmqxieRQp77RPIME4Is4IHM92IfhNZEKcecF3Y42YDujVNSHtceAPR7s2HIDJMt8uIHfYxNs38GN%2FJisJOa8TAXh8JD4Z7wpCmpGbwa0cTt8yOslynTC0CRi5ht5y%2BWmU4Ez8wo9sD0PIEEwkvmGywY6pgHIdLJJvFikUh9RHLPYiCMroPjuY8ToS4rm7JI%2FYfO7yirZMKywIN%2FUic0CIYkpNVoK8LoAalaf28a8pwv%2FaY06jA%2FlJGu4yWYNy%2BQoJ2221boymBfXXm%2BidlG0Yq2VCun00rM89wiySk38dtV5HutGUxNzkstLc5AJN7WTnDA7T07p6kwxnWNzxT%2Bl5aeP1R8%2FiT2rTnOcgX6qfe1fNvEbGViv5BT2&X-Amz-Signature=9ff0a0cc84b84f70d162803220a97cfb1e752083d8da520932d0022ee1d9534b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JK2S2MV%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T025520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAd6rKteNaZd2UUeSernRY0ixEmX0Mu002UQsZyhvbmIAiAZgB578mfzsJRJLQpdy%2FDrcQs9lHkpUyP%2FAsXDj6vdPiqIBAi0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCXOyk44ajJq%2FF8k8KtwDsUlmWQnkwyP6z5DhHqKt5ew8%2BQrgSq3BqSmY1nRTwbJt%2FmDeQt5xB0E5YskRuf18r0fVdHsmGEVuen68bx%2BVAgUmiZD5mHa5uuJhe42N%2BE%2FQqtNUOKYTTfetvE6ewz%2B8rnuo6NBXcZq024Hv2uBjgocPTbDOvhNEmEpzWVfYmFyoDLbBAnJDaSoswW8dYQUnXCUBTw2dWUfNo%2B0odYNr2i974TzD4fShDk4Btw5if%2FIH5UvHQftKxnvwTUt5RV3DAXgF3WMKuvxP2VcwCuDmzgjsbSKuktyC0i37WO2YNQWl5FKkXyqOt1Zua6SVX%2F1g244i6PnY1xcp4ILP7bHSuM58iVbv6fKrawLvSD5exL1HyNxOGlx7r2sDGZF%2B79ng4EMdp%2F16j%2BLCVDS6Oy2gfCfirDQM7UuVk7Z6IS8d3LFTRbG%2BJDxslN9lt%2FJXjzO8ZplCGrhy5%2Fb882FJ2h0PjaIm6Ztc%2FIFOa0RdpZZLhomEXmqxieRQp77RPIME4Is4IHM92IfhNZEKcecF3Y42YDujVNSHtceAPR7s2HIDJMt8uIHfYxNs38GN%2FJisJOa8TAXh8JD4Z7wpCmpGbwa0cTt8yOslynTC0CRi5ht5y%2BWmU4Ez8wo9sD0PIEEwkvmGywY6pgHIdLJJvFikUh9RHLPYiCMroPjuY8ToS4rm7JI%2FYfO7yirZMKywIN%2FUic0CIYkpNVoK8LoAalaf28a8pwv%2FaY06jA%2FlJGu4yWYNy%2BQoJ2221boymBfXXm%2BidlG0Yq2VCun00rM89wiySk38dtV5HutGUxNzkstLc5AJN7WTnDA7T07p6kwxnWNzxT%2Bl5aeP1R8%2FiT2rTnOcgX6qfe1fNvEbGViv5BT2&X-Amz-Signature=329a81953e39c3d08c15636bfc33eb030446a449f3bea97fa764a461aabafe18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









