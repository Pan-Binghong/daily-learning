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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ASD7TA7%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZmwQFEKOmzpEkRqpjoD7s6HzONor%2FtCnqLNFS%2F7i38gIgCjfvwSmZAJsVz82w1%2FQapLBUNdIIvUaGnVlSFRAgnyIqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOIo630OYPvSuPg65ircA7aMsS37M7VU2%2FR7gq%2BwtaucihZfns7O%2F0uneSwJ6B38z1en5%2Fwezp9UPIDsKgdqCqTIAm%2BlWamk3p3lM3CzcWlVyULIgh4Y6QrPGf9PTgM2O3fJLJeEnkNXLIy3qkH1pvYF1%2Boxw6ho0qvW4M9gIPuq9RqFlRE44KNjkEMVnyCIQzqdh3WFmOMm62o7lXfQnlMAySCXdzWoh0o5j5PUy5TzWynxdwoJLBa%2BcbrQLvBE4CsBN5uSQxEaFxhbG13bedoXNvrxcxdwk11Xiy8zLeoTDkjX%2BXpMp1KAHM2mUn6mM%2B31TekE1VcbTumWSWyJ7Qrzr%2FwBJTkykZe8nGE2Qm1Vmr1WLbtP39RPZh%2BsI%2F41KAR1uKeV%2Fk2beUPR2E4FKP1GxF3t%2FGRGapcLbm9BhhkgApfBNhv149zFulNt63KzES9PlCfNGMMXC%2BaHQ6LvvnBOCFvkW9gV1%2BR5Bq%2BvopcyfqBt4nx2lmULCZUFnCefM%2F8RJDv1DoYtxnbv6Ud%2B02WwrIyWQyudptuaulnxdKLzvsmT9nQ6%2FJxjjdhOVfNq5o8WT4i21ec8Wrw3cG%2FBJfqmedg%2BSKB9hY4DoHRcguHHJREw3uqSPlBbyWELJjqFYj2O8LxYh2XTIStLMKfEqswGOqUB7C9kIxmVqYlGROmSCuuiWCvwY%2FwYN%2B2FWySyD3CwDrBLiTmjkdZ%2FCDM7INcuqvPn74Jn1XzoBK1CG7JDN1QpFkW5qhnKCbxJWAwIJ4MwPCdNjd77KfOkCjlLOQ5liA5JnS25z9V4WicbNOUPWhDBnKzNYMveoLOxkmeOIeFwcbave2ObmNc3h4eCIj8%2FgOA6zLtJfffIDl6pjYXu0ZSSgyLUjr5M&X-Amz-Signature=6214f8f2c2c08a68e406cabc51d06c13f122fdef68f4ef63585e45f9e35c98d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

