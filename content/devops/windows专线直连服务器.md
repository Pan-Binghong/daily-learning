---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W53QASST%2F20260108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260108T030005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA0aq37mpK60z7ANyfg8blZuGmrsulp2WQYsXn3TrogoAiEAgxuIdkoEVa7hPPo1ogJLX8UDC40wO7Z%2FAVlKbVV8KUwqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJbZl7XSYhANNJhnircAza2jHXNCM8rxhKYJZIOLQ0KEplBZ9oGlpv8JI1tT6L7hcwLnjA2CjrW53H%2BPpNipZjxL6R6VOWf2i8hrOcTtMF7gWwTRTa4vBsrsIS6tnYCeF7b7Y8H98WoxLUVxS8Npt1FGpOhxuA3rIA1BYW8i2WDuO2v37i8OCr186VPKAPSOFhkAPfwKm8i%2Fey4sFOdk0K1TP26FFwZuZ4SceBWJqEs1L5Hw0lxfHyyFYhYlJ2h1uDJFmxYZS8zJ0F8DOeKskZ0BAwJ8ZuBufiGVc8k5Y8m%2B%2FoexHt7vc4hXTSXNOYkVkheQSEWJvR5r5XOWBmbENztbR69mU3ymb%2BKI7XGZwqOPkxyzPCBtq%2BMNyI2R%2FtiXjWvP6H2AS16PV6qNDLyKWhbzF8RMVSd0SHosPNBSddUWjJKWXITst0pLuQ%2Ff39%2Fg9s12Ebndyz40b%2BwuKHkIixy15g9jsqZ484g6bzVykmAsOkDJO06f%2Fzaifxgk%2B%2FscsBKCxzuCHOKXDGMWkaugQaA9smkGlxDJrbbt1ovzs78tO%2FvMQK9gU7u6%2FqPAf7lDdr9BYkrha3G34ZcuyMBmpObg5WlYuMO8YLfwqOdLKdfoM9ZXU8Q4b6GF2IJq78hsfcKvgCugwEjUiDHMP%2Bp%2FMoGOqUBjZb4JiN6MnPp82WU230Aj5WFHezN0yH%2FR5ZbCo7uJ5DwPeBZVXc8izBc54bcTcYjk1jQ5Ju7Tms87TP%2Fvff%2BYatdvFNO%2F91vLKp1Qto2kEmd%2FTYQmTsCPP7swKoMepd%2F8nvJfbDjAoegKgovA6qq3FbJ6PUPEQGXMnWx7dIgVDx1xsP3FYRKeJhOEDaz108vN6BzVnLRbW7yWderJEgYL4MSbGjx&X-Amz-Signature=d6655dfdaef6e3c1a50ffa20c4c1fdc9d7eaacdbea9a99f2eea233356d0b7768&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

