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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXPHQK75%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T034411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQDlQ5o3AqDw9%2FPSF9HHSR8xoGAIk7shR4%2Bjs3aat3jfaAIgVfJxL4RnUh5k3Cm2lx8R7AixdDZQDqfRQdyox%2Bi0vLMq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGj05glUgZvvaRmnlyrcA37atgaFvhGY48iVppr9AQA2TrgnvmOWEq%2FVpyu%2BN2G7i5sD40nagpdWu2TXjlZZruXzyzj31leT4oyQo2V5gHzWVExFmIWtwpv%2FBOXRI6wMtQYE3KjTKravDoow08Srwi7XyDiJtd4PnTu9QKpZXxp8zkP9VPADb4ujHYJ2NAYHVGqaGbabbx0sdlCuztM%2BZwbB12Y23MzLI1mt2nStQe23aH4j6lrZA%2BBlIP3khyDiUE55n2yvqw6bc%2BMzq54fKLrIS6eRaZM17EzMqveTm13SK1r7erCiWHI0i89RWe2aZQ6WLtGe0syoJEjM5guSncmwiupWekx40BNskTpfJGIf2V9m4ESk%2FE6bRDMxYYTZ6P51GyK3TJ80IHOASTBMWMNdoFzFf6GxnmCEPx1yheY1tcoW%2F6iVuSaM7K9f3L3xU00ZA%2BatlLN0kV05aGPqiApRx7XW6jhe9VfeBzvyeX8vIRu19EYoX2gcO3qXnetPqBsPHyDrcnhOElUjiLHlTAxTnNGY7blo1g6gGKyWGMZTXWAP3%2Ba4IB031TKGcwrB1%2BgAI50%2FclpjO8cqZwSnU4P6DbtalTUfK0kls4wvK7Zc%2BsRPvVP6Ykw3CPTGy5b1pYB3acjuOWWypwDCMOmdxMwGOqUB4jpaw4vfRGOr5linUYBh%2FKMYVYjIrFW0uWzwQsY%2FINMsEhifvWRYdkFq6vZLnjp8zRSCJ4735P3FOoNYsqDJJ7BdS4baLYB%2FpxZX8DVT6bcX5h7c8TZQMBna4et%2Fn7jRJ%2F5r95Te%2BrOkFkqzl2lTsWpkPaHHDK5BjSaxhvdkmV5xuL6hCHHn%2FSiKlm41Xj0ALN5OlVBUL7JWIJyzCaCrvVcWDMh7&X-Amz-Signature=e5c0658aa1bcc18b82f40a9cb416da4283b5ec881d591276ba48430bc2d95450&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

