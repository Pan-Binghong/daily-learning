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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF35CNNY%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCOk%2FjauERKdqPCbhGBmp72hCzxidcQrdX56uO2O03YEAIhAJPumfOSyUgwu%2B0QTTIv6msqCtqbl6NF5Wt9GG5e0nHJKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFmPdNQhUv54uVi1Yq3AM2luaIQ9%2BPut1lbC7OSqIff1TOsIdh77OJQAhTw1mFY2SP6atxxoysCdcD7bkaPzf2xmKeY%2FYatQpbVYWgusGA4%2FrqotOxH1kWjrCj74OTB3yT9Dtvz7I3t3fG8i0CMxiwsgHNxwERgpQ0pxB5uq84qKWiQY80qJnrVhuG8M2%2F1Kw7fmPcWx5bk6DJ9s5sbTdmb48lsGG67jEkC7HiVl5zYV1779o1TkGSDI%2FaU1E6DLYEsRxEb3VuWPyP7OcKRoUlt09Nt%2BWmg5oXOIYOXoIsMb0s8uzkEuh6cQH5VgRumzzHxXlXVgpzZ2gnKEQNFgihxuQfd0HJUJXz5KL%2FbFu8eSnDrbpNHkkxNo1AoeQrIU67hJYVbVKMPqfAIsUC8D7WmNb8noU6DWa54X8pQaVZ3lKoOWl%2FQTvFojeoyVIjbg8orAM4bvSyUTp41TX0WCpboIGZhWoH6yKQJL2n06O77ECCrI7Mogimrg%2BRQXgNLLdtCa%2Bzp5Vx4m7cVaMVoOte60281yfAWlrRgd9T9uGb%2FJrBawc%2F9UROyCn%2FaGLXLmvxLj4buCdbZKN8O7pnMZ453MJW1DD8PP37MLMwhsDE3PQkILIsLmlWWkGhZMAn62xEeXWbI%2BKUGPVxizCev%2BPJBjqkAedW1Os3z%2FXdMFsG2XXH4bLKuKFpF7zDmERQI%2Bcr0NlCbusEAiS%2BGCy54lTXOVO4P6rOl%2BfY5XFxOV%2FF0OWHCboCkyja7sW04Ndul1YOWt9hBG7%2BukvDKuWqooGFolAFbSvZsltVdigzJJVTrdx8JklNT42UnaQ9srgewJD5pTzMZDOPGhG2Bf3Dwa0ORLaBgNePmoiTmKA1nkD8bsvmd%2FYvE1Xf&X-Amz-Signature=4cf11300da2e94b99fe6a1410efa46d2b02f67a0fe299fec9120c2f4d4d586c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF35CNNY%2F20251210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251210T025318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCOk%2FjauERKdqPCbhGBmp72hCzxidcQrdX56uO2O03YEAIhAJPumfOSyUgwu%2B0QTTIv6msqCtqbl6NF5Wt9GG5e0nHJKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFmPdNQhUv54uVi1Yq3AM2luaIQ9%2BPut1lbC7OSqIff1TOsIdh77OJQAhTw1mFY2SP6atxxoysCdcD7bkaPzf2xmKeY%2FYatQpbVYWgusGA4%2FrqotOxH1kWjrCj74OTB3yT9Dtvz7I3t3fG8i0CMxiwsgHNxwERgpQ0pxB5uq84qKWiQY80qJnrVhuG8M2%2F1Kw7fmPcWx5bk6DJ9s5sbTdmb48lsGG67jEkC7HiVl5zYV1779o1TkGSDI%2FaU1E6DLYEsRxEb3VuWPyP7OcKRoUlt09Nt%2BWmg5oXOIYOXoIsMb0s8uzkEuh6cQH5VgRumzzHxXlXVgpzZ2gnKEQNFgihxuQfd0HJUJXz5KL%2FbFu8eSnDrbpNHkkxNo1AoeQrIU67hJYVbVKMPqfAIsUC8D7WmNb8noU6DWa54X8pQaVZ3lKoOWl%2FQTvFojeoyVIjbg8orAM4bvSyUTp41TX0WCpboIGZhWoH6yKQJL2n06O77ECCrI7Mogimrg%2BRQXgNLLdtCa%2Bzp5Vx4m7cVaMVoOte60281yfAWlrRgd9T9uGb%2FJrBawc%2F9UROyCn%2FaGLXLmvxLj4buCdbZKN8O7pnMZ453MJW1DD8PP37MLMwhsDE3PQkILIsLmlWWkGhZMAn62xEeXWbI%2BKUGPVxizCev%2BPJBjqkAedW1Os3z%2FXdMFsG2XXH4bLKuKFpF7zDmERQI%2Bcr0NlCbusEAiS%2BGCy54lTXOVO4P6rOl%2BfY5XFxOV%2FF0OWHCboCkyja7sW04Ndul1YOWt9hBG7%2BukvDKuWqooGFolAFbSvZsltVdigzJJVTrdx8JklNT42UnaQ9srgewJD5pTzMZDOPGhG2Bf3Dwa0ORLaBgNePmoiTmKA1nkD8bsvmd%2FYvE1Xf&X-Amz-Signature=fadb662116558885d7732e61f4683f1c99c83f5843dd865f7e6d8912a9a4cd9f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



