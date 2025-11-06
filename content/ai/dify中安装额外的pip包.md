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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3YEWYBS%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T024516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDGg0cipbtl%2FfjfKH%2B8aZDNh5l8ExeQQk89nrrraSIY1AiAaQ0%2Ft2ovrsKfjIums1SKIrkdjsY451LX%2BYTZvuGjIRyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FhGNfwWDw7gGstH6KtwDq41X%2BD01FNlNQVRx1wCKYxOKZXD6X6bIs%2FDDFfic2bh0%2BYA83ccW993%2FfH9WL5QNq7jlazLJcYKhaOiHvKI6faD8pz7ypKfSggp6LjLFPjO%2FZNGZUmsGExK9uZDvwhfOGaMcT%2F6SsHKmK1iaSuMq3V%2B4e%2Bg6ayuclYcQ8eD5a2J8Vqgw26HGkM0PR2ZkgIiWNehA3y%2BoCAdEf2nqXqZM0LveqBh1YRkF3IfO8vE34G6F8IP%2FbjlgvsvDEE8QrCAaiBG4gtDTYWiHyEcn1j9Ms%2BmbfxmgH6rcG0dpRGMyiq%2Bgbvr%2BKl8Y%2FAOzbERXp%2Fqk1MNqWF0yDXjdrA1V9F1kUY8hzREC54RONwKkgq4FDILE3VDo4P4u%2FVPgjcC4q0gFTIU4MINOaGPC5zZpNABFxNOo%2BM5GIS7qcKGun3IWGf8HbUFZpr5orBI%2BmvDOxgCUktOUJyuh5YcpVmNVeoIxyqJtNMV84LnzD2LhWuhrC%2FgN6OB4j111hKOfpPwHbNwWT7bzNTRrWX%2BKvN%2BpxOV2LrcZh4dDIoN36%2BERzycOMNH81SSlredMn4vyjX6MvLpAZAYrXfISn54geuWVV99q3PTQ7eDuatgWNetB%2Bpe%2FypZrIkpfHvxENZLQCFIwy5WwyAY6pgHXLe%2Btt6rLAweUvo93lX0dDCrOK6UWmNLL0UwFxEAsVQtyOGQEmLp%2FZ4hjm%2B5lguOEknk8n5%2FB06Fz9jHLqP2jrYGIbTEJioryhUyUsaLHFOl1LVuh8o7dDNtUZOZ3Z82U9XHylpxDNDxmJWu6fTcfuGRS8o2HdmiDH4hJil6hGwpYGfn8eraViWCoiFPfaqSTshF1pNNRcQuZDHUnvV7oFIBdb7F8&X-Amz-Signature=6c40c15b48630481f5b61f3dc7722a9a3768a78f9eae3c689ccd17c0b9c7dd7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

