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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWWOVGAM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T015025Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF%2FzwI1xU9e1DSEezkzjpCr70JKM56Wv7jt5SA%2FK5PZqAiEAu3c33bnLev3R0F%2FfTD%2FAO952JsBh%2FAnVEjfYcHwcwYsqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJHrGyrUqHXOTcUc0ircA1o7povS0X9SrB7auZLErfcIUBRQEOy0BzfZZhdTHTZiSXtaD68irjD%2Bn%2Bb9i9VuK0HezmU3FQ9OzW4LcUbK0PsgA4Z7i0PqetTA6UlAF8xXiG4BbVtt2iXUK7sXGkrooa271NqwF632KJ2IWglC0JZPvJeYjnZM%2BnkJJ4xvngUyBf8PEB89lxKR3vjZ7eKqxeAQIh1mD5MBNIBI7G6ogDxcKOHoYh0ueYpYJAcE%2FJAjGw%2Fe5FD5ueHBKC3rRCWZLcdteOhPvH5402TuOmc73D6rSPXymyzuSp4%2FuvDKAk%2FAAkG2sJ4xqqWP2Zo31GXJxlt8ugk2ltTuNIo9lrOzokwSatCXuKqMc1x6sRycvzQZ8RF2yuEO3TfKpc0w0O5E4tqvV0RCQJRQHon5D0XTi7KjMXFBOC44fx8DOcDLQP2kRPG4Sq1lX4v24GkisG%2Bffkk%2BXbtlGTcEwb3wOw%2BqER6sclNEKNHo5sTYg9kx9K8MepJN%2FEyxg1wF5K3xCKZWo2tZOe5ycjxXHe0%2BNOwVpr2y2KYaUz2bxP8fD4o4tHtoOqjL9R%2BhAZG35%2FKKORCSOvISjRilgpu8Z5nqTB6tjD4kOflh8ZawLfLcD1F1CPSmsovjHAxT7bgSdPpoMOXwr8gGOqUBxjYJjY5mKoDOpcMY1tChhCmTPn8fS1BaZ%2BiTiM%2BASxcSHIfHyImBTNzkDIeokTUN2kpXbXIIZ%2FoCyzR4A89T6h%2BNsVJgM6V%2BejCh%2Fb3RuL7Y1eWdezc48%2Bg%2BZGzGgIVLhwuEulErtajozo8K3C94qD45eduA1mmqwPiiyp8R5OnQlWf66EfJ3VnHAhpY8aFZHkBpgZQJ9JUZoxfIq%2Fuzn5NKZLO7&X-Amz-Signature=813e3cf05da9e3b0c0f09790c142d17d56e5949c28ddb0be40a8986004a47918&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

