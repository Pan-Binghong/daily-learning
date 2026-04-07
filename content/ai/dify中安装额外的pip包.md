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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675UYN57P%2F20260407%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260407T035032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIQCvM2hlQANsrSZtDdKXQF9FIFyfncQmVz05tssmVgUCqwIgPIKnOE5b8XLosMq5PHcD0KChUTkeBwdZzTeC0jt6uX8qiAQI3f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLa4L47NJ1H%2BO4N9JyrcA%2FJ9i3WKELllGEMBApSsz3yFpQrfSDDWBVg2uTBeetOvIB8xhds3NanNzZEEY%2F4jbY3H%2F0dq8tCFsJkymwiJLdpwthEadrEwomgqjUvtkoNEBzRErmXpr9%2BiR1yIM6gcjRSHObIEhw3k19MWaBI9Cgus%2BG5yE8a0lvV30CDdi3kiKwEh02jZzl3iM4yaaDaNL3FS5ztM5VIZXk1onkfpzl%2F55Cli4iwckiYc3sSPb2yBXxD%2FLaLbNWakqXZsmzOonQh%2FZCwBYA816uFOoRG9sNLgifmZd5%2FpmogMe0wdcE2UdeQF5nUIVSGUiADbxLtbkyM4317j3Dyd0JduJDnmlvgSeQZ9708C66CKAo%2BwzPm4JjzH2xffvjnuykk%2BGi4BNUwXD%2FKX7suqJ3FcKAQCln2RrRAPa6He%2Fwsde2feQQ6j3JuwlzB%2B9ESKIKYEOx747vrlk6ssa%2F9P6%2B%2BqBt89kKS%2FtqN98jDBHvc6Ow0LcWKaIdFbVgazJKAEtXSLXPioNXp%2BbTLCbBJeW0HDEzmi8mZjZXqW9VC3%2BY8ZJZCr76Tv8tR6hbr6R4TymK4vfLeAS3UU3vKZWhyz3q1HGFgNPMMdCHJ1gHeSlGfPWs3owQNFDgTDdp8%2FPOS3wG%2FGML%2F10c4GOqUBaRfxIl83DJ9HDBJWwmpIO4EDyy0eDAoO1ccZVUapLAsgDvNbi%2F0DW%2BOuJrxKccd9DIgeebH2krDgOBwf8iMc6nRDhyYShVfC8zHynY%2Bswv%2BaLUb94AlmIu%2FhCvZYO1IN%2Fu4GVoRk7%2FMn9s7V%2F3EamwjcSQW8%2Bbv7YaaZepcjkvMAvFO8WHZPdvqPDHPUmD2%2BlxeGXEW%2Fi0J%2FnkvYg33%2FIEKi%2BKPK&X-Amz-Signature=1eb936c508ed1c2a2030e738db51f2210a37df9fc7dca7b5bd615103d507e495&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

