---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
tags:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7SKZEW3%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T032932Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiosyGHh8G0sN8MBZVFr9wZU9KHPYEQmFq%2FqrVJZrheAIgK879DUqDH8Fo8o4rZP3UPoQyBCykFwYjn7nS0bMm3wIqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNM7HmJ0xW5vrHV8SyrcAx%2BkrgBP4YIMcIpw5Vq4q6jhTh6EpbNN9PqzzND2Tw6OgqJahpy3ZeU7g3WcEDcoNjaPCqsSeT4OnEdw5n8x5x8502Ad2BFISjnvVtEINR6kqx5cNWnHUAxmM5Zm%2F17%2BaFtrEbZl8RBFKZHD0MJpUCjrCH2tEUS7RTEDUBM84TnOhLA2lNsbRm%2Fy%2FBn%2Fng9ReFssW7Jk2aWlEeHju5JefMrlHYnoq8OgWAo4VxEWU0P2dG1IRhvWjsbpFzPaK8Z%2FAsXq95sv%2FbDTPDD2A7W63aS108d0UWSnxZa40jIG6K0HCIbGa%2FjblmyDqzHQlKlcD3OCXFvvsa7BqbNBqVz6UaDmT3duVt1XK4q6%2BFeGi2%2BPML3AyvinVk1bpB%2BVZuYgY3H9jPias6SMfBv0cMWwF2przVeCAfYgSqZSt8fXffCGiTorcri9ZMGPPTxn%2FT7CDgBcAZJxZmMYiks71LCWCuM6joHvpJS3hv17Df0KtvJLUSJ8EN7E8qy0zG82QPFd43bXPvi6xeCiWPZy07qw3RTTr2e177%2BKbH6mWHTmzs8miFwY2hl9L09de6D6UNTJp7vuKD5CU3PFqBzVz%2FyqT7c%2F6kCoMEG3ZLRlmHklruJceZimdsALZYqUsPvcMLvJ8MsGOqUBUj3gtBvUbA47GFpF6ql12htkzu6E6FeqRuJteAMgFgIRDQG9HceybxAsoEMyhA6s6M4o7S7YShyGDtO2dyGtTZWCZiYT5G5LhfgRnyk5avEf0Lwx4904SPFYEfGJCTqC73yBkUbrrDwGaof4c45%2BN6NrJmwtSxwjw9N0bOT6MZwUwTDnBpEbF5KDHSyKefzFp6OfKHGgJOhOOfmxuy%2FJwNDWrxw5&X-Amz-Signature=fe5d20e4f78ea747d81d87869933318d02da45f3cac3395e5a8e3ff2ed212797&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

