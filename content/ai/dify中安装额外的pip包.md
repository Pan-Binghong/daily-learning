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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMBKZUHC%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T030011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDnpACU7QZVjlwuZVYZXEoMtye9WHzuEulQVfmFVnJX8gIgOgRia9tCuEApJ4KAp6QCGKz4tk5qRhuFRgP%2BLCWjPHsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFIpo1H8%2FtlbBpGBNCrcA%2FX2FF2gx%2Fqssroxrf9OCCbwfz6BUNcY5EEGzmuXAVeLrh4%2FcK3t%2Bqtz9gfSMcP%2FMOGylGjP7wjpzFwgDWk1aGNuMc%2FAJiGJUX0d8cax1kqT2DfUR9MUU%2BuXdHv5W1N7hydEbaei0yrhaREbsPbSKZygCyu8Qc4%2BcYI8aGB67XqI8ebweaw5agjk1i%2BGAHx7OKkKn4tkyslnORyvu0gHpdUIh%2BtQOH66IX6O7ATo%2FoQmx3aml2aJJYgqjvzquexTXnhoMZiiw82ltMYsGZ%2FFJBLI28YxmDv%2F751GmHZ%2FoYCtiuS7J3Ipty1tCDvpzt%2F1kBHbvg5bQyw6fYEN%2FVo1qC9Bz4qiChJbZhl6FgE59mzrYPA71ftJ%2Bx1ly%2BBrONw%2BmqGtK%2FdFbT0ylCT83q11UvXAIQuDXhWy0BfHHYQiMxhAq1krbKS8kll3S9CTDxQayY9hg41pI7XAWZdMhkvXExq40YIqAw4nCAvJnityv57P97jJqQMNrFmpI8jS4LBsk2%2BeWVy%2Fr1ZodwWEGDuwHsHcUgBNubKCs4%2BAdRf7d8iwTlKHIsX7J90j99b7yTKBjhiimDxiAiFrGGMzHmp2kysKgJgCoi8cjfLeqQwBiQfTMNLwFnUp6PUojKSIMJvB3MoGOqUBfoEF8IAzhzk8LQ7UbPO2fCfMR8JOcUG8DaBm6bYn%2Be4iew4n%2BhH8dx7jwvQ%2BznP5BySvRS1GObCC47j4JNzxnqOr76l4C%2Bc55tqR4lehly5YbOOF%2FDkLxi7NbT8l6ynd0kv7ibxZx7PCRRdVVZo2FKY3QQAaWKJKhg0ThFW1v3AqPqfSWeJj8qryGN1KwM6jm5nBK4a%2FWRRphViUX9IPXBLdGm%2Fd&X-Amz-Signature=4c45a89def1c0ce35abd43f850414d6a6b7383a0979cf220d73c76f61e28a42f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

