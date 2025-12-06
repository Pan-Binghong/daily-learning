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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5DJQAYA%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHk5Rfmw%2FQZpdxqCUvofHyXUSm2cexPpjm%2F6JCsSfArzAiEAoXr1nMM1FEga%2FtcoiugzZ%2F2Vrx1RU2QOxd96TRwCzgsq%2FwMIaxAAGgw2Mzc0MjMxODM4MDUiDOTQqfxV%2B14KIfApwyrcA91zUUge%2Ft%2FfQKnJPQn06KXUrRqneT0iAbMco52VfIHvF4S2rYDM8sHiTUnQkh2Zlav93NkIBYsTAOwqvmcq6NsRG1sLgThJFyCRrOOXILRtALd0%2Fo4izKp%2BbUEwChBVRPWwWe11oecIlztgNtENGkY7chFWjhKawFfT%2BHGg80uEekrtXLYuzqQALQvm2tuJQUfwFHL7r%2BgOg%2FSIfmF3Gr%2FBfN2pvv4Rg8xEfMUYWLPq%2BzFiZ7Kw1jvxSCnbP4a5mlZbAVM47c0e4sTyt3MxR3l4DF5Vj95FG4qk1kcgGb1Tm37dnGrTqITn%2FnTP8LcBJYvn%2B8beYXnm0t8jFypPoMwwXRImrtWA7fQBvNtgpYI1PRFYIXlZbP%2FcKZujBSeVgSwDaAulPoUbDi9IFSWWbbK7mHNZio1%2Fys2VIttmZLUXh0EVQDjiBqysrdyMy7WfaHMvF8lBdZed0RNrrPqyp8xBixMTJS6FRxwkLAl7tvS6tBmnDd5girUEBSqWUGw8o3592LZkrlQyuN7%2FQ4S3mKq15Vh%2FfWNrsO17HIWtTiSQXp1eGLYHuOqXmtDvk3Pq3SBKM3FqBEWFxXCzRYrRWiApiS3nks%2F5hS0XrBCOJqUuMuGrK0v9Hk9TpQXHMJOnzskGOqUBmzz3XtEeP86jYOZhhhcrgKAfftyKECYlPRDFQWzl9C%2FIMSkczHSqHuZ9FHU6%2FyRXd8zPEs38D2AJ8A8Lw7yEphje3YrKBc68cJ02TwRlOl8A4IUe6UUBWhGuvoeIcwVde%2Bwxmtb4eiXmfKPmQ3mYBR4NAqEn0eNQKxfuQcFzw%2FsmxIXDla%2Bn3BcDUp08PjKtM2blx66%2FlwVH2fJ4kwygPAc4qOIa&X-Amz-Signature=298031daf52e060df86c71fe60d4e49baeea1dddc26a96a2cfa93545ecadae0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

