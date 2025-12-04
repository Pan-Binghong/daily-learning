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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHNMUPXF%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCiGnwJHrEyzgP6B8o03ODfCyYeVtyLczxlm9CJTu4a3gIhAJJg4kNGtea%2F4zPDdcgnU4YaywfLT4IVqdLT9IVc2%2BzyKv8DCDsQABoMNjM3NDIzMTgzODA1Igw0yQCwNeihs%2BJW1RUq3ANqRdNsBJecqk0Ufpjijs3IKQg4KppF7uUPyzhCNAYFQQZTs9U4uUj17KXmEILLzyPRKwvOMaiC3dMJm7nwK0edSkavV5MwhDOwiB7QAAvUhgiUpdvTEPTyoxWkJpTwG4DTGWMPVv0rGpP%2BoOxnqOKt7YJd2IwipJpoJSCkqR3qt0Em9hk7vXMmCiLE0%2F3wzEApaiOpIH8YNsyMkNytKPJUlashUlZQiaBZNEgJsMDdXItjkGnwW7XkFcAbGkHcdgxaRkZeHn2e0Ikrc92XJwUy0%2BNiPmvH9OcKDpKE6Hj3PwOyBinalPJaWILWUQEN%2F9YN5yf554P3tj0OLXUQ8pIjaOGHduoDSLy%2F7yHiU5Ma0sc5GFNFXXGzFZwRSH3EYmF2gS6C2rHgnwrU1XRTuzSSDCrJ1vYM0Yc1v%2FvjEnVXy8RvttsKH7ap%2BrRFu0USbvchLlaRLWLqLVcyNhS38bLQqW6sOVEGprLsdPOimm5nWd6PNYlTNf5%2BeDQAsSdrtbM4edLepnHxKQ5UR6jX3uKpqEkK83fSJeWJuGcnQ0UCXAX8T%2F4K6DoRH06o%2FJ%2FG9UUiWRn4%2Bui5NLVZc5qD%2FB5HhUgxdHCvkDLvotDkFXnPIjBZEYUaStcUhE8S3TCn1MPJBjqkARLgNPvl28VLppMo5KuHAZTYT92nldq1GB3%2FENHAkhfv1hnbM%2BzygUzEQU%2FrpKmnRrQ205Kz6fDek4MKaJMilTDQw3bd2jmi1ZuU%2FXrtUwcZ1pVZXdZW00dnpR9KDm1dCsPC9xFfHS%2FsaK1Kj%2FCpz0DlSifaFd%2FusxFcISJzBflgEMjyWqh2x719qBIND3ZmVY%2BqOgbnIOIDTYulITrr%2FcgBvrSf&X-Amz-Signature=8745a75f94a2a6631ec94fac905f8543ab6c01fa105bea367db84bb968577f10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WHNMUPXF%2F20251204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251204T025116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJIMEYCIQCiGnwJHrEyzgP6B8o03ODfCyYeVtyLczxlm9CJTu4a3gIhAJJg4kNGtea%2F4zPDdcgnU4YaywfLT4IVqdLT9IVc2%2BzyKv8DCDsQABoMNjM3NDIzMTgzODA1Igw0yQCwNeihs%2BJW1RUq3ANqRdNsBJecqk0Ufpjijs3IKQg4KppF7uUPyzhCNAYFQQZTs9U4uUj17KXmEILLzyPRKwvOMaiC3dMJm7nwK0edSkavV5MwhDOwiB7QAAvUhgiUpdvTEPTyoxWkJpTwG4DTGWMPVv0rGpP%2BoOxnqOKt7YJd2IwipJpoJSCkqR3qt0Em9hk7vXMmCiLE0%2F3wzEApaiOpIH8YNsyMkNytKPJUlashUlZQiaBZNEgJsMDdXItjkGnwW7XkFcAbGkHcdgxaRkZeHn2e0Ikrc92XJwUy0%2BNiPmvH9OcKDpKE6Hj3PwOyBinalPJaWILWUQEN%2F9YN5yf554P3tj0OLXUQ8pIjaOGHduoDSLy%2F7yHiU5Ma0sc5GFNFXXGzFZwRSH3EYmF2gS6C2rHgnwrU1XRTuzSSDCrJ1vYM0Yc1v%2FvjEnVXy8RvttsKH7ap%2BrRFu0USbvchLlaRLWLqLVcyNhS38bLQqW6sOVEGprLsdPOimm5nWd6PNYlTNf5%2BeDQAsSdrtbM4edLepnHxKQ5UR6jX3uKpqEkK83fSJeWJuGcnQ0UCXAX8T%2F4K6DoRH06o%2FJ%2FG9UUiWRn4%2Bui5NLVZc5qD%2FB5HhUgxdHCvkDLvotDkFXnPIjBZEYUaStcUhE8S3TCn1MPJBjqkARLgNPvl28VLppMo5KuHAZTYT92nldq1GB3%2FENHAkhfv1hnbM%2BzygUzEQU%2FrpKmnRrQ205Kz6fDek4MKaJMilTDQw3bd2jmi1ZuU%2FXrtUwcZ1pVZXdZW00dnpR9KDm1dCsPC9xFfHS%2FsaK1Kj%2FCpz0DlSifaFd%2FusxFcISJzBflgEMjyWqh2x719qBIND3ZmVY%2BqOgbnIOIDTYulITrr%2FcgBvrSf&X-Amz-Signature=decf0b47b29f1f3f0cc35c53572064c3c9b4898389ba34dc890525812280f5a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









