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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNQGICOI%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIGP566n3RLPkiPQgG44FiIQPELRTgY0KdSlVY%2BrVE%2BFbAiEAsIEv1E8o2Ac5STQMcj6xor%2FBySmlgE9EOm3wv8nHdnMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDP3q0yaaGmgs32d1rSrcA7%2BRQTHT0EAjuaDNU0DWAmqH8BHec3br5by88iE4GLBK92r9jImEctWrLpcY0klhrUUPwWB2jnJ0ZR%2Bz5lr2e9LXj7oUIZmvJB1MGd8BlRw5HD3H65xPsWJEpSuzH9P%2BqDLJO8Ty7oNEuhkwckB8Xs%2B7AZQ%2FP716Wj3XAfOhZyPHPg9rBT8PL4NrthIQ38QYu3fBbIIpGTGH927GkR9ECX1G%2FpZnZJjLML4op%2B1e0rtliQLBquQoMNE0Kr1byctPfYWdSyQJPpxVGlkcT%2FRZew1MIekuk2jsbbkekvQGxr3LADBny6nemlqQztjc%2B07sYKxyf3r9AZCP%2BsONvzDh2LON2MFvQ6S%2Bz%2FGiEQjfushsgt%2B2n19x1DOlUjxh8bjuUrJSa7aVmR5tqRtWbyxl8dm%2B9pTEe5FplXUDxHO5EABfcOtJEYBYPuQ8bPEQSXyafKF0VvVmGqC7mS9lB50w8d6%2BqulYdZ%2FwsxHRIGnuPOXynnAC5quC%2B5KM%2B2tFDfuxn1jq0CZdZZn5SrOfzIth5pAj6QNEEJ%2F7Gg9EwipfgD8CgN9n8lBqpzRbq3neAl7hG4W7mZBHjbrTwMCQXPFlXRhk7Gs56OKvMxNKDFnhrntLJqT2j6VZI0rXM1%2BiMIOG1ssGOqUBhgXT6bn8tXwYqAFuYIUJ%2F7%2BEj0rJwJ8BaYh4dlxazuun2RYHwVQVsrFAEkeg3t0Bx5oHjvdAB0AZ5sj5VlhFWj9iKSeFteuyEnYtwbifAfuMWiWt5Ab%2BpJ%2BnDJnd%2Bp39o0fsqzciALS85ixXYMXP1eg7zJ50vPf5ExIg8b82c23a9WZV3%2Bcd%2Fucidm%2B6uCr7aMA5FEPLa56cFB3d5LPn9MyBscSB&X-Amz-Signature=ccfca5e8a67cbbad16704cd9b8b5d8636f5d8376b1afc51a4e5b3a42a57a8b45&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNQGICOI%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIGP566n3RLPkiPQgG44FiIQPELRTgY0KdSlVY%2BrVE%2BFbAiEAsIEv1E8o2Ac5STQMcj6xor%2FBySmlgE9EOm3wv8nHdnMq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDP3q0yaaGmgs32d1rSrcA7%2BRQTHT0EAjuaDNU0DWAmqH8BHec3br5by88iE4GLBK92r9jImEctWrLpcY0klhrUUPwWB2jnJ0ZR%2Bz5lr2e9LXj7oUIZmvJB1MGd8BlRw5HD3H65xPsWJEpSuzH9P%2BqDLJO8Ty7oNEuhkwckB8Xs%2B7AZQ%2FP716Wj3XAfOhZyPHPg9rBT8PL4NrthIQ38QYu3fBbIIpGTGH927GkR9ECX1G%2FpZnZJjLML4op%2B1e0rtliQLBquQoMNE0Kr1byctPfYWdSyQJPpxVGlkcT%2FRZew1MIekuk2jsbbkekvQGxr3LADBny6nemlqQztjc%2B07sYKxyf3r9AZCP%2BsONvzDh2LON2MFvQ6S%2Bz%2FGiEQjfushsgt%2B2n19x1DOlUjxh8bjuUrJSa7aVmR5tqRtWbyxl8dm%2B9pTEe5FplXUDxHO5EABfcOtJEYBYPuQ8bPEQSXyafKF0VvVmGqC7mS9lB50w8d6%2BqulYdZ%2FwsxHRIGnuPOXynnAC5quC%2B5KM%2B2tFDfuxn1jq0CZdZZn5SrOfzIth5pAj6QNEEJ%2F7Gg9EwipfgD8CgN9n8lBqpzRbq3neAl7hG4W7mZBHjbrTwMCQXPFlXRhk7Gs56OKvMxNKDFnhrntLJqT2j6VZI0rXM1%2BiMIOG1ssGOqUBhgXT6bn8tXwYqAFuYIUJ%2F7%2BEj0rJwJ8BaYh4dlxazuun2RYHwVQVsrFAEkeg3t0Bx5oHjvdAB0AZ5sj5VlhFWj9iKSeFteuyEnYtwbifAfuMWiWt5Ab%2BpJ%2BnDJnd%2Bp39o0fsqzciALS85ixXYMXP1eg7zJ50vPf5ExIg8b82c23a9WZV3%2Bcd%2Fucidm%2B6uCr7aMA5FEPLa56cFB3d5LPn9MyBscSB&X-Amz-Signature=6586ae03d626195b5faa87d913ff2be501aa81f9e52214ed5cfeb09253b540b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



