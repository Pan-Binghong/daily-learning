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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QD3AAZ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDU6%2B%2Fmp%2F%2BrK7aeJNgLRmMBuL55MWl5Y%2B4LxSHG0kux0QIhAM0dmPWKXfuk3R8oBEhuLj8rYspQ01Hy6mwjWBsoRkeMKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzL8M8ginYXGHmGxmAq3APPwvQmjcSl%2FdCCeckFcTDFUY1a191kc08m3qSb%2FAQNc2MT%2B4SrhJfn0mnGLKYwX05I3iKw0TlYGnTBFnrU0c8%2FkOv04PBoxX38ruMSTmKDJbH%2FdWDk57nntXZrVbF3jD9LkxSlqvXmE1346LN8kEL7cIkvctDUUrIyiWnABa4j%2FVPD4lA6J%2F%2FC9ZnfWUiTA4EM19XTtGQPCKvhESJra1VrnenfN6zKmA1kzlguI6OHlMv%2FsCQ0puZ5QVQHtqkxLFx4tSJIzI7tOl6SFJS2caaAzdF%2FKyu1Ll4da9OWILtGisK66BwwZykv1S5X6B0v%2FGJiQXudiG1220Lg5yPKg5VaajTpGnWkOthG05MOBgRVKpzNP92dFaL70GU1Al0iA4dtKXZyix13WCQzKKC0dwD65dTTEGl%2FKXNZr3GmSVkm4u1D0AcZMZd%2BppfWlp4deCvsAdIR9oTbT3bPEySdtx29a0mIrmRRbn4qQ4fVUno%2Fw9UpsFa9UDIz2mkoQw9Lx6IirZFKcGZl7fOgi1Gl7a0qddhUed5967%2BEO6Tc3z%2Bhl7bVWP%2FACs3ROka0Tn%2BqMqzU%2BcKzTlQ9TA4qCvXumyaZqEsCaCUYe1vPRSPF4tWul0%2FgZwFNQXMmH7qTajDt8a%2FIBjqkAdh7a0wFY46XA07vk9spMmnQ4QmfSeM0S5RyJ8wZ1pAfdpgFxoFlxtGxn3m9V1gwQUf7JtILN2ghzZSKikTV%2BfaRA7GHgulgn9AsuWOCSnFkUXoa2ZwPbdb3Gqn0PS%2F6FL%2BFjDbvLAiorhQWXa0yyPxzkWzEWDYOmRE8Qj9RAMoccDANlGOlRqD9XVPbmd7cEBecxCPgFlWmmrZSag3kUZcMsc%2BP&X-Amz-Signature=2948c3f4fe1739bd59ae0b7d5b3f220442566f3d8c98991b661274de0d7e5001&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46664QD3AAZ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDU6%2B%2Fmp%2F%2BrK7aeJNgLRmMBuL55MWl5Y%2B4LxSHG0kux0QIhAM0dmPWKXfuk3R8oBEhuLj8rYspQ01Hy6mwjWBsoRkeMKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzL8M8ginYXGHmGxmAq3APPwvQmjcSl%2FdCCeckFcTDFUY1a191kc08m3qSb%2FAQNc2MT%2B4SrhJfn0mnGLKYwX05I3iKw0TlYGnTBFnrU0c8%2FkOv04PBoxX38ruMSTmKDJbH%2FdWDk57nntXZrVbF3jD9LkxSlqvXmE1346LN8kEL7cIkvctDUUrIyiWnABa4j%2FVPD4lA6J%2F%2FC9ZnfWUiTA4EM19XTtGQPCKvhESJra1VrnenfN6zKmA1kzlguI6OHlMv%2FsCQ0puZ5QVQHtqkxLFx4tSJIzI7tOl6SFJS2caaAzdF%2FKyu1Ll4da9OWILtGisK66BwwZykv1S5X6B0v%2FGJiQXudiG1220Lg5yPKg5VaajTpGnWkOthG05MOBgRVKpzNP92dFaL70GU1Al0iA4dtKXZyix13WCQzKKC0dwD65dTTEGl%2FKXNZr3GmSVkm4u1D0AcZMZd%2BppfWlp4deCvsAdIR9oTbT3bPEySdtx29a0mIrmRRbn4qQ4fVUno%2Fw9UpsFa9UDIz2mkoQw9Lx6IirZFKcGZl7fOgi1Gl7a0qddhUed5967%2BEO6Tc3z%2Bhl7bVWP%2FACs3ROka0Tn%2BqMqzU%2BcKzTlQ9TA4qCvXumyaZqEsCaCUYe1vPRSPF4tWul0%2FgZwFNQXMmH7qTajDt8a%2FIBjqkAdh7a0wFY46XA07vk9spMmnQ4QmfSeM0S5RyJ8wZ1pAfdpgFxoFlxtGxn3m9V1gwQUf7JtILN2ghzZSKikTV%2BfaRA7GHgulgn9AsuWOCSnFkUXoa2ZwPbdb3Gqn0PS%2F6FL%2BFjDbvLAiorhQWXa0yyPxzkWzEWDYOmRE8Qj9RAMoccDANlGOlRqD9XVPbmd7cEBecxCPgFlWmmrZSag3kUZcMsc%2BP&X-Amz-Signature=bed75743e364b339cd795348b8d676968e9010383e5f76947959a0768fa55a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









