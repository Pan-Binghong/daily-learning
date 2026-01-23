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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RE3PXHCN%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCMX1rXZvaABlFbf2%2FM3ap0CKOu6hQCuNvcOah%2F90%2BzLwIgFj2TdIbtjxhaW2Fm62VZbxAWlDHXl2SAVFkVLPwaJLcqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBIsIKgrReA6w%2FIDgSrcAzbdVrar33jaZjXYy0lAna14ghmrbTDax%2B7AJPxcIZ0LnI3k%2B1hDsVAMox0LqpuBYq%2F%2BBp%2FUkFWR0btGhsub3jtDjPolEF6FPARXWOs4cEwTSo2b9CPwybzp9Qtj49iOeH%2BIN%2BeUk44R2Jv0uBEuxUAagT0XgtO0xhMwRryBTc%2BAoPDTiQHuuFl00y4tKpX2RAoblnvLdyF6YZa6OMZIOn%2FBwhK%2BnZvdg5jPCoZkwG32Dxo9ypwZZ9dultqQxJYIghFvT0XjIDMxto%2BQjblmunZCil2PtVupOspyzsgjNVE3H5GlexzcOexEtJqsyZlqNX3nNlGTIokwA1eUzB0%2BHM1ULJBDdMZl15eML6fSOmwaJIZ2aguUeWg5IwgjEPAAr9yfkjFYtCb%2Be5o84BHwW9vdmytHeXhhKkng7MDglw3ZEp1i3XB9CD4GEmVCo0fhCzD8nc%2BwTXbRFT1YR0Z1FWnUue6TdkKel74heNnp5ZjuEWrO9pN8GkV7kZKp44Fbf4hHGPwD9J%2FsOfXqREC4oghP1V4n%2FpFOTNXFHUrLBCCcjuPGTgCwKID6jRwmhNFI%2BQXT8wmsu30GoH7fxgFEyvr%2FHEH7RqvQmcUizJHBG88cA9%2Bt7TX7l2fPO%2BmWMIWvy8sGOqUBlo1sHcYXsSNCKxQnx0MkoyImub%2F36fsxMW3tRSe75uAhOQh3ZvFUH4EZlV7gHWMaMlHhcXlgfmjWJaFagX5Y3IIMR%2BJdxwQtSdMHAqSOqBBmfwkGfWQe%2FoOMnU5RqrsL9QnBjFUGF%2F%2F51gwyrRWP0PMAorIQP1T6vamOkAZB3ZtXIDMJ40n69biUJxOpuXUuV%2FyPIUUgMFgbKOJ2uF%2FsXzo5axwQ&X-Amz-Signature=79d27b9d401545423e0b0ac2156de9921439a9d43b732513c3ca16d823f28236&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

