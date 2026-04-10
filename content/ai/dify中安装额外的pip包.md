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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXIM5NQV%2F20260410%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260410T040939Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFsaCXVzLXdlc3QtMiJIMEYCIQC809ErWuZuJAkfN3vVIHMef9iJmfbk30fKkc5YT1PecwIhAIgIX9VVQbZKTKuPCREBmc52kZSBeQjTNs7E86oCRwTHKv8DCCQQABoMNjM3NDIzMTgzODA1IgxAdGTmcSfdlByxkRgq3APfGXUVjRNJPutTvIyf9KiIMc0wfzISx4sU6%2FmyY%2FX4lSNKa%2F6n0VTtHUtxdF%2FavqxMa%2BE9coaPO2407FYU2Gceb10b%2BgPxa8%2FydQYqXXiabojB2PSas2KqtRj%2FQtRYIOg3Ob%2FOD99JJLUGE%2FUD51e5ddmmeowaA%2F%2FoK%2FzNpEPDXMNYJT%2FlDAL8p6TcsXZJbhDYoEKaHcEO2eAutYmdJs%2Fl%2B0WTDN4Uxct0fx%2BBqDRuG1c2ev6d5kS72RpyMfBQuHzSDSu%2Bbmq7ikh0qlucK2REOWFq8RUSyIzYke27KxJrVhgepE55L1CZlXbFCCk%2BLrtsEARIR0DM6H0F2m2QxTYewwhRlwd7%2BHOv%2FmJIqgF977qBxvtlalrJzHVmG3GotFna%2BPW9TljJi5oo3oEF%2Bc4chyX3l38DAo3v%2FID%2B2yztd1sVCcA3orzuqWBcaB0f1erK4oCvV%2F08v%2BNSQ%2F67q67Ih60a%2FJCthJCeBi99MyQG7XTo1i8SW3KFrcl8z8WSt9khzchjXQMU8fXyfDeQJyOHTy2HIL6vSSW5T4zA3Tvv2GBAOoWoZ8yLmDCEsbPK03c87A3aTBJ9bUGo0TPT23C7mMSd%2FyrBImKM7QD%2B%2BWSWsuWr4fB0BKuOqbzUVjDrxuHOBjqkARb%2BR9OP0swo77QT4%2BpCxuwr6WkAm1H4%2FPdSfucWuwdssb%2BUkD2SDxdhWEDaqb%2FP8%2Fb7tQyUcnKQv%2FOScw73cN9ReFLoPp1UnHXVeXU2wxgiPuo6wqumZG%2FfRK%2B%2ByIRCYYlh%2F0xD5dc4xHWhr2fu0A4nskXwCT6%2F90%2BAAbXFo4VupV2qrMDk5si%2BJw2IMUurGtTPQGJH1xnzSPGRbq1m8dnK2UUu&X-Amz-Signature=d0f10cc204be62f9bfc5e06da52a3381b911bbcb73bb9156d88c99077d39e750&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

