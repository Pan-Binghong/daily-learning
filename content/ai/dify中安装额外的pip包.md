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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6TATLZ%2F20260418%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260418T034934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCEqz26M7gKn0oMXxN8O3FA%2FQ%2Bff7pJ4YSCMfZzYOU%2FLQIhAMaHgwVkcFqbYZffNZhOqew%2Bm51ECBCQZmtIIsqEQN8bKogECOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwl%2FBod4L59009iVC0q3AO8pEYbJrSJ01iAl7fykbbJ3mhN3Xs79gKSvHebsSn8DYKVlJLVDaxIDJR9WwigVjcYrTjotMxZ25njbJLiZR0YRX4kMUkSUdRdhP9Cj%2FfGOd91SZ2MwdmAKb28U3Xd%2BgyfGsQpQWIH19JpzVxj%2BPI6sum9kII8a%2FxyS9R%2FjBoJ5xV4gYuvuL0BspFVaD6qvSDl0EekcBZWiOEO9l0PESY72MhnAhmdkIZh5v%2BAc8uj2olvbqdTyfQ2BL5faY0lhqg2a8yghM86dTPh71xNV6V3MH9UJ5f3zu7HNQ9dqe8o7WWsI9uqo8hEGTzTN5JbCvecsKDcUf%2FP2K7w3jrmE5XKR%2Ff62Tdhi52ZsYZsNl9c0lnd9QvvtEqc%2FMnFwHq2oQWA7a7DgfCxnhnz0lBaHmCVL5xApQsBp7MAdMoijQwXRFmZDI96cq45R%2F2bbI8c3O0Qi3me5UIs%2FobLvlEHJjN5GEHEyeF851TUrsevjGKfJHhOAmaI9enhGkLTxN%2BGmDEjrAnDv%2FjEik%2F6hL0sASlJd1%2BBhW6RQHiHrPi102yMpcDuPyLt2KutWTbEMDyG0LIWkZMp02yMipG1A6eCLD3%2F2Rge52zA9FB1boIp2i6iu0ZgcOFR5XhHOB2iazCSrIvPBjqkAUkXkE4zvE9Ikek%2BFFIBGm9IUOa8Kx7vsvo%2Bo%2FFT8s165Pa4pt41V2Kr11vjCoBxy3mYujJKHsoFU7TZg%2FI015Xbh5ra66YnSbxel9R6SHlVBcB4lFOEHAzCiBD4%2B0SpoUQbJ3Kkltbzsa%2BFgbhjXbLLgU6Je4VHFwVK1MF%2F7cmGKM1mva%2F3x4LZ2zEJ%2B%2BIYLME2ItWEfsexVo6ZfOGtUrZWBMW%2F&X-Amz-Signature=e44a534eb0715871b9d60550d581bc9709942a1c95b9f71465cf57f30f8908a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

