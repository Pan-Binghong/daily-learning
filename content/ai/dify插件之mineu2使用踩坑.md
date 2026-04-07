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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQECBMWC%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQD3IIomMgn%2FBm%2FbZomQeROt5ku80GsURAGDb5Ny6sO2FQIhALdSdNOcHBq%2FRm84BVZ%2B4KN4qLUEZa%2B7DsjPvdovKl%2FeKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMWTieTuicadLDO7cq3AMra99rcYhIViEvU3aQHoPrsNo9HrNqOZCauYLysOAWvdSgcY%2FvwXTbeCnMRfyAR4O0MSXeYEGvPU%2B8PvvEMa7%2FTZzrAhcw9ywZM3eXhzVikLyhWUdlJf0CfThWY0%2FhicBIwmr35ZbzMdBfSHJGat3fgt%2BsA0%2F6IX%2FE5Us8GvvfIQahHw16x5rApcfG1oM7B50pfXegDYsZGaZ0dUaPDYSQdkVI4J8fEXopitdF0vPhrwYH0%2FX26FBQcJfWfPCW0s8Pz0Z6AbT3pPf78Bp7X6SdPJJdPQNsH9dPLzJ6eoBgYsdlH0V4%2FR4OgLIbyL7xzRMo0%2B8zi%2BZdoh2T6NLS1HuTKB3yuH%2BB0KWm1JPcWi5ncjsquuFN5lW%2BjYkJALo2yDAOYACljpXVxRXFbKXfRlNpWjfEP2axzPJD4lGLzKfBI8KXp9BmxJD9FLQl9hCBCSiOvsrATO2wekdxwr5InsSbkEOxG%2FEaWmEAhKDFYK1A2lE1H1BHAtCkpe3ZEssaeY5xmiBcbfW%2F%2B1UQ%2FhjmAXeQQreTgqr2c2bFcLlqOo7rioqlhpCOiupeLHsIusC6thXDTGHCmtysetrWvXu%2FkTIrhHInuYZn5m8UfkXmOjgp%2B8zP%2FHyzfqInl0qgQTC89dHOBjqkAVLYTVRj%2FXY2nXnrkLPYSZZa%2BK3O4Lplr0dn3JUo9pedQRLSdryQ%2FBlXy8LMmPutb419wp6AYEZoLwpmKXyhSpT9SJSbqB276S%2Fwka9VwVp%2BbcJ4P5b8CwtvhfJaJl60cDOhpa491%2B4AULc3%2BddlNDEj2mX9Bo5BJ%2Bf5e8znYQo0djttUmljxqKxTM88UHHozEr0xo8eZ9utfrtus474evgJN7ih&X-Amz-Signature=1cedc277aa4596ceacbae9aa7dd90e4dfcb0b9f0d6785942bc0d592fe4c91e39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQECBMWC%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQD3IIomMgn%2FBm%2FbZomQeROt5ku80GsURAGDb5Ny6sO2FQIhALdSdNOcHBq%2FRm84BVZ%2B4KN4qLUEZa%2B7DsjPvdovKl%2FeKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMWTieTuicadLDO7cq3AMra99rcYhIViEvU3aQHoPrsNo9HrNqOZCauYLysOAWvdSgcY%2FvwXTbeCnMRfyAR4O0MSXeYEGvPU%2B8PvvEMa7%2FTZzrAhcw9ywZM3eXhzVikLyhWUdlJf0CfThWY0%2FhicBIwmr35ZbzMdBfSHJGat3fgt%2BsA0%2F6IX%2FE5Us8GvvfIQahHw16x5rApcfG1oM7B50pfXegDYsZGaZ0dUaPDYSQdkVI4J8fEXopitdF0vPhrwYH0%2FX26FBQcJfWfPCW0s8Pz0Z6AbT3pPf78Bp7X6SdPJJdPQNsH9dPLzJ6eoBgYsdlH0V4%2FR4OgLIbyL7xzRMo0%2B8zi%2BZdoh2T6NLS1HuTKB3yuH%2BB0KWm1JPcWi5ncjsquuFN5lW%2BjYkJALo2yDAOYACljpXVxRXFbKXfRlNpWjfEP2axzPJD4lGLzKfBI8KXp9BmxJD9FLQl9hCBCSiOvsrATO2wekdxwr5InsSbkEOxG%2FEaWmEAhKDFYK1A2lE1H1BHAtCkpe3ZEssaeY5xmiBcbfW%2F%2B1UQ%2FhjmAXeQQreTgqr2c2bFcLlqOo7rioqlhpCOiupeLHsIusC6thXDTGHCmtysetrWvXu%2FkTIrhHInuYZn5m8UfkXmOjgp%2B8zP%2FHyzfqInl0qgQTC89dHOBjqkAVLYTVRj%2FXY2nXnrkLPYSZZa%2BK3O4Lplr0dn3JUo9pedQRLSdryQ%2FBlXy8LMmPutb419wp6AYEZoLwpmKXyhSpT9SJSbqB276S%2Fwka9VwVp%2BbcJ4P5b8CwtvhfJaJl60cDOhpa491%2B4AULc3%2BddlNDEj2mX9Bo5BJ%2Bf5e8znYQo0djttUmljxqKxTM88UHHozEr0xo8eZ9utfrtus474evgJN7ih&X-Amz-Signature=788c4480666d7acf073dd516ec2756cdd5bf6e3b607ed3b7cd94fdeb4ecb4823&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



