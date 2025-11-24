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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FVKHXDC%2F20251124%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251124T025445Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDDNq0NzNtbd%2BLtNWSR4KWar0h3edGRU%2BoDbl9EM0b3LAiEA1ZrK7cz%2BXWed8zTcTGZa8FCc%2Bam2CjAFRYlBN%2FEsL0Yq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDIh6BsoI5v6KUAND5SrcAwp3EzYmAiEjccJjdSMznJAs9g9dKIuf1FYePgPWccT2eCwUtxDGGTk1HihePOwdtx9YN3%2BEbsZ240S6xOKnm3miYMWcilv93m2Rje4xFR9dlKcDswtQR01R32B1WNjzCC82jkZd93mZOAOdYXXQyLYaY%2B9YCfbPWszbH6uhoO1XSmAnFEqSmmMigKoCB%2BRe0SuKPoxYbl8IPF6%2FM6GEZDe5Uxe%2F2RswhFt1%2BWqvOvoYskfFj0kVObqm0N%2FZ8NN8uhkzI9dg0E26295Yftym8arV16I%2FY8Vl7K5GSJUIF7wp9fzXKwkJ3AAKbwHXOHO%2BwjbFzdYvrlutr2%2FXB%2Bz0IQxAo%2Blp1G06g%2BZ8FCYwFr06hi%2B%2FtGnyLfVN6jvS58G%2FtQZStSeoWkCJ8Goe49i0WsyH00sg6IgqGboZcL0MdzC7QDu7oOgZ7HbT8uEFO3SszyTJPzvn2K5969SHQ%2Bw%2FPsP2b7DU8xZQa6Eiz3SkAqflkQ3hozm3MVrrWD4BV%2Fc0H7fRd206Oiw47bUskdVP%2FPwnmR5HWA8opJlaBuQ4UQ8bRJnjUwgpwbEZC63DlK538ziO7wdQzQUBqd8ExuAXOCtNzlyEPIwInQmbBQqTXvKtq%2BeoSFvW4uJ4VT8dMPHbjskGOqUBXuc%2BxdIoRcmQMMvCVE%2FJ97vIbjxeRnENEnBDmz2VOZZ7gHJEfTSfWMBCBoJjAqY9ntzcxEBkTmjQ5iuKpEsnsCpYx81Y9aZGiWtq5q5ox79SDfWPcbeO9M22es7ohyo6IzAqwN0OJWJFd1sIgmb%2FE8eY0UtsdEh1o1aNQ3b22lex9vMFC2VqElTZd3Mtam45VDRLunvXHxOmMiX7xTDrAWY02uqM&X-Amz-Signature=853cf427dc56fc8034289cbb871950d01f0dc1d44d1de6af686fd705e0f8cd79&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

