---
title: 多模态大模型_mPLUG-Owl_部署
date: '2024-11-22T01:44:00.000Z'
lastmod: '2024-11-29T12:33:00.000Z'
draft: false
tags:
- LLMs
- mPLUG-Owl
categories:
- AI
---

> 💡 支持视频以及图片推理的多模态大模型mPLUG-Owl。 记录安装，推理的所有操作过程。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/cd01d11c-96a2-4d07-82d2-51ad7aca879f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR3REEYC%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxC1hFitjCsl9kN6NXHoZctoY7p21l%2FyydryNxDrKXEQIhAII2In6UDINg6T1AFyIJ5LSWzWWKbunC5sOlXXblKQvAKv8DCH8QABoMNjM3NDIzMTgzODA1IgzuwHIfQ40drcEzMnIq3ANPCdAid%2BfsztBDbYsVwN%2BUhYCvTjwpGaRCQ3XROQKuzN%2Bdrr9SOECON45NxPk49xHiboQYwin%2BhI1yNAYgSvGu6nGtp%2FOKwH6ofV%2FAHhGc%2BvODPNicOSLLOEXmcbVo7C76inXs1e2OvwuVwvIs%2Bm4xLJ3YTpvTgY7KvFt8QfvxcSnPHenlZ43xtW8FTqsa%2BDe7mbyk0IwC7gZHWTLQkOY3d%2BlaKFlrT%2FuWw%2B89oqa5sn%2BniQNAQQmjTvxwvgjibbAQ87csEUrXq6CH3rkez%2Bi47Fouc2bZB8VIRXAAAqe7wDI0bgGhIEq1fRqURWUSb6yDvhiNZAyJqoi0rsxjUsX2d30O6%2BUewasX%2FThVYUv9ErjEOqbL72ofYtsYGOp24Y5rxFCHJK2M5HcKPcIh0EFX7aqnQEhIZeIMw3v0%2F8eyzObmh668Pvs5TawYgcFEq00Z3ci38QQqfqUCne6oj%2BbJFgzVkq9nb2nsNLALLgVMXe54Ch3M0Zv6piJooPI%2BBChSGjZW2K74A%2Fl7XACrQszGulD%2FROIHhJwZas7axAyrIaRspQZQE23eT7WniMRhGKU2YMBMKtcJd98p15eFoRqOIY02atKGGaD3CAOJJopVfbhTXCW6dGLInKcQjDDfrr3OBjqkAdDyHjyOgEHrvHaOPR2yiTFOYlvuVSBZcUJ%2FPJyzO9e%2FvBOoNr7BJCebUctwsJ8kLG9RyaJNSs8h8EAb3pM023hXyxYgAuMnicxfne%2FaIzZfEarddkfgKOOwraGWWDo3JJLDi2gl23q6duCmRk0h8az0O674MtkGFF%2Fg%2FrK9DuZAD%2BK5BLATz6o1iAJfJRxXfux8mHy3bEGXjbBOchnFfw1IXkhQ&X-Amz-Signature=244452c154dcae3af64347653afb670765bea1702b03d300576a2b0ce803916a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 环境配置

- Anaconda安装
- 创建新环境
- 下载代码仓库
- 安装依赖包
- 额外安装
---

## 模型下载

mPLUG-Owl3有2个版本（2B、7B），为了更快的体验，本次实验选用2B参数版本的模型。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/6bb075b3-ef32-477c-a6b1-f0cc80c6f8b3/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YR3REEYC%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxC1hFitjCsl9kN6NXHoZctoY7p21l%2FyydryNxDrKXEQIhAII2In6UDINg6T1AFyIJ5LSWzWWKbunC5sOlXXblKQvAKv8DCH8QABoMNjM3NDIzMTgzODA1IgzuwHIfQ40drcEzMnIq3ANPCdAid%2BfsztBDbYsVwN%2BUhYCvTjwpGaRCQ3XROQKuzN%2Bdrr9SOECON45NxPk49xHiboQYwin%2BhI1yNAYgSvGu6nGtp%2FOKwH6ofV%2FAHhGc%2BvODPNicOSLLOEXmcbVo7C76inXs1e2OvwuVwvIs%2Bm4xLJ3YTpvTgY7KvFt8QfvxcSnPHenlZ43xtW8FTqsa%2BDe7mbyk0IwC7gZHWTLQkOY3d%2BlaKFlrT%2FuWw%2B89oqa5sn%2BniQNAQQmjTvxwvgjibbAQ87csEUrXq6CH3rkez%2Bi47Fouc2bZB8VIRXAAAqe7wDI0bgGhIEq1fRqURWUSb6yDvhiNZAyJqoi0rsxjUsX2d30O6%2BUewasX%2FThVYUv9ErjEOqbL72ofYtsYGOp24Y5rxFCHJK2M5HcKPcIh0EFX7aqnQEhIZeIMw3v0%2F8eyzObmh668Pvs5TawYgcFEq00Z3ci38QQqfqUCne6oj%2BbJFgzVkq9nb2nsNLALLgVMXe54Ch3M0Zv6piJooPI%2BBChSGjZW2K74A%2Fl7XACrQszGulD%2FROIHhJwZas7axAyrIaRspQZQE23eT7WniMRhGKU2YMBMKtcJd98p15eFoRqOIY02atKGGaD3CAOJJopVfbhTXCW6dGLInKcQjDDfrr3OBjqkAdDyHjyOgEHrvHaOPR2yiTFOYlvuVSBZcUJ%2FPJyzO9e%2FvBOoNr7BJCebUctwsJ8kLG9RyaJNSs8h8EAb3pM023hXyxYgAuMnicxfne%2FaIzZfEarddkfgKOOwraGWWDo3JJLDi2gl23q6duCmRk0h8az0O674MtkGFF%2Fg%2FrK9DuZAD%2BK5BLATz6o1iAJfJRxXfux8mHy3bEGXjbBOchnFfw1IXkhQ&X-Amz-Signature=af579db4ea047ff286a14af2864c9103eb16a232d33af3e28e42ba5ba1d2699c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 魔塔社区找到模型仓库地址
- 下载命令
- 查看
---

## 模型推理

- 参考官方README文档，创建推理demo.py
- py文件内写入推理代码
---

> References

