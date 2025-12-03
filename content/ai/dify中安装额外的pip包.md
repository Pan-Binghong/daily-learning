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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663H3ULSZX%2F20251203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251203T024846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJIMEYCIQDfFqgVrdKp%2FiwsxunQhJMwVkaesNYdlu%2Bhwruw7FW5TgIhAOLddCY3y%2BpUsl2CreAsBlQDnFs4Fwnuva6mLka3XtQ%2FKv8DCCIQABoMNjM3NDIzMTgzODA1Igxezc0taFOFkCRGQYUq3ANgoEEis0bnpX6%2FMGb2bH5ojXVyIhQMsLnPB9eD0J1S07gysKJaNjgKW%2BdZjNnYQvNAQUk9J4LNTUjYEShXM%2Fp0TL4qDlwdqSRRk8aWmW1Z4C5BeHnQRpzAiKUTGCCPGzfFvj%2F%2B05%2FJOAuUTnSvJcT46za93NpTQLCm6fZEPJyePN9rrVilpxfBwlwGXCMDMOQOLCM0UVipXvNnhcMNnK1nUnOwaNPfizM74Z1B4qjei81xHQpxoLz4kfx3HGyz9Z3Rk%2F9GxAN3gPLjFPx0ApAzxQY4Fap39BvYyJ3h20YJ6H0QOMInTtTkfdyFyBLmSENwpKv7vJOutCF%2FLiiBc%2BvV5vT5EZUZvF7%2BRNhf1eMI6TDvO55%2B1uiL6nDD6hiw%2FdWOjcb%2FUlDLVSYIDZzzje4Gsa28jazW4iUiorVv3jvFHp9XVXx3%2BduaQKqJ%2BycYk3WuP32EghSnz9VL8cn8SUgF26pf0Eh9or5MaZqpC935x0EOaArmi5xkLoLMC9EYALTfGi13gKqT1K4r8Ou2roxh6%2Bylf2dgTPUyJb5jJqSRBvx38UoPYYsIqepxG006XSZmTUibStJskrEN%2FbAGVO%2FnxcFkgsBzbeDiw1cbdCObVFB9%2BZSQpt3v6PhbFzCwlL7JBjqkAZ6ehSQ032UszqyzMooj0cEHl10UBeDsQQ%2FAjIjfSXZU4VRqXx%2BrxK%2BHOBlv69as409XtA5K1R17M0siqHltj4gJRIOTBeQM1nlXWYGyacD%2BSB8uYzTp1S81y6NqOW5fGC41Fw9iwGST8vXYbCah4QqSMAJMuNqyEnx0qRgnCfmWTb4qxWCT00pxjXk48TFE%2B%2F7CMsvfcnRKA1Y5VRZWwJfyzQDM&X-Amz-Signature=24a0aca23036f77b7766554ccee9eb5e5655f02eb67437444f0631beafa34d60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

