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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DAHD3QD%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T023919Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCe2Zdt8FIdpBREfBJNRgKmpUzts9KOyoLL7vY1k1%2BlIwIgXp527FY%2BGld1KQ%2BNX4RZFQ19k1Nn4DWtoIIBIjjDXqIq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDKd2kP9%2FtjngTOvDYCrcAyZ83mJ7snZZ6e3u97IjrvNlYieqc4Sey5tDwe%2BeoqtLJYC4Nfa%2FdHjnHZfG0nedUdNBgsbFSSbnDqZ5JmK1wCI1YDBS0dCO6Sc6HyahExNKivNKEZtcZeP3zPr5OONQMzUQVzrQ5j%2BKfzt0xMrN6mc1hnwDMiWidHZykE5rgn2io4ya5UYf7491mRta0C3cLdb1moF%2Fm70jRdvpoRCtx5zvYGtL17L%2FifTFb52afiG7iHRozCYLonrxaDAJPkgG9pPMUIrMKPJAn5oj7Gr%2FzU4AOV6H5KVKjxePL7j31%2F4VI64l1YGB9eKx4P4kKL2aH%2BdrBKRnYNxURMj2WgHW4tMQGWaxl57RtM%2Bg2i4jl2Ka7wvfGxtkUeVfONBeUZd2fTvTD70ydDUZ6scWhydMu0qg3vE3KETKfzGS9Cf6HW3a9KJtMZLNdE77Eavj3ZaVN9GlGYVaswManglqaxStLCT3ffHK2uCupxFQ%2F14zwvrzrKmdFUMujjTgr%2BZ8P3EBOhXgz%2F4I72ga3an6fgbGKYNzr7kjU3uEXcwzEcRJi7F2%2B9NFTkdZmPz%2B3joUfj9knLmXi4TJlK5mocW%2FjC8ArSR0ZUPrKFk6p8m0E2ES14ElPygHUUhrKbUHGs77MM%2FA38gGOqUBEPZzi483JsedWm%2Bil4AoaxtqUX0tSG3uOmuxHzlbqWRSleGR1YIB4ddaIetlkTn7WdRa6NjWauOwW7tXxpvHLMlUDYHcYaHOtpt%2BvJkkRo6wyxF7IaYnREPzOGfru6H1fMOBHwsVE1wsntdYW2%2Fu1AZjzwLUP6Zv8FYH2lKrpxh0Pw%2FKNiv8IXnkIkDUBn4Lwvnkz6K4kr2ruhUFGDNmVheYpMqO&X-Amz-Signature=970f8ece5b4f65eb27153bc387cf56b5ef13358c7be24d4516f4d423b74d0a0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

