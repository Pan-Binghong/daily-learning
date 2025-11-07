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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WYRDTGC%2F20251107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251107T024308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDz4p5dkXGS1calWOs9z4IELKcqLRz5Kd5gNpyPFW%2FE3gIhAJXbluBRXxLlCANyL0rjmquCRPEoCmLr0fZ6abYYHLQ%2BKogECLT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdNjV%2Bp%2FXjX%2BQn6bEq3AOv3ThcHMD1yPdmPEFxPMElX3jmIiBPUj3PXNHy1E9o%2B0SsNhWK8spWIxtpD3YD2%2FTsdC2cCnwaGwEd3jp88qVxXMieLgH9Ev8UvpaPIOnb0x5K9rr7gdY8I0BGURNkUK8nnEN%2Fwmul1smmIMn6FbCCY0G5a8qPTM4R807S4Quqh%2Biw5PhYGUld%2BDP79CcLGD6MGAUZRIv3z8EciTaVa6jsF7FPZTuesyLhfKJiVA07I3Z9lttkm1gucXHU2tAgIfVYB6regJ5TXHgBGTiAyEax0q0iHNipxpIKs81WvuoTzpc9XSjFdMmUa1bfiA3XIY%2BdOJDbgThicB1BNO4Pxf0vhqvzvBlewjBkIR9o3tXT5wVDYtFJbmPdDm5%2BQoz67tA27oEtuUbkURMF%2BeNYSaZGUXtKQIrBCvGlIam8k4e1Pc8kn1IQyO42etkfVJ8Y0KB3NSiNXGm%2B8lb56f2ZuiVbVsY3xq6eEPU51CiLGGlQWo%2FCgpPVXBVXQd2TwGiayrm4buCa0tY5eSkX27kgLeACXP8bDWpitGy%2Bi8AHsEwXObFE7%2BbYkqg58BVLmoz%2BBOnqQPn2%2BciQTOUWVsMYg9w%2FR13zAHBjwb2ht%2BW9xrMD7Mp1FyMF71iNq%2Fk3mTCGtbXIBjqkAV348BNCi97F6v8ZkXnhJXNybH9H%2BfhnuBMGnQ%2BAF0ttkgwdVOJkgcoDH2qBYMMM4rNCUmLwR1koUKcqZAzSPXQPnozYkc1ebdPz40%2B8dg8s01XCeuyIaJLPF8kk4tXGCUswwun096pWWEEXZDILUvY%2B7kT3ao4wJlWmlkeBVvbH6k0Zfo13YqqEx65dUOBy4NlLQNA5HHtOHu7sFib3lB7HuMaB&X-Amz-Signature=a4cb77a48b7361c2ec42249f13bd386e714a58d2586d150ff2f3579e451f4af7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

