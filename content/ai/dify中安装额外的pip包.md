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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46636XDI6B4%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC91ReahkJN7bp6%2BMuo17jfHl4P%2BI9Ej%2BjVaa5gBNFhgAiEA6yC2rKsF6qKTjf15nN08lKzcmKI1FLfPLb2JSr3E7zkqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAE7QwK6fXClxMEn7CrcA6cW72BIA%2Fm9q8nNgi94LX5CYlx8OgcFXb921Rrb5EF1OcKmCJDIe5WbCkxvaCT%2FmcCdFMeAFkUiGIyy8q8QzDTlp7YmejLkHGoC%2BtD8mOJ3VRddr546hv65wEyd1yFYMEKrJlhR0zN16hMoDDkcutmhUsTXkOMI5p%2BEMYu7lI%2F%2BcPz7OvAoMEgqI8x7%2FnpPsBwrcWETFYEpxzWo%2F0SS7C47wywBCs%2BujHH8IDwlS%2FZ%2FbzpKuDCkJvfvdDz8bglgLdPwgZqpjZxD%2B%2FvQsAM7yxhoLLsC0t0QLL2mrhO4RiYuWnt1KWovWqwY%2ByOmvlAJa5eMFETOLetgHZcnCAUKnLth%2FpgRMTSsq5za1E6o02yW3mvMtsm5pBS2tieA8GCxwTSruwUqUDc9CVZmh4h0nNah5QiknjxLaRMdGZgZfrSHcDC1ws%2Ft8EIOYVNV0BLDNqtzgIc%2BstMXiAJI0eX3ONvtkfjnkmm1LJ3bQ%2FtYKSH2beoUYncO2ZTAsMImUqmqXSrPWVjEVstu18oGG0Dax29iVQcs%2FzQDVZEolX6p9YHgjUGBk0W7nbfXIlmp%2FJOcBSQsaf%2Bu%2FXQ34mPDsVsx27U0CioLBEZaB02eNi7LsDlpRYm5mEWCSXcgVR7FMOndtcsGOqUBihWOTh2avDhX7w8cB%2BAtszhA%2F86F6rAkA8jc2LgxhKfLiONlmAaZAk94i1nqwolzGwPwG3PVJUaRYXJUGREva1Gmw2a3vMjrjg2Qp4NDLqI65rZOdc3wYh7m%2BKBgDvbaHRkHgKK2HRLjupuJ2zkXaVtqw1HPmJPJhLnJSaNCxGao2XZXVT601Oal0LGXQeo2dNlknYXT%2FCWb7GFhQSv8TocUpd6g&X-Amz-Signature=0064d4d3560230bd494882a8f9ca4c04f3d6361c4fe65a00693620993b5a39f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

