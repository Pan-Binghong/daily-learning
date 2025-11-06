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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMJEEZWM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAy8lYtQcbpIb67NniQHcJdj5edSRa16VW5OxzPn7XXxAiEApAChPk2URKxLw69xfAgeQMDsNDM4%2FaxAG2jQuUrBI8oqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH7ztj8r6FtDeY7NzSrcA2zjrpa%2BAv1%2B%2B0T8Ga6mvxNLDBC8rknof8Zq320uNTZ7ulcbqXdGn9h1%2FEZnFp4T28yxSKjetc2Tc6pifC3VI%2BfCfXgsbQQE9Ba6WQdE69qNn5Gm%2FNIY%2B5QB85S%2FRO29XbL%2BDw%2BwtUPwS9RNuHz%2BB9pawezjQ%2BHoSPoeGvwNYu7fPDGA2Atw53rDAZSBFnFulnWE0cGW0pzsDAgpnRVccNML6bU5UqajTvmRGOXdEuDE237EDMoNFvCErRbDdQ4YpoYmMhFSDtmcM8luK9oT%2BXxQAJ9LyBu%2FEPfmxDU3KGgpZ9HfTumsFWJUqgqImV3vq7efmRIM3AA3aICTacc1AKcKRPf25WT%2F9QFEoCWcC15vMfbWbnvdvPizxb4%2BQ3iRSvrbghB8ISRjYUYayXjerlDo3emzn%2BY68qKJ066oIkKDfSY7WgOqz6%2FagVxS99jUoOp3PKq7KXR2dtx9PV8yMGl0MK3jZFQIg0HvS9I3KLzOwwdKVmLFK9Km6CcVFLd8d%2F%2FMJSrUfXi1yOTphJ5HdlQHydV0QrGyEnY2Ttx1GjugV2CRvFzGoRqLWgZcenHkid6QGc0kRy8m63JOjoiCHXdLYzLt4zYnhqxzj62Ft7ubcb9TKM9ZzAD95u2XMMnxr8gGOqUBJJXqdRLdtRj2959DfHb6bohxYSOpRO0P29l9mzESivGACqgnVAkkoJ1uErHHunDl%2BNnNs1ri1QqKG22nne4lSWNL1ru2pc16w9lOhSNzyUMZ4fqGGXNDjieL6D%2F0zqK70HwbButKiwMYcjCQ2tT1IIGD8hQwMPrSFslLLBxpIwELjqLpC8p9mvQTa%2BVHo6c4nxm%2B4p2P5tcYcal%2Fr521sgwrniVU&X-Amz-Signature=7620e2451c10db539739bf66745b4aaf0c153194cca02b6a6ca32d1cbd334165&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMJEEZWM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T020904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAy8lYtQcbpIb67NniQHcJdj5edSRa16VW5OxzPn7XXxAiEApAChPk2URKxLw69xfAgeQMDsNDM4%2FaxAG2jQuUrBI8oqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH7ztj8r6FtDeY7NzSrcA2zjrpa%2BAv1%2B%2B0T8Ga6mvxNLDBC8rknof8Zq320uNTZ7ulcbqXdGn9h1%2FEZnFp4T28yxSKjetc2Tc6pifC3VI%2BfCfXgsbQQE9Ba6WQdE69qNn5Gm%2FNIY%2B5QB85S%2FRO29XbL%2BDw%2BwtUPwS9RNuHz%2BB9pawezjQ%2BHoSPoeGvwNYu7fPDGA2Atw53rDAZSBFnFulnWE0cGW0pzsDAgpnRVccNML6bU5UqajTvmRGOXdEuDE237EDMoNFvCErRbDdQ4YpoYmMhFSDtmcM8luK9oT%2BXxQAJ9LyBu%2FEPfmxDU3KGgpZ9HfTumsFWJUqgqImV3vq7efmRIM3AA3aICTacc1AKcKRPf25WT%2F9QFEoCWcC15vMfbWbnvdvPizxb4%2BQ3iRSvrbghB8ISRjYUYayXjerlDo3emzn%2BY68qKJ066oIkKDfSY7WgOqz6%2FagVxS99jUoOp3PKq7KXR2dtx9PV8yMGl0MK3jZFQIg0HvS9I3KLzOwwdKVmLFK9Km6CcVFLd8d%2F%2FMJSrUfXi1yOTphJ5HdlQHydV0QrGyEnY2Ttx1GjugV2CRvFzGoRqLWgZcenHkid6QGc0kRy8m63JOjoiCHXdLYzLt4zYnhqxzj62Ft7ubcb9TKM9ZzAD95u2XMMnxr8gGOqUBJJXqdRLdtRj2959DfHb6bohxYSOpRO0P29l9mzESivGACqgnVAkkoJ1uErHHunDl%2BNnNs1ri1QqKG22nne4lSWNL1ru2pc16w9lOhSNzyUMZ4fqGGXNDjieL6D%2F0zqK70HwbButKiwMYcjCQ2tT1IIGD8hQwMPrSFslLLBxpIwELjqLpC8p9mvQTa%2BVHo6c4nxm%2B4p2P5tcYcal%2Fr521sgwrniVU&X-Amz-Signature=cd35bbb8d361089c0c409a7e2b31b5fb2880948f060f65dcbaeff6fb4ad5127b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



