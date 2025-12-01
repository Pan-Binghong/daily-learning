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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U7ZYPPA%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDmil8Q61patIh451QaWHE%2FJdoGsWQY4zuEKWS2Yj9NCAIgHCEpuTkesZZQL9bxFoNJJpXAbT9DP0kDe1etdsJzV2oqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbAe7aoiMCY2fH8KyrcA9F96sIX1%2B4V5MJie4jD7kX5jdFQX9YO8FnNfKwsyCHZ%2Fk8xq7zeyUzuVgaqgMi3v8dC%2Bnwnc%2FHiD4uhpxt5fXDefvlulDcmFCiROl4YT%2BPvYcou7WhrcXw%2FN5J7h7wirfP5E5GwKOYwoN3Qgjv0GCkGk6cvFKX2jPT%2FHBigCebWeau%2BvTSr6aSqwaKCVTJ%2FPSgYku3HxYqovEf49T9nDugmEzr8zKnrYmdQZEKIIXCVp8pgGc5vECNSlXg69IgUm7NJFDdP7LqsbPNpWogiAT%2Bko7MJLNi1wr39FlpxSTkcXR3TQsSVxiGJyt9nI7EfZBwujj5PvPhWA3UqSviBz5PJYgvygHmd5imVr2o4DblXpqrnKC2bqBGaQlw8QiycBB%2BUyyyXYUldHSQd8lBKSuhWvTVL%2FYnqx4wTkwHBvm2wjFhBdbl5aYw5AqZv2A9CQb%2F%2BIzojkrE5c54QIx%2FLNt6hEJ7V8zIvF42gCMw1LIKfWpMc5jAyRunnuuoZPke9TYJ8fp28V2UeweE2n4kFKOV0GtNYjxcJQBBQcX83eIhrn8YPZhg8mibuQR0Axa7BzeaZRuiizn2V5elZbVoL43f1R5aCOQvrcjUvzdVFGmD7ldDFd9Ez4%2FNnxl3sMN%2BGs8kGOqUBBLJVHEv26BO6kfepnY684vx%2FYyXILm5ZHIbXpRwZzf%2FMUI5miTP5bhswdipQqxSv%2FYw%2BOxpXhKxOnMEHbURFZ6Pe9%2Bi2W1eWzA%2F1AY9O76KNXQIU2YV4hDlp8tS3WUA5x9cXoo3%2BC67UgdhpOZgmm8ePswVm0fwbvX%2BDWlc5RPK9ulSIxHPagYAtGRgp04RFvgnOs%2B%2FeV%2FTvO7PPNfdGLjwZUVpe&X-Amz-Signature=ce614ce1ec3c6c1c3be141e9a76c227ded284a70168b2f8210d249cc508db041&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665U7ZYPPA%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T030938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIQDmil8Q61patIh451QaWHE%2FJdoGsWQY4zuEKWS2Yj9NCAIgHCEpuTkesZZQL9bxFoNJJpXAbT9DP0kDe1etdsJzV2oqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNbAe7aoiMCY2fH8KyrcA9F96sIX1%2B4V5MJie4jD7kX5jdFQX9YO8FnNfKwsyCHZ%2Fk8xq7zeyUzuVgaqgMi3v8dC%2Bnwnc%2FHiD4uhpxt5fXDefvlulDcmFCiROl4YT%2BPvYcou7WhrcXw%2FN5J7h7wirfP5E5GwKOYwoN3Qgjv0GCkGk6cvFKX2jPT%2FHBigCebWeau%2BvTSr6aSqwaKCVTJ%2FPSgYku3HxYqovEf49T9nDugmEzr8zKnrYmdQZEKIIXCVp8pgGc5vECNSlXg69IgUm7NJFDdP7LqsbPNpWogiAT%2Bko7MJLNi1wr39FlpxSTkcXR3TQsSVxiGJyt9nI7EfZBwujj5PvPhWA3UqSviBz5PJYgvygHmd5imVr2o4DblXpqrnKC2bqBGaQlw8QiycBB%2BUyyyXYUldHSQd8lBKSuhWvTVL%2FYnqx4wTkwHBvm2wjFhBdbl5aYw5AqZv2A9CQb%2F%2BIzojkrE5c54QIx%2FLNt6hEJ7V8zIvF42gCMw1LIKfWpMc5jAyRunnuuoZPke9TYJ8fp28V2UeweE2n4kFKOV0GtNYjxcJQBBQcX83eIhrn8YPZhg8mibuQR0Axa7BzeaZRuiizn2V5elZbVoL43f1R5aCOQvrcjUvzdVFGmD7ldDFd9Ez4%2FNnxl3sMN%2BGs8kGOqUBBLJVHEv26BO6kfepnY684vx%2FYyXILm5ZHIbXpRwZzf%2FMUI5miTP5bhswdipQqxSv%2FYw%2BOxpXhKxOnMEHbURFZ6Pe9%2Bi2W1eWzA%2F1AY9O76KNXQIU2YV4hDlp8tS3WUA5x9cXoo3%2BC67UgdhpOZgmm8ePswVm0fwbvX%2BDWlc5RPK9ulSIxHPagYAtGRgp04RFvgnOs%2B%2FeV%2FTvO7PPNfdGLjwZUVpe&X-Amz-Signature=799bc4a0393619991fb03dece748e36dedef26db90aceb012c1bbeb461282fe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



