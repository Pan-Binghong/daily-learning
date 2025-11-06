---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662O5BEZDB%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICgpBztip5mWUqguUAzTYsH%2FFGEUrg1YNLCmfd%2FI%2F2PYAiEA1lnOgSYKD4v%2BD1jokF5VLlgF%2F5VeAAxl2pKrZe9N2C8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCbQud0CJvTOlyvJZCrcA2eL4ho5IZLGewRNLqt6UhtwLsYMQ9d1UhW%2BCH0YNwuK%2F04Jk0G0GbvrHtWILRAvO8R4PkXw3cC9rvp6JhUMPILJ%2FQ%2BYwo4ZzpPLJD4u%2BIRnPQ3j2%2F1CHbyJ6OKsD471xNPvxBJZq%2BIMXfbwASKE8WnM6JtwtT7sgYh1nzlHHGbiOmcQRw7Pu8Jf6Ry5oFjFfhhG6a5juccJNjB8dqDUEWylo2X8PS2UoeiDm39PsmyN9hOwVGsXXghrKueC7e2o9d3VrB1aaWDf29p3XDZXnm4OfK6%2BtJibdSG72njiZxTDvHDEvZetnvG7YljevME%2FhRs8ZTg5scWaL%2BpG%2FQ037UVs%2F1d%2Bzz3lPczgs3ysuty%2BCh4ydqn3MpBJBJG2o63v7TWD0gj55BBwnnNhZWSg%2FO7Uk5H1R7Cj%2FmBIcSxHZtvX1am9gbEJHPoSaXz%2F95xJfrhRyVkKuxDR%2FT7amgOWl3imn1UoNVQ5oJEM9dKRQUiQHyWNSuSgSWQiODqvEQCWpY9xPJVinNZKRITXlGYAk0CyXJpmFY5faTiJjcIFpuJBJdJyqYDwhgVgd%2FslhA2srUv%2Bm4DorhyUQJ2abkwg4Vyjt0tnz7A6CjRFwVUojxUkAlSSQ%2BfPPog8UjpPMKryr8gGOqUBhxjdGnwPNFeFzouOsQ%2B4VCfWteeO7%2BY%2B25kCVYOSYUg3JXGx9nfi8McvJdf4kAt0jkEGpFPSgdUHhc4LKUeIX3tEcBxB6%2Bb3faW2iZO7H5e3ikLSS19bNA%2BLzeMq1R%2FLk2CAEwX9aIO8jY3jHXscXglSP5sc7RGpUreR8vn7LIYB4A2c%2F9d7abrzUe3CfIewtRLW81ZhaHWPl9xdnr2J%2FMm4igsc&X-Amz-Signature=2ca0bcf41a4f2cc9ed99655f1719f8271bdcc8f155d461f84649c0db7dcfd0e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

