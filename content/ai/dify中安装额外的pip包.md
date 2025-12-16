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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLI2NPET%2F20251216%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251216T025520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBbJNCyKlzO2hFDvcOxVL%2BLyHtaiiY8BZYiDf8NoFmCTAiEA1vQq4R%2BahKbMHLms7GGUNN9Nop6OGbUEtiJ2nnRoqAIq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDDdEw34rJeGAoC7sVCrcA2FWduNP7seKuTXfpl%2FVFaKRL1eSK%2BIOX5t4vCaUacXESZZl4Ip1THaNp6HurZ3MBhfo37IG32mk0visH5bqEKtjaq2GdNWF2ySVY0E7pG21QklV2JNn3FGOE66RrJr97dKDBPuwv9BDaX8LfbOjlhUjhkCptnwrGMAumyq4weoW4GHbVDbQcH4wF0QoxRGfU2e6LgLvMHa8QCtJrI0mBUXcGgOoO7IjtTm9I3qNciyg7mwO%2FRf7AcYVgT33cLLaHOav4OY3qG4psL1v9jXOC9s2mlsPu46t6FLdyYi6xF1xZIkJY4iIVC%2B8dpU9DWgDXV3EvwrorKTMCCUMtHtL8gr9ESGxwSHAcFcbfdEuQt6sw%2FdV87%2BIM0vctFhW7klmNaQmiDbadF16NcMBxxulL9sZxAZ5E3SbTPbCSESOc2nrtCFxVsM1NOZszNfP4sNmlJBdO%2Bp%2BbMgLHHuJqxsdltoHLKDliF%2Bgrt%2FE8CF8RR42AXhSUMUX8IIHmifXUKGxFBgYTNpg7r8ARlvD4HzdQzUg3YMzG02P0%2BpB9OxomL4stbi7%2FSXNSfY8CGBit%2F7hbS0jTC07Ahfs%2B6HnZZtXLZA89J55elyKfvhr2NdXnXU6tUiwsXn1MyjGizCCMO6Mg8oGOqUB8EEviJ3OEYGgNrw49KJbDlR2nyI0qJJN6H0rM24ETeNBPB30Gwhcbo1pJT%2FA4tObBC2IfBhcZJuJI6zogK%2Fxl5XeGBOl5N3qrqK6l%2FJz7Nm7RJRSErfKK%2FhMpkRoYOW3evo6nP%2BEpheiYJmBvymJj%2BdP9wcnfwFC4OhOiP2U%2Bd6EQ7GlGX4k6B1m2Of%2BG7Ii4EcDQT%2FHTJsXnQaO6DTsxM01vi9N&X-Amz-Signature=c608ebd8ba5cb70814a37c6eb203a197062a997e4e8744259c2df60e80334368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

