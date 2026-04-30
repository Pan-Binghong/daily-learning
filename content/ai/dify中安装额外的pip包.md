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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO56X62Z%2F20260430%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260430T043424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIHjba%2FZ8v9utZ8osqK4IWg%2BJ3Wgv2IudHZb2qnqYRPHcAiAg%2FdzOn1uC2tJMi9m%2BJ%2FRkZq7yJpIXMMZsM5E5yvszzCr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMPkqUqZJlfHzlEmWLKtwDzQUVP%2BokEHFayQifHi6kzdjUcB%2FTB3YF4czDDNXx3ZnVIGW8K2R6fBhbkk6Pc3sscNVku5f7mkgT9abN2Fi1zgLWQRVLY0aSt0s1SZv66vmzCL8zL9CVm%2BfuZRbl23B5KBo7%2Fbd65ARJRoHR9%2F2CRCjZJmTRXQYDtyZpv%2F2N%2FHajM%2FGOaXaL2pT8UQT6vB3YuKWtgOfpr1MLeJXbYiYTwS61YzgTwijV%2FwZx14u66O4hTf9q57%2BjKsTeq5fovfA%2FYC0HEpL%2FoXErMuRCNGC8SgEMafurnpoGzY60NNS8oVV5WtwS3M01cf3lzAdt%2FqB%2BG%2F9X%2FeCXIdm5o4zLe9oLHnoDMq0Gzl2TEpBQCIqKRL3hQvirNEOxwVDv8jYlYLMmjACQX68IdQARZayf0jvHJFlosJ07PBrFnGF9vWgaMFrC2SqF%2BzZ39ufDI380BeSe%2BJ3YwRe0No%2B%2BdGATNrTG5x%2BtRFiU6AkRs%2F5SXNzgqx0CUE4jchHtGtLNuzgq0KjlWYsYuE%2FnBaNLfzic1ixhyvePXMZTtxYAd7AIjewlbOwPJrE0xrsAkaHV57ETPpZaQjapGX%2FGHQjxUZyFP6dw4BdRX2camNM0H9%2B%2FIbbfmMRSRQpig082hgwiwU0wlrHLzwY6pgED0igpssevom3ZtnEdeLIc9GkjR0cYaW9B9rFN3u5NmoOe09l85K7C21zqtqCx0g6d50FBNmlPGaSgD8%2Bc7O975TkdlV2BIhXf1n8LmFKOUetwKNjuJOBTxAtrFQKZoBImTfjmRcEKl7VpqSdFlBiQO%2Fu9h1AWNCqc6l%2FozSWvgbhDIROXPWohbB7dge8FShbTymQeiXt%2BzNBAi%2FH%2Fu6pEq29xOKwO&X-Amz-Signature=3750e25bf9dfc80ad685ed3d26683adb2801fd3538d63533ba99afff427bd90e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

