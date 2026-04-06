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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W6VDWPUR%2F20260406%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260406T040920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3ryqZkh8Xk9fvvShiclzO94%2BShxObMZeArEILZnOskAIgcBivLrLnYF8HsvlSPo3rp6AlRsRDLvwVPEVljeXh7EYqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNj20PczahxX%2BeGAvCrcA%2Fp%2BdkbXqzmavm%2BsHgVxfxyAZ0RccvuyDfx%2BWQEo6AMBphVHJ2Y7zl4dcVEzgbHUsTCFfzgNox84RgqG3oQT24ybz8lMiuBnnvGxOLp3QhB2VwovsAWHWlJa%2BsDiJAC4AXBG48HBdQJSWK6haWAfUdG0C1%2BCrnLqI8GpEHdJPR64OdQZUiu1%2Bfcd0o5clTcfoAL3EE5w8Z%2BN2jgh1ArDZ%2B8tq5wSEw%2FbAkbLrO5ADQwjIjIGMf4YyfioTWgq57kNo%2FD4k%2BpaGH4EMWWGhAmGWOIyW7cjW4VvUWF2jsxyps0sbzm2cajceH9db58AKwTTpuvqOqQjOwYxKigTiVuQqekAB4KJFeXq3dUJNcbolH7HthcrTof6WxG8n54V%2BvhBMDKxXOBB4uXXEcHznh40HXihcJQVrmaInJ9uHJe1AaaaduiPlouYXSjfPSyjxHGsYWwggFyCZXKaJtR%2Bo1yt0Vr2yxdMj24BI2TlLQlOuY%2BovsfiNwyBLhHSPPH6VUR7CKaAdbvyRCKj24yMpUeh%2FK4r2GFwKVBkoSKGqDcvpyjPY3EcYPE1Lr%2F4eeJQoeVkYF1lKzQLu2sgweIHUlmPl%2BePKYx2kUtIyuInRWW83rrnCgYpLeMlLOnZTxXbMIyzzM4GOqUBFHVOEnzNgeAYiIw39xE4kKBSw%2FTPiP5SLH2yjEjfz9g3f1b%2BlHMb9KR4M5xZhUXyHI8f8vnCYHJ44uZB6dsU5GB%2BSxYfV3fCEjsbjdqNzNzMD48X%2Bhd1Rrr5V4PKoxYxIX7FuJVpgcv0C5ipGV7H0XiM0GdD3RhjAwcsPgocHmFU0v0L4bCOrQTKCuP8ZJyMmHvWZn9tvfGIiHc1H8u9JQ4JkrQ2&X-Amz-Signature=ab704034ae1ef28453e01190a9cc1fda4c29d7797f2df37fb3fae7015cb69b3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

