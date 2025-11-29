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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLERIQDF%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoVcxuvpbCv4IQZ4UOHjcfKe0akGsdjoFLxvEVfQ0O1wIhAMF2kq8ec09uJpppevSXZxgkXcWDURMaaB5%2BbILxw0PGKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxF7MflLQYWFmuVDosq3AOesSZOcYjO7f9rU7wg96rNuX4VXd%2Ff7IBJPDqnfSmUVcQPzF1Ps1oM41HTg%2BkaaO1Gyl6TR26dM53YBmb0Q%2BRPT70YcjfdVoLiAFzuFA4sYnOdYCP06NxQkJKTiur5x%2FG57WQrGfxDPeXSdhmx0ODxQtVyo7Y%2BsbfXnOncyplKnM%2FWj8seOmJpmYEl4jGaF%2FWXasqFJcmjn8cb13Sg7kNvuIQzD%2BU0MGL4j1MEiid1uzCF65xCRyEnJCSg75rx3Kf6koZ4nH%2FmWcty9Lm3%2FXKOsqTy0%2BkjdiSkKpEy9ZcYuWWRmj1ehkgdCTHQks%2F8bAZU5Ohrt2ALl0OBC2t9YFDGHrFcY1A726v627gRvBsd%2FQt%2F%2FQTmiyqviVdzM7T0ODIsTMrr1SkdCznk8OzcuWwqu6pwF8WRvpyZxQqplvsW9o3EIPm7XiOZVezGVdo%2FCO4z4c76LwhvMFXNSmmdp4%2BXnbpsWfEhHX%2FxhDCXlsPRPWjTsaWO9jEcv1c3oyTPa7NZFnDJUJYo%2FdhrZguqQsrWkq31BDqLBOOQY1QVY1ltN56%2FoduoAXD8ilP3H9siZOplGTb5kuasD93OdtTf%2Fz36Eq6EKnjWfMYsXIwhfDlZr2BxB0Suy0BDtTPg%2BjD3l6nJBjqkAUV0P7Dnu32f12JcyKo%2B%2FRL6osMYvGkbHQbGlsGiQHCxqKxxeTaYNA0CNonLCHsr3NnALm3%2BXiO7YqOXdMJtecT%2FLRPqBpPUt26cxgPMMungoVrzzFvvfUFbOd8n%2FOWRv03CaR5cbnJA%2BiSQHxinq47SgcTPCJEhf08kCdc3qp1AeyXErPRIAe9YWt4njvtQjQv4rtkZR1ZgJgsMQLBQxQ3oVNiD&X-Amz-Signature=eebf6f894718e9f45cff44d24aa9400351560872b26f30e9ecc04fb869290f2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLERIQDF%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T024355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCoVcxuvpbCv4IQZ4UOHjcfKe0akGsdjoFLxvEVfQ0O1wIhAMF2kq8ec09uJpppevSXZxgkXcWDURMaaB5%2BbILxw0PGKogECMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxF7MflLQYWFmuVDosq3AOesSZOcYjO7f9rU7wg96rNuX4VXd%2Ff7IBJPDqnfSmUVcQPzF1Ps1oM41HTg%2BkaaO1Gyl6TR26dM53YBmb0Q%2BRPT70YcjfdVoLiAFzuFA4sYnOdYCP06NxQkJKTiur5x%2FG57WQrGfxDPeXSdhmx0ODxQtVyo7Y%2BsbfXnOncyplKnM%2FWj8seOmJpmYEl4jGaF%2FWXasqFJcmjn8cb13Sg7kNvuIQzD%2BU0MGL4j1MEiid1uzCF65xCRyEnJCSg75rx3Kf6koZ4nH%2FmWcty9Lm3%2FXKOsqTy0%2BkjdiSkKpEy9ZcYuWWRmj1ehkgdCTHQks%2F8bAZU5Ohrt2ALl0OBC2t9YFDGHrFcY1A726v627gRvBsd%2FQt%2F%2FQTmiyqviVdzM7T0ODIsTMrr1SkdCznk8OzcuWwqu6pwF8WRvpyZxQqplvsW9o3EIPm7XiOZVezGVdo%2FCO4z4c76LwhvMFXNSmmdp4%2BXnbpsWfEhHX%2FxhDCXlsPRPWjTsaWO9jEcv1c3oyTPa7NZFnDJUJYo%2FdhrZguqQsrWkq31BDqLBOOQY1QVY1ltN56%2FoduoAXD8ilP3H9siZOplGTb5kuasD93OdtTf%2Fz36Eq6EKnjWfMYsXIwhfDlZr2BxB0Suy0BDtTPg%2BjD3l6nJBjqkAUV0P7Dnu32f12JcyKo%2B%2FRL6osMYvGkbHQbGlsGiQHCxqKxxeTaYNA0CNonLCHsr3NnALm3%2BXiO7YqOXdMJtecT%2FLRPqBpPUt26cxgPMMungoVrzzFvvfUFbOd8n%2FOWRv03CaR5cbnJA%2BiSQHxinq47SgcTPCJEhf08kCdc3qp1AeyXErPRIAe9YWt4njvtQjQv4rtkZR1ZgJgsMQLBQxQ3oVNiD&X-Amz-Signature=b57c3ffa41dd7d500967fc4d5ea01f9ac111c0af9fad59732fb2b082eb14b2d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









