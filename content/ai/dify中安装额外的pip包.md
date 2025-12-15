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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QXM767GT%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T030010Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJHMEUCIQDEA89KfHFofMfWzP7aVNyjF2x3wPpbih1w6bR%2FMKGi6AIgbeF6XcNxmYdfNiCrKcwrpH1cKiZlvytkwAqrR%2B%2BuVmUq%2FwMIPxAAGgw2Mzc0MjMxODM4MDUiDAXYD5ybwNLcBFzy0yrcA%2BdXcKE5IIDa95NE3hYg3Z%2BXn8oJr1J5FNMgyo1CYJzk%2FahGmWo9k%2Fo9LZD0jGFeLgi9HRmWbPbtUsTIK1bkupF39kd66ZnUbhLGgRHX7TJ3Wu5oplqjqcqQXt7a%2FKJdx3nRlTfXMXyEG3Z7ZGhCBqrnUDFnnfs0397NJnCd1MGWJidV53qYd2smkXNIaNnlgtz0BvK%2Fro4r%2F19%2BGzuQaHD4ehCiZcqL6cJKSpO8izGAIhI1k9g8qySkJSLKW3SZFu9SINMyK7iRPFxtE8vyo0ZI3no0fos97ydIpk%2BJm%2Brc5JVwGPjqCBGAjSel5p0DY%2FMi0%2BlwyMd7if9cGuPJ1GeyAOBJkBNan5w0EpaEr3YKJWRu7ZlQzpM4EZaoJyDh9SXJ4u%2FVV9grspaCeOeFqovRdRQr8hVe1lo2fChPhiHAXMrt7p%2F5CT6f%2B6ZrwoNAmD3wxTAIEUpFuk9KKFYe6tGdhFdz7JcJXjoNLT9qJk0MJ%2Ba2RjCbl2Rq9r3C%2B8vGv83juMnofBQRG5kl%2F9sRDuUSFL%2FJ4mPwrUmTvq0m2kDVdz6d8koLQv2j9KIZ9wpcp0JREWW2RTKa6jwSZ1rqVVovmFke8QQjuWeBGPf7MhPW8fZGEG5JY1EJOPUxMN7a%2FMkGOqUBp5PgwVs%2FKd4X%2FyqYGZYjKpai5HObBvTvBnfs7557TrqAParL%2BsWgdcqetcxtzxNgsF6MXmVM9TotcRYpq6tr0Fwy2DvlP%2FerrOCtWxHTl7xaqbTSs8e8%2FYy3mmf4UHpZx5r91wIoMfbpj83w45AfJ3r3QgpEN7l5RyCrhRV5K7R72U%2BOc8gjjxmuaWfzjNl5alqLMYtLdgrLSmQQ%2BTKmiMnjcxA%2B&X-Amz-Signature=f3bad9107b6f79be8d95ec3c1fa60ae9cbceae181e00a0cbe11fdc6abb9d4aa5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

