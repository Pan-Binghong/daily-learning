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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663FCXY3DE%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJGMEQCIFW2EgZuX87MA3LF03p9hRVlaCeD9OYy9yP5PCQjiWdWAiAfkV%2BigVRXMsHgEQ95gCBHn%2FmNjko5wHLod01qkzlkOir%2FAwgcEAAaDDYzNzQyMzE4MzgwNSIM4xTB3B2P7%2Ftw6cydKtwDNc5BgryhkirG9DCdpoOFtZx3K59rR%2BMk3fEnWFnsI3PN%2Brbo3WPfX2zcIT8cs%2B31z025phlUogi53F%2Bh0XU2VnfecGWdZ0nDczR9zRUiJVj1VuNfX9FpTRWl%2FSHNQh3zvHpgP7x3eVE8xqB1VmhFYCTCO3T28u5F6TOljjEMfzMuL1kJ1aGkaLkvtDf6CKgcFSeH98n0z09e0Y2wO14qPrpY0CSQXdi4AtkjueLYtav5zCHyhHbr48vc8xcKQsmbR%2BCV1Mm7BCYM9DPC2TO9FZoxRoM5%2ByEH8Tc6A1a2J2H1lNjSf%2F1NIemesW8nmCIGKfSCjqHojOWwzF4hCezYADe2mr4PDJS7caP%2BM8artKu9Q1drQ8D1vApxdsAIp%2FNBAhVDWAJbC7c0lu9UAXTp1pkTI%2FqNydErzyKTMUig0KULQDPy5Wp5%2FWjJe0hap4%2FmIXYix6b%2FSSXg985JYIuW3%2BbQAEBTo68e%2BcEABB4lwqcQHfcbBnAvRrmnP%2FLtRF0GUnt5hoHbaISME50f0X0v%2BsYF%2BVh%2FMmklLiJfLIl04vPa6Aq5YcxuUvqAmhNQtYDj%2BAVkkDyxAVk5TPDQkdGlg22wFMccKlWvyQnYGoyC%2BUKDq1O%2F9wmvE7UIbc8wr4XWywY6pgFcQdAsSooldN9mkvJ6clOx0kQY2DN%2B0s5b0myE63sGfA71zCbvbfhWsmgzGFcW8Dm5lORtvqFzDq5al4%2BqB2RDwLx28ewXpNCtI2u0Z1qr1a%2BfHCHLDjSETNurtsos1OGU8E6v1XuGatotsCBuZ%2BZeReUzXEzLg9xdEY7yIt1ILLaCyvMSyRpImKGhk3bjUg5aSMLz9Y3tdQUvBSz28f%2BD%2BRtkrBdi&X-Amz-Signature=17028fdba9e3164eb181fa450b747f96f3edcb2a9a4e10e88623cfb9e845a3a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

