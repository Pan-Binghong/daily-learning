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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/84c70f26-507f-4869-ac2a-5568d999fa76/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH2EJV27%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGUwka7hjHH7cro4bdZFKOHLOPjdPhl5piK2uJYhfQO8AiEAuR4hjoRtzozPJAqTTl%2F9Q5m3u%2BhCoVglOdLMOMWcTMIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwmCEM1ELvSsRralSrcA1qe3WWRjEmZvhsYge9bkz2%2FLd59taPYhHvUYF6%2FXqNfmY%2BG3h%2FUJpH%2BM%2BnHJunDG%2FxTjmvgbtEdEqPUFN9JSIspUzEsBfPWKmqC14uwBnRQqW3CwjORiWgnG9FadsRDwjxrvyrikGjd%2BabWpzrod1mqCm4tmaIIb98GNLMNYt3oWV2hBZUw%2BQu0iLyzwqKEbqUFFvHAy1M%2BCaPZu1p%2BCqCwImocEEqaJHjyIgFsEw2i4GIg0bgH02K32FOi1I6rH5XpRdQw3DOqKagms2dpXrcY00ydVcaF4uU6adkOqngzpRbzIqsRgmg6rKoh1YZTEe95qDLXBE%2F4cMtrZxbsKyKpQT6EOud2qaRPlE2fd0sahIVfJ4nXHJHrPcNsPZVjXakMkfUkQarHr%2FmvqzeNUKVs1Zg4DUVbtcMddK5Z%2FPQn6hgFLOl2z6sLtuECJgPkjFKoywLMDTY%2FBpwD%2F89tMteSY840Y7s52YcS8Q6AbY0%2Bi1FAVJRtcfJN8OLP%2BkDI%2BuCEZSOl0auTUP2QKfKs%2B9bo8RXUnaRv6O4HRT9tMxGYOD8%2BSob7kcvMExJnU7CvdpPXCnSGdkol%2F%2F2DNSFBK41J%2BxzsGjCQmra8IxGtZLYxdtTeFkCSrDu0pux%2BMP7ctcsGOqUB9QbxqyX0V7ZwbWSVp1X9FYyGsCL0ep5JRNgEo0yiXEALWiUb17BPBp9A24zS8f7q4aGDAkp6K4o8oYFYnPFEsJL2W2SRg6gSHjlNPP7WsdfDGFudJ24%2BM698dQtZTWTSO%2FQbcXpckPzOpoltbRDGXdusLqeiJ0sIAEVpQJS23I0RYOK7LST7iwoip%2Ft0ar1%2BFHE9nN76LImTNaWS4nt04nbPSafM&X-Amz-Signature=6dc2f9a7622f747d055244538bebaf90f91a875119cba7cda70f3125d342b4b7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

### 2. 配置

1. 获取API KEY | 在官网申请即可
1. 填入配置
1. Detail
---

### 踩坑

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/eedc93e7-7aaf-430d-918c-fa4fd03fa6a4/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH2EJV27%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T030834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGUwka7hjHH7cro4bdZFKOHLOPjdPhl5piK2uJYhfQO8AiEAuR4hjoRtzozPJAqTTl%2F9Q5m3u%2BhCoVglOdLMOMWcTMIqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHwmCEM1ELvSsRralSrcA1qe3WWRjEmZvhsYge9bkz2%2FLd59taPYhHvUYF6%2FXqNfmY%2BG3h%2FUJpH%2BM%2BnHJunDG%2FxTjmvgbtEdEqPUFN9JSIspUzEsBfPWKmqC14uwBnRQqW3CwjORiWgnG9FadsRDwjxrvyrikGjd%2BabWpzrod1mqCm4tmaIIb98GNLMNYt3oWV2hBZUw%2BQu0iLyzwqKEbqUFFvHAy1M%2BCaPZu1p%2BCqCwImocEEqaJHjyIgFsEw2i4GIg0bgH02K32FOi1I6rH5XpRdQw3DOqKagms2dpXrcY00ydVcaF4uU6adkOqngzpRbzIqsRgmg6rKoh1YZTEe95qDLXBE%2F4cMtrZxbsKyKpQT6EOud2qaRPlE2fd0sahIVfJ4nXHJHrPcNsPZVjXakMkfUkQarHr%2FmvqzeNUKVs1Zg4DUVbtcMddK5Z%2FPQn6hgFLOl2z6sLtuECJgPkjFKoywLMDTY%2FBpwD%2F89tMteSY840Y7s52YcS8Q6AbY0%2Bi1FAVJRtcfJN8OLP%2BkDI%2BuCEZSOl0auTUP2QKfKs%2B9bo8RXUnaRv6O4HRT9tMxGYOD8%2BSob7kcvMExJnU7CvdpPXCnSGdkol%2F%2F2DNSFBK41J%2BxzsGjCQmra8IxGtZLYxdtTeFkCSrDu0pux%2BMP7ctcsGOqUB9QbxqyX0V7ZwbWSVp1X9FYyGsCL0ep5JRNgEo0yiXEALWiUb17BPBp9A24zS8f7q4aGDAkp6K4o8oYFYnPFEsJL2W2SRg6gSHjlNPP7WsdfDGFudJ24%2BM698dQtZTWTSO%2FQbcXpckPzOpoltbRDGXdusLqeiJ0sIAEVpQJS23I0RYOK7LST7iwoip%2Ft0ar1%2BFHE9nN76LImTNaWS4nt04nbPSafM&X-Amz-Signature=3c9c9dbfb5987daedb80821d7b2e423cbf60cf0d8ce443b13c410324edbde4c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 解决方法
---

> References



