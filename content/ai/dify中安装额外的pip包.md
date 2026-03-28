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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VRLFG726%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T034018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJGMEQCIGDY%2BfB4vuuL7BzjS1vCh2NtLDZ1Aj0f%2FSryk72DRlqtAiBAPsy8sQW3%2BdMwlyUxPt6AqT0cImzEkszd29d5SXN9QiqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwcv3UtIBgOuG5S6UKtwDujrkBDhlx7yaBm8iMpVcXRK9bk0d4zRhe%2FjYhCls3ddoJ1Q0Mw%2FUKwkdVbeYI4ybTkEghlYRiV3GFdH%2BSnV0zY6BAvBYELjlr9PBhNnvLDdkNB3PuDlXdEr%2Brb4%2BoA%2BI%2BJdPE8nJp%2FS1HIAfxVlVD0HVDZ%2FW3tD2Od1FqtVeTJIxi%2BhbU0NXCh%2BQrgjWo9sXg%2FmnUSwh0VHOrr6m742dJAyEbHGkHcJjrCeF8GgATk8DaoiBrx6VSKT9WabM%2BT5fdRPveyBM8GrtzgzVa0B6szymKPCaac94zI%2FiSR%2BAxA1ATI%2BCmtEDiz%2B4SbH7XEuu6ltfSMJzStUdJB8JOxNml3EC10FbBUCbJa%2BcFbCl7xoc4wSGlHk9f7NtYnQr5pD1obl6EFWhLzco4MUngkZ%2FNuw%2B3IAPWBrFoU0Wot0gg%2BtR4ojdlN3yVd41jesKDEm18bxHorauIX8dXTl6Exda1VzkbV6mDdL2jSze5Nque6msRmyjvz57s9ep7dROUl%2Facl75gvSEhSP5L0usB0TvRWdphkbMWg4hh%2FJDgRqB3hlYsx0y9x4JX2y8zaRuDwZDVqRTrmEAZD4srL2%2Fnch%2Bo243K557emR87onWWPLgbx0IZOoUc4p9PtF5FY0w2%2B2czgY6pgEtLczGqdF7EYk3Tmz%2Bq6BXALrvpC9B0Law0%2FpSnvMzYI5OCvdstn7G2IOTdXug7U3zQxZSNqpRwaRU7i4lvWuisf3jP9HlknCDcchycxKpsue4F1Hun6V40ZAechvk2ERZYgooB4MtR3Rd74PqXNzTZp%2FJo6WtoYaqL9Xl%2FyVfgo%2B98Lc9sh620aQAU6yAoqlAIiebn43GR6yVrnEGJOGJy2hwR7jg&X-Amz-Signature=700a5aeb7a269b55262049c6913862950728a15efc951925f8a71c0f43374826&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

