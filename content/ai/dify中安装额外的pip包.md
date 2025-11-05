---
title: Dify中安装额外的Pip包
date: '2025-08-12T06:08:00.000Z'
lastmod: '2025-08-18T00:58:00.000Z'
draft: false
标签:
- LLMs
- Dify
categories:
- AI
---

> 💡 最近需要在dify的代码执行模块中运行python-docx库的功能。记录一下怎么在dify中安装额外的包。

---

## 1. 找到requirements

在 /data/dify/docker/volumes/sandbox/dependencies/python-requirements.txt 文件中添加需要安装的包的名称以及版本即可。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQI6KITK%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGRT7JjGSdD1ZoP2Y2jTw4efsdKMOV4LPeXlnHzmT84nAiEAvyW10KMsCGP%2Fx8qk8eKoDhF9b5f2wsqq6aEhf7F87TcqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFLJMZpjWo841R1%2F5ircA7p4Cu2MComujeL1NPLBifjZMiJ4L3%2FIV8XOdq%2FZJBlOTgBzeRIO289%2BA5DT%2B5D8qvrzu5WU6W6lxJgjRL7z8odEz3WutWpEdk%2F%2FwL5t0cYWn%2BGpXB2f6yMaOt25ydhYM4ji9cm11%2FuZoiRqQH%2FHX%2F1%2FjsbN1wrdTwWibqLh4bEjvAyyVAyXSXJNQ867U%2BaVCRy%2FFc5iakf%2BAUogVqpiLBW2j2bgL5nuwbiJePw6dwlmtANLCoAcMs%2BTmi1TUAgqfwzZDdsXkUfZ26kgrvm28%2FShw6Q%2BOpS3DL06kEYsf8YCg%2BYvHlB6Mm8wS3mjDjctfpH9iBSz6poLCZOYJuA4WVwCT6HiMz%2B%2FAfYyVn8xkdcZiE48%2FVsUPK7EvMszQOJvwituwmfOsrLI2ZU3w5qZLgkzdtrCyeP%2BryQNxeG%2Blow4%2FCjsRGFnABBNNTwdtCfTRFw6gkNBXnkQIS2ULjBpWJ94U%2BF7D4hM5FG%2BJYKHu5ORHcZkSFdYC5MGDlUOlrnHSxb2gACU0hGezBjIdmJVFT3OiWbx%2BaiwRPiRCrypljUL2f4ahVwFYE0n0%2BWxoEqKmTMh8xjsg0G2Pxp8LqzwsxATbKmxz0g3jkPAAo6bzmsmYonBXYsWG9aCFaXaMMWfrMgGOqUB2%2BF4O%2FTM2wiC1uO1RngEm00U4JI7HzzoX3RCcjmM20Sgek8eo0WDJ6tGLzrSwSCQNUKVX4AoZID4XHjq%2FpFOzCSSCyqgbnX8nIoiS0pTJ%2FpCd5%2BHT3oZDvhM1qlU7r2l2VXWCMNWmZKFhXEO8Cy0yR8IYqB%2FuZT6T7R3U4%2B9PJDt0BwgmUwljY9jwOND1C427CxIUXCygkuJ2Ji8b4%2Bs9uJthCVf&X-Amz-Signature=8da2fe0f45c7104c8a7c95843cc3f21e350e3b8ea253777137d79a6a2d3c06ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

