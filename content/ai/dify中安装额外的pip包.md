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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QD7QGLH%2F20251227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251227T025231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDDkXGaoX7X%2FCfRdnFq7m06RYxgEts34bCAyYrAJNtZtAIgVKE%2BSkSA16gQM1fmN12J6jJnQ9p0WbYXYex89fMhbVMq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDOQ%2BWWcpiox00mywZircA5GK2%2FrWe3iOpo%2BN6Z6k%2FdkE24moPVpXT8JjkuMVuCpOVxISX8XI1Qv7P4lsbr73Kh7YMJDfgZFJNkkrMWPKkkTSzZovW5deieQajqZo3%2BQ9qYBNRB%2BOY7VUTpcgjYzHnpdGVPFp8%2BP9Y%2FB3%2FLtY6KqdE0UhB3OC6Fa6VmTWn%2F2%2BCSIJERw5RWGJ1AX1okuAw94d2SWVzfVR%2FOzvrTIkVSCSF954TBXD6LuWC6Z3B%2BQr%2F8HoRBtKD2VJVexhHVucOiIGxfCbLmIOSK2TgAFwrq3tUfgk3yyZoP0Tc3PGOPly43AETY062TqTLa75XmaZ5jnv4Ot97y%2BPEUUTKhczlItk62EF8%2BZt5%2BPtrDDs%2BkkTLlPG%2FRGEwjm61Bf2E41%2FI2z1OBT95fYzv5kODZlnAycoJoundtJ%2B2NGs0DYKfLxqrJmj2i9ztCCdJDcfOCrpgUKJOCjApSIAjn3GAAdj0JUmtCRYkzJcD%2Fuhsji8H1RNIMLJ4dgSGzsXbbtasbCBZAMAuiYaVDpD176faBoGZkFTfZoMjS46ZZm0nxna%2BzPPIeQggDlUWw%2F6mQDMjMz3qZYO5fxC3ShnbnDmch%2BaWOPcgqPx7qCkLyJ3MvolcNF9WiwG8qGEYJmDgR8qMLvnvMoGOqUBHWZauJwlJbcubk9lnjd9SYBkjrjend9c1HrOWYLRjzG7XXNUp%2FKN92lpOR5nqChHYQzitz%2FCSG4apcGUMDteRTZDmuG1v1pgVozsF5zIsjcwRR%2FlBc0NRLOJ07oqANDcqziAca8EJKYGMVmuuHkVbAL31UGCBrD4UUw9mD8S%2BpouQoum0p3XklaTVknXoQFBZyNwdCgPO1HRYWLSNOfRpnUFCjj%2B&X-Amz-Signature=b4bb383459d69e29f50d37a892442f9091451554467b2ad86e397194eb29e1ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

