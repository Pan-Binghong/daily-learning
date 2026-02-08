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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46634SRT6CW%2F20260208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260208T035527Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAeJugWjYGs5Mq4r7v%2BCcF9HcxsUQviC3BBynhuaL17vAiEAi2Q%2BubiQeV7QOc1ts4ggL7%2BjIPXH7qNWfzpG7LvS3i0q%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDKlOyHBZrL41B7YS3yrcA9dHaegHIoYs9FMttakDho9lOKG6NgnjSIRdV9%2FoF%2BD7icpf4yugNfKdLzDaxlcYjgBoIkNdduiAEVPx0nf6O9RDkkH22%2BmVeANZnfqlyjai4pe%2B7SwXnMYTLOSW4Yu3MEm6Cwjkn3xRBtkn33QMEuute0Zg8wR0iZY%2BY1gh2HWCP3nIdWA2cci7DBBr9Vymk%2F4TJqRYRoFBGDk2FmSNO%2BWSZEI8OVVS7E7lxebOOmXK4pM%2FdRc8JJn52xILyB1by0VplSiiz%2FmOJCn4h2Vz6iCMNPIxqVc%2BfWcALQhl1KgWXg5WbDIKhHz92HL5IV7oMVB8Ij4Vmle%2B%2BEt3m%2FCq4UXz%2BiYV0CSoWwU%2BgG6alWher8mnvEJsEV7F6JuHFJw98U0cUOszwKBdrFKOZevAAPycbtfxfd578RmxBqIVn6UMtJLnVGQJjcX%2FTzji8wiQrYhiOaA8XBwVEOc%2F8O5%2B%2BxuLsrGsUWlPheOE6B0XiWjbc7yfccqcdePbuGa%2Fn%2FHjmAdxhUVrBuqohzwt%2BnSoEH5H0LGlw2sRt6uQD0IGO0%2B5ewOLvdR2jffdiwpUVeJZAdIziODoNtLU7%2BaKFJZvlXS%2BXbpT8N4%2F%2F7FmyId6XJrM6%2BiUd5Xa5%2ByD2qACMPqMoMwGOqUBoN6csG%2Bmv9Sy5Mx2OjGHpH1vHFxmBC%2BvyesXIE%2F2aUpZ%2Bav93Y48NoCDYePh6SkuSIR6JcgMTW65JhTQE1S0Laz87byFNl2CfSItHmnGwVNP2mzoNB49qs%2Bx53sBOkk%2FmLuoknmme%2ButTQWJrHt49WGXcqlNdKH4qzmcPJ7Dk7M1qxHpxCm787rSoDn1emWSJljHbSe465tthZf5UqClVOzOMBez&X-Amz-Signature=2955eb45623d81d7d4dfa84b69b5410071fd3b0e5ebb36271f16a448a72ecdf9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

