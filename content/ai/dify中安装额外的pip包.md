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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKFE6MUP%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T024941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCseEMKmV0YthuLJBQkWdvGt51oZhr4yr9Zd7160dYirQIgX4SgOY18gRIYUO5xvWWf21zeQZ2m3OiJnBqzcdy3lz8qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOxSnzT21ErYK3sg4SrcA4uLVpsEQy2eIUxJqexw67RRgz%2Fg7fDa7zdmWlWLEhN9AjTL8ZvWaN95jqB8rj7wA3m0D6gQ%2FKH%2BuxuihqsuNQ1orDhP4HbLXgQEbDcafZ6UWDGu%2FiwrIRmXw9esGHSFKxfu8AxfaO8Lwo4p%2FpPRP7q430qj1JUgCQ4eU6FQ7zxJIInnwSp6hLV6H5rD50AtSkkapzApDclhU9r1IN6%2F1cK9EuYqbPCIKNSyRfpWSokEKfEDsgz8s0oUr5UHtbv5yNQJTlhw%2F4kzmi3oHi%2BX6ldnQTYXSjmErg5CBOPEM3kXa9xILPKNIa9d4GaYAth%2FkFXrEImW%2BKmEBxeG4Puh9y3aQIA9TonWi2XfWkKIJfv5ebBAvQTBxzRNF5ZIzbDflrbG%2FAmLzSsiUnrrZQMwjiw0pf71uTZNshaknmF4zivi8lLJ%2BjMqCP9vc2V4erC9UHDAGTG1DgqDL86VJq6cYwke4WQfSsPWyg1WvRGV6j12LDPp%2FOCSx061r51d8W578HKJ%2FrVXnqNfzs5Ifyb1UDspp1%2BT8khjtpO2DyTG8qCp7Uhp4RbJ7CTvPSKeyfU%2FcYDjKB2Vzhyzuio9Fs9Out%2Bs%2BBxZbFgTSsDZ9WRzDVbeJph0GUU30uaSdS2pMP3g5MgGOqUBUlivrKnl2jBuT5ldQo3XkNF15au6rK4kcosSqASYltlgBqrUO1Wl%2Fy2YJFxKW8ddtOZ6pPiaUm2vAPMTSLoqV6A08AnpDjHE%2FQ6KWNuqiHnPsOXlIRlTPyb8IDDEyGkY36s8VHPvs7UogtOj8dNyFafdmFi%2FFVIowAucWlSA66jVYtATyI%2FpEpZwNbk5becfmigPPXch4gEpMTVJ99TflIXEe30p&X-Amz-Signature=daec64a860aacd4e944d0df43ddfe2ddcf0a7d8cc276da9d13a33492e7955cd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

