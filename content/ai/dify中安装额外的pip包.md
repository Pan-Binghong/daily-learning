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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U2QIDUUE%2F20260201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260201T035020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICZSlFTo8Z4uPNa%2Fk2TWW0JJoeeaUXEySO27vpBBGxuAAiAQUBywYAUW8D%2Fj9eg5kJEXTUkkYVvvDWLfXUbEOQFXXyqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTcIbPm7SYHLMT4xCKtwD%2BR9U1spuvO8vggGj8IzYG9ZkVAgUEt%2B%2FYwCxeryFQfDyfpDWG8BAkHPxw%2BdNmHgnjUzE5QSIuHmVbh%2FsCq9IEWaYmE52LLx1i2MWWxddUJq84DqXxVTb2eIE5Scx1eeVVqSTpYQ1cL83ta1N%2By7eg2djN0Xb73JvlI83UQ8aDdl2TF2GBDcbnklcocxlETsVjU2lo44FXyx1pM3HuiKq56PE%2B7Zrt4dKzzAAOOtpDel5BHWl1MESRiEFnMJ%2FL0d3R9RBwsJO%2BJDEDbL25gVKFJjZTVC%2Bygi1y6hgoFJvW38jYzQ9YXhQ5%2BMHkwG1kfeTwS0%2FmMDgqyAAdOrCMzNUBw1WroPMLMyG3JfD2xiuOyEN6lsUi3vV4tqwCXPE3WcviqHNS6wG7gkE%2BCYx5zNtN4brzC044PyCAEJJ90iscigguCbqh5V%2Fh7wV8fd%2Fu8QqPUZjmgv1SYGwIpVqcqNj%2FjNlIdZxhoqvwwLu5OQ8%2Ff5Y1UOwhBhjSrV%2BZHKFFtiYLxc7uRDSuysSH57euYWjOAP5BeawaEEgJ6FtKsHKwSfkWFlkIDE%2FbJFx4yrW1pXpwgCLZDsxHV%2B9zI7hF6sqRJHA5sjyCco59R%2Fax8WsisUybbWVUugoftMuz88wppP7ywY6pgEyqIIsGEIFn975Jkwh1s34RtiZsl874OwqyPOHIVB%2FrpLKBayVh0tDK9lCsg9wCvyuLgvelifxopsix5ROYFR3yMb3Y0uQIy2NdW3ZVpO3lgzGotKWj%2FclS%2Bv3iAe3QBvCljEGRpvZuYh3UD5FdbClCSK%2BfQNFoOnxXdPhb3crZvRCE8zPnAbGcyrcY8aRjRTA5%2FBSZo0U9R%2BoJnsQrF8W7cKEkGQ%2B&X-Amz-Signature=62e92b5c450af60437631eb16830e924f82d7ca5f87ea3d823ccfb94b65111e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

