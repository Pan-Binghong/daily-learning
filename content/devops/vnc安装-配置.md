---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMHKWBVV%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDqDGMsZYykGQIKYpU1vxuR%2BveOEQomcsfh4%2FDWjEEG2AIhAONoT3OBupDKdnxqlR6Ezh46MX0%2B39vNKE5wC%2BZGCgu6KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyui80XcJoXUnneLQgq3AO9HHnzbCwUNGsNRIqZGFjSvzcXXzopSuqn0Sb7Kutfq44%2B2FBuqXerTTs8dLloTM8nT7v%2FaaF6qAj37E2w9XnJm%2BR%2Bg1kimQTC51pxefwaenT1uGLxlOcNCtIL%2BlHggbqCw2NOb54gKSRQHQ5D%2F4npNV5K1tiDCMQjz89FyZH3qpY1RvTcfKuoduFAaOWMsN%2BT79YJch6QF8Djj4ZFvKujlmKlgjYqr57GsyF%2F%2FZaGfLlmeEJIo1CHZdHt%2B7E0pLiirpzEfICyBhxBNvFj74YN6NMR4hBDWBIIWEhDYPQWGgZSDO28TYzBWwaciwnciNJKmRxybxsJquGH5WODAXcEvczZzR8jRvtBWzIJxUSkBxQzn19gkirFzg4FnPaWFHyZX37UCqpf%2BPjqjklpVSXDApxsKFMuAMsRHG0Zxr5Ga6Mf2lQmsLHrHDdyQBV18P8%2FBLeH2AJrqUS%2FRUj9W08N7oAleMGu0b7U8lKmJfSzY83IDlUrlz6vuE2HxWXHv0G2JBy0wsCV2j3mYjsKkeJNXjYa8gfala%2BPP7f0lHtvlAYEV2lEDAiaQ3h77Cu7DIGYkCVqUl6M253d874ULr4zKkxWedPtw0N%2BaRRyZDAXuZVD0RD2gMMbIqPDJTDB0LrIBjqkAciVoxLCBEMgRybbSe5K83n5hx3xAlMBW8hm%2BWvamSer0f%2FBItMcEDj60LR1ruA%2BejORbrIaT%2FjbB7CQLgj1hxS5xYsQZyGiuSNU6Wj68x8CbPtDWlcbbPXNzFeDhy01cUfZebE%2FxrCT14Da54UJ3X%2F3NZLGVOCSi37e0SM%2Bz7NxY7TtZh6qSgtM8UNbG%2BLJvZLoDYGCoSFM8%2BMbqlMLDCVZ6VVU&X-Amz-Signature=a0d339e39ed968c04361da041c2572b8a5ea033dae5b7d29afdea2c07347a9b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMHKWBVV%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDqDGMsZYykGQIKYpU1vxuR%2BveOEQomcsfh4%2FDWjEEG2AIhAONoT3OBupDKdnxqlR6Ezh46MX0%2B39vNKE5wC%2BZGCgu6KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyui80XcJoXUnneLQgq3AO9HHnzbCwUNGsNRIqZGFjSvzcXXzopSuqn0Sb7Kutfq44%2B2FBuqXerTTs8dLloTM8nT7v%2FaaF6qAj37E2w9XnJm%2BR%2Bg1kimQTC51pxefwaenT1uGLxlOcNCtIL%2BlHggbqCw2NOb54gKSRQHQ5D%2F4npNV5K1tiDCMQjz89FyZH3qpY1RvTcfKuoduFAaOWMsN%2BT79YJch6QF8Djj4ZFvKujlmKlgjYqr57GsyF%2F%2FZaGfLlmeEJIo1CHZdHt%2B7E0pLiirpzEfICyBhxBNvFj74YN6NMR4hBDWBIIWEhDYPQWGgZSDO28TYzBWwaciwnciNJKmRxybxsJquGH5WODAXcEvczZzR8jRvtBWzIJxUSkBxQzn19gkirFzg4FnPaWFHyZX37UCqpf%2BPjqjklpVSXDApxsKFMuAMsRHG0Zxr5Ga6Mf2lQmsLHrHDdyQBV18P8%2FBLeH2AJrqUS%2FRUj9W08N7oAleMGu0b7U8lKmJfSzY83IDlUrlz6vuE2HxWXHv0G2JBy0wsCV2j3mYjsKkeJNXjYa8gfala%2BPP7f0lHtvlAYEV2lEDAiaQ3h77Cu7DIGYkCVqUl6M253d874ULr4zKkxWedPtw0N%2BaRRyZDAXuZVD0RD2gMMbIqPDJTDB0LrIBjqkAciVoxLCBEMgRybbSe5K83n5hx3xAlMBW8hm%2BWvamSer0f%2FBItMcEDj60LR1ruA%2BejORbrIaT%2FjbB7CQLgj1hxS5xYsQZyGiuSNU6Wj68x8CbPtDWlcbbPXNzFeDhy01cUfZebE%2FxrCT14Da54UJ3X%2F3NZLGVOCSi37e0SM%2Bz7NxY7TtZh6qSgtM8UNbG%2BLJvZLoDYGCoSFM8%2BMbqlMLDCVZ6VVU&X-Amz-Signature=b961d4b7f8c669a18a4087c8d618ad6ace71aa8d49a9fa30730fc155c6c3cf19&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

