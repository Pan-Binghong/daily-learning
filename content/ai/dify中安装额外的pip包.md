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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ORNGTNV%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T030727Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRhY3LhXktVRnyTALLkQXs42AdR0PJrLGbo4WvSi5YAAIhAMjFgeBKc%2FCb8epZJ42aqUsrA3qoJevZiWBqFzOqjPIYKv8DCEwQABoMNjM3NDIzMTgzODA1IgyYERnTK2T4ObKRpNwq3AMlMAqXyBsvUoKzTaYJ2%2BDaaLn4k%2BtVHcev5ZXzPTOFFkVb7EXbZWoN6JOSPQ0dUnmNtiMqWtSoeZIuCjZIvNiYQYqdlmN9PsDG0x0D4XtEUlU3mSgHFfUnbmbtrWuFbKNbfHDwnCEVXq2CWpGJvUj7FgepkwLethSmRNKGGYEZzhSb%2BlmZmk9Fltuc5IB90lZcQLpJ6TN8uM2GLZVN8RkDtN3zYpHcvzS45f1OwY6l3j2ThPmaGevdyleml%2BVexfY2ZBGySrPGkiKYyb9wSeWtuSsJxpEpRaAcqWNLlbyGEx3r7iUTAbfsTYfMysNOtEY2u1tI%2B5Du%2F9Wqkhl8OfQhgwXMX2o8A%2BOmqjdBO2NhvZU5dj%2B4trU8WgaoTT1Ov%2FRiLOY698agZsB3ACBhrLg86Rv8pldijpc4XvEc3TUKdjBXibOJlmUPqBakwwnZzOWFfm5UFxY4OAbzGf4jFjfAF6ebTy%2FD2hA4Qfd0nB0se86Sf2Q0AxTp0wEc3nw9IoWAHZ%2FbQcK%2FUzkW5ruERqwmKvh400k2kzPWBLW2k5qNKjUyEC0AQ6%2Bgwg%2B3suHBIODpWaVXQ39RDs4oQX7yyL1v0k%2F5Yu6T2YAJoTEbmpqHmb2BGABHRMcGTOPA2jCI0%2BDLBjqkAX0FkIqfIUiqwvYqspXUfJkRoHYO2CzujJpfffV4BFYA89hrTSDd772vE1ePpCjUV0fEJWJ43NFo8n585JeKP5KX5hClc32QuXt2HEbUHBR3CIqfbVQb2vqsu0C49lFXp0gMoXdgXtdmudxHbxl%2BArcn8pHXLMOEzL9NzmdY5lbmlec%2BzON4l3ZAffOouPf6iDZ%2BoT5wi3s7%2Fin0lkbl1iZSCYfI&X-Amz-Signature=bbd977ab1cd9aa2017892a39e36c75dd1b60af5285f7be2d4c276403b03eb9c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

