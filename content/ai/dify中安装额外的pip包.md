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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBZV3CMU%2F20260115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260115T030032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCID6RyFu9LNqa2FxvEqEiRfHk7p7EEvPXSz6%2B0Dv9s4i%2BAiEApoSTVmNDQsuqhyuVFOfa8YZ0oBGat3AYOMHwkXmMoewq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDJgOaj9QdR5gpxH4SCrcAyca05FKMo3snLXguD8NYs7z5Kok%2B3J93yEZfJS4d1%2BeqlT22flYV40u8%2BkRCBeY6AgbM0d6FNW%2FZ76RLHhWGULjsMR8uY5tULbfIIsG2hFKbBnlksuOdgCHOH5tmXDHKFwfs23wfTg9byIdJrdIs%2FmxAKOa%2F7ap6BMUST%2FQdlIC7JoVl7fd5tYJ7tfwiAnNAfvCWo%2BQi2JHqGXx3xEwFXRwcCo110W%2BHERbO4X8m7OBcXyCj5yib9ZXvDfGZOofb6FC7q7v6BfsEFGkulNkCyMnpJZFGHvp5x7nKbEp1VM%2Bivqk4SHoEBvPc6I0Yc5OKEfOOp%2F%2BVvEuypYeHIbOeRgW7OrEy%2B2Axd069kY%2BH9h0QVm2mwof57cywIBf%2FqBsls0%2BF7QA1Z2pUzeh5Y9ophuAlR73K99KweECXXaj%2BxX1ayujbnb%2B37LXymDHceWf9ZdBQmZk5MUJE7mgFbIAnIfhMp732Och1jXxVTez09pGSyMvAlbq3vZSdVi5WIrkGoH1aEr6AAvEhtiPKEZ3lG%2BAlKHK12%2BV28idlUcKDMWIk5Uq0tepGxEtKb%2FxU6YfCeIwEmr1rpZLewAh6agmlgASwer8ETgj3BDUln4xpW%2FqMfwENt3CqZ2yA6PoMO6bocsGOqUBTcUuH7FnaRM0IjKGyr14jqbUThkyWretPNqxV1cT6bn3psVp%2BwvSJU4WDNjmeg4oHjnG6F7wSKgt5DtbI%2BMjQguirZFF8UfSKiS%2BgEAupVRbDfuj1DIfSe0EkUgdPhEZB3K9neiWTgP0qaxmNtO8Tac8KWhEr9563zNJ9bfeuxe7d9esnmwnKK5q5IobXUVZc1qH3eVcAP1SPlK8MwGCVxxHtR%2BC&X-Amz-Signature=88d45b218663a26fcd857aaff4a885aad57bd9d0fdc7539bd468259f3d3438c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

