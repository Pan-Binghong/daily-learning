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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFDBWOWZ%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T030221Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJHMEUCIQClGv1onFjRYcgOifG1WgLEoBz%2FpTG28LNeuYyh8hMYLAIgVZXxENt4V3h2DVory9O2kA%2Bn8HzdWcVMqo3x%2FkV4UUwqiAQI7P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFFh8k2JRwtLrtlVJSrcA0ExeYevZGOumiY5t171sCvtIqdRdsZXVyAHZ7M%2FsVzWmnbF6KQ4%2BA8Eg8sNKs%2FC2GkMPorUbQz2KLSwUUgASIqIxyVfR7PdVSkF2kRjVpTSuzq6FuA%2BPe9msVoRY1Zad3GwaGSLQAP33E%2FwhSNSSVbnE%2B8V0OXK2ZcpfjpDxHJEUXyvlw1C5VB%2B2ut2WK1Nytgfwfn4jBmB%2B59e3MXObyBHQq2d3qY9qVpgemHb7Iw6wbxKgNHxTzAtgmkaWMbekhEoBXyypadPwkYY605wQbz7IPm%2BjKMOIBjr2oC74MCPsYTen57vDlaVqiJKuvyxM8h16QDAwiaKGLLweKWVT0%2F9A5gfV4kwJOHQPn2eE8iOCyGDxspmQSDfz7PpAaso6kycr6woAxt%2BNLOodXnVTI%2FLvjR3dNiFj1Syd5RZydJL9GkA33RR58tVpC%2F3ggE63nRn2igd2XTXbqGfzGFmOAB2gx45vIdyfW3p9Bjd6ZnCANLk6pYUIse%2F%2FYXi8Xfm%2BhkNSYhTnj9D9vn2su8nzRv7iTiX8RnPEfgj74grLyYaJXTHrZv0%2BnlSO4bMpIhEs2d821Yq3ajF1kUvTZfJIEJ26Vn8m6vtKsHvbSS%2BBMjZFvQqg5aKvPiogUQgMN7kosoGOqUBfXHYuUM3vS8l6xuPZoGu4MVBspimE7P67KUZDqCUaxb%2BxC3c4VdX%2Fxh09govqHh31XAwUR3VsJE%2F8XS%2Bu0RmF4cs7e2fpaTGFRYiQrJCum%2BHY3rXg6FEwDPUOnN1lmDzz5r4cUq2aaS2VfHQHHDVrPT%2B9ZxdjK6VaTFcDdglqLlFlt9jtDYPLsIJKKcEG8h0H%2FEiBYWhTXWBnDpizh%2BTLkSjDZ1V&X-Amz-Signature=1dff8a0cf51f342a0fc8b2008373e60ad9c451abf28a29cafecae6923bbe1c76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

