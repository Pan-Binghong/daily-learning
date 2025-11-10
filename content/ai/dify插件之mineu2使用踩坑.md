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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D7G44NO%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC3gPJ%2F4nafru8XfoZnqTo3PrZx95Xe5gvlpV%2BEKKV6%2FAIgFPkeuNZ6VXeN2pD%2Bf1N2h4eGvvco8mx8KzD%2FXymljDgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEi2Lz26s553CzbxhyrcAxBloFWccqU3FVsM5sWKnqDsH1IJeu6HCtN8I4iUW7fbXe4SreG99P5kC2SQlIr6qdv%2Fp%2BB38uqFA8Uj97vCMDCLhx9YhYqZlweXGwdf3lu%2BzhMaAmGxwhglkxIEbOxoxMoXI5XwD%2Fu2e8R5nL15I1hOrP1chLl%2Fug8IRQPpQw1tucI8bdtW6vreNCR521yWt0A3m%2FNBmVQrTAc4Yawp0wDDtO2pJ7jyr%2BaBe4lOaeAnK0z%2FhwUDjJUEPoQ4ZPR346uEuy%2Fh%2F%2Fhv7u9GIzztwvv5YdfynwFxbGWvJuehwx9sSd6tDNBnp%2FNXdQnt156WPIXDnXFrdPCVh5rPgEVqbWxKhjUK8IwCbb%2Fhw2zYo8W8Y5IoTiLVrvgvNCDghKrmF%2BAeF1u%2B09F12uNDIdAHmgcYMCROKasFSyW3tibtob5F6qE7RyJ9YbHF4E2%2BaAk8YrZ7NOEiLybe%2Bb%2F0S2qH3%2FRYAdfg0c%2BGxrn7sA3meQJ0DF6XWNKxQw63jYhxx6VUgTqEoIxLU3sMHF4jcYAV2fbBGxzNapw8LO758RT0CXnq7TP85pnaH5rbsanwr%2F9XLQB659SKRmSFFogX2MnVCVlaQ8mAGMZDCsaGvnxiYuSaszGrpnJBiOUoXWIYMOSwxMgGOqUB2M9vczZ2J7vcbLrFBRxBYs3vnAL4FjionVQI4eO7G6S1nHBWDUiz6aVIbtjpAPBbvdTjGRf0EZL%2Frb2C%2FzYODM25e9V5mcvWPiRKPlr84bzViamjLLXOxAoWJRjsWWouZ%2F3dnekgT3HDLlXYNdz8FzWLEIvhF9WYndK4g%2Fphksw5T5T%2FtsA6A5ftoMFTzdhJEmTNHhJopTMNqwI7aS1%2FYJ4H4zgZ&X-Amz-Signature=da43beef45bf349bfede0e8f540a9ab7692e0dd6982f915d362ee9892f65ed31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665D7G44NO%2F20251110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251110T025002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC8aCXVzLXdlc3QtMiJHMEUCIQC3gPJ%2F4nafru8XfoZnqTo3PrZx95Xe5gvlpV%2BEKKV6%2FAIgFPkeuNZ6VXeN2pD%2Bf1N2h4eGvvco8mx8KzD%2FXymljDgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEi2Lz26s553CzbxhyrcAxBloFWccqU3FVsM5sWKnqDsH1IJeu6HCtN8I4iUW7fbXe4SreG99P5kC2SQlIr6qdv%2Fp%2BB38uqFA8Uj97vCMDCLhx9YhYqZlweXGwdf3lu%2BzhMaAmGxwhglkxIEbOxoxMoXI5XwD%2Fu2e8R5nL15I1hOrP1chLl%2Fug8IRQPpQw1tucI8bdtW6vreNCR521yWt0A3m%2FNBmVQrTAc4Yawp0wDDtO2pJ7jyr%2BaBe4lOaeAnK0z%2FhwUDjJUEPoQ4ZPR346uEuy%2Fh%2F%2Fhv7u9GIzztwvv5YdfynwFxbGWvJuehwx9sSd6tDNBnp%2FNXdQnt156WPIXDnXFrdPCVh5rPgEVqbWxKhjUK8IwCbb%2Fhw2zYo8W8Y5IoTiLVrvgvNCDghKrmF%2BAeF1u%2B09F12uNDIdAHmgcYMCROKasFSyW3tibtob5F6qE7RyJ9YbHF4E2%2BaAk8YrZ7NOEiLybe%2Bb%2F0S2qH3%2FRYAdfg0c%2BGxrn7sA3meQJ0DF6XWNKxQw63jYhxx6VUgTqEoIxLU3sMHF4jcYAV2fbBGxzNapw8LO758RT0CXnq7TP85pnaH5rbsanwr%2F9XLQB659SKRmSFFogX2MnVCVlaQ8mAGMZDCsaGvnxiYuSaszGrpnJBiOUoXWIYMOSwxMgGOqUB2M9vczZ2J7vcbLrFBRxBYs3vnAL4FjionVQI4eO7G6S1nHBWDUiz6aVIbtjpAPBbvdTjGRf0EZL%2Frb2C%2FzYODM25e9V5mcvWPiRKPlr84bzViamjLLXOxAoWJRjsWWouZ%2F3dnekgT3HDLlXYNdz8FzWLEIvhF9WYndK4g%2Fphksw5T5T%2FtsA6A5ftoMFTzdhJEmTNHhJopTMNqwI7aS1%2FYJ4H4zgZ&X-Amz-Signature=f05b5955d96e14b702735148d774d2a510a55ad59ab1ebd9162f7fc93c0a4991&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



