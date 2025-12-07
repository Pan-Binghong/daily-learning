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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MR25TLH%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T025825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDJU%2F7Ac0Q8QyW8IA75uRAfc7yTJH5Mx9ml01m9AuckVAiBuuCn7AOVocQ5PxEZgO0SbImrmYXwH5n7lBikEYxuEiyqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML0ZVgXjY3vIsuubKKtwDMK26oiI0Xki4AxziJjK%2F61UQHneQnQAJEe7rvRWaMev2f4mVHC7ttP3vq1VRS0PblDW%2FjUe9%2FtOdCUTrtMRUV3Xmcz2j2NSYzaFuCEQj2bDbkB8cmXMhz6Dx2aJJyXx5uWtcobZXitwHNl1OvJUNC5Ap6zhntJdc5bW8HEbeEgeTeQM35Ai14vpd7CfT3XRLdcQmzBHcwVUr45n5RS6eUNPY6w9Kj9OqMPSuM955kexZuCWlVIrOJqNnvuube3QH8Q3AT6IaFiQrTQi20YY9J%2FfKgiOHPFip7YU7zOkosTwzChtQK96KXOSRKMbyrYDZddeBis2c2AO%2Fi7GmTLtgJdUX5t8gAxB8b2DQIfQkSafjcsY3v7fTMCHoQXZhePbBnx7zqjL60gzPbR6OD11jxSUrPTmVPC2wNKqPmtDtSbAhDoKTxe0qOqHBsBiQ5yJO8TaYcrV%2F1bWQ2CBRmYYJ5dHXRvtFiRZMgVbDDqat7rSBml14xNMfLrRz%2BKC4%2Fn4XzaexNQK0HFyeKJawmBedhJHVY6v86n%2FYjcmOYKwP9GpA44J4RaIBV8iBHqSkSQu0Itbzh1tjyXehdb4CoE5TTzbEZOAt6PiPIlZNkEFa5MTZ76A7ehKKYJoBtrsw6v3SyQY6pgHTLfs7yMLeBNlYmJlu4s24pjjJvAHEmImu0bUjj3rNlNaIijGbWeF32d%2FKBGKFBv0hrvojMEpQEgwdih2k5NVcNjJDMPwaFgaLyedJ%2FbbqOxZGay3LLS446lPAqsy9lc3BzrP%2FosAAFPNXsR4GZpUhh6CxOOV0TlYPQVLh4Wa6Wu9GuzdxvUtW2CHInMKlBGLzOtOEGKOCUyEgaHxj8ht5P7H9S24x&X-Amz-Signature=6490af575cd97741fa73f8bae9a16c85accdb90190d5f73821ee2ae6b752ad91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

