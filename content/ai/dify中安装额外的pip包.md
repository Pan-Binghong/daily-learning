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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y52HH32S%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020902Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIC6Kzic%2B7yDQnJiMIknZ9ZegogXgaFYEvknHtM1sdG3xAiAEIvapmS191dV2zzJN7BJFZ417ZurQmwY7Ky5B2XOAEyqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAlqyxdMapwYejMUcKtwDIt%2FPNGwU81ZFGz2JI13SmtPwJN4y3xFNrXJsVUMZar1AlkL6ya73teNMg8PzZPfO25YNVGSPKQTiFkxbzKQQUKht468jjJQ3jJG%2B8ZePnF4vfGDIEzwsa79H50K3juDuKuWE88b69gaFWN%2Fk3OKs%2BDihWRAEoWE7N%2B2PMoh1pMII7rLDr1pu5J43bNI3AkumB1%2BHnO1poPJmSlN256kwe5rS1WOdawsRb8xE8QUaa5NeuA7YLdUmDka1pJli%2B%2FO3BTBpbQ2PA%2BtXSS6AN25wwdOJQbqKu6suJ7AwrnA5VVocLa8hvzsQqfaSvhzH6UVZilmPq8%2BSPbffAuTIlDsL4zTvOmcmODPqLWhYSJ4h7Ics9XTJY1VBbtz08fPjniJv1OrcrL9nfsfZRVf0Wi0jSkBqK74JLzo%2Fe%2Fmlik9tzyDh4mVmRCbK5W3Rv%2Bg9MKxl3%2BSJesJDFLkB%2FECVpuC%2BFyzQ1Y5MTef4EZZbdTfponOkR7OVCTcI%2BMpmwS5tDfX3uE8N21s5V2%2FD1%2B4rQII6I5C%2BS3mtE6duQU1s9HR3XKBdnpUGvGxV2vf%2BW%2FOBVA%2BMxiBZT%2FYrX0ZQvr69AOcZUPlfQBWH4X4zybBT2tPWslY0IWydqqoLG4OjtEsw4vGvyAY6pgGPzxfXzEgzQ5PtsWDktvnbtSaZ24f3n%2BjhthYpR75x%2F9v9VDBiJAVEpOLHZeeBERDT4DZEycQptwyYWY1lwdP5aVw8fkG3%2BMY7k0JQxqotMxZNS19iKyoQXa5GgiapvWkq%2FRuWqi0nMaL2ijIwkjh%2B0l2rpus%2FBBEs6WWNyA88blWs0I3o71EA%2B%2BUIhRRZKWuOUxFp%2BsmyPah%2FuAQdB1lCkHEqnsyT&X-Amz-Signature=3e04d4b7138e0a8138f831b6fa03595e0621039376b6666bbddbdfb297b3841e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

