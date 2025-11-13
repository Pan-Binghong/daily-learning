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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWDIQUBQ%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T024707Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIGz2Mf%2BoUeS2Vs4rH8mpsm5o%2BCpklcF1waZOJ5QrMjRXAiEAjw5qCt1N53hLCNY%2BA49hPJoO92dlYyNu4gVAy3lj69Qq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDE9KZdTQ5Xx4qhMtwircAxMSFLoMzsGZu9l%2B1cG8Pfd0AosYCVG%2BtnxUKAMLnGDBHHepipb872c8i7gfs1tpjERNfJrPBv2u0UharJRXR9%2BAPzFp70QJLXITW3KfQSqgUC%2FEtJrUlFEZN2yS0PjQbI3uoyCwAwALGL4iRHp%2BC62pUcakGhWuGQOh9h35mWhNr3gEpG4wMdhKnzN1NY76wVuuETvaX3Eqiw73JTDjS%2ByIFyCm51DZZ0p2eDE%2FRHxG9lcSKnTsin7MaIry3BIbaJZxa1yYgzVb3XwhngiM9qAwhlEVC1rBT79V4rXIJYboljAEMcVd0oL1FestWpagmRa6Pp3v2TP5k4DptS5BwEqke6cv2WJXVMJGgGSEcblx4UYSZUcPAlXXQUoiMSAtCacqDM38LXpIaptxwXIYpjBDrFgMOpEVFWe%2F%2BjwCwucK7WtUrcyVLW5MGmcjC%2BJh0ZHxbkg2ZZ9XHXiTHjy046QCnuNeolVDwq9hc1B%2FXf1rLnBfahDdKkmDECT5DzWYS42uCkFdT1dXVtmjpZrceYEHVn8sVNfU3RuGeAvkPZBTcQqXSFKcbT%2BwEWlz17F513ITUExU3Vq2rN97RggNJYM8Sq5GaQd60LCtBDm46PCYn5JpFzNZEZg5cFecMJ%2Fw1MgGOqUBVIFyU7qd7KPKpTFbjVvI6PX%2B2SldbhemTQl5v%2FMX6RQGGQDMnJNSyFGTtpfeZ6hiqJkTgk34dAEoTBJrv8YU2FZFoCcJMKZymH3ix7G%2B9jfop5TTPVWd4WveSwSXsE4lC9o7HJLABCJTstGzmV3zM%2FoMNAaaJUoOMoRSBwQ%2B7VyPvsV8ZI1Rn%2BrrIGZ6lacV%2FlZbQAEz9dx4vnaTH1jizREZiccm&X-Amz-Signature=67ec6206c7bb02e3fa063e1ee96ee4baddc693937e4d3ae16da817c4a110ab83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

