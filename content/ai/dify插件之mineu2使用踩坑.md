---
title: Dify插件之MineU2使用踩坑
date: '2025-08-19T05:24:00.000Z'
lastmod: '2025-08-19T05:34:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 MineU 2在Dify插件中使用过程中的踩坑记录。

---

### 1. 安装

https://marketplace.dify.ai/plugins/langgenius/mineru?source=http%253A%252F%252F172.16.0.138%253A9001&language=zh-Hans&theme=light

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2VG5ZLP%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCwUPlHNlVV7R6ArEu5Pb9upZVM%2BMWv7Kluo1CQvLCvfwIgRplu5q36Q9fyGONrlqqlHHR0RE%2Fj3DzWGk2V2lPZyV0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDNspVSy%2FAaQqa3tUtCrcA8G0dDQEsOvXLWQRK0DxXDeRxCwajYHPEirXY3gwswIHuHe8Yqh8t7rAstgoZPh6ioOERT%2BVij741CYbVtK3SOJ9JOayEQQNL6nQFlf79zLlKZbkKoMrXCmeHZz2NVKIa4gmmW%2BOoFXviTtN6XyEYQ7XPAk9bWsgA1O0iVZbrkIhol4LeSFNKQtndl44gx9V3XtB0C2W0uTSyQjDuZehFbPzVkYIF9U3najdoivA7SXelpwqYUqHNjRwbq%2B8bLx5Ixh5%2BP1zttmY1ewp4r0JDyPzGeHbj8Wffo0GfU%2FjGUVU15nglDxvirktqxTBthy2SyeoXNI2hZU0XvOlVuy65pwyJ7nE8llaZdI0ZkHwQDwBfFbALosJSFJyD%2F6vvsZ8qPjbR7TrlKzAW3DaGmpENYgoeG8jTvYzQb8UZWfekEd859KU6gi6hiaxfBAOqD0qY%2FeP09mFFaiUmOowChdHQtaK20j3WCLi58Sayi4L9BZfHkMjKUwBJJnEAXBlZh9HscBXJLi9DUfaJ07euoV7e7k8LuWB20obFcW5wsNJkx2kt9snuZLHldkw0JDFi0xdKs5%2F4Cl1hFzOkrU0rhCGMlgAgKZeu9E6jdinh84%2BrYf%2BvMjMsPl2cmDh1y1qMOToiswGOqUBy7ucwgOPLedeESAfo4US7gJy1VBHjZkPDhO5SwGvxuSkI3f7TTz3ElZDAwPGrKfhGskde283HoYBepaZN77JXyPo%2FgOEjW9E5d%2FvDZ5wb0lnlp%2BbcqaDGO0fgRnVpY3PaEJv1LyAvg0DgsinGTPHAJgJWahgxuiTENY5duVHA%2BRHdkRrvtY3%2BsmSTgMbhDEgqjvVVdKjzyhtqW9pSRaI91fIBnlZ&X-Amz-Signature=d23f7cc94ca5d0787e5836be78b3258c123a1e1c15c2a6ea309f848d2cbb81a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2VG5ZLP%2F20260204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260204T033330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCIQCwUPlHNlVV7R6ArEu5Pb9upZVM%2BMWv7Kluo1CQvLCvfwIgRplu5q36Q9fyGONrlqqlHHR0RE%2Fj3DzWGk2V2lPZyV0q%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDNspVSy%2FAaQqa3tUtCrcA8G0dDQEsOvXLWQRK0DxXDeRxCwajYHPEirXY3gwswIHuHe8Yqh8t7rAstgoZPh6ioOERT%2BVij741CYbVtK3SOJ9JOayEQQNL6nQFlf79zLlKZbkKoMrXCmeHZz2NVKIa4gmmW%2BOoFXviTtN6XyEYQ7XPAk9bWsgA1O0iVZbrkIhol4LeSFNKQtndl44gx9V3XtB0C2W0uTSyQjDuZehFbPzVkYIF9U3najdoivA7SXelpwqYUqHNjRwbq%2B8bLx5Ixh5%2BP1zttmY1ewp4r0JDyPzGeHbj8Wffo0GfU%2FjGUVU15nglDxvirktqxTBthy2SyeoXNI2hZU0XvOlVuy65pwyJ7nE8llaZdI0ZkHwQDwBfFbALosJSFJyD%2F6vvsZ8qPjbR7TrlKzAW3DaGmpENYgoeG8jTvYzQb8UZWfekEd859KU6gi6hiaxfBAOqD0qY%2FeP09mFFaiUmOowChdHQtaK20j3WCLi58Sayi4L9BZfHkMjKUwBJJnEAXBlZh9HscBXJLi9DUfaJ07euoV7e7k8LuWB20obFcW5wsNJkx2kt9snuZLHldkw0JDFi0xdKs5%2F4Cl1hFzOkrU0rhCGMlgAgKZeu9E6jdinh84%2BrYf%2BvMjMsPl2cmDh1y1qMOToiswGOqUBy7ucwgOPLedeESAfo4US7gJy1VBHjZkPDhO5SwGvxuSkI3f7TTz3ElZDAwPGrKfhGskde283HoYBepaZN77JXyPo%2FgOEjW9E5d%2FvDZ5wb0lnlp%2BbcqaDGO0fgRnVpY3PaEJv1LyAvg0DgsinGTPHAJgJWahgxuiTENY5duVHA%2BRHdkRrvtY3%2BsmSTgMbhDEgqjvVVdKjzyhtqW9pSRaI91fIBnlZ&X-Amz-Signature=2c66efcf5c13ebfa67f807083c660021279bc2e67e224d242b24bc63a6f41000&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



