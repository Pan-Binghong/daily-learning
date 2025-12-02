---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HIVPD7I%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T024928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJIMEYCIQDC6X%2FH49mkpJTM6ABSvzKKQdpm6udKytTj3R71x%2FBwKwIhAIhjj%2BE8e8uozIcMLsbcmdvZz%2BHmSFK7saTcYXk8UKoGKv8DCAkQABoMNjM3NDIzMTgzODA1IgzaJvJJSKw7ZOkD2qwq3AN2ksDtQ6%2BlotuBsSIb8STg341muWddhIL1Q6byLncC%2B6IX1SvNvPHV2xTswJYtZkQbdwYxbJVZ6aSrQ4rErfTKXHgHRRhb%2BboBINC%2FZCbWVmKLWGeAg0e9hYFj88%2Bl7zYmYb9PDIJIHzgeK7HS%2BYHipx9G6QIiVOBysceeFx3Ztq97RZ%2BH5LeFUdVji8yKWXyX%2BA6Nz2FKHHRyN1Tf5m0uRs6fRP4neXUQjweC00w34wV0s3vToswYNDnWVdCK9ETDlXa9lxLaSOGyboIqvV75B9%2FiMbq%2F0Cf4Lh7eAO24Mn8g%2F9s8ErU9IY%2F5Sses9B0kMz9FE76uxB2hwJeIS1aZs1GWolOYIkC91YMW8hECR3mePbtJT%2FAM%2F1DkeCflDGwpce%2FGSEfOKv6WVU3F4Tj02lAbYWIyw68Ot%2BJr%2F33aIAo85ud27UGWd21fLTMLW00pay2DsiosWJ1Ts1XTcugT28irAwchrIlxhTCav3yZaDAcwgQuGYsXrVfn%2ByUruflzvooPQpKsRUN1Ai0AUIJL%2FfyvcsxJO%2F3pUcy7CkP08Gk2URY9sbXiYwIKUBStFe24xnNhF8cZJI9RBxNgSe07CXspJl6b6UtPxvHfYyOYdf%2B9mLs4mG2zTF2dVDC33rjJBjqkAVm73waXtJlVaUUMWG7vf%2FPWQ0sPpym1F%2FIPIxLz1kZ6stvxzI1S%2B6BcMzIqxkYQJ%2Fn6R3MjoLnHC%2BOYbJjq3udz3ewYalPZ%2FbPHl2iZEP%2FAB6SMSlEMW5pTBMQe1Prd2g9BPoOxvBpx2ajTwvbwbsJl8uaCrwoTZumzL5SVauGE9Sood4eD%2FSFJVZv%2FjA%2B2Vnh%2FIW6bJ6HfFTrkMbrfmKmOywyp&X-Amz-Signature=d2793a251af677237f3c2819e0419617f6235d64fc791b2c4eded9e2094e3843&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

