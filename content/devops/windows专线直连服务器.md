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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5EWD7DU%2F20251108%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251108T022637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCgyYOXh5YbyBNftbenRLi9WWTAhuTB4vuhvnvPpTYtsAIhAL9O6a9q1QD41QzkRghFRH6zmVrOXpCicwg1Vi2Ne1i0KogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwWQF5A6AcIajSePqYq3AP%2BCzvLKkMp1Kyncpk%2B3Pa6QIR73HEda4e7f91fXrqFQHjQyQvYZwtyRrfYsQOqsCd23TMwKbIg3w9%2FHI%2BU4ffqThGlTrYK1WnPUrB51ZCrEogWeUbSR%2BHaQ%2FK8Nl5K70ucoEtV3%2BqK3hJAUjGlU%2FuVmjADbZlBMef7RBRWr1udz8KRtPvt3%2BhkxDxehcnovh7oJpGv8kRZEjCdi0Gk508ZpCygHwudOS4y61patf6EC%2BHWH9rb9OGAUWpP0H1CWUv%2BIw%2FAjJQ3Bo0ss52KzzTxvG1etgYFNSORrz3pm9dnpLb%2FVR6iLO%2FcxYwb%2F03QOSeVDKnh4bKv40sthcYfstfCGETHvXs3A1EGkHxXnWhOQPKZyJgmcmEdwPdKqehP7KoYTyRzsJBY8vxLQYyyLFPYICcyI1TxoT5nCcUR2M0VUV1y1rSXOvj6ttzzGeGwvhH4SG65uGac3izpiXuoVEig4qYP4DJEmUkfw6jZhVT0e8yFefcKCDtRfwMu7QmiN1ea0qr%2BB9%2BOcDHxLWlx6tH%2BjqCyDBR3UnCYEa27r1sLD02T0xLHf%2Br7x0C9dW8BeBF9my4K%2BZjeNdY%2F3evrxqtGcDr1hF0jrziz12VJjDLmTkygRfBgF0lXcHxrSDCu0LrIBjqkARQTIzUEULB%2BqlXSe5O%2Bc7GagDl7aTGjK1xhtF0HlY15opQGZK3sgJkA9WaiOpYLX3E08fAdbJEVtUyvxDem5yduDEvnQJELAg%2Boz8%2BbNvu0CbcUU1%2F8QZVl2Wy4OfgFG%2FiDYamFT2cOOpPoGafEOc76KTzjV5A0vX8pukg36EMgbCnO1Et7k34FUZEuybVE3I121gsGRGlYcyHZAOTgdvj%2B%2B8c5&X-Amz-Signature=cbbbd79f9723cb6c74ac710c569591202938431a6e5d3f8c0d0e1b4ffa980ce2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

