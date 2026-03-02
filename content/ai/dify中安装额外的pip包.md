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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSM6HMOR%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T033225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC40gFXiIpiG1toCqGietxZjeOp3eVCs21zpNoGFMXO9AiEAgdWbLdRSB%2BWhTw3RLNmjooKxZA5JFS2GWK3b2OlNd%2FIq%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDFfzEV9VFexxQ3xDGyrcA89QKtyp8ksilhC0EPUdX6c26Fw%2BAhjbqgyva8ZTaH8%2F5eO8HpvCph2eENMAuQVfsTUc7xtEsnq3VPAm6QLVXC79PEjapYXc%2FPQiQ%2BKvqEwJaWY50NEkM%2BUeJStmpnS7UGcwg0ZS1ZUKcEntFvMylEgkXQfZ6XlqgK8vimYXj6IEKxIKQYdhmrug5FSpJMMYkrF%2BbEqIu7m4brhg7Br7khIJ2uokeu1qfVNL33FEg4TFSvxBMTdATLUk%2F2z%2FMGj3kA%2FyTKg04Y57RpF1LV7hI%2FMX6MXwZ%2B2hdvTNhoFatButTQUEUFRZ3xb6q0LjuGJLxHSNVN1jy6g7SYML3ppzk8XzBCH4VC0HSvZB6QjZIOpVaMJMneatQ4Eox4GZtwJhKwB9MNeSLneLJNIBsfo96rcz6SZ%2F2C91F7dG8vwAJt7pJpksXzsIiCeaPymnswAPF3utaLsHOev7Q1MhtEaU0S%2BFVBg0DlPnfd7Et1SZC1VU0IS%2B%2BJlw1QHA2az%2BaaGvoilwSOgG6zgnZi5QZHCAD2zOMG5Tx1FQvwUJ0imBBa7yFAr%2FRba74ou8YKna3QGcqoIgdy6ck5PBjzgBkFjOI3ESjpCeUpfrIUrM6HpXC30XY76wggKmrusfGLprMK%2F9k80GOqUBBy%2BTiztpsjRfbd%2BRmh%2FCwcAzsMjZotW4WhGxKBOLNTDG4RJyGjcM2ROgKvyUVIh4yOQ0etZT03ZneJUGndwXPbfKgRF1ZuUZyGBYRTmYibtdvq6aTXi3f479zrNpYPzVWH8ZTdDvqmAT5jWN%2BVnoi5EGAWb6r3dinPCEx6%2BwGncgnOD9bA0YrsjPCZ7vZxdJx%2FkeKfj%2FUZ7ilKA1%2FbduI9aDfGM0&X-Amz-Signature=5a16bc799b240ab33e61013243bc06bd682da185c6021e38eb2a24b083c289e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

