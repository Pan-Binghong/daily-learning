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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U353FEOK%2F20251130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251130T025807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIHiikHWS0h8SOF80XVL0nsHsOTMqIjSl1CWPStvsLCO9AiEAwjDZS6pjo8zQhPDM8gHvQy2XeYmhMnu9eqHEqqeSw6EqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK7MsIbTtydDHUqe%2ByrcA3DemYzLJRrHSDEoIcQM6fmHwJG2xfBdn2X2UY35iL%2FJEaO3djwiqgVTnklWB9TT4tEw1gwKaxNfdvOH55RDIJeWrrNp%2BuJQf2NcZBUTMT%2FeXAv7WnO6HkkM7UrMP2Q7NhS6cBM%2BquL%2BRMQjRGjrfmQGrF2JSzzsaWSt65g%2Brx%2BviblPbpkP9E3iPkh8U0BwQ7E2mVyY%2BJnYOtTOM4lpqUnuQecDCNWFIb8Trbn15WvIjMm02znYT9HSqCrI2ODBG0XYQQZ%2BqpDeEeCqxvIWsJ2strKCsZyNr68in2Os9rcaykRUlkg%2BADYBqW2fubk9AVaRBeW0DBCIU0JrMsGjymS6UkJA5XLJTxV%2B1FPZ2zbWQRt%2B7AssFKMWcaV1vOG%2FMdKjxv9pkU6fmtesmojD%2BGL4OM4IAL7qsNq77F6u96UHRosRxRj%2FU8yYu%2BBl4RDteNO96bIzbq%2FYEGbWOe8DN0d3%2BTBEySH4y7fwjgi%2Bb8tm2p0rvsQTVUwr6mUVQHA0EIv4iMv6AeK5ttpldm8Ggie89cM4yVOAnoo3vhjXkLwWJHhS42Ndh9YR2zQIE2TPVfl5KywTXAy2X%2B9mdNxdctQDD0awYOqbGSVaCCIyTBXp7jXU0zXddMdMsh%2F5MNHVrckGOqUBQSB9cqf7%2F5mg%2F0Gf9w5NDkR%2BOaCpmJLnX9%2B04HDrXerSn3%2B4BJh5Q4u5ZGF8TiOQU%2FflMq35IOJb9mCn6v9%2Bt3bXe7hdTGbW3lz1%2FQ7REPCWKuoHR2LqDDyexvzo%2BGuu8oJddTW%2FyHDZ6UQExw5aMnCrf%2FrPFRhHmJnWMPWCFDFCPahVZqtIfSjdflYauCAYvapnaEkIARIk6rKITA%2BCMRjCLnrx&X-Amz-Signature=e0605f38a3236c5cec52e6c3064bd8ef8532e8cac7c62bb7e5c73980ceac4a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

