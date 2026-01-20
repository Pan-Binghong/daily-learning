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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QX3EG2T%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHVJWjHrJ%2BAG7WiqKsBzV5oGrkfZpjRroR8yqOTVRhVwIgbg5U7SrzjNL6i5i%2FRGcwaMysB4mJVEsMs5PZUwDgePUqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZ%2BldDf2fwfUKvCSrcA1pGsR%2BP5gBwbJyzrihflC7lKRnv2P995S8zTupEGY9XhtmdcbSnVMlzXSqlQhHXuXiT9ZdfzjZx77Qo8YOvEXFO9mtYKM02%2BkLaz6QitH9m1oV9WoIHyTr%2BVRXCmtIv2npMRHL5hSrbb8444oRzyo0enn%2F7GQyYL1Yw0Rq%2Bzf4OZEy1Xl1y6z5S%2B%2BXatQtNsGeeIuLsau1KlUzQitpkPRkPk6Z%2FNnhy9qLklvD5b9ptP5FZUt1cMnDm3eC3LAJpj3YxC3G1CR%2BTg5awKDKI4E6ubCobLyNmhg2vYqNxj0pD%2BFdKa4uaHLIskQFSl6hfj%2FxzRPtKpgTdvopr7pCpnl16mnKWYUzM1NQu%2F93AyFAY%2FoAFPf1ta%2Fib%2BEtqkq4ANqu7JA0LLaMAXuizY9Lcqcm51S9b4VdYEMbEIEXWTwJsZH0e98MoAuBRUByiOX5CGorzwYNJpPKu2pkBedUTQHX2n6KRbZ1wb7vOATpjTH%2B4wTJbIHsBDU1agNJm9CsE7Wt9b2p3hnNi6vPQfqYKLwd9jCAz3GB1sWAjQ6TUpDAlu4K8OR4VuUZOtI5sinchaHI%2FCGCvQ5SZlAgUL475al8aXq%2BRBHi8r59mSlytCvFK6nvWLRG3uqQRRazUMPb0ussGOqUBzXkVETlYJ5oy84z2RgjcQ6I57ozPh%2F9ykVky7gq5nthvzoDIJfUcicPRE4NcoOT9L68l1J6851V8Kpg%2BwK101zf8gOl4Z7RqS154g5xPtNK57g8ajLt7CxBWmNgviiZt0dWeh%2FNXjKD06CiqJ1HN%2BYJYrLaVtBPj9SJ%2BfYXVkU3yJLuF9egA2O8Jc4%2B0fWBhpvkYiqmKFNPY2q%2B61p5NEB9goZ9G&X-Amz-Signature=cc72c2a4a7641314a5eea96e5f2e94546c2ad7dadc57e9852c2ccb923d2c6871&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QX3EG2T%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T030319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHVJWjHrJ%2BAG7WiqKsBzV5oGrkfZpjRroR8yqOTVRhVwIgbg5U7SrzjNL6i5i%2FRGcwaMysB4mJVEsMs5PZUwDgePUqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEuZ%2BldDf2fwfUKvCSrcA1pGsR%2BP5gBwbJyzrihflC7lKRnv2P995S8zTupEGY9XhtmdcbSnVMlzXSqlQhHXuXiT9ZdfzjZx77Qo8YOvEXFO9mtYKM02%2BkLaz6QitH9m1oV9WoIHyTr%2BVRXCmtIv2npMRHL5hSrbb8444oRzyo0enn%2F7GQyYL1Yw0Rq%2Bzf4OZEy1Xl1y6z5S%2B%2BXatQtNsGeeIuLsau1KlUzQitpkPRkPk6Z%2FNnhy9qLklvD5b9ptP5FZUt1cMnDm3eC3LAJpj3YxC3G1CR%2BTg5awKDKI4E6ubCobLyNmhg2vYqNxj0pD%2BFdKa4uaHLIskQFSl6hfj%2FxzRPtKpgTdvopr7pCpnl16mnKWYUzM1NQu%2F93AyFAY%2FoAFPf1ta%2Fib%2BEtqkq4ANqu7JA0LLaMAXuizY9Lcqcm51S9b4VdYEMbEIEXWTwJsZH0e98MoAuBRUByiOX5CGorzwYNJpPKu2pkBedUTQHX2n6KRbZ1wb7vOATpjTH%2B4wTJbIHsBDU1agNJm9CsE7Wt9b2p3hnNi6vPQfqYKLwd9jCAz3GB1sWAjQ6TUpDAlu4K8OR4VuUZOtI5sinchaHI%2FCGCvQ5SZlAgUL475al8aXq%2BRBHi8r59mSlytCvFK6nvWLRG3uqQRRazUMPb0ussGOqUBzXkVETlYJ5oy84z2RgjcQ6I57ozPh%2F9ykVky7gq5nthvzoDIJfUcicPRE4NcoOT9L68l1J6851V8Kpg%2BwK101zf8gOl4Z7RqS154g5xPtNK57g8ajLt7CxBWmNgviiZt0dWeh%2FNXjKD06CiqJ1HN%2BYJYrLaVtBPj9SJ%2BfYXVkU3yJLuF9egA2O8Jc4%2B0fWBhpvkYiqmKFNPY2q%2B61p5NEB9goZ9G&X-Amz-Signature=b0615270ceaf0e1ee60548a56a7b201e9be91df111d1dbe088bfb89ba13f8fb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



