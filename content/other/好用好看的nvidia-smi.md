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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7F5I72%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIG2LuB6icT09Rnu5qSTpZ0FFc4RbJBtfUuc0Kx9GZAXVAiAE14YmaAEWg0Kb47MWgnuKJSJyE7buwIUK5%2BxFKkjPxCr%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIMn06O7SnCZKLEc6jGKtwDYxrqEoW9I%2FOzU3RFRwYWStBWh5hD8RrO7yxrWHHc9TJRjXZ0swGSn6cjWS7dwj552JXz5tCJo1Kk8CVXGpBAHiwzm3RsUb0l8cIQDeQtd%2Bip68zTf20POBbqClTpgKlaY2nd8RGBgPS%2BmtggW8pLhGJO8y6K26ox5HAje5p%2BePF2UCsYzI8KbEqj4HN6ZGVqCcl2O72lC%2BfIVn70onJ1BAf50Mvv04NdYFa2QbJ%2BXm%2BeFMazmVAOSBxLrRvoJk7yiCB0Vmtax6YZn3XFGB6uUCpmzN5KFAMDQVPLEqDMopAoguPyPdVKJInvOnCHjn8DG%2FbK%2B5y0YdUdu2gjDZg8JjkDddv8qhYzmeySo6jMSijV7QJErQlaamDWhl9fvb%2FZ8LGQ0dJNiAxR%2BOVzb7%2FDYRa78y1cja5aUVrOeQnIVeT5%2FdvNU%2Fo73tvRJPZIhHgyRnvqjwx9sUpwMG%2FNJl2nsGG6dm18SnrTIS49o4ZZNk7S0AaiH2f64U07THYdrVKpVBsCx3Fr3pTrAwaU%2F6QE4dJ325YRjni699wGxgyefJaGkuc%2BTsDTGXBvQRHi6zZDSCMk5UniqtwRV8vBZhRNiAph%2BgGH0r%2BluBgf18c4iuBMkkVRvUaCrExwBqswosDPzAY6pgFy6awY6skthYAOq4JEzXEloV%2FqIroAAlsXmcKobBG%2F860hBhUtgBAPtYYegatYrtVAEHhqCaP3nrFEERfTODWXvSHUehxPzdF6Okd07C1AJfRR6a3Rt2HChJtlXelWik2SkkXbjA9sTyVfyA6wgLMfE1Kba0gLL5RftdxECJNgGyYFXMo6OkBeWdW3DAUzaP0Jlhjvp1rxSlImrG%2FhDGc%2BDJwDxUob&X-Amz-Signature=cb0db5f86b2221b299cd4736ce6cb0be0894a39f5f59b8d04669bb8eba3bf0f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QO7F5I72%2F20260217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260217T033919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIG2LuB6icT09Rnu5qSTpZ0FFc4RbJBtfUuc0Kx9GZAXVAiAE14YmaAEWg0Kb47MWgnuKJSJyE7buwIUK5%2BxFKkjPxCr%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIMn06O7SnCZKLEc6jGKtwDYxrqEoW9I%2FOzU3RFRwYWStBWh5hD8RrO7yxrWHHc9TJRjXZ0swGSn6cjWS7dwj552JXz5tCJo1Kk8CVXGpBAHiwzm3RsUb0l8cIQDeQtd%2Bip68zTf20POBbqClTpgKlaY2nd8RGBgPS%2BmtggW8pLhGJO8y6K26ox5HAje5p%2BePF2UCsYzI8KbEqj4HN6ZGVqCcl2O72lC%2BfIVn70onJ1BAf50Mvv04NdYFa2QbJ%2BXm%2BeFMazmVAOSBxLrRvoJk7yiCB0Vmtax6YZn3XFGB6uUCpmzN5KFAMDQVPLEqDMopAoguPyPdVKJInvOnCHjn8DG%2FbK%2B5y0YdUdu2gjDZg8JjkDddv8qhYzmeySo6jMSijV7QJErQlaamDWhl9fvb%2FZ8LGQ0dJNiAxR%2BOVzb7%2FDYRa78y1cja5aUVrOeQnIVeT5%2FdvNU%2Fo73tvRJPZIhHgyRnvqjwx9sUpwMG%2FNJl2nsGG6dm18SnrTIS49o4ZZNk7S0AaiH2f64U07THYdrVKpVBsCx3Fr3pTrAwaU%2F6QE4dJ325YRjni699wGxgyefJaGkuc%2BTsDTGXBvQRHi6zZDSCMk5UniqtwRV8vBZhRNiAph%2BgGH0r%2BluBgf18c4iuBMkkVRvUaCrExwBqswosDPzAY6pgFy6awY6skthYAOq4JEzXEloV%2FqIroAAlsXmcKobBG%2F860hBhUtgBAPtYYegatYrtVAEHhqCaP3nrFEERfTODWXvSHUehxPzdF6Okd07C1AJfRR6a3Rt2HChJtlXelWik2SkkXbjA9sTyVfyA6wgLMfE1Kba0gLL5RftdxECJNgGyYFXMo6OkBeWdW3DAUzaP0Jlhjvp1rxSlImrG%2FhDGc%2BDJwDxUob&X-Amz-Signature=69385537365e35081dbbcdd43a94ac3b944c49fc37bb192bb889c468e9897407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









