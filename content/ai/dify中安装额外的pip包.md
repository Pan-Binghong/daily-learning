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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NSGEMRH%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T024635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIDCH%2BXS2i8yrw96neD4W10zgtOYRfjojP73FAc0pfhcaAiBAYK8jA4GwqKL2WeB%2Fe5c1edwQHadkt1aRtGNMr7pWKyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMswIbp%2F1F1d1zhFfyKtwDEx%2BjXZbDTOIdKQGNzbjVjgbTqu4ubsvUHYoxVckoTuYWJPiI7q5NfF%2FVFgLLgHHYPNHJID5TquRKyIOlZDp95Ct%2Bn1aC%2Bw3GlVPwBvw5XXIISd6%2Fp6Wz0HKJMefvNvWo3xTk0azZ6huwkIfbtSdfGQjhYq1RnYo2mTJJksjHdk5dkMVgyOaHRZhCfVn7S1SZi4htqQAFn8uQeHz5AUFuQUvG16xUlbfiQE7czo7xKHcAzEHx2LuJDjd%2FxuOnxoNK0rQjC0DjypXvpJqeW7rXM2IPr6d1ich7PZx%2FgGkII%2FpZT4epUkYoh4Ew%2FjnvHmJgsp3Ox1ZW5nfZSLpkZzePqRJxlfy%2Bfq00xs0s6c7bHH9tl97x8CpCVG3%2FuvRO33BPQ%2BCSwmZnbAfY1h4hSsS0AvCV87ZVbw%2FYgx%2FKWMkjPbf2kIAdRyyKkliUa5Gv705U9vN6d8%2FYMeU6hraj1wZTHuKrT2R80UzILQ%2FcrkkbQURwNQ%2Fnsjgjd1UzivGEvQRith5KWg7mX%2FwwxhFJfj77JpLiik%2FZPxH5Fpr2vynlecx%2F3toBjp8h4EiWHl2Nwp8Ch4Uv%2F1Ho2ppumiaSTi40kI6roUDq2pGeY1ZEP4czF3o5KljpAoYYNg83zIowvo3zyQY6pgEL1vNhFKEPr3XJmMNgVg567KnVsDZUTVlm8adsYfS7TuzBWM3ZPrv5BZ2r%2B%2BXurRZIbIbL7AsvBYv2LRCsBui7tDpGSaiRtceP2RFM60s6Ppii7ohGcZBSkVNJstMQhs%2FcsDZ878%2FLpnglB9yCq7KG1w9OL9s6WRUphYSfLRggOo7l%2FENIms5O0rK2xv1InpN4QrAAhiX0eAFj2sbrSIv5BzNMNbxO&X-Amz-Signature=c7f07bb25b0dc6d63187e3f808e6f749f10e8cade5301d4ab0f700439505bba1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

