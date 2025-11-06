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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YATNJRLQ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHC064Szy7fy5EYTeCyNw0ZbEOW6bVh492WxPT0tDO5TAiEApW8fgKv1jWvRH1ONxPrveO5BiNNK49T%2B4oxyuPMT0zAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCvOfaFWdTBVv5im5ircAyrADwEmqa3pPryrslEXfHfLGZAmUPMu%2FZs7QhQQxxCYxwPIDCvhtgTntK%2FkkccEO7kwV9aV5vbRDqJz87L0tW6yhGqn3%2BozZkZGbOdeS9VZFxeBGVR4RqzMueIcVjdYR%2FjWHXpFxi8ow36DctxgUM3aqWQN5Io5feEetpFWz6EGaGcgj7%2FU9r5tA1XeixU%2BUg4g26Hb23EDubwlLlRZELYiSndj3U2F4gsmtuZG0QjAF8xDdZJoQgxmPrMa0pWsm1p5%2F544e%2FdzPnHREsAtN3dnf7v7l9YRvyxU5vQUoQnPOc%2BcqXNmqbbSatic3fyDSGqgjc1EXkD%2B1bVDILNqCIMUaIIDb7ttDLoI13B%2B3U085%2F8cuPD6TV3XUVBFSu1k5OvvOHQEN29C0Af%2Bn6qreEFWfIXrRSmBkILlsH3uRGfN6PAwYoqvangyRxDCgLQ442SQDadpIFdqx7Kw%2BktbgdpKRSZjiLSNkIU5OT0mdWLCoUbDElc51iIhIiN7%2F9u%2FVJaqppk2tlQc8Cu3I5TmDTkjfZXJ%2FZJVCgO%2BXB6iTpird7nx5ntsOvUwSkY9FQMeKVUBfjLwqrIGPhqgdaskZnlvSo4Hc47fPXdvLQBJ3UkuMB4qhYD1tdpBLJSIMMLwr8gGOqUByVEcPKe1%2BRa4bIOn34YcY%2BQMKcDnIKJQGvO%2B9oaywgr%2FJHbcbmrSVv%2FgGC9P5L%2FaptyOeCaILiHKT6tGEaOmIsZDsjvryHunAmDs1QeTEbYndA1HNdd5UJOUIjqrn7xZt8zq%2B5XMgnnnykm7c9QH3GLaCneaJdBMaCcmfnoFYLaT3TwB9Lv2RjvrHr7Ri2b%2Blomrtwx8ShCzHnBMYosc7CqxYtGZ&X-Amz-Signature=09b19ee53d2f46a33d603a85daa5971e73a41f5fd3053280075573dd409bf90a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YATNJRLQ%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T013119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHC064Szy7fy5EYTeCyNw0ZbEOW6bVh492WxPT0tDO5TAiEApW8fgKv1jWvRH1ONxPrveO5BiNNK49T%2B4oxyuPMT0zAqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCvOfaFWdTBVv5im5ircAyrADwEmqa3pPryrslEXfHfLGZAmUPMu%2FZs7QhQQxxCYxwPIDCvhtgTntK%2FkkccEO7kwV9aV5vbRDqJz87L0tW6yhGqn3%2BozZkZGbOdeS9VZFxeBGVR4RqzMueIcVjdYR%2FjWHXpFxi8ow36DctxgUM3aqWQN5Io5feEetpFWz6EGaGcgj7%2FU9r5tA1XeixU%2BUg4g26Hb23EDubwlLlRZELYiSndj3U2F4gsmtuZG0QjAF8xDdZJoQgxmPrMa0pWsm1p5%2F544e%2FdzPnHREsAtN3dnf7v7l9YRvyxU5vQUoQnPOc%2BcqXNmqbbSatic3fyDSGqgjc1EXkD%2B1bVDILNqCIMUaIIDb7ttDLoI13B%2B3U085%2F8cuPD6TV3XUVBFSu1k5OvvOHQEN29C0Af%2Bn6qreEFWfIXrRSmBkILlsH3uRGfN6PAwYoqvangyRxDCgLQ442SQDadpIFdqx7Kw%2BktbgdpKRSZjiLSNkIU5OT0mdWLCoUbDElc51iIhIiN7%2F9u%2FVJaqppk2tlQc8Cu3I5TmDTkjfZXJ%2FZJVCgO%2BXB6iTpird7nx5ntsOvUwSkY9FQMeKVUBfjLwqrIGPhqgdaskZnlvSo4Hc47fPXdvLQBJ3UkuMB4qhYD1tdpBLJSIMMLwr8gGOqUByVEcPKe1%2BRa4bIOn34YcY%2BQMKcDnIKJQGvO%2B9oaywgr%2FJHbcbmrSVv%2FgGC9P5L%2FaptyOeCaILiHKT6tGEaOmIsZDsjvryHunAmDs1QeTEbYndA1HNdd5UJOUIjqrn7xZt8zq%2B5XMgnnnykm7c9QH3GLaCneaJdBMaCcmfnoFYLaT3TwB9Lv2RjvrHr7Ri2b%2Blomrtwx8ShCzHnBMYosc7CqxYtGZ&X-Amz-Signature=453db14e1b15eaa254d2068e0fb6ab48e46d2823e43fdcc5d9aac12fceeb5087&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



