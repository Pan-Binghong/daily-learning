---
title: 好用好看的nvidia-smi
date: '2025-03-24T16:02:00.000Z'
lastmod: '2025-03-25T02:21:00.000Z'
draft: false
tags:
- Linux
categories:
- 其他
---

> 💡 找到一个比nvidia-smi展示gpu更加美观的工具。在此记录一下。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BF3Y2J7%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcW4ggmkxsxSicxtI%2BKxma%2FasUtdXPaBRX1cLGi0M7AAIhAMZE0mNo4UXWm5i0bS92enIR2D77mxWeHHNK16g3NLiEKv8DCHMQABoMNjM3NDIzMTgzODA1Igz5lokl7zNyvxOPcMYq3AMn%2FsjquJjt9EfjwetGEMMLAJrr%2BKxsGZnQb80g4nS4WWB2Pb9j%2BDjfaAZTPeSB8EBqf4%2FAuz0c3RKUNRpSmDXVfsY2m%2FwYyfb7TOxoa8vIoYwhpC0cFASGe9nD6SW8SgVYnLrp4inDqHY%2BZkgOzmiVVAfJQSBAPwNMaPiRg6WaJMruivLXuV19NNb3PhOIoGq26V0p8gq52FiziDT0hieDeNBSc4TumDR3H1a7zIJVtrqzM4LB6omohGREAtYDuxuo9byWEvRXKQeevoBVwIbYWMO%2BFWiHWCUno1UGGEOdP7jN2wnDA2l8hpsFJMuX08HfFfM0%2Fj3GkukjMJ%2F0HkGvc7%2FGfBhU%2B2RZEkv9SqO2zKH6fF71ZxUAFBLtaMZWFKw9wvQhBDaYcsciX%2BjIS2g%2BH9wFq7eSwZJ%2F2lsA8L4XKQbRnb%2F%2Bv5Uahmh9Nm5x0O1%2Fb8Jiu0GhejckZgOzOyeI25i08QYp8UOnc3EOumZcPNLaaQw1pod0Ojp4eTIzCtw3fU6GgUd%2Fb2QSwhr8D62C9WjC7%2BafA6BXkh%2FzyZWsP0EmhTkqNomDAKF3Xz745cWq9l3Ybwl97ZyBEZl6aHjbIxc0BB38AtiL2rK9YlXyDbn0s9P%2FLmY2SS5k3DCwwN%2FIBjqkAaxtGEOjUTl1ZYSTeeYA9PZpVzGoS4CF1LMVDnVXmP0IQKU31D9gYYtwJVKfdOaeGYx7DDY%2FUhScBlThtSGV4aT%2BpEpkdf0eI%2F8brjx4pybfUx4AUgDyS8Dt6kmOGuzgOcDeiGpBBKeJUWrMNntzVpFRCWuNOw0ulANsLyLoerv3TdJm3KqyWgBIUbsmv5HNo7AJm%2FZ%2BojJ5fuA9piSq00wzELxu&X-Amz-Signature=6fea8695af50a4134cc36bf6dac1b8aac86775166dd6d6ba50c6af8fe8ff85bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 安装

```python
pip install nvitop
```

---

## 查看gpu状态

```python
nvitop
```

> 查看更加详细的gpu内容

```python
nvitop -m full
```

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664BF3Y2J7%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCcW4ggmkxsxSicxtI%2BKxma%2FasUtdXPaBRX1cLGi0M7AAIhAMZE0mNo4UXWm5i0bS92enIR2D77mxWeHHNK16g3NLiEKv8DCHMQABoMNjM3NDIzMTgzODA1Igz5lokl7zNyvxOPcMYq3AMn%2FsjquJjt9EfjwetGEMMLAJrr%2BKxsGZnQb80g4nS4WWB2Pb9j%2BDjfaAZTPeSB8EBqf4%2FAuz0c3RKUNRpSmDXVfsY2m%2FwYyfb7TOxoa8vIoYwhpC0cFASGe9nD6SW8SgVYnLrp4inDqHY%2BZkgOzmiVVAfJQSBAPwNMaPiRg6WaJMruivLXuV19NNb3PhOIoGq26V0p8gq52FiziDT0hieDeNBSc4TumDR3H1a7zIJVtrqzM4LB6omohGREAtYDuxuo9byWEvRXKQeevoBVwIbYWMO%2BFWiHWCUno1UGGEOdP7jN2wnDA2l8hpsFJMuX08HfFfM0%2Fj3GkukjMJ%2F0HkGvc7%2FGfBhU%2B2RZEkv9SqO2zKH6fF71ZxUAFBLtaMZWFKw9wvQhBDaYcsciX%2BjIS2g%2BH9wFq7eSwZJ%2F2lsA8L4XKQbRnb%2F%2Bv5Uahmh9Nm5x0O1%2Fb8Jiu0GhejckZgOzOyeI25i08QYp8UOnc3EOumZcPNLaaQw1pod0Ojp4eTIzCtw3fU6GgUd%2Fb2QSwhr8D62C9WjC7%2BafA6BXkh%2FzyZWsP0EmhTkqNomDAKF3Xz745cWq9l3Ybwl97ZyBEZl6aHjbIxc0BB38AtiL2rK9YlXyDbn0s9P%2FLmY2SS5k3DCwwN%2FIBjqkAaxtGEOjUTl1ZYSTeeYA9PZpVzGoS4CF1LMVDnVXmP0IQKU31D9gYYtwJVKfdOaeGYx7DDY%2FUhScBlThtSGV4aT%2BpEpkdf0eI%2F8brjx4pybfUx4AUgDyS8Dt6kmOGuzgOcDeiGpBBKeJUWrMNntzVpFRCWuNOw0ulANsLyLoerv3TdJm3KqyWgBIUbsmv5HNo7AJm%2FZ%2BojJ5fuA9piSq00wzELxu&X-Amz-Signature=447c65b8e473e8ac61d9447b000e8c19a3f145c41efb0cd4e7b1bedf2d6c43eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









