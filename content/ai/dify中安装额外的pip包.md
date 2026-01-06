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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJQI2NT6%2F20260106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260106T025918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDo6wukfHS%2BKi54%2F10YzsXdvKaneiYd8O7OJjcAcqQSMQIhAMohJSzAT9xsLdr9%2Bd5uVL5YqTa9EbvvnBsMxQBp62YlKv8DCFQQABoMNjM3NDIzMTgzODA1IgzSPVtnoUBqMJxL30Iq3AN0IgbX6YX53iUpgaU38Qn0oKd8mzggZzl3IuF4C7dF65xCjbNVVMOcI%2F31a50UljAeIGLiyrvJO063yItu9OgsEUU%2FElTBu%2FKmf9PTY1FXcJ9s4HtH5LDtVrmBdgEhEeAz%2BDPXEsnqNh5l269T8KPEQpwJdr8CydKzGsXGFCxqS36RozAQuLxlwAsgwiRS1xmJ0CfiTTjfvjSgbrvDDdJQH3Wi6a1FtoRmtnnlKpCC1UA7Apf5e222BXtJjHgNXbd1qasrPi7L2kJyg8n7F5MhiVrffjclKwmMRw%2FxFIfoo2LCB3LrCsb4%2F7mHtXLgF5TD0um9a2kPRmsN0qv9sTEGbpCFZxv5pvE%2BHOjbdqiw%2BKVDD%2Bzy8gN0cJApSRh6KGTkBnRTPYGfOEfbX90RhWftuZ7zcNUQbOh92%2Bmir2r4tUgY1xJMOsXt3kp5viPq7g4vREl9Gwn23gHKhvvmzRHusHWre8lxrHRJIg9Sxtq13%2FNVrVPFqjT8AZKWczp0WK%2F1iu0bshWYwKcPzsPE7lRX0CbRQcB7w3EfJ3ulMOg6F6ErO%2FegD7MUTU2F980Nft%2BZMBmbUd0HbGZqReey6b%2BhnQNglkssN1nok1jwPNhhjDOvg5Y9oonfPc7xCjCe5fHKBjqkASKX6ozm0ElOyGGNY6nY1vmaGh3plfV2%2FqLuU9bklxFLB%2FzV7%2BYDsS0uTC7a1fyJsGu%2BL7J0YLdj0RtNtChyTr6DIOTX%2Fb3n%2FL%2BeL0FWYkR6RAhw5%2FL%2FBFlJiGcr1XAN8Q1CW%2BuQaBen8inBocuULKDZNUG4ZkbPZ%2BmCmw1hUkWQaSAG%2BXGrFyty6pyULSKWu2Az1hsw7MwyqPTEQIX3g9%2BM7CC5&X-Amz-Signature=1cb7976446e319ac3c3d0c27e4bcf767f8f3fb012d860b6dcade4162cfa5d504&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

