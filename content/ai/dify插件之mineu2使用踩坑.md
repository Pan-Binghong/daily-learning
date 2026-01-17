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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHT4UXO%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGiPhGziEW38M0zBGmCTKuSFGhsQ9Dx%2Bwe%2FTM7R5er%2BYAiEAhOD3fzJNpJJs1HYFsGt6vS9d78UrDdi2ctTtmZdMGvwq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDCzqLyq3KrgUAEhnqyrcA%2BlbGvh6C34UJWLySU7BFY9O0bfnSgOfQfyRSreN4Fxdv%2F%2BfCY5wdh3q6LvE%2B2FKQ2fkKTIkmqU2X%2Bdgn7%2B58cKWrJWDHhiQ98V5AzNA1ZxjaBdsx9VcQFLjN8KEswjv%2FMRuXqLxl0nU3peV9YOqIMs5WNi1G7Qc69Ab%2FWwecB83LNgM%2FijHG9hOIwbqhV6x5mgqdjrAIyR5rzrY%2Fk8tBSsTa5PQMrOnevCa20WOB0TYl2Cz%2F9TR443DXbNSQQgvSC0bADHUadsYfNxHbwhkLwWWYN%2BxyyCQpnyYPTv%2BHCliP86MkjGdqMg1u3IhfhsH%2BJ2HiEPzhmIMoVcf7GbT4nG9MdP%2BTjOBd1u1kxa7kmg97rKlwQtQnMrpms7fPvzLsepwyB%2FO2VpqvTbYNKo6IFC76GU3gi3N5ZV8cgQhBbnUhmUbg6rVqLvs9%2BznpWELfbx59MZRVmsEAF2Daq1lwj6jIrBE5XfbOcJL9cAPNCcf0EDJYr9%2FYajj3dKoBtFB24Q8E2xvMeqk3c6hGlrYNvr2YGbqoMaNgPnGi905aRQgLZcGSqHzN2F7sTpJzERhmFE%2FwzQ2SlhpgAHTLRENlFRlrWhCXD2IFuQLhBmH1xvb8ftM6nZfqdJFm2z7MPfRq8sGOqUBEC6cwRCEABV0KuEdJX%2BUgIl0hc52Oh56WMjb%2B6D2iiFDNXbg%2FHOz8l9nh8%2Byy86o%2BmkKdpZ0%2BOATW4H9103wqfcHg7OEIpxYKgC38Pfm0LLY6WPoHPQ4jBhB%2FNf75s8mEASSbd6FbanxVs%2BLtrPufZxJx7DNmhRFT94fqRrt0kUJF0%2BYIOJ3kqCl9omisFqPlGnpbUkDIQqvMvyxTSqAHkpixnyF&X-Amz-Signature=366b8a85cd4880cb08d2438f23b11f03214720fcb90e9a21633a2aa44d65a852&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNHT4UXO%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGiPhGziEW38M0zBGmCTKuSFGhsQ9Dx%2Bwe%2FTM7R5er%2BYAiEAhOD3fzJNpJJs1HYFsGt6vS9d78UrDdi2ctTtmZdMGvwq%2FwMIWxAAGgw2Mzc0MjMxODM4MDUiDCzqLyq3KrgUAEhnqyrcA%2BlbGvh6C34UJWLySU7BFY9O0bfnSgOfQfyRSreN4Fxdv%2F%2BfCY5wdh3q6LvE%2B2FKQ2fkKTIkmqU2X%2Bdgn7%2B58cKWrJWDHhiQ98V5AzNA1ZxjaBdsx9VcQFLjN8KEswjv%2FMRuXqLxl0nU3peV9YOqIMs5WNi1G7Qc69Ab%2FWwecB83LNgM%2FijHG9hOIwbqhV6x5mgqdjrAIyR5rzrY%2Fk8tBSsTa5PQMrOnevCa20WOB0TYl2Cz%2F9TR443DXbNSQQgvSC0bADHUadsYfNxHbwhkLwWWYN%2BxyyCQpnyYPTv%2BHCliP86MkjGdqMg1u3IhfhsH%2BJ2HiEPzhmIMoVcf7GbT4nG9MdP%2BTjOBd1u1kxa7kmg97rKlwQtQnMrpms7fPvzLsepwyB%2FO2VpqvTbYNKo6IFC76GU3gi3N5ZV8cgQhBbnUhmUbg6rVqLvs9%2BznpWELfbx59MZRVmsEAF2Daq1lwj6jIrBE5XfbOcJL9cAPNCcf0EDJYr9%2FYajj3dKoBtFB24Q8E2xvMeqk3c6hGlrYNvr2YGbqoMaNgPnGi905aRQgLZcGSqHzN2F7sTpJzERhmFE%2FwzQ2SlhpgAHTLRENlFRlrWhCXD2IFuQLhBmH1xvb8ftM6nZfqdJFm2z7MPfRq8sGOqUBEC6cwRCEABV0KuEdJX%2BUgIl0hc52Oh56WMjb%2B6D2iiFDNXbg%2FHOz8l9nh8%2Byy86o%2BmkKdpZ0%2BOATW4H9103wqfcHg7OEIpxYKgC38Pfm0LLY6WPoHPQ4jBhB%2FNf75s8mEASSbd6FbanxVs%2BLtrPufZxJx7DNmhRFT94fqRrt0kUJF0%2BYIOJ3kqCl9omisFqPlGnpbUkDIQqvMvyxTSqAHkpixnyF&X-Amz-Signature=a5c56ad4defdbe56ff8b381afdd4f5b0514662378ad642fd36f3adcab8e7bb7f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



