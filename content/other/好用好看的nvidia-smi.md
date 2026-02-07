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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBXH63BT%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFS9JrdF62Uk0TGnT4Tp3imZQrdFF1KE089O5KU1xHo4AiEAnKxY98mPAStVYFNBhD6d%2BqoiQ%2FcxDHeG4J2Ve%2BhAm4Iq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDGu3Q4jF7cOoS5F58ircA9CfXagRe7Q4eX5wpGCnOMVpt7teSqDJuT%2BFvU5%2BWhtQK8Er9WoCsj0I8B2N77jhGnEcLNmHf%2B3Z9SBqah8P1u1tFMq585XFgiwWA3J9xuKLXK11zBblSH6d5hKBRhO0g1q%2B1vDMyBme8Q%2BNB8Kjugro4o%2BYw8L9UTLpOy2PSvhvN5DUZLUSu3%2Bg5dmt64Yd4mijo78l183QBt42VUEvnHOaZRcxGafonxW9w%2Fb8iDE3%2FWz8M2%2FJOXy6oDRnjGy9paYkN7y%2BJLIJYyzI9He60rUzNg%2FO1Rbq%2FOXgTjtbtX9jlyp%2ButkCmC7jsqBGGjIT4ZgpumxU%2FznEZ0aOUMfeooz6AQUVBeQZQbwmqaaSIgBuz8Mjna%2BIacUm5JDAsjSi1kYVWQ9ECqYNpr6ximjRX71Umd1RQr4lTeOfL0Ss0RPRuXWuWLHy9qWh34NS98WDbSvCwaLGff4YI2Lz3jUxdLbWO%2FhsX%2B173I5aHpbXg4BEbA1DCSWdvCBXjnSGI0L%2Bn0OBsXO5lxVOLNMcfQog5wzWVP3wSImRUHCOhyj9l8VELno3dBXMBnpR%2Bj2B173T%2B9ssqIkmabCIKFdfwVSh8oMJ2WzKJWbz0BN%2FZrVRHNp4R4GQ3E7salizzriKMJPEmswGOqUBmpRCumKOcshoiGq2yjbPxpzevqk4kdl0dw9W5onu8Bgoty3XFB7KJShaFgmG%2BD8k9U2R2K8ABjO3ZI2NqYZFGOH%2BsQ6hJDjWVAGRr%2B6rcILra32K3YPfgnrPyj5b7FaBAnfKDpTA%2BF5GcN0vgxDsg2b7FDKLNm6GSPJm0cAvipV0XPbSW31i8JcrnidcdRZL%2BxiYbOJgc2i2Tz1M43AYEnfFVypn&X-Amz-Signature=fb31309e10f250d3709f0544ef38fe7af3942079936c782b903a94b5c0f0ef8f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBXH63BT%2F20260207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260207T032835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFS9JrdF62Uk0TGnT4Tp3imZQrdFF1KE089O5KU1xHo4AiEAnKxY98mPAStVYFNBhD6d%2BqoiQ%2FcxDHeG4J2Ve%2BhAm4Iq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDGu3Q4jF7cOoS5F58ircA9CfXagRe7Q4eX5wpGCnOMVpt7teSqDJuT%2BFvU5%2BWhtQK8Er9WoCsj0I8B2N77jhGnEcLNmHf%2B3Z9SBqah8P1u1tFMq585XFgiwWA3J9xuKLXK11zBblSH6d5hKBRhO0g1q%2B1vDMyBme8Q%2BNB8Kjugro4o%2BYw8L9UTLpOy2PSvhvN5DUZLUSu3%2Bg5dmt64Yd4mijo78l183QBt42VUEvnHOaZRcxGafonxW9w%2Fb8iDE3%2FWz8M2%2FJOXy6oDRnjGy9paYkN7y%2BJLIJYyzI9He60rUzNg%2FO1Rbq%2FOXgTjtbtX9jlyp%2ButkCmC7jsqBGGjIT4ZgpumxU%2FznEZ0aOUMfeooz6AQUVBeQZQbwmqaaSIgBuz8Mjna%2BIacUm5JDAsjSi1kYVWQ9ECqYNpr6ximjRX71Umd1RQr4lTeOfL0Ss0RPRuXWuWLHy9qWh34NS98WDbSvCwaLGff4YI2Lz3jUxdLbWO%2FhsX%2B173I5aHpbXg4BEbA1DCSWdvCBXjnSGI0L%2Bn0OBsXO5lxVOLNMcfQog5wzWVP3wSImRUHCOhyj9l8VELno3dBXMBnpR%2Bj2B173T%2B9ssqIkmabCIKFdfwVSh8oMJ2WzKJWbz0BN%2FZrVRHNp4R4GQ3E7salizzriKMJPEmswGOqUBmpRCumKOcshoiGq2yjbPxpzevqk4kdl0dw9W5onu8Bgoty3XFB7KJShaFgmG%2BD8k9U2R2K8ABjO3ZI2NqYZFGOH%2BsQ6hJDjWVAGRr%2B6rcILra32K3YPfgnrPyj5b7FaBAnfKDpTA%2BF5GcN0vgxDsg2b7FDKLNm6GSPJm0cAvipV0XPbSW31i8JcrnidcdRZL%2BxiYbOJgc2i2Tz1M43AYEnfFVypn&X-Amz-Signature=636f82d51ab3a1a348c54321de5085c198fb75dbb65753fda4aadedf83fb88f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









