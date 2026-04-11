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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SKHB3YJ%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T033934Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHMaCXVzLXdlc3QtMiJHMEUCIBVqDWnALgm5x00BXuEaPYL5PMPyCM9KUN34dnLuXwGkAiEAgbyMOCdSIcsILOXBK%2BaB4QqB22NLJbNETIa%2FEqviWnoq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDIkS1IqGCfZ1l%2B93NSrcA6GxVyjwzTKbc6hrSRQ0bTuym6RQfBvUdJjnD%2FTBCDYKE%2BimG3D%2BSBoP0THHJJ%2FxbaqNT2QXe%2F6%2FUY22UGhHMOdEf7NDvAOOLAnpc0vYPTBQHhy3BM5G5fMbdsFB4ttHHkWY%2FNvOE%2F8M%2FXsXzzYsqchRcVSOoaR2fp9FV1eNeKpPM4Ve8Wh1SyR6zw1GBg4kSl4LzIKJ20t5ChAHFD3LTisW6OkGd5sj2xrcyNR0qrkauTly1vaSWg377r%2B5TvWLTet2foRD0ofx6Mx4zWKSITMBSBtZ%2BibtxgQndeZ23PW6VTFmlwrHRP20oJnk4ej1HXflPlGLx%2F%2FoxylT%2B4dTfgVYEQG3pNDWvOi1R85fSPQq%2B8YqlhvK7sKpvKs4hOcukeVpmpVZyYOjP9sUkDJx7F0VPP3reAdfFhq%2FBSxl87tdm0e6BuMfNf2j2SfChGK1Z0X1rtai%2B7Ykzptq4b0q2N6Y7KvGqDI%2FQZiTpcgfkEMSADTAji8Tpk6mybqUjkMSWmgQsdsCKCS1PkdYfDEKl%2FIkkGCZaleBMHmcJsSrNFDBfXrCp0nAaZ99%2BCxIK8s3dlVYkJ5Q2HxhNdvyi%2F18XzCgolZLvf7pN95LcWukPl3U66keg%2BpL6rGpWKS9MO3p5s4GOqUBKV%2BNhb9Adn78D%2FvB6z6Ezatlf9w10bNxbkH2GYKPJ0bA5ONMXeVYhXiW7a47sc4uceddlaU5yXb8dF2AQniE7xoRQWnUmcHuEiyKStJ%2BS8F1hLBpNdvP6HYatxAVAfkAZM9OMR5ACBREGiSP0bqRtCqHUwjjkwozRZgKjR9qxNKsckIGylfkOnhrWkYKfVk5uvBNWzmv%2FaOqyeRku0c1rHFsZgOR&X-Amz-Signature=f7580ec2940acaa962c315fa4c65edc26a52869f81ce44632174220246f35dd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

