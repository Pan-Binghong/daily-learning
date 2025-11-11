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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQF357JS%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T024459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJHMEUCIBSdHiH3xiIoogMeLqT0UdKyzoCSaKntENMJ9zGhbNrGAiEA6LRIe6cOKa3biq0TqssOLHdWr%2FlHpwXohOlHnso%2Bbnsq%2FwMIFBAAGgw2Mzc0MjMxODM4MDUiDKbWWxWp3oWQvxZe4SrcA%2B7dhyz4gi68H0hkjiet8XVoua098L%2BRcgnWYwNfPJHtCS3mbBz5JzkDNYijjRb4dsN9pP3kZ0dHWAXVZcFnSR5mYMCufbY%2Fwu15BKWflFVRQlW73cbYxqzgRkLB6%2FudWgdZQ%2FxjTic6ZB5RtYk2YDOLcxD%2BDHl%2FTRv3IEhuNyoB9iYhCuxU5es6hP3llXVNZEKRkCGjljvjSa6gjin%2FBQnw2xd3n2MO0fin64w%2FBbDGVxXdwaOhjwac3vBiplBzGNEoltl5AWdk77vruvQYomDUyVz3khDOB%2BONBqQnnSChR2190lW9eFoPp07eooeS7gjIXpydSX%2FYeLCQq08FhmH3dTio4IvPwVfc2kVXwCvogmtheglwBn6GJcH2GUdBc3UYgZ4BzMCKNRrkC%2FnqEq4k6ZgiXY493PH0P1RES80%2FG39IO%2FO%2BE8BxHVTeOaZiYfHHbS87zMmpHUA0%2FndvQ7ikn%2Fv%2FWnBlNGV%2BIHQe37c2gMiKobcoVrcDwUi2QATURqFf8qu5UaWJ%2FszlB4bRk%2BUhg7Zd6emfw%2FKJoF2%2Bh9TAiIlFUVJrjOXnISXgce8mnmIgbiap0FQOsGof%2FtCafVUywIDteX%2BA2b99RUD%2B2lA4gy1z5L5%2BmoLoNe2aMMC%2BysgGOqUBNkb7IJpczZy%2FdBmxWA%2BcM%2FUEmmDMukemiILASC%2B79crUY8rdXB671LseWve1ad4BgqYb%2F%2Fo3QVfzejOf4IdMM1ZaVzkxskziVisM4dsx%2FvrFs7JIr3pMYiDmrXMOuRl2M2mK1GsEALivi1MUL38qELc6oYPnShKqcKoYcWpz24lmEyclDIqVFkzxYcVHQ3F3niSbcZ6yX2Mfw5dX%2B2un24%2FB82sm&X-Amz-Signature=c5c10223c6b0a54f83b19f856b2824b8556ac460cbebbb8a8a326567ce5f783b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

