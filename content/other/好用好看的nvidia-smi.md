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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MBSN4Q%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFaL%2F3s9CH2HpewtoXxHOfctCf6d7863o1iSS8gEOXTmAiBYEc6Ix2dXbiaczhNa6LKcGd%2Bv2G2kCBm2lXU5nPhyHyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkwlSgL6cCadZb2HfKtwDoSrgRGgZ5fpARWsKQrWLT35l6nPNUFwL2Foh1HqmTnXJxuPgbn%2F%2F6%2BBnJ%2FrJrXybwO1hmZ5EGVXTv4UW7LeeqC3LFwDQd9%2BjPxejTdH40ftAW4rEC%2BbAvWz1itCCHJBZ6HMHGUhoWA4BTuxO5Zpexr6zsPESGeiK6RomtOx74Ek86%2BuY0NcyX5HWAX8uhOBh%2FvOGjb%2FS2BYaJJ%2Fq6nVxQ7luKYZ7M2hVtP9EqeqiO3K5w5m3eaOUYYiwBBf7qP5e5O%2FuUKoD65eggtZ3QR%2BGIJj5PLKyb%2FSJi70YS%2Fdr56dKavvbl4gUdu4Cmf4yUIyvrHxBAUTPPnVDCtP8M0wOQFyEhghENkq%2BNDEcViURRq4m9pV4R1s95JOqp%2FRhzv0G72N6U9sG6qTKrq4A4HP9KbRYbxEm9dxPnyUhLe20vGxKm1NlPRhDCkdktnmFO1pj%2BiOy67TeETRcZG0BPcgqjTiX8ScIVTG2QQW6As6%2FmgUPgunyYksx3Wxikc81M4i2hpry4QNVnfjQNqnWFDJ9ODLRiGvgiOTA%2FcsH0NEuzJLHHUmNkJo4EYBlVlTrga9uD7fRI0%2BfjzF%2F5PsPTejI5XQyxS2XaoFdK8bXtjqXr43B6lV6VB3qVSyTRekwm%2FicygY6pgF6AQ9L1aG%2BsuPeMXnbwqdru7WuQYzXfBEiFAGxmqbyFpkB5qwvvQK6ULvsw9pKzAUUN1MgP5AAX0rVhdRboqyF1TkKAHiJ2SiDo9hJnu9XSWn%2FFFDJVkf5oLYIvSsAhUJMi93XtpKIFwneR3h0%2Fz2IOKO7e7rGM2woFlIMpto%2B2vmwEdnwi3lYjpoFsnIh8RKo4O66ORTlcXu05t%2BRy2JaSMwrSNrB&X-Amz-Signature=53f2296c652a0b8aa3c3b34a9a6f4da313e01ba152fc8b2e5cf8565288201694&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7MBSN4Q%2F20251221%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251221T030149Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJGMEQCIFaL%2F3s9CH2HpewtoXxHOfctCf6d7863o1iSS8gEOXTmAiBYEc6Ix2dXbiaczhNa6LKcGd%2Bv2G2kCBm2lXU5nPhyHyqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkwlSgL6cCadZb2HfKtwDoSrgRGgZ5fpARWsKQrWLT35l6nPNUFwL2Foh1HqmTnXJxuPgbn%2F%2F6%2BBnJ%2FrJrXybwO1hmZ5EGVXTv4UW7LeeqC3LFwDQd9%2BjPxejTdH40ftAW4rEC%2BbAvWz1itCCHJBZ6HMHGUhoWA4BTuxO5Zpexr6zsPESGeiK6RomtOx74Ek86%2BuY0NcyX5HWAX8uhOBh%2FvOGjb%2FS2BYaJJ%2Fq6nVxQ7luKYZ7M2hVtP9EqeqiO3K5w5m3eaOUYYiwBBf7qP5e5O%2FuUKoD65eggtZ3QR%2BGIJj5PLKyb%2FSJi70YS%2Fdr56dKavvbl4gUdu4Cmf4yUIyvrHxBAUTPPnVDCtP8M0wOQFyEhghENkq%2BNDEcViURRq4m9pV4R1s95JOqp%2FRhzv0G72N6U9sG6qTKrq4A4HP9KbRYbxEm9dxPnyUhLe20vGxKm1NlPRhDCkdktnmFO1pj%2BiOy67TeETRcZG0BPcgqjTiX8ScIVTG2QQW6As6%2FmgUPgunyYksx3Wxikc81M4i2hpry4QNVnfjQNqnWFDJ9ODLRiGvgiOTA%2FcsH0NEuzJLHHUmNkJo4EYBlVlTrga9uD7fRI0%2BfjzF%2F5PsPTejI5XQyxS2XaoFdK8bXtjqXr43B6lV6VB3qVSyTRekwm%2FicygY6pgF6AQ9L1aG%2BsuPeMXnbwqdru7WuQYzXfBEiFAGxmqbyFpkB5qwvvQK6ULvsw9pKzAUUN1MgP5AAX0rVhdRboqyF1TkKAHiJ2SiDo9hJnu9XSWn%2FFFDJVkf5oLYIvSsAhUJMi93XtpKIFwneR3h0%2Fz2IOKO7e7rGM2woFlIMpto%2B2vmwEdnwi3lYjpoFsnIh8RKo4O66ORTlcXu05t%2BRy2JaSMwrSNrB&X-Amz-Signature=f525f83c65caa60ac63fa384967ba815a8fea2407504f035278380b9e79151ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









