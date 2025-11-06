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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RJ3JXX5%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWwTo4FjidKQMVYcJNuEVqSu5ZwAmFYdLIfaT6UwSS7AIgQdF2qPgxS3UCuCqe%2Bxpd%2BfaeNt0skLupbCX1fEEgDDUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh6PwjIxKiV1vl%2FPSrcA6%2Fw1loV3VrlpzK1lAgHSRDufCmydrMW3RE8YRzzv0%2B1jLDmkYfvccFQGYhaFOI4pXXERRG%2F5OkZcwMCbC3N36WfrCocSUnKEVFsw3rj%2BsDqa9K1pLIF%2FqW1YPH8PxQvKn0GLyqdp7EkLUOs63qyEkJ5xlnsNCYDdSpEojbg0NI6PDx2rloXFnpiE0w4Xt4XrKqJHT3b5pKcHQeMOBtA0UbpVEBBrUO8bjlmjR0mgNFSQ0H26bM94orZD%2Bbqpx4RE9IG440Wqy1psy2XG4%2BgSIMOhKd6z4ltW509a2iRjF%2BLZ1iD%2F980f31%2FmfvUMU4zPJjDBiIoyQGMlcAv23UsE1qqessQueQntQYKJNywKOCFANxLURPjvaWlITNKeyn%2Bink2uKZx9iwAZG7E%2FeJEMJ8EkjPSexXGi2PfvQwgHiW%2F360Ms%2BG29Qy%2B4k3gmEowvDUpISQZyOM50Zzx61akJTH5Lhp%2F%2F6B61RSbpZ5XnsfQCYQBvxphUyZQ%2FqUdczJU3Y%2F7Fn19ai%2FuWRAL7eIqMlrIVZyKOSqbHXYb27tChrMie6Em9cTyYVvEjijg6So5Zv0w7b0mxQgqdFVgx4ZrT2fr7cUcyk63J3r%2BRNy2%2FDsXXoZbZC%2BRBxFaSa18MNjwr8gGOqUBwB7soq9zuWMH8q6n4%2Feg1DF6c4k%2Bus453EWaBauUb0O%2FHE520CgevTVamY1Jh3dPtZblfEGhQBOwjfta2kUpVm6qmtVvErUWlm0cHo8NuUjU%2BDRacbLnCCSUHyOXhDL1WIDoMlEzT13fCCnSUL6%2BGnIpqnsrZp3JRqQ8Am4Ye10VuUvaGmAhf1%2BxQIFjG4a0aQ%2Bm1kKQc7bNzC4sEad9f3CN4HMi&X-Amz-Signature=3f92e592e69ea558b2aea69f79942f55f4b5b5b951cd4bea32238440cfc7e255&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667RJ3JXX5%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDWwTo4FjidKQMVYcJNuEVqSu5ZwAmFYdLIfaT6UwSS7AIgQdF2qPgxS3UCuCqe%2Bxpd%2BfaeNt0skLupbCX1fEEgDDUqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOh6PwjIxKiV1vl%2FPSrcA6%2Fw1loV3VrlpzK1lAgHSRDufCmydrMW3RE8YRzzv0%2B1jLDmkYfvccFQGYhaFOI4pXXERRG%2F5OkZcwMCbC3N36WfrCocSUnKEVFsw3rj%2BsDqa9K1pLIF%2FqW1YPH8PxQvKn0GLyqdp7EkLUOs63qyEkJ5xlnsNCYDdSpEojbg0NI6PDx2rloXFnpiE0w4Xt4XrKqJHT3b5pKcHQeMOBtA0UbpVEBBrUO8bjlmjR0mgNFSQ0H26bM94orZD%2Bbqpx4RE9IG440Wqy1psy2XG4%2BgSIMOhKd6z4ltW509a2iRjF%2BLZ1iD%2F980f31%2FmfvUMU4zPJjDBiIoyQGMlcAv23UsE1qqessQueQntQYKJNywKOCFANxLURPjvaWlITNKeyn%2Bink2uKZx9iwAZG7E%2FeJEMJ8EkjPSexXGi2PfvQwgHiW%2F360Ms%2BG29Qy%2B4k3gmEowvDUpISQZyOM50Zzx61akJTH5Lhp%2F%2F6B61RSbpZ5XnsfQCYQBvxphUyZQ%2FqUdczJU3Y%2F7Fn19ai%2FuWRAL7eIqMlrIVZyKOSqbHXYb27tChrMie6Em9cTyYVvEjijg6So5Zv0w7b0mxQgqdFVgx4ZrT2fr7cUcyk63J3r%2BRNy2%2FDsXXoZbZC%2BRBxFaSa18MNjwr8gGOqUBwB7soq9zuWMH8q6n4%2Feg1DF6c4k%2Bus453EWaBauUb0O%2FHE520CgevTVamY1Jh3dPtZblfEGhQBOwjfta2kUpVm6qmtVvErUWlm0cHo8NuUjU%2BDRacbLnCCSUHyOXhDL1WIDoMlEzT13fCCnSUL6%2BGnIpqnsrZp3JRqQ8Am4Ye10VuUvaGmAhf1%2BxQIFjG4a0aQ%2Bm1kKQc7bNzC4sEad9f3CN4HMi&X-Amz-Signature=fcdeb2bbf7590db451a192eb300f83ff738010f7db7f9e9a1270da6318566906&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



