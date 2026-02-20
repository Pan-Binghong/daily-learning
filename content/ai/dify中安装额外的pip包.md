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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4SUBKMQ%2F20260220%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260220T033425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAT9tflIYIa2hgU2BpkOnjhp8nN9%2BBQ8UuxFkUNM7KvVAiAQ79PEvi1bitkqCz4RN9reMwIpwFbdR%2Frf3QRM758nxCqIBAiM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZV6ZLqZcjZ%2BodQrrKtwDfdjqJbXMM%2BLqqEKkyH5A%2BrQWQlugMiiYpvEaseFdS9vMJGr%2Bf3tI1I42R4h9STsBKk%2FPHTX0Dd6Q02WrPjlao9YczDZEcsYoeRthJz3CfQex4O54IGxNygkaA5IMHZ%2F8qZwMfyDiTJezJ6YHgzycatZIFOlb93JIs86e1ly8nvjB3y1m7%2FoAgh1%2F0Jxe72gKjsiris3Xkcn0RlxLEwViyfpJRwQ8SYjeGFVpOCAMTs4%2FVdJ1NxgMEJ0kix3vtGA5EmNMoNKH0496xnyjb7MSPmoko72Xy99JU4puXrKd4Cua4JigO%2BeO4Gz3vQ23MD1seFuJeXLU8XN70HQ2NqmqaFIQGEbMB8%2BIXtFC4KK0xPnjt97mOHLFBeb5cxrHFnVWNNYfM2ed82jD1mKJk7n%2F7r9R%2FMcpO16IT6LN10oTBDVmF%2FlueqO61mOh5x7X8gcuoa4IcUsfDFjlWXvSmu9PoZmbZLuGEk6fgig64xOGf458A44R9eYsgSC0VattbjPTloG2gzNKI%2BkTi2%2FifL3fJwW6XrLEIK1qUj7Zx30UDJI8RnZwh2Sj3uaYEuG2jnrjRAtAIgG3ZaUwLO1TVdaKpEBxmRL14BIPLeWEJolUWkWwqPDLzgcdP5ZWl2owppDfzAY6pgEs8QkExtYzCBmwc3pRTPb%2BhPhQGGcA0QROB2N%2BTQryVUPOySGDoCqsQ7jYmuQstDQU5LNe6mcaz7dpx4bQyZwq9oha5mf93%2FVeH8OFWjFdoMGA0ChhMIYPq%2FEkCIKFPrGpvZtfvKdff6Dfa%2Fylsihd9xmg6OOWDpHvtfmvPNZbXDkxm175Hs1%2F988E6DbrbgTkxc7yOivIPNd%2BakTW5NhXdKu9gzm3&X-Amz-Signature=8d24728d0ef4eb906e209d7826237e866337d0d90b884f20b45260580ba89c2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

