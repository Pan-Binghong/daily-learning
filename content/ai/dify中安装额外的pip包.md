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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKQGTVED%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T070702Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgBB3PF%2B0Bw7ABOZZT2cTal4Io%2BN%2FPSuiNtrSR3bzpSgIgazGBG5jJ1i2daLy9R9JmilXN0AQheLpTc94LvmIiQjAq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDPFMLpWSpWIeKrd93SrcA1jfg7UiY%2F9WBRph1uTzZPWvOvipFqhr1tReRMa86B5lwl%2BQ4hY5bM2VUbh5aSYEXX2TZnBPjeprf4Q3t8yNecyYS9LPubmxcIWY728kzMzwqFK5jmMa3FnywxdnzyJMG8Muaf62kzIaxlGmPivKBum98qA77DWuIfKBHAMtQ%2FYEYSBUv4iVDFv2SBsjUpxuKZeR3ZSK10bRzIIlcpRxezUfGeD77dCFroWxRheqK0eY6lQwVCj9bWuiL7d8lh%2FNywKLcJriL%2FtwIyEM%2Be%2FNqiqKZxSMrKyAqcZTbMpmEc%2F62Ml8sLXESs%2FkNb5e%2FpNVklp0aDNQ53jl%2BNEBmrB2xj6aA9tR0XViXHQUaS16COWUq9XyNKQ%2BCe6kuczyRIgSNb88%2BJeayJDlj3h3aA1R2%2BI2OoL9v2Ge5mxny8CQCqJUDMpw5PBBLjjbArM5O8J0GWEiveoFR3%2BBxRHhWapPJTeqgMjzwcbiQQO9Tuu6Tu29nrMza14u8eLk3d7hB7h882pioPnRS6lyVbRWJol%2BuF%2F8PsQBs%2BLaqMMgtHTlF1Aibm0EUdQcZlBPC9ULFNFcgc6Lz0UIW8wL8QuohtyxqZBJKXm3kqvHZTJk0zFafZQNssraxesAbRoPuXxXMJKtvc4GOqUBjuqfe%2FI4FChWR%2BJP8Z2YbF2C7t%2FS3Zp3YKxg4TqXuRJpA4t7WVnoUMcwwLxg6xVaiqkBQn7kTUBM7SG7H5lgZ6GI2yy4h3YQ5R06IGhEpvp9dxP3IDAsXO9tW4h%2FuJdKqbPRE0EBSqIn1nApX6B7itaI8Bae4H3oWr5PvlmvYpweXqx2jjbqKyZlnHHoPp0C69hiaXCrfqzA0EE5uoybR5q8FaZZ&X-Amz-Signature=04a9f73b9d68432c3728ad0589ab3da95d3b86905c86971ba953fd2a130b1057&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

