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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/167921cd-a496-4b4d-8768-9b56d39ca4ed/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4YKA2IX%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGNRalfKEBYFczVXssnCzLoUKfht2qGL8a3Cu6o9NMuIAiBdOCYaiz95zvBQO7P5k3kzgBZsSF9TXnyh4VyqonPNtyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIM5E%2B9VZht9aSXUpr%2FKtwDDQwi%2BFgIlNdBXAbufVW6uqdAkZWkbsDzofyXjFNnlsB%2BFPWogHvp1889Rl%2BhXSfXsiIRROAgmDERqipzD4hS8%2BjgEi7DNVYFLH9Pgupzf3%2FxEPeLph0Q8a69UYdkvot8DVcKRWvSpaoE4xVp9GEV4fRN138UdUJ9RY9g4heuXj27VS2yOSt72rI%2BrLsEBXnZcOhDYlCeDdiClKo1oAyMFG3UytQZkVV%2FqwrVUilF1P0l0WDjtyUtk30k6VBsHEvb9Ma88ER0zT663%2Bx9%2BIoRHS9GMDjfg4d9SdCcAUKIezojKg%2B4TcdCDpft3oIy793vPN8pMiMAloLDU7PySe%2F13WbG9tKYrrIOubRy%2BHdh%2B96LouAm8k6RyuSuQjUSzv2R4vgEh%2F%2BXrbZMjZHFkWiqhxEP2xnI1%2BrlUw5HxT%2BiF1yAn8e8O71UI47Y6WnLMo4LIRU%2F2PWR6mH8%2FkV0gVDK2WX9NcC%2F0%2BkSB3w7HUJl5RQ8usu9zuMzDLsoO6OKoyoJDi0u90MhE%2B6QFZTIN7V7h6nf%2BFSzQD7yuqGsbPyLrLvYQekfgmNXelaPnWtmLatluuvt%2BxzzP6CliEuiVhk684fxjRByDq1WeafCgnjuU6pCZHeKig05Wpj%2FQqEwzZWJzQY6pgEjU7ERZuvULBfMhgvuknzFcN55ckcBZXfQlZwQhurzbTC8tpkBgxcuwjxD%2BmoWFIE7FvN2kSFImj3ZtjiWy6FpujCvTwjwrCfJQPcBbNAvwN9ngI5HE5c8LnTG2g2NOiSr6f7ZqIDGKjk1Jd7OZWOfys5IleOFH6s6pKjaN54LDdFKLjrqXIpdMgg3oELCK7H85oNLDp5%2BaVYyK0CiSjLa20RO7psb&X-Amz-Signature=11e8ff177a314a2f438283d5501ec1d03148a90c3e5224c7a80a88e063794a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/38595db5-5c7e-4dcb-ab27-48bf45fecafc/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z4YKA2IX%2F20260228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260228T031330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGNRalfKEBYFczVXssnCzLoUKfht2qGL8a3Cu6o9NMuIAiBdOCYaiz95zvBQO7P5k3kzgBZsSF9TXnyh4VyqonPNtyr%2FAwhLEAAaDDYzNzQyMzE4MzgwNSIM5E%2B9VZht9aSXUpr%2FKtwDDQwi%2BFgIlNdBXAbufVW6uqdAkZWkbsDzofyXjFNnlsB%2BFPWogHvp1889Rl%2BhXSfXsiIRROAgmDERqipzD4hS8%2BjgEi7DNVYFLH9Pgupzf3%2FxEPeLph0Q8a69UYdkvot8DVcKRWvSpaoE4xVp9GEV4fRN138UdUJ9RY9g4heuXj27VS2yOSt72rI%2BrLsEBXnZcOhDYlCeDdiClKo1oAyMFG3UytQZkVV%2FqwrVUilF1P0l0WDjtyUtk30k6VBsHEvb9Ma88ER0zT663%2Bx9%2BIoRHS9GMDjfg4d9SdCcAUKIezojKg%2B4TcdCDpft3oIy793vPN8pMiMAloLDU7PySe%2F13WbG9tKYrrIOubRy%2BHdh%2B96LouAm8k6RyuSuQjUSzv2R4vgEh%2F%2BXrbZMjZHFkWiqhxEP2xnI1%2BrlUw5HxT%2BiF1yAn8e8O71UI47Y6WnLMo4LIRU%2F2PWR6mH8%2FkV0gVDK2WX9NcC%2F0%2BkSB3w7HUJl5RQ8usu9zuMzDLsoO6OKoyoJDi0u90MhE%2B6QFZTIN7V7h6nf%2BFSzQD7yuqGsbPyLrLvYQekfgmNXelaPnWtmLatluuvt%2BxzzP6CliEuiVhk684fxjRByDq1WeafCgnjuU6pCZHeKig05Wpj%2FQqEwzZWJzQY6pgEjU7ERZuvULBfMhgvuknzFcN55ckcBZXfQlZwQhurzbTC8tpkBgxcuwjxD%2BmoWFIE7FvN2kSFImj3ZtjiWy6FpujCvTwjwrCfJQPcBbNAvwN9ngI5HE5c8LnTG2g2NOiSr6f7ZqIDGKjk1Jd7OZWOfys5IleOFH6s6pKjaN54LDdFKLjrqXIpdMgg3oELCK7H85oNLDp5%2BaVYyK0CiSjLa20RO7psb&X-Amz-Signature=ff4debeeca13a51620e7b52520020dcc2a75b9e8fa4408a7ef147f9e882185e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









