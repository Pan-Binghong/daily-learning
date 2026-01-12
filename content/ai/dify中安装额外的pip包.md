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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIWYORNX%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T030743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJHMEUCICSugoG0puxKKIeWK4LAnMriDYg1%2FdABO5KlBemVCrkdAiEAp88U4O%2FVUW0NHBgGGs8D2eJCimQoCs6qnwYxOB9G%2F1cqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHhObatXEoi3clDgGircA66l9mNN%2Bxj8mL7kBnunMx5XMqmRAFPSiAarihATJfGC5E8RgkUzprJmHvvy9yKf7YB2Rjd4zHUVNjDFgIJHEuGbnab6aEQu%2Fd1HEsi%2BnhdWrkLhB%2Bu6Eb6w6%2B3pNsczhXkbXmmwmemxhkmhUZeJQ0gk5WNvWrMsV8TMu7ZKnBiokrqBZipNSJ%2BQJIMBHWcoePrWjO8HkVPXGKOJeiSFF293Ry%2BHyOBYILJj9hr15zyDBEK6VnLmjTwromP4t65pqc54h3Y9vMaKzmHXKun59s0Z5C68CcO%2BfxKMvUb%2FGjOvziOv0bgM%2BG40RuBwOZ6n4HoBKv90Nwmh%2BCcCUFRlodJigkx8aQG67vIdFM%2BLRaKm8gXrFdQ2bpC1%2BQOBL7U5Mh9R7GvppMz3rpGnwBkRLkAtmw%2FI7tPx09ixowQ6NRPgxVVETNNy9D4IFgLilnADTV72WrkUwnNCi50gt0jSOcDhhO25mxnOyqmJndZUYbNw1krEhZfpk96uuQZrzCCpSwONfmPm3BPFmW31OSJStZWhSik972u9UPro0sK01jVvU0NC7fTDgaZlx7dXDAjWS0SYow%2Fdv0YHg2J6jRGbupdptN%2BRyrz8A%2FYPRW3FTk%2FJ71lW8uRyrkwxln8RMML3kMsGOqUBBudyEzKP8%2BvZt7mKsFk9usSqzqigoMu%2Fcbsru8%2FWr9iJSLIELNTCl4qGbyaJzdFwOX3vHEszUp6nF2MsbnoD6451y1Srb8QCzUqDLISu%2Fhl1i3UXqldu7rn782thgDlTbe6Pr7zy3%2BxsH3b6AaTPBtw5pSCAPJXFzym7T6W9wiEowqa%2F1PFLtRQ%2FFDQNKDQuDfZLFWz0sJmVmt1ytOFcdifrS3%2F%2B&X-Amz-Signature=5a684d81d0c1b281c5f6e04daac12bc4a838c7a188fe7697b6a5ee8e8d817f5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

