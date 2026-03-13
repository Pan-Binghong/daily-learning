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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C7CVRTG%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T033054Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC8SrOSGINKLiXmDcGkedzWQMK%2B9Iv05rPTjJ%2FIclwVDgIhALCYmsodJuOESsY4weIpv9rK%2BDUbvLXixAq0Gmw8bF3RKogECIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUXlAztF5CCOUZlU0q3AMTZCxdEGEIpLORrnOb%2BHcD5MyAiG5rqACLtlVeDI%2BS5SQynmbi%2FsXVuNgp8zQ36hmab8PvVkWJ6s0wHjal6IIjcgPJuFOD3fCovmT56itdyQkf83bct11r1FVULscKMJoM5jsU9ZVS78aiZLmB%2Bzq4qkNtwJYz6pnwym%2FkVoc4kHbY%2BzdrIwtUhbDsd6jMjhEwYUenmvgxOv0jjHarSZzj8pB0DFFSlCJymt36nYDIqoFnhqZzE9iYYDzTPPdmz%2FWHUyhUWoADO6oAhiXUVR1AUg%2FXTjvtMcjAtvS6DBXPusQDo6kzZF9tf7H1VhX2Ejj%2FuNJVbHImizutvhS9n%2Fp4PA93Jxt7YG%2BsPwilJ9kMtyXxNV8uiIx%2BIh6nD00%2BniJatGRqsU44pI8Gemjh8nJqm%2F1B0XFtYz6f2Q1Y69iJAub8gnlPhyFT7O3QbZ5MaZVvfEw43jVxZsimNhM1P9ZbZSk45NUD3TzqxVa2PCmuVVHm26w19CXxETIE7cRm8dF84NEWMegt1kv%2FnreKvoEuft79w9IJpXJWpPlQJkEpnUg4wRdZdSHqTYi1wYMU01rLZUCJgyrf4rk9iSuuyr0rt0IooRFovI61uuYdeGQWZYCe8LjvWGAhznwloTC8uM3NBjqkAW6v0dQQLehrwYDCEJPgDsAx6iXr%2BIFfxw0dQotdJSSUqSDdyUSOKRXRNxVHNt9vBedEL5R8JfKzLkLn5cnAL1DQGxBUoia%2FHLAkcAgaES0YCFmYA3oflOo4fhqxn56dk%2BwRLolJIj00Rg0c3d2HrUbmdV2DI%2FA7TBJ00tgSMIe2EKKP4wh9BGiLcfVI7ijA4%2BS64JI%2B8L52WnxPQs5kwbOQCivw&X-Amz-Signature=5ce1d02772c7a3d23b9f09a6986a2a9b39eeb8119dc1c1a412c431d55654ffb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

