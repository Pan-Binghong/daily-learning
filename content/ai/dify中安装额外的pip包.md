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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMH2GNA2%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T033223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJHMEUCID7Jf4yoylHX%2FYrsST6QiXAGlVkXL37Xr67a30Nhl8rfAiEAjr%2FVKJj0tt8YbRan7f9Q%2F%2B6ZZKPKgy8lrBDvhgz3d0Mq%2FwMIDBAAGgw2Mzc0MjMxODM4MDUiDNEsBqbzggx7oc03XCrcA4Vr5%2B8xNf6Vg6%2BXjwMDLQf%2B74Im7A0O3R5SMIUobWmm9PMH%2FKSg3r573pmyEhXWbBfbC3Ssoi6t4Gmrp56AhK%2B3Eyv5HArK%2FLHyMkq8rZTcxPq7nGx8xkGgK1sqKPxl%2BMO%2BHC2V%2FJeqsEVGyaHOXRFo%2FASbqcJmKxeO00I3ot91wqe7sIQV6N5ZRq7UuZNs39ga6IgT0Qfci94mI8wBZsiV64TZOymx6QEXnbB%2BV2C7rXtxemKLhzUyPz1T2edZZlkg6Y61PrNGcRplcnlv3moe92rkYuF0vviqd0ajMx5pNCpIuvxbz0EA%2BCZ6lDaB87YMkXzX5qax6kgT0jSwm%2BP6J6YiqUP%2FjYvSZ2wZ1AZrbe72GprTlgox2eXgRKhEJXwZjhT6NKiCJFbSADg2zy2%2BgYCoucKIhVjy5QXMFQzkz06TuuN%2FXjZiQkqIxDq%2FA1Pow6GKaCFq6Ao1hPDkZ9nxBNt4Vt6410mN3puFQ35sJU%2FdkRNACyNVJ9Dg%2BWcz8r8cyDVJEQEhz81%2Br9yx2uXU1CdcfGwP9NbDqTnpqT6Jf0RwYN3Uxfd8V11q9fQKGm6HO5dH%2Bs4WS0pYHblvg25NCmkjwCbYsrF48TQLTfcwMeoaLl6Q%2BglQ1a6RMPbBs80GOqUB6tiL57TlFmAtNT8GZlyNRyhivChM0YcUFmSfVRqLY99O%2BbtGm%2BFlcy%2FnjvRXpt3%2BkdGbYcBdujUKi4eO0nzuSd0zUhn2CW8l087yd6YgyqhxN32doDfXTsREH0YLEkrv0v93xxGUhpvqLoanjctU3FCjCU6GGnU2sm%2B2LmgiWrMbP4evzZCTSRDa2MQxyQ69QsRHZibqOJ1ypq3zjPCxJePmExui&X-Amz-Signature=b30a5ae361e7c2e52b5adc2384a1519c41e300adfa114cae9671e14c7f533e69&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

