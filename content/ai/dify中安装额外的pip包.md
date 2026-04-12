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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DQD23PZ%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T041242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHmsFGNccpUUAyBKXLHwOP0aniWWQG4TOSwB9bihwcAbAiBBkMOqEgESBPDaX1E48TtRiDrmpEwv%2BIhFjnV7%2FGaNvSr%2FAwhUEAAaDDYzNzQyMzE4MzgwNSIMEud1OHG%2B9CcrzJCQKtwDFoqwi8Zv3hCuuuXRZCw8K%2F5JZ9UuFNMUZpHA5XDGIE8zk%2BhmCB1TYNFv%2FncI3OShhAJJfjZfGDqBgRgaPbRDacdvPG8AoNkBMDxdjQexc%2B1KqbAwvfWaQcB3uafbPHKLHSSaTT%2FnvJYrNsVOJ6REtcX14L8%2FXxW%2BCJLQFodWkRiuGj8AZySjv44G1w7a9pecebadyZzeZ5Ev6lSCgSqX8QJ%2F91wmISQx9WiVD%2FiuQ6rJBsPPKAWZZnwTM29kn81RMyI%2FI1xq2NDVKhexb89IyBix3alL7QYWF0Axghx2coFnpiPP%2BVysZDHw%2BfgHQBrXXbrSoq8I%2BSJZ5E6RYrSBnmcFdh4uB9PS130JXn0WQuZzySpmwW4dt7RS6pPJ9bDO1nCMUHnYtYwAm0sqIG9wk%2BUKSKOdEg9mkKS76EHqsgEG%2BtErqiHq88dZ5dwUxnCoGs26jWjo%2FHMtooccck9q6enaMI5XVbFEjKVoV7decCrXgiq%2Frn23umEdtaRJt%2B4YXKZN1jFm9Qbb6HoAJZ%2F3Rl4jzGfImD4W%2FLTKvWWiv5VovoBtcZijceM5m63SlJTQHD9yx1hFHrxrzQq6qYAUlEKyGv%2FZ5oE5U8312P5nRnwq%2BEiJSy4aJbJXvZkw9IjszgY6pgEkP5uNjNVgrM7uITPscHb7jUEdFq%2B031RUheVOnW0C1oScGa9LNwnd0QiFsUQRqMEl7BEp%2FpPQ0MEJp6wLRvwjIMrHi7yal23mBLGvyDTSwJhswM%2BSIC6Ih%2FiD8cSDrYUx81eoGoJTYdO9NGNXwW3q5BthNobPjR%2BVo4UaTx4VvjoU9K1336NvHSg9uaUtV8RGx55YQaH4KtpZfigsMhHnmA1vxWgD&X-Amz-Signature=94b97211f335b62c70f9a8f3ee953a7e06f49f9f53dae8c010984ae1bcaed2e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

