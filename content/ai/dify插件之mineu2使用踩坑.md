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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O5J7EB2%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6CgnWNen1tD8roCUKjqBKPlb6bBmMCFOuPZNQykRMLAIgLpez4wIsvMb923DzVR%2Fu7oZtrl3SGTWGW71%2Fp4yb5CAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDDT7tx3jCICYuT%2BxXSrcA5JI04eGGQOjt%2BQAGljX2FmteXznydWC0YoPqsel2ne1J0Nu3eWOR77tDBhpDr%2Fbm%2BGK3P8I7VwAmJD%2F2qDg9tpBhFD8%2FapvwolUVpIFtqa47nPvlR1ZKEbWYSjN0EIir5A9Z0mmW%2F%2FzGzku7ZvaUe4q7GcJLyAMRaddE2igTiiZUO84r%2FLMKzqAtqIVExMhIiFLSzC8UHlQvxLxrzN0FgcGVJsp7zkciluKaLawW65o8saIg%2B00aA9RKBfu3osgKpGjnBTo55vYh9xySibBwvcRD2O9dEaMIoHNfxr%2F1rwPpkdPzc7IpbB%2B52y0k0DtGuiNCjgEwU96rOqLhb0BD0G%2BmHYRnhL7%2BNEgoIuXC%2BS6esT3cugaMKoatBHJiWH8ltETdaU0w4zxGt3kKofDhfiMgZGj3zajhmj8Kk2twmJZnd6zXECsYiJJ1oiJkfpw3m7jvxirCzCL9UZpr1Wl5RTKuLWy54Im1%2Fg%2FTc%2Bg1q3cV00hwg2ej8KuY2Zjw1mZcc4MFuQZUyA6bM3sNXsDEwuJmw7LEx7pilBV1WcJq%2BjefFelQtqNzSFnARMfEvqE6ttEL%2BQ%2FoiWak1StBM3w9wWkkdeLcwKQ5jXHAB3q%2B%2Fem5tXz%2BX43zdBw9F4QMInOt8oGOqUBA2ronUtAKwi405sKsyGBR5UTiFQlOtWkJNC04VPliZHzkN%2FyzK9AkUnCdkgVoKTQanoWxY2%2FgBX15ITzXoXtKgSgbko%2B8sczNBVi4fv66yWC%2BkdNmL%2BGAF7tiHc6wXll18erWaBKujr4bJCRFe2ULrJ6Y30%2BUgBgATm%2F%2BQUYpTCCZepB5fvkLOeuV%2Fm6moNjTSO1Rj2F9Opm%2F0D1hv8Ms2UIj0%2FB&X-Amz-Signature=863af4ef21c0a6e3a4ec7f24b8482629ed97c58604823614e350aefda7967aa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667O5J7EB2%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T025535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6CgnWNen1tD8roCUKjqBKPlb6bBmMCFOuPZNQykRMLAIgLpez4wIsvMb923DzVR%2Fu7oZtrl3SGTWGW71%2Fp4yb5CAq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDDT7tx3jCICYuT%2BxXSrcA5JI04eGGQOjt%2BQAGljX2FmteXznydWC0YoPqsel2ne1J0Nu3eWOR77tDBhpDr%2Fbm%2BGK3P8I7VwAmJD%2F2qDg9tpBhFD8%2FapvwolUVpIFtqa47nPvlR1ZKEbWYSjN0EIir5A9Z0mmW%2F%2FzGzku7ZvaUe4q7GcJLyAMRaddE2igTiiZUO84r%2FLMKzqAtqIVExMhIiFLSzC8UHlQvxLxrzN0FgcGVJsp7zkciluKaLawW65o8saIg%2B00aA9RKBfu3osgKpGjnBTo55vYh9xySibBwvcRD2O9dEaMIoHNfxr%2F1rwPpkdPzc7IpbB%2B52y0k0DtGuiNCjgEwU96rOqLhb0BD0G%2BmHYRnhL7%2BNEgoIuXC%2BS6esT3cugaMKoatBHJiWH8ltETdaU0w4zxGt3kKofDhfiMgZGj3zajhmj8Kk2twmJZnd6zXECsYiJJ1oiJkfpw3m7jvxirCzCL9UZpr1Wl5RTKuLWy54Im1%2Fg%2FTc%2Bg1q3cV00hwg2ej8KuY2Zjw1mZcc4MFuQZUyA6bM3sNXsDEwuJmw7LEx7pilBV1WcJq%2BjefFelQtqNzSFnARMfEvqE6ttEL%2BQ%2FoiWak1StBM3w9wWkkdeLcwKQ5jXHAB3q%2B%2Fem5tXz%2BX43zdBw9F4QMInOt8oGOqUBA2ronUtAKwi405sKsyGBR5UTiFQlOtWkJNC04VPliZHzkN%2FyzK9AkUnCdkgVoKTQanoWxY2%2FgBX15ITzXoXtKgSgbko%2B8sczNBVi4fv66yWC%2BkdNmL%2BGAF7tiHc6wXll18erWaBKujr4bJCRFe2ULrJ6Y30%2BUgBgATm%2F%2BQUYpTCCZepB5fvkLOeuV%2Fm6moNjTSO1Rj2F9Opm%2F0D1hv8Ms2UIj0%2FB&X-Amz-Signature=0f57070974bfee797d6ffd14548fa542e424cd4638fa86b4fa5b8ab9d968ee3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



