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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFUPKPMZ%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T025044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvhvuZ5FWKOX4FjbaYn%2B4CviqNZxOC1VM0TAZZjA%2FiaQIgD0atVaL8b7Weol9ZHuGmyzrnvfLugumsY965nJcFTQAq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDBeMe%2BVQ%2BR8d3Z015CrcA8MnwUK%2B5raJ%2Fs7fXvzO45TrrE91Hn%2BC4wotmgQToGh8CochQ9k4M2g6Wj2dXr3%2B%2FKnOPtxdQGgAP%2BSmctF1cNGSODwB7fZFFQwlAnxh%2F5eAga%2FM1bELOmNtlyn38enF0KUsvmFT9lRuOwLNwy4XaxheQgrdhyENQCNMiKe7%2Fx%2BPF5i2Dc6gafrZth1MOH3ZV3lPqsc%2BUu7uQxwewZ%2BSPKMydxxd4j28Rx%2F8VbP58M1rWH2046BTSXeKkEFEM%2FZtJOpS9Vt%2B8p58gAx8FrpcFKq6L5V1Pu%2ByrHAOSk%2BNkMAcBjAfeBEfIV8%2FlSk%2F04sq%2BiskcTkQLwBAb537z13Or37Hzk%2BaydbESeetLl0J2zPr9tyzf6j%2FteRVr60Lxrryiv9963nYonwy79RQ3Ml1swcK219Qked1U8yTxOPHfk2UO06LdD270NUXNQINomWhYcIIUGJ%2BKMdN4C5DG%2BVIQ4o4cwGsaXYEq23BLT%2BUKreJWCbB2CtMZCCGQUBYlahioym0IRxLkbH4evKuj1Saej7JiheLakTrjp2bHILpoQ4%2BMHIa4IlR2g3yPC%2FmLzlzGXf39HHg1sixeNgBC%2FbJaveblgzib%2FBxCZuc%2BievVHt6LNzp7zvrVAHhUhr%2FMOayiMoGOqUBzSwTE1PlJEeHGp%2FebAXYWYIgrKJYkm%2FZDgwR9oB4bLIZgdfwPekOiriGEhhUPHs2ZQ63Sl%2Fypvzs6RZKSkXidnnabrDWpZNVpTAVA9eQ46OhPWChvy5N1%2BPKEhp7lEFD1jd0HdBUqbeJ54jIbpTvveuCKcchXHv5Qk0uSW7jPlCkGsUUrSjSYeWACwiNPy3xa5N%2FcwA9dzHz9fVxjLwsuz9KErQZ&X-Amz-Signature=01205db88cdf179fa49d7ea03ba45edf4fc83e4c7b346732a856d8ee9b255c54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

