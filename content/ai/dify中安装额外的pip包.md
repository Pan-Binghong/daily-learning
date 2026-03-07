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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UDAHQVKR%2F20260307%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260307T031930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIGTfgNHqVFpfLwt98vOeeN4OI29UVU0vYXvBvfC%2FbJ8OAiAVk8e7Equ8z%2BA1CyejQJZHcyKvgJ8UnfaP%2FoOEL%2F7RYyqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbDcsTmouevnwJUXLKtwDe3B6kCTQ2vFZqHts77mSoxBRVBGUz9CZOr5sHc%2FdSvyc8Vua%2BF20ZeOBT1GX9w6MbVIO22YVflwD33kgqzSuG%2FL78r0i9hL2MFVCIeVRG6AXPihFQqFLI7DQrCl0nv3MvKx%2FSOao5DKeXm%2FueMHMvUT2jN9lJ0DWY%2FBVBW4nfnnYqbLcZRmJPzPlmOXv31qXWvvziu7JI8CELmseAPVFhBD61WfTJQ8iF%2FQHowkHyBmkdvVrDduGnSYOg2QJPO73SCM%2BswsjHAZXQCdz8o9UY9Ksj2NVL8GD7Ncb0dxGtFhId%2FlwFcV3MPI6Xs0sAWGfs6dSq10TOgwY5kTkUyDx27tghNj1Jq7qbMzgEb0pOnsV4YM3x1g5KbrKP%2BO4lxhA2LP%2BqB1oBQcpUv1HHEyZfNUIGIzywMQzr76jC780Bwr9xZUSeBLuKHR8cbae0YqFHovY9BZNp6tNaLFPwgrB7NbeVDJEnXxl1ONLA2HKFyPThH%2FljH3quLauD5oXB3T4Aj8AzQI8HyXtbR0lpRCxeW1AeuqhFLE5g064CFyF54f%2F3Ssk4y%2FaqTTgDl9dPeOBgll7s2CH1glp2m4B2qceYzASZn6iSQDeyUDauKsvyDllheaDno%2F3ytjfz%2BMw8ZOuzQY6pgG1vQRReRj%2BVE3DFdhB%2FmVw55mtor71TPRWIeiB7aioga1Ex8k14OhloV1dWvLuNhN5uibyJK37pQXQJeA5%2BioqmD9%2FNYi0S4dPsemaY6%2FoaaB8jkkfRqlKJpckekip%2Bcm8nLeCWgLBtBsANUTlxAzOsg0ae8dpofG4xOqCSwxHO1i0%2F5fUyeWh1yCRJfmgSEiwNYYLmz8iZ2CDFAjQ3ks63c2T0utt&X-Amz-Signature=f616d4d02f020cfd54f4f159b3081288ca47a416bb2c9c176e079899f0e48cce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

