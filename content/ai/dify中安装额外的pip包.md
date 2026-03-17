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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWPPBAGE%2F20260317%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260317T033534Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJHMEUCIDwGnXpJ%2FuiCjVU2vbioThcjjoaBBKX5kblVxdAyd66fAiEAwXXMnUAtKAdd8UnbgcxP66hNZVbwRs%2Fs5ZosuihFFAkqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5V5Jer6wLIR0TK8ircAz9Ol%2Bw7l1a%2FtAB3yIJgcEtO9yFJQu5NvRG3tMCPUgVp%2B9b045V9qYzrAebjmsorS3kqU9ATJPejTLprOtJRhU%2BGeZuQVBDRgL2a90rsDgErTn6RJWXjpYuVwvxJ%2FSU7ZWLNVGrUCNjO0AUTZgalpggY%2FcBjBat4QdYHGavkIWZVh2KAdpDVzdfG4gubYDhhF6jpqObDLrz48gfmC5eIfTG3lGs9X0B%2B4TNrXbue6oQUA%2BVsCT656CZNulrZV07z5OnqpnOPJxB3K6EQkeaxGSq5Ed05JGt2BCmIKxiFN9f8mEdXRN1Bn3otewWBbVIE3x6cMHCkiB8%2Bv6EXIw%2BcnK9YCT6HTqZKsI0vSqfrRAXyGxQKSbYtsmxX5bPA%2BAi9u3YBYBoasa7Hy8onvypnPUoti6MyzdxL%2FJ5Swmr5X%2FCD26yql9cRL05qUm4kIx%2BtSxL7HzCwFgQbqQWiqzaqWqdauHDaA%2F6D5bI2sb2LCjdIbnVrlcXtMdCSdITiyAT7xjlyz4WRT%2BzXKzt6l3nH%2BUCVBOn660WzfsTJCyejmYJewF5HDYQfvqsog0N3kBVMVKYd%2FOV7c0B0WmJjvQkSnBn9BcC%2FHRx3mKzvU0UP9Y1TYb5E%2Fk%2FeaRZt595nMPro4s0GOqUBC3mqLAlgU2xJIG8yBA8b8F2wpawI1QlXq%2BXuvkOsM4NV5Kk84Hy8APEH0tewgzGcQbdHQW0UYHiBOqhAQ6B%2BTcMFgrpw3nhCxpR2FyS0As7qVqoXPMfm4VhErryzKbT8CXCOUc0R%2BRz4kCte4uB6PtK1P9MFMxKzW9tX3AaHNBF3EB29vY2bbOL%2BXGhMEhWmLJ8lN5BLL1V8rZHqYyPtNdcfpcEL&X-Amz-Signature=c384cedbe949355b81228a28e6f16db42b8c6aacc119625f41a0c9646e28d3f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

