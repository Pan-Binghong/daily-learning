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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU2SKNDM%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIAQGR08ylB3%2Ba7SDsQPOrqtDEGv1s1MdIK89PYcaXp7%2FAiEAqxdygwTZsWwYjv8PG%2Fl%2F%2FKWUKauVMn1QonnGCLgrYBsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVnvj0J2cwdXXBuUCrcA4P2TszG%2FioQspVLq1oJIpro%2BQCa2zKGB0xrG5wVRC%2FvYluWJ8l4kzoV2W3V1DmfmCO8kWfZjrCdG79QrbHn4JWDUxDcNzopFoTyjNP5S5Uhr6JbHTq7yAoS5UKLfMPFW798Y6MX7vYqSMLzSfAZGxkgjnwvzUTEp3pUmRMXdTQwpQDbBfK2JhA7x4cujZbTykfvdz8HyP2cvjV4pp79ZPQ5CBSIbmnTZOJJFo2QeqL4evi27%2FxzfSSuq3lOiPmPsQO8vz4ksO%2Bd6%2Bogjgt9ze%2F3GkBUcirIgpU%2BAWC8YjVQHps3caL%2Bo1Dd29lnLiXGmlk1rbgEfKZhDbu8YXFzKbMgj%2FtNKqux%2BK%2BUF68EG7IOsy9USrprzVR8xArihXtWsDsXK3%2FWGSagsMni55j6BhlYa73%2BSDVRdQSvmtONddPxWJonLDmvojfXzWiY4ZNpZdHmVIO3DEVI0s6vlfNTm4qwAMwe89kMBiQ4FPi1pdBcCbi2kR1WICBFynGeXnqu3GXSU1YyPm13ViIZVU2giQZxTo75n9ieGSl2kfrJXNOWE7i5Z1Zgxth1P6jtjZYU8TYcwDNGieDbuLaPlBSY%2B%2FAXrupeDcD7OKhai%2BPRbVb7GYjATVzTf5iLgELpMMWuy8sGOqUB5k6p409TZiz9miH%2B38wKDbbxdFc4NiScZCCiWOAKzXYNvQcEwY%2FGJUaGZoydAbwpXhuJBUDMw3blwocKmuq%2B26oxOObwr2zqlvcwEj3G8eNk4V8vnTVgKrR1JV%2BtN7PWPPJj%2FSRyE9pDQrE2FaXKY9TLN1EwbrRH2mYs%2FgV6U6nIu%2Fa2vutuLKY3Ij32awKtCHhJcfiu87XBkOrIQj9CFzZeWJ4m&X-Amz-Signature=06265b987681fde8da155f714228379937b41962bc5ecb1a3f9f48e0e073848e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU2SKNDM%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIAQGR08ylB3%2Ba7SDsQPOrqtDEGv1s1MdIK89PYcaXp7%2FAiEAqxdygwTZsWwYjv8PG%2Fl%2F%2FKWUKauVMn1QonnGCLgrYBsqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVnvj0J2cwdXXBuUCrcA4P2TszG%2FioQspVLq1oJIpro%2BQCa2zKGB0xrG5wVRC%2FvYluWJ8l4kzoV2W3V1DmfmCO8kWfZjrCdG79QrbHn4JWDUxDcNzopFoTyjNP5S5Uhr6JbHTq7yAoS5UKLfMPFW798Y6MX7vYqSMLzSfAZGxkgjnwvzUTEp3pUmRMXdTQwpQDbBfK2JhA7x4cujZbTykfvdz8HyP2cvjV4pp79ZPQ5CBSIbmnTZOJJFo2QeqL4evi27%2FxzfSSuq3lOiPmPsQO8vz4ksO%2Bd6%2Bogjgt9ze%2F3GkBUcirIgpU%2BAWC8YjVQHps3caL%2Bo1Dd29lnLiXGmlk1rbgEfKZhDbu8YXFzKbMgj%2FtNKqux%2BK%2BUF68EG7IOsy9USrprzVR8xArihXtWsDsXK3%2FWGSagsMni55j6BhlYa73%2BSDVRdQSvmtONddPxWJonLDmvojfXzWiY4ZNpZdHmVIO3DEVI0s6vlfNTm4qwAMwe89kMBiQ4FPi1pdBcCbi2kR1WICBFynGeXnqu3GXSU1YyPm13ViIZVU2giQZxTo75n9ieGSl2kfrJXNOWE7i5Z1Zgxth1P6jtjZYU8TYcwDNGieDbuLaPlBSY%2B%2FAXrupeDcD7OKhai%2BPRbVb7GYjATVzTf5iLgELpMMWuy8sGOqUB5k6p409TZiz9miH%2B38wKDbbxdFc4NiScZCCiWOAKzXYNvQcEwY%2FGJUaGZoydAbwpXhuJBUDMw3blwocKmuq%2B26oxOObwr2zqlvcwEj3G8eNk4V8vnTVgKrR1JV%2BtN7PWPPJj%2FSRyE9pDQrE2FaXKY9TLN1EwbrRH2mYs%2FgV6U6nIu%2Fa2vutuLKY3Ij32awKtCHhJcfiu87XBkOrIQj9CFzZeWJ4m&X-Amz-Signature=1094b08fdcfffdc5a5413301ae49c9976668c2a54b9f314c76247568f13f1bb9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



