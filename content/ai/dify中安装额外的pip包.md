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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5Q6S4NV%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T034507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH7x3O6rRMmsn7zAJ%2FFAG%2FOcXDgkI4mn4edEIrEUbx2cAiAFhc%2B5EaL%2FmKDHg7lDoH67PzPspAAnNwsYAFn5WrE2KSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkn4ByIl%2BqPiv3WPMKtwDe5mYFNkx4vGeSx9S2mr6tgNg5nXZ4%2BdshocubVsQkRu2iKFU0BhMgyYnk4zU4t3ElzdPYf9ExIT6HD0LSKFSrbJG86aaYjZKacBMGMMNzTPi3jWgv6Kn6nTCDtH4c7ojI74oM0zhwp9sy%2F60Yx2QJswSk06X6yUAfqGQpu2gfVU3VU8oNzHPnMuluA7rDo2IXssB%2F4fBnqCVXWPo0zuUwt5G4mwbD0SqiNJi3bbB%2F59732a28SRlyULJiulnrizIOEYNcoPrGPYV797HWlUqKArD4yOcqg3TCNC39N9r%2FKvNdgmCGt93jr4IApSop1Oes4wAY2uykQMNxK%2F1%2B6%2FzqwiLOi1UbUyVDiS7%2BSiLEyt3fEjhqQOMPipP0z%2F5vGnrvax2dJKEV%2FSH1lKhNkZWtzgQ7ljG7cuhLBVkNxIwniYat3XB8%2B3YwLkTO2HOH3Lfhi9CtXTPKGfR8RsnvpyIZ0OLVyy%2FqFQjfL%2B4S%2BDp7CZPhDQFIe6E0qsf2KrFu66%2FaDNdmmLcNG%2BaoL%2Fe4Hi%2B4VihHuicowChoBrREW3EG0nprzBLQVv9wuvUG0YvpyrVd9Tn%2F1QuamIAkNuxcAygj4TS1G6lBzDdwddm1BNBguDJoAKHMAXj4uwX9Bwwi5elzAY6pgF40p73yNOVUdv44oAEqJh2qCYwaxcgDeCfkOKwnD6kt%2FDofjFUQwoiDL04J%2BFJAvBOO9Ud1J%2F9kILKKkaxMV%2BmcNUIGXQ%2FcO4aen9qNkCO27stYGGx3MOLmkEiygysghXr5%2FhVLETZx7rvW6ltTyGbNKRLP%2B1ejDdT1gm5YDQAHWyAltjJNoSClnIMexbeXSAn6m%2Fus8im1UVSA3F7nB4x6Ol8bi5m&X-Amz-Signature=0c7bb206fc45bbe404131196b5884ebf9428bd485e120c346e3170ad67b0c2e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

