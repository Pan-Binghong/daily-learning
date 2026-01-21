---
title: 基于Huggingface镜像网站下载大模型及数据集
date: '2024-10-29T01:52:00.000Z'
lastmod: '2025-03-20T00:51:00.000Z'
draft: false
tags:
- LLMs
- HuggingFace
categories:
- AI
---

使用镜像网站下载大模型及数据集, 以及配置下载参数(本地路径等)

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/dc82f140-d63c-44e4-bc53-0bc220caf11f/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT53LMTE%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJXZtWP5kKTvthZgXDX3oCCWlv1QtE3isx29LXYqnywgIgXc00jxotgio4o0Wa3oS5wYeQFgowLiMV6RdcMmFdkNwqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4ck%2BffY1UXUOuGMSrcA0KzU6UJz9fxV6v29ePRoIYnqotlY8Wa4T8UeteZPW7NAcVGIJpQWuRUsFD%2BVp4d3IdbOyqy0Dvaaf%2BTUgsSArdzrlhx3%2BkZkJURgRR0KbvIst7eujYo9KkzzAl8dJDZyy1PEU8hhW%2FAULn2wLqskLtRaclcez5Viaag%2FxN3SRFMYo2NXUCpaVthmtw67IjP1eC%2FZDpXtFQ8R8rOl%2Ff5cz6fu7m3dzavpjLob%2F%2B08cpneQC3TX1tmIUhOdtK5bdeRb446X9cWPlOt33v8P46OlmwuSjysCcLJL7%2B2nrriyJcQrEs%2FTNhigJcjC%2Bo1kDBUfo5V4GpgsbaelTul2eSJQfCQqV4j7kJDHYIpjUGBoNRWh4fU0WGhf7QlG%2F5BRPgs9ohGvgTrGZBblkfmIFJ9suNNyKB3sRomaU%2FXdWvTt0hCoDu%2Bb7RWzzTEf25dunLE1sMo5WdcY2FBvmb9ORlGE8i1BscHfzn7ZZeiXYsd5h%2BdYfBML%2FiPUHYm%2FxrlUBOWfTckrSnlPseVuTU00Tns0qMXa35IfvQn%2B733w68ZmKl%2Ff3CBUVfXNHQqWP0T5KIV%2F5acW9QLtWAc1e5%2FxDpNRcxej%2Fqt6QjvkEllXTVzgdTtAdvmRh8P4a6ChQQMKTawMsGOqUBkb1AsVnXMdUZzRdzRntJcG96ngHi5%2F0amNtC3t%2Fow5vM%2BTev%2Fb3GRNIEMH3k3uKIzbzMu3IC5ksa3qdMECBvhSuk%2Boai3R6PdztjV5%2F8hY2XkBpOHUfkO3MdfC4yBMOi98%2BWVporgWymzBm5e9TtdgOj7oMbXyEgmHcYa3kCwnh%2BTo0T8D4kCy5bs%2FrWvS%2BQoSD9HDATCVgMj%2FPLyTXDpKqHlPGn&X-Amz-Signature=1c41daf39743df534074e9dc9bde82ae5450e048b5b3f60d7a6c53577357114b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 基于HF镜像网站下载大模型&数据集

### 命令行下载

- 安装Huggingface依赖库
- 下载大模型命令
- 下载数据集命令
---

### 代码下载

- 首先获取Huggingface的Access Tokens
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/22b8dae9-3302-4380-a23f-5402b524f0a9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT53LMTE%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJXZtWP5kKTvthZgXDX3oCCWlv1QtE3isx29LXYqnywgIgXc00jxotgio4o0Wa3oS5wYeQFgowLiMV6RdcMmFdkNwqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO4ck%2BffY1UXUOuGMSrcA0KzU6UJz9fxV6v29ePRoIYnqotlY8Wa4T8UeteZPW7NAcVGIJpQWuRUsFD%2BVp4d3IdbOyqy0Dvaaf%2BTUgsSArdzrlhx3%2BkZkJURgRR0KbvIst7eujYo9KkzzAl8dJDZyy1PEU8hhW%2FAULn2wLqskLtRaclcez5Viaag%2FxN3SRFMYo2NXUCpaVthmtw67IjP1eC%2FZDpXtFQ8R8rOl%2Ff5cz6fu7m3dzavpjLob%2F%2B08cpneQC3TX1tmIUhOdtK5bdeRb446X9cWPlOt33v8P46OlmwuSjysCcLJL7%2B2nrriyJcQrEs%2FTNhigJcjC%2Bo1kDBUfo5V4GpgsbaelTul2eSJQfCQqV4j7kJDHYIpjUGBoNRWh4fU0WGhf7QlG%2F5BRPgs9ohGvgTrGZBblkfmIFJ9suNNyKB3sRomaU%2FXdWvTt0hCoDu%2Bb7RWzzTEf25dunLE1sMo5WdcY2FBvmb9ORlGE8i1BscHfzn7ZZeiXYsd5h%2BdYfBML%2FiPUHYm%2FxrlUBOWfTckrSnlPseVuTU00Tns0qMXa35IfvQn%2B733w68ZmKl%2Ff3CBUVfXNHQqWP0T5KIV%2F5acW9QLtWAc1e5%2FxDpNRcxej%2Fqt6QjvkEllXTVzgdTtAdvmRh8P4a6ChQQMKTawMsGOqUBkb1AsVnXMdUZzRdzRntJcG96ngHi5%2F0amNtC3t%2Fow5vM%2BTev%2Fb3GRNIEMH3k3uKIzbzMu3IC5ksa3qdMECBvhSuk%2Boai3R6PdztjV5%2F8hY2XkBpOHUfkO3MdfC4yBMOi98%2BWVporgWymzBm5e9TtdgOj7oMbXyEgmHcYa3kCwnh%2BTo0T8D4kCy5bs%2FrWvS%2BQoSD9HDATCVgMj%2FPLyTXDpKqHlPGn&X-Amz-Signature=ecc8eabec0174ce258d80bc594e9de0d72554f47e998a85bc9f1021213ca1633&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 下载代码如下:
- 下载数据集代码
---

> References



