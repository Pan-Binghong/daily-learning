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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOA3PMYR%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB8xPfg8Tf7uhlZNTIj2%2B7Bk8bIw3qL04XSdp5%2FLuvm2AiBh9Csut%2BQLPmVPVM%2BARAPlPFlFdlKCpUbcG1VoQYUqlyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMgOSyHP1bhgpMIZPfKtwDREm8k7W6ES8VnxkEs3TTXPZMPOMfkYCKvXZX3R4HUqMeODZYeDOfBDUfshvRFfV7WfBsE8o4MXfMHLef11050ulOjNLcf9SIBbYARXzvPnVW0pzO3HP6AXtJsu%2BbNYMugEpiqnAxvROLTfqHXudlT6UxhjiFICDMR4pS%2Fk3%2FlEx8SlD6khkG7pfvM8EFSaMU9%2Fu5Hgpj7aQl%2FXBfFs2d8R%2BUs5xNvts0IBwbrh4e2YIZBp9OsF21jLMTJtslC5GB8CLQidu%2BU1W1A0kOxUoTWB1s%2FP6mLpcPQ0OGGdOTaLxpVCQ3GHo0j5UkIAw0NlUpX4lSqfsSPKfCYF1irjl5Ni7vo99y%2Beqhb7x5kSptJU8SQ37ESbZlfiyHF4UIduXUvDkISYANHp4d%2FuekVPpu9mA5Yb1Gz7vijXLN%2F5WoRTisofIl57gxMOIXUUzH3oNym3YSRLfZkTaODypzGPx6wUs50a%2Bz2Q1KjcxDBxKjAXYYEKg%2FZtEizcXaSBgUSG3aRqK6%2F%2Fli6Cu4z2IwQejnlZJoX9oxSFjgGfsNlMlDFj8N3ulWWstJDSEYO%2BlqH027eFafY30HezYHfhIYFdhejbyJzhi2BShR11cTxDjZHLyXcIBxHBe%2B6Tr33twwvvCbywY6pgGYAQxF0X5YjH%2BHi9PWnVDvNS4%2Fl6L1sc4OJQH2rTnnoY1lPZAonZIneJHFQP1NNq%2BhjxcfqjGMNOObwMEpE%2BXSqnVsWIkii6tz88h%2Fcef8xueyAeE6kiec9IkUzD%2F9WiZR0t%2FOUo6a86L9Xm3AlPeCQGEmgw%2BeiueL7ePLc%2FjHMZb11wZcC4Q%2FlPiBSkuk9577R3W9FFfSWhHw4WL0xDAAz4fXFBaS&X-Amz-Signature=0020f202fa96478dd4cb6c961d1529e7ae3fb0028adbf094ca7041242dae8fde&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOA3PMYR%2F20260114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260114T030633Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIB8xPfg8Tf7uhlZNTIj2%2B7Bk8bIw3qL04XSdp5%2FLuvm2AiBh9Csut%2BQLPmVPVM%2BARAPlPFlFdlKCpUbcG1VoQYUqlyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMgOSyHP1bhgpMIZPfKtwDREm8k7W6ES8VnxkEs3TTXPZMPOMfkYCKvXZX3R4HUqMeODZYeDOfBDUfshvRFfV7WfBsE8o4MXfMHLef11050ulOjNLcf9SIBbYARXzvPnVW0pzO3HP6AXtJsu%2BbNYMugEpiqnAxvROLTfqHXudlT6UxhjiFICDMR4pS%2Fk3%2FlEx8SlD6khkG7pfvM8EFSaMU9%2Fu5Hgpj7aQl%2FXBfFs2d8R%2BUs5xNvts0IBwbrh4e2YIZBp9OsF21jLMTJtslC5GB8CLQidu%2BU1W1A0kOxUoTWB1s%2FP6mLpcPQ0OGGdOTaLxpVCQ3GHo0j5UkIAw0NlUpX4lSqfsSPKfCYF1irjl5Ni7vo99y%2Beqhb7x5kSptJU8SQ37ESbZlfiyHF4UIduXUvDkISYANHp4d%2FuekVPpu9mA5Yb1Gz7vijXLN%2F5WoRTisofIl57gxMOIXUUzH3oNym3YSRLfZkTaODypzGPx6wUs50a%2Bz2Q1KjcxDBxKjAXYYEKg%2FZtEizcXaSBgUSG3aRqK6%2F%2Fli6Cu4z2IwQejnlZJoX9oxSFjgGfsNlMlDFj8N3ulWWstJDSEYO%2BlqH027eFafY30HezYHfhIYFdhejbyJzhi2BShR11cTxDjZHLyXcIBxHBe%2B6Tr33twwvvCbywY6pgGYAQxF0X5YjH%2BHi9PWnVDvNS4%2Fl6L1sc4OJQH2rTnnoY1lPZAonZIneJHFQP1NNq%2BhjxcfqjGMNOObwMEpE%2BXSqnVsWIkii6tz88h%2Fcef8xueyAeE6kiec9IkUzD%2F9WiZR0t%2FOUo6a86L9Xm3AlPeCQGEmgw%2BeiueL7ePLc%2FjHMZb11wZcC4Q%2FlPiBSkuk9577R3W9FFfSWhHw4WL0xDAAz4fXFBaS&X-Amz-Signature=6bb3fa5d3a2d5c27d49a700c93140acf11849dc23bccc1d27ea908e2b7886bdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



