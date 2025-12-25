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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UY4JHK36%2F20251225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251225T025708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJHMEUCIDSHG45xMIbopWkCYUoP5W2RUb%2Fl1LKrbHAipAcyW%2FmrAiEAnnO7h1Og%2FIhkvtFuzHkFaXR%2B%2BKQ4chTu3Hp4dC03GDcq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDLw8czeLwH2fOibZ%2ByrcAzW%2Fg2sxoYrLBUxAelZxs%2F67WH%2BNp5MJMlls1mBlSVvFR%2Fn2610DazuWmjrQxw%2FBvb2h8uXJhBbFzg18LpIifFijRFI%2BOIzcxDMSGhGiXKoKePOGyaqN%2FfOhuAFY05DTsYRqKaxWSiRhrWQETj6em%2BEkSEb%2FxbEMsy1T41hZitakjRzx3Zd%2Fr%2FOwhHhEIJ2u1t8K3FiHJ5v0S3ovFtgHYA168cYL%2FQuKjY6fhF4mDGCcNjCmQrSgIRcwfA4H%2BaaMp5Sv07viiy9SUId9RroQMGITiHO9Ic%2Fqln9Rk1ktcBta8jpLE%2FTDgX2yS3mqbMK1dMfvxyNXQ4vE014I1CIKIgOiTVeTPc9LCVvMD9X%2B1iie4BbuHcnrdmeQeuGQ9UAGkYTeH%2Bce%2BSYIwu8vnAG8fl5%2FSIpPqTvAbfQAWSmg5dTnP3Mn8XU1qUAB0p6vOBWapTzcKouJCVg3DnIgU20DSWkpBFA4r5VF%2B0QgvPjPjK9IGCFuaEiu%2FUGEsEsjhrnijVbmOpih1Abk6St3%2BZeHQfpMWBpirt2Gqk4fsrRL4xP0cv85mVD%2FgSBQjRDT24lKblBz1zNA3fYTOZZztPPXScBkehqAn1TlWrVjUtK2Uj0RjOaH2zswEmIORxoHMMShssoGOqUBIm69OssvWpDEsjQr2R4kdZL1RR%2B5FOY%2B7jHolk4bGozAU6ofvFOYorhkJE%2BqlnJnS%2Bmj4DHBPYuW9xRkHhLSnMG6RejXKMhqJVjd1%2BA2tS0rqJTj4kbbU1Ka6HH%2F4TfHEgZAkCNksupsS%2FofKbrWt%2BnJUV5%2FN7dww1P0sCs5zORf8NtqxI2HzjvPF6FssM7sDU6vw4icxRK6TYl5F20oCOkhNEfD&X-Amz-Signature=e20e29a839727f0e31fbab900a161ab93e730f4d78d166c9ce98142b344ace2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

