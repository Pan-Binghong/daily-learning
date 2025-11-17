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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466276UCHFH%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQUQTYfpwnVcbDJdiQXAcjSWmyrlspxaTl0Nw25k1KxgIhAOBsQy350GkZfEm7kTVIAmaWFLVm7AM2bt1rH%2BrE2BDVKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1wl9ShEsV5TMWaygq3ANms4Vi13ZbcRHiLSY7M7zYxL9rseKURcuj0X4T67V5BIVxXlaEZDyyMurZEqkCVJr508ERtFVDftxuWZSm6nXHE7QSYn34KMZs%2FxYlBY8fvhH%2FnfQujowHZh2snscqTqE3yF%2F2s58u2P5BEL4geTGpId%2BdsPx8QS2ORC1rZiAmsljMz28fqQ6pTTuF%2BS85BL42PnzwIX%2F%2FE7K%2FmayE4nU8Ai28h3xwxUBmkYlwD8IJd2UHn3CRj4x6hIi5Km0kxHr7WYo%2BygnVkyLpywczB1h24lFM3ZD44LkIuFJErLvcKdrhZq9MamZcBosbQQoEX7LcMykQRkocfrsLpNTDOWJXEoXVdmfkAJ9PBbzJ5UARGUjyLEI94b9yeRDC%2F1sDcZsX53%2BL2t7L7Q%2FU%2BiluKFQws6Cay1Zu5Kw2xN%2FZaYBtVxUsDepQiEMEFymfP4Aa99UzZI3qyvjhZ2YRdQQxXpD8N58w66GXn%2FGBUd9WhcW2%2FOYLGr9qyoDhLoLcZs%2FpRLNP9YpXf1Xr6euvOeQ2uUlyFh783SplAZ8NLagHeEAGZpYwiBA1UtLwS9IyaayGSRR0CgByFPtL%2FjhDRkjaCIyMmgXyfmM9%2FHenGFt%2B1pR%2FBxlaycULrftgWPlq1zDhgurIBjqkAWzx6RFylXZlTg4CFSwSQ67vwrMLoeoLRP3U24H1eHD3r%2B9LUSWBXj7kvcIpcZJ%2FGlIvYW46FnvUT6223K98J8FI1WzhQ6Pe%2B5%2FWpgQxTz1vECM%2BZVZNbdCydjJ6%2FN91FdrxMXrs2gkqLS8kBkFLKfd%2FjA7nsLCjDFNB%2Fh8UZQdpBCSo%2BdI%2BHfHeHUHgKGnNdQ15HZvGHJBNnbU3z0k2BdGIwwwC&X-Amz-Signature=07a1b9e813ee67b1675a06b853010e28a4b17ef691850194757983efa16335b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466276UCHFH%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQUQTYfpwnVcbDJdiQXAcjSWmyrlspxaTl0Nw25k1KxgIhAOBsQy350GkZfEm7kTVIAmaWFLVm7AM2bt1rH%2BrE2BDVKogECKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw1wl9ShEsV5TMWaygq3ANms4Vi13ZbcRHiLSY7M7zYxL9rseKURcuj0X4T67V5BIVxXlaEZDyyMurZEqkCVJr508ERtFVDftxuWZSm6nXHE7QSYn34KMZs%2FxYlBY8fvhH%2FnfQujowHZh2snscqTqE3yF%2F2s58u2P5BEL4geTGpId%2BdsPx8QS2ORC1rZiAmsljMz28fqQ6pTTuF%2BS85BL42PnzwIX%2F%2FE7K%2FmayE4nU8Ai28h3xwxUBmkYlwD8IJd2UHn3CRj4x6hIi5Km0kxHr7WYo%2BygnVkyLpywczB1h24lFM3ZD44LkIuFJErLvcKdrhZq9MamZcBosbQQoEX7LcMykQRkocfrsLpNTDOWJXEoXVdmfkAJ9PBbzJ5UARGUjyLEI94b9yeRDC%2F1sDcZsX53%2BL2t7L7Q%2FU%2BiluKFQws6Cay1Zu5Kw2xN%2FZaYBtVxUsDepQiEMEFymfP4Aa99UzZI3qyvjhZ2YRdQQxXpD8N58w66GXn%2FGBUd9WhcW2%2FOYLGr9qyoDhLoLcZs%2FpRLNP9YpXf1Xr6euvOeQ2uUlyFh783SplAZ8NLagHeEAGZpYwiBA1UtLwS9IyaayGSRR0CgByFPtL%2FjhDRkjaCIyMmgXyfmM9%2FHenGFt%2B1pR%2FBxlaycULrftgWPlq1zDhgurIBjqkAWzx6RFylXZlTg4CFSwSQ67vwrMLoeoLRP3U24H1eHD3r%2B9LUSWBXj7kvcIpcZJ%2FGlIvYW46FnvUT6223K98J8FI1WzhQ6Pe%2B5%2FWpgQxTz1vECM%2BZVZNbdCydjJ6%2FN91FdrxMXrs2gkqLS8kBkFLKfd%2FjA7nsLCjDFNB%2Fh8UZQdpBCSo%2BdI%2BHfHeHUHgKGnNdQ15HZvGHJBNnbU3z0k2BdGIwwwC&X-Amz-Signature=528e4b7c141611d979f8111defa8ac0be3518289bac6d18283fc913ded1f5eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









