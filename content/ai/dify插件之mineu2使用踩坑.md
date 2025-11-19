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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYKE4TCG%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIHlbYNcuppr3umzCitEK5Ojk9zt8auQVe2WRpAXmoiHrAiB%2BTSIPr0IrvAyulOSlz4W5bL9MYswyJNgz0SjvCQlDKCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2FpLfS04HhR7%2FWH1KtwDc%2Fv8E%2BWVadrZ6qdlH92HHEyJEZ6leDdRDONBXFTYCmY6C2XmMFKb9P%2F2gkq7A6DtD4BCuNHCRQhplncKqplwKwEzxUxyDpA7RRjE%2F0Zfvqz2p3JlJWNtv9qx0mlIMuFCHke1Feeupo2wY11%2FvTzgj3ikt0RO3MGy7oFmpWtj%2FCo6DYUpeW%2BorIRUTVeUFrBpOwCwlLWxuW9ELsN2pOJPn8jNyWYNeXB0nHeS7vNCeZ23GyrZyps95yh15sAyFd2AmEW9Ybi0vA5sxtgGkMUPYctasnJQSp4%2FqfRmwfJmXlDlz2nuDaUmN1pWrp3srk5g71GxXJXwDBOFr%2FOU31pZwe4I9XsR8iVR3TemZI0gM5vTJ%2Fp%2FoN7d3boRZ2qHk%2BaKsQoM9EkmREY9jqtqopsiN6qW3vXL2DsvbJJdIS6CDfvX6JWNbGt2KRbIduxkulZTSGXd3LqJmyJQqjkqOOaj8%2FsTIAcb3dkNudow5PQzbkyna2MUTvFxFFsf0%2FWd3cQ1wehv0reXyc4d2ElitZU1s3kY0cAdh8N0ciVzOVGVlDhSL7gpMytHerwPCzHh04bF7DCqBb94p%2BtrqUzo0Qs1N4R%2Bj737ztPzN99WZUDtmdDAyQU399uZM2XRXaQwysv0yAY6pgET7XlwAyhec1WGTZnS2Y9KYssIwyUgSIwKarE7g2nXtfB6LE%2FjzKrCX2zZLl3HNQf4%2FJEYjbErYlGGrqcdxwLajPVhIsm2amoN599Qbr6hjkK0cpfOsAZeaeZYEii8tSw8QURRp3cTesicCzU1TSUMWPR4jl3jM9MUFBHYlfepCIEB1gQYtjgzY7sbjdwrEEGQmczln%2Bf%2B8dNkNEfO71ZQeq86o6QY&X-Amz-Signature=b3caa9cbcd08725c3e76820f11dc1512ac537a20f5f01243725fe32dbb89cb31&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYKE4TCG%2F20251119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251119T024405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIHlbYNcuppr3umzCitEK5Ojk9zt8auQVe2WRpAXmoiHrAiB%2BTSIPr0IrvAyulOSlz4W5bL9MYswyJNgz0SjvCQlDKCqIBAjT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2FpLfS04HhR7%2FWH1KtwDc%2Fv8E%2BWVadrZ6qdlH92HHEyJEZ6leDdRDONBXFTYCmY6C2XmMFKb9P%2F2gkq7A6DtD4BCuNHCRQhplncKqplwKwEzxUxyDpA7RRjE%2F0Zfvqz2p3JlJWNtv9qx0mlIMuFCHke1Feeupo2wY11%2FvTzgj3ikt0RO3MGy7oFmpWtj%2FCo6DYUpeW%2BorIRUTVeUFrBpOwCwlLWxuW9ELsN2pOJPn8jNyWYNeXB0nHeS7vNCeZ23GyrZyps95yh15sAyFd2AmEW9Ybi0vA5sxtgGkMUPYctasnJQSp4%2FqfRmwfJmXlDlz2nuDaUmN1pWrp3srk5g71GxXJXwDBOFr%2FOU31pZwe4I9XsR8iVR3TemZI0gM5vTJ%2Fp%2FoN7d3boRZ2qHk%2BaKsQoM9EkmREY9jqtqopsiN6qW3vXL2DsvbJJdIS6CDfvX6JWNbGt2KRbIduxkulZTSGXd3LqJmyJQqjkqOOaj8%2FsTIAcb3dkNudow5PQzbkyna2MUTvFxFFsf0%2FWd3cQ1wehv0reXyc4d2ElitZU1s3kY0cAdh8N0ciVzOVGVlDhSL7gpMytHerwPCzHh04bF7DCqBb94p%2BtrqUzo0Qs1N4R%2Bj737ztPzN99WZUDtmdDAyQU399uZM2XRXaQwysv0yAY6pgET7XlwAyhec1WGTZnS2Y9KYssIwyUgSIwKarE7g2nXtfB6LE%2FjzKrCX2zZLl3HNQf4%2FJEYjbErYlGGrqcdxwLajPVhIsm2amoN599Qbr6hjkK0cpfOsAZeaeZYEii8tSw8QURRp3cTesicCzU1TSUMWPR4jl3jM9MUFBHYlfepCIEB1gQYtjgzY7sbjdwrEEGQmczln%2Bf%2B8dNkNEfO71ZQeq86o6QY&X-Amz-Signature=0884605653491a4cfa28a67e1d4ef92978e3afcc829bfcaf901b2910ba2c2ae8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



