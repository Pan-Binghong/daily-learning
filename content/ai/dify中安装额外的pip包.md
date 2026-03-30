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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAQ3WCNG%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQDDMNpFIEb%2F7wnzWp6iLVqN8jH4lXJf4ybJ7mafhvYzMQIhAJxdFSKApPVDvSqmjQ3W7Evds5qDZT5yBOdicIT3SB8QKv8DCBwQABoMNjM3NDIzMTgzODA1Igz2YLA9XsyaS990LzMq3ANrya6aB25tmI6sa3dnCNoUEUuVzfVYLJ78o%2FosB3xIqw9zeZpnXgC9U4V5Jy8BJTS8c4vvG5altF4BhNr%2FX%2B7I%2B6OmnVe2Th%2BneKj4r9Caz4IxMqLNKfRC2Ml6XzsIiU9f%2FRHqzIfTE8ult96RipB7msfIWTD1MNhtN89mxaMnxWyomF%2FNmaclr4z384WqX63I3aUE%2BR%2BbAQunbpz6NApNkJ8vrjQC3btghAxN70VWDA9SbGueJnKkrC%2FNN1rgPR9v906736h%2BPSjU1asep%2BZmJFODIIf%2BS4EhcDT3ouRjFSh%2F3SMJIhtl0f8%2FdMgg4BYxptIkyJbc7%2FPuJwOhHTacEmEigBiawGYbxs0KkUYU3g5tMhDWvoOn7Ek56AYRf6YkxtapnfUiJKbUdahieA6sUVIklM0l0JWJ0EdgliTLTim%2BQTskPxxnhhummuzVdigJvOGLoIBLrnVC0AWj7OdMd%2Bq4XT%2BT87fdpfYN8bljNchkkWB1LGb5m0Sj0%2BrRX2HxrRGLxkLIvk9vzGm9ak5XDuxQ59qMxlejhaBWPJxNdyrsb5AIhv1NM0gHZFXfBlVVOhlXH%2BwtQQfS55RKJBY0p3B8wLNqmdZjuvhABwjclnqU4BfoITXM%2BzntLzCFyafOBjqkAU4RVcpSo%2FpuyynU2FXBOHVN3w137Qb9kl13BZjFX0gyTFJL9rdmAiYeIhDqJmP%2F5EEztHUc%2Fam9nEufzVl6BzuA6BsHWx6xnfJ6xsFkI6293FrbYgDtZjeTYY6dhXJeBlHi3PBtQu2qdyggQ1Ff5QU59eKBi4tgjBn1TsXN%2Bwr0jsN67v1OkS93xDeqEhofrtZuOKVFQJqcbBZZrq%2FaOHRotNtB&X-Amz-Signature=519c4379339b9ef051d7c09f6e3211321570c1c465b08e397254b6cbc7eff231&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

