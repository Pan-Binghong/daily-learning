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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W27B3536%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIB%2FnTAYvLEFgWoRMaDDdKRCugFhN5nSkgiKJjNG5Vx3UAiEA8Cwrzgx%2F33t3eeDIpYcJWbxXogHvLcNFfPtVJ22kwxsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDLf42XHnewOOIOLvlircAxPXCR861NBi4fnzCYyIEHW9MF7YuNSCxcQfbW742nVWb8SBYOqf286vPqGhZjKExnAGgdTXcb3AXur7wjuBiXtjRI%2BJ0vMKoTmGZNJFkIp7y8zYzwfcbYLnt5x%2FtxYEmR1Rg%2BDl%2BGpFKfh8A2KEPGBHeHZYxtZGW8hZMhuEZ3v4H6fa9h0Kmi1syagcy90RvAX%2BLff1rPwaJjCiQafdKtWbrFL8ZnjTNKxSeI3bkcQylYHGieB1SnEmDAmzfb3TakFiivUpGLHOMFSANY4jl7rlD3GOctKV2uQltfWPcMvWEMydkn03SXAWewVZbqv6dIgjSroak7qQleUYT%2B6AeQdwCKY8pywoY7%2BidOvHTAGqluYDxbh2NtUeDclMgOTUtBi6IOOysvKmYah%2FUV%2BU54ifhfuGCE%2BoJzmrhhjYqgw7I%2FsNkDUIpbkyaU10Tc5bC8vhKRUHMq5w9UGq5apGNpnNXx74Q6Rc%2BC0GQLINK7JbCzcEPfF1hZEuuI1bpuinkqOuF90sSKo42OhmE0jcTU0Y4zUTSwB3zj37P5Wg%2BQnAtmFhl7JZllueGr0lYY3eBBvW%2FljU3a59CO7rOjF%2BatY7%2FJZe5pNn5xG%2FA3Hb%2FsGCz1yGcIu3v3F%2FAvGTMKDjz8gGOqUBgzNV6FySYHXU3vBnUntLVJfLM8OC05GgQfYYkmoFL9umDq81XAlWezIY9u05P4lLkeKo3nSrYfXD8pHkPal2HcjPzt8QPs6J2U%2BiOsuEQwrmGj9vpCSUQGEPZpJp9Nie%2BwpDs8Rzao%2ByOuXZ05HOm6um23lWP0BStVRmgnozzKwQicbpf9qmGTfF6hmj5ZC5gBxQy27lmYSjZi6t12RpZbsfc0P%2B&X-Amz-Signature=cf4730c3c68daae8bbafeb5907a7d65a22d17b0ddaa9d692abf5e0f528e7515d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W27B3536%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T024353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIB%2FnTAYvLEFgWoRMaDDdKRCugFhN5nSkgiKJjNG5Vx3UAiEA8Cwrzgx%2F33t3eeDIpYcJWbxXogHvLcNFfPtVJ22kwxsq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDLf42XHnewOOIOLvlircAxPXCR861NBi4fnzCYyIEHW9MF7YuNSCxcQfbW742nVWb8SBYOqf286vPqGhZjKExnAGgdTXcb3AXur7wjuBiXtjRI%2BJ0vMKoTmGZNJFkIp7y8zYzwfcbYLnt5x%2FtxYEmR1Rg%2BDl%2BGpFKfh8A2KEPGBHeHZYxtZGW8hZMhuEZ3v4H6fa9h0Kmi1syagcy90RvAX%2BLff1rPwaJjCiQafdKtWbrFL8ZnjTNKxSeI3bkcQylYHGieB1SnEmDAmzfb3TakFiivUpGLHOMFSANY4jl7rlD3GOctKV2uQltfWPcMvWEMydkn03SXAWewVZbqv6dIgjSroak7qQleUYT%2B6AeQdwCKY8pywoY7%2BidOvHTAGqluYDxbh2NtUeDclMgOTUtBi6IOOysvKmYah%2FUV%2BU54ifhfuGCE%2BoJzmrhhjYqgw7I%2FsNkDUIpbkyaU10Tc5bC8vhKRUHMq5w9UGq5apGNpnNXx74Q6Rc%2BC0GQLINK7JbCzcEPfF1hZEuuI1bpuinkqOuF90sSKo42OhmE0jcTU0Y4zUTSwB3zj37P5Wg%2BQnAtmFhl7JZllueGr0lYY3eBBvW%2FljU3a59CO7rOjF%2BatY7%2FJZe5pNn5xG%2FA3Hb%2FsGCz1yGcIu3v3F%2FAvGTMKDjz8gGOqUBgzNV6FySYHXU3vBnUntLVJfLM8OC05GgQfYYkmoFL9umDq81XAlWezIY9u05P4lLkeKo3nSrYfXD8pHkPal2HcjPzt8QPs6J2U%2BiOsuEQwrmGj9vpCSUQGEPZpJp9Nie%2BwpDs8Rzao%2ByOuXZ05HOm6um23lWP0BStVRmgnozzKwQicbpf9qmGTfF6hmj5ZC5gBxQy27lmYSjZi6t12RpZbsfc0P%2B&X-Amz-Signature=81dc5c2391636add322c542e8f0925c5c0c17777fac4939110529ea7f99f65b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



