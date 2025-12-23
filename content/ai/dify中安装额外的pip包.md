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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YDTFQOI%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T025644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIGGlQDk8e2%2BZrY3DEG9pawxMs%2B5LgZYVBuGDYkRvgt1OAiEA3yM7qibX1VuIAcr5d26qsCEQOB7N3lV%2BbwczfOsKvHEq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDBK8iq1%2FUjv9Y6WPAircA7MrLfXIiy5ZPGp1%2F3W1pehcqAuISbmt5oDGzJTvaonNpo4co5abHIEoQ0DALFeXMfpvPVmsZvLILhYDtpcWDGSC3mc4p6YugINm0mz0trsM%2FYRzY2%2FSNZ735%2FOqrZTA0sjmks1aPfBlMYZAdmo5ijkz5im6f3Mj%2FcEhSPqzHGK28dCn4yErRhEScldJkbp5EzAZ3DNIkZhZ0%2FHGAZ2Fbao12oscjMLn8HlpWwLehd9s43oQO5oCNKn72XcOHY%2FWv7LQdTCq%2FZM5F7rmVyA8PvCp8xNQ034LsAIA40yYFzmC8U3T0kzcY84JU3cRKLCBzcGdUm2A2D%2FGrtbPh8UkNoVESY7%2B6VcWWBoiWuYEHjdk3EPOGqZ9O700Mq8YLqV7ynH07cmR%2Bhe1zaGXn9HsSoVYU1%2FGbOXxcGagw6uZGgenBtDhjjLIPTuSOVg91GrUBGRtp6PGyqWVcafAZkQBt5rZQdx7JY8FrgzkobMnr4V5Bam3cdRY%2BgkqdKFsLXhyLuJ0omaUVJ2sx1USseGy1J%2BN85mXCY%2F7carWrzep8uynenVOVodTDEnyVGOyv9uYlb7YzW8nxd80zZEr79CaaLK4vMFgtgbojqObbjlRA32Bymxm6Rrdukh22WKTMMf7p8oGOqUBtiwAsnXdl3izZNFsbldoFTnGlC%2FLLI5vWFXNhcFX%2F1hdGnE97q6Se9XuDXNFvIzwQyR%2FBkH0Hp8%2FkuKl4v8MOAwySOzTFnR4gjduJXOZMsV4itpp34NvBrZxtoSkcht3yK%2FvJLCeB2%2BbiM1VVHVSvaOi7zwzkGVbbEPH3hOxnfq8OSuhXz84Uf0OMT7Sni3RMJG6Vvho9%2FjcGg7UKeRdL3H7BrE8&X-Amz-Signature=dedcbbe18798a7943d3375589496b6bd80635304b642a2af4a78094f2e8ca426&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

