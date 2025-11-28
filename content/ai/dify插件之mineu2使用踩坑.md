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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6GH4JC%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1AwuioOjzRybuRoVLUyFjLi4uIxk%2FZdSsJUgs87QzlAiAWRGJ5rThOpPFHlQTiF5Un%2FhgZqd0zmATIfUV3sxFJ%2FiqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJoEwTwBPUjQce67eKtwDosUabW04jix0Krk6dNS2PS%2BoNRlDb3MdpbongVH0Zs0BGoYdl6ys%2BAGb%2Bywf1xVY8pAWs9MjB%2FdhUfdH2E%2BiJsyYqVzHQuvjhX%2FfeSXDEG3B1hxHvU9NbiFADXQQqF6ijjslMGTv8pzib%2BvcfgKJTWzirjdN54pyfmQr1ZIHu8%2By9TGRmLuPjniozhAGMPh2oavKK4emgI5P4Gdp6TLunfI%2FWKUjq2Tar9SjOp9TaFLu93jRxQQ%2Fc3rHQ%2FzIQbyUt%2F1YsXfFh%2FQ9FlnCAwyht%2BdgSYHmKeaze7dGmDllY0sJs7sYPGJgyjxdw4LfQHIAsqbBxRHOik8RGXsHfHth7pcTaM4atuTbhZ9nv8pzS6s2Xki5lNvpUdq%2FYhwgAlz6fhJoA8P7XbSSaqOEu61FZdl%2BAj402MRlEqJvSZLZiom2woZNeeMFdDecdpM1KfCvWZXbaMSSuNzCdfajF2cZp74aCAjMj9mYtpBprSfIzW6jPjxrixYSvia%2BbODf393V%2F%2FNEVIlreYWVex5iIphAKTISnKUJku8VlmRwc62rJIyVRAxdod%2B%2Bhv2SJ02S%2Byavb36MdpQbfncLm6cB9Dy3n%2BPXZgJxuctfZUCTnyeEyrIfWZXJr85n6WHBXlAwxIKjyQY6pgFduovNMYMXmUbCY717JE3UHbjL0wxVgGFcnLO1B9%2F9ygSaO5mqT5UTNC5WVw2IuuoJi0LXGCPD3auCRziuphlajTl1Ple7gMgX39TThu3JIsVJ%2FNbgFGradhSAydp1PAQX8NMyNIr2nIvpz7iX5cfA7f4Xr0Ht0T2Y1q9JLlNu%2FTkaxRl9y0K%2BSVnMggVRsUbmcAD%2BNASXK3wCuYFA%2BliayzbW%2Feva&X-Amz-Signature=92bc2b2a92666c6d47c81e88f02372efa5f8795341a35c54a4622c413053ea42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV6GH4JC%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB1AwuioOjzRybuRoVLUyFjLi4uIxk%2FZdSsJUgs87QzlAiAWRGJ5rThOpPFHlQTiF5Un%2FhgZqd0zmATIfUV3sxFJ%2FiqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJoEwTwBPUjQce67eKtwDosUabW04jix0Krk6dNS2PS%2BoNRlDb3MdpbongVH0Zs0BGoYdl6ys%2BAGb%2Bywf1xVY8pAWs9MjB%2FdhUfdH2E%2BiJsyYqVzHQuvjhX%2FfeSXDEG3B1hxHvU9NbiFADXQQqF6ijjslMGTv8pzib%2BvcfgKJTWzirjdN54pyfmQr1ZIHu8%2By9TGRmLuPjniozhAGMPh2oavKK4emgI5P4Gdp6TLunfI%2FWKUjq2Tar9SjOp9TaFLu93jRxQQ%2Fc3rHQ%2FzIQbyUt%2F1YsXfFh%2FQ9FlnCAwyht%2BdgSYHmKeaze7dGmDllY0sJs7sYPGJgyjxdw4LfQHIAsqbBxRHOik8RGXsHfHth7pcTaM4atuTbhZ9nv8pzS6s2Xki5lNvpUdq%2FYhwgAlz6fhJoA8P7XbSSaqOEu61FZdl%2BAj402MRlEqJvSZLZiom2woZNeeMFdDecdpM1KfCvWZXbaMSSuNzCdfajF2cZp74aCAjMj9mYtpBprSfIzW6jPjxrixYSvia%2BbODf393V%2F%2FNEVIlreYWVex5iIphAKTISnKUJku8VlmRwc62rJIyVRAxdod%2B%2Bhv2SJ02S%2Byavb36MdpQbfncLm6cB9Dy3n%2BPXZgJxuctfZUCTnyeEyrIfWZXJr85n6WHBXlAwxIKjyQY6pgFduovNMYMXmUbCY717JE3UHbjL0wxVgGFcnLO1B9%2F9ygSaO5mqT5UTNC5WVw2IuuoJi0LXGCPD3auCRziuphlajTl1Ple7gMgX39TThu3JIsVJ%2FNbgFGradhSAydp1PAQX8NMyNIr2nIvpz7iX5cfA7f4Xr0Ht0T2Y1q9JLlNu%2FTkaxRl9y0K%2BSVnMggVRsUbmcAD%2BNASXK3wCuYFA%2BliayzbW%2Feva&X-Amz-Signature=2cb1c9a30df392d40bebe43ecf43cbc53bc67242b8ca2a32d89be3ca52670cfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



