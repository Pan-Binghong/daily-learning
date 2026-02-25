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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U52YZZZ5%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJIMEYCIQDBv8MAuMDRwVvvCaU3MFMlEkUMlyrS9%2FNvwKi%2BOvmvywIhAP1BVXJ1ww3rXSyybJVZ096Trb4rmxuXMJLQsuFfdisuKv8DCAIQABoMNjM3NDIzMTgzODA1Igx5892z3dHzYDo1D3Eq3APTj3%2BCpjjEI1sYgVLVAUa6FeBfBHJYKFEyHR0mYQ1vdUkwVUKluTcB50HGOY9g4hLS%2BB8WyPLotz1ZAztcgO6w0is8jtspltNX%2FYsUhpFw2M%2FQ3ElpHvB5Ne3e1stZexfUqocgXsV1OTDI5rPB4RVVYi7Uv1xnCocala%2Fs8Ah8iV6GDWj%2F%2BXf9Nn09EBeXPckafYlJsnvywCsQLSuAXbkmQr613Icsaf6N%2FGztsNwS%2BK7c2%2FuWCyEI4gYeqDhuQt8QXbmZPL%2BQAZJT0J3AS19haPUYQesINYeabY6xWZWYdIKQYJGOOr1WkyW4N6uPY0bdzz%2FCJT6lgONh2c%2F7S2uto22k3BVZ7jagmVvSqEPlDPGbI7ClJG6JmDmbP6eaH6IvvIGLEwoXc3IP80s0ft6TohaaZeAOuQEq1dTYFgN%2Fn%2BP1MxJFeGBRIljQLm04JCMhe4yijvlArASLX%2BSHDWj27kB1HOWS7ONYBFLC2sydpk4IpJmHs%2BU7toy95Tjr1P9VMzS8596P8PUr2qPYSWjPZp1WsF%2FZhEJUf6fqlfi9iPs1rROESnB1l7Z028lZ%2Bz97CWZ%2FgdWYyLD0mAwJrfzZKVMYO6QfazBUBR%2FiIXGK%2BGcX%2B4VVeIPxXUwt7zDbg%2FnMBjqkAeSFtobbi4tVyafInhW791MAZyF4rBbQ8wg0Tf3goq9lF4ZHU77C7DeJKtgpquKdCqapE9KJaS7SKrAGUT612INkQL0VH4OKlS2IHsV3%2BUeWuJwFKCSq%2BPWfwOPw0KqvrVPVwgbNLjQrmaz%2Bb%2FpklrYjI5zdQboncjXEMDvyD5ZbGNwk14BMYNQnBsdNBiuoRd5zDNJ8exxp5xatoDRwBTbKwcH%2F&X-Amz-Signature=089f519fbfbc5a074d0286409ca8b8ad6f4689888d68aefedc5dab1fa431bf3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

