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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYSDL7HM%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCz1su89DR4Ii%2FuRIfP8eLe7UrGBXwK%2BjmC6olLqqC%2BVgIhAI3aCu%2FTgAZrRePWtRH%2BZlNBs0pz5lDO7cJ6Ivnc18RFKv8DCH8QABoMNjM3NDIzMTgzODA1IgwVQ476LLD6MsKiw30q3AM3ERm3n2PFl6hbE7fq%2FEyPjmJJeaf4zZXkc01y6lTqYf%2FgXXoApKKx%2Bo3jKOSf5l7OhihbuWGZoW%2Frrnqdu6o0aMBIwnTDgXCyEpX4DBg4gtIXntO3RBudhcZl2Ea%2BKzDQgSctZX0HJIyvw%2BkzevFmvqHgN34QYN8enxKr5%2F3ljZ%2F2LMmjOK2hFXHVnQkUfIIvi%2FhI9E9bDFtqp1w3AoIZtbrNxR38eRn8Fw3G5omYH26ARE%2BoQwCRyTsSMjG%2Fd9GoruTLmM0d%2BSH9qcVHTg87zhCMN7lUpz8LQPha3cak3yN3091r40qUawbq9NFC2kQziHNH4zsDUC1NtjLCvYCGCDrLPnCtwB2nQbrXOzFn5REPICZpU6tEAZhJh4G1v5Gy9kWExzbnRbEMD%2FtjsxUnoJs4%2Bkg%2BHWMGuUU4XmX05%2B3NTPrFSXBTP38OrGU2wL%2FHpHd4QId3q432mkXjtg0OjJrS2%2BFzjaEO8m%2FV34vOf%2FkReoYXkuPqL%2FIMzg98vax3pZy765Ayo2st87DzQXmgOBCa6WLhRqpI0t93AlcgbYEpTDdWr9ZECAcTBTkGjwD4THjR%2BoeJSxH4IzN302TVhqlWjVukdIVo653cIDanW1eX7PFEWSZYxAL75TDVrL3OBjqkAcUpeksZ6XkSSP4y9bd0%2FDF%2BFgtBAMUfy3RJjF7i3aapCEjeybsv%2FdghlJrz8uyw2KdbkZ%2B422JmNgX0sgFlZrbDMzQveZqLK9z0Y9Hg74py9bpKXB7BIzlG%2Bf0sV5MIyRN2wi26ZQZiKFNMVpQDTbLkOLHE1baTdtflwidqbPnQGmg1vM4NEWnEAtsyNuwElSZ1dab45PVoCGrOXXRW7xVKuyF8&X-Amz-Signature=2ab7107a2a7a98034c34eefe2c37329b7f1a19a126feed02e8e975423bddcb44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

