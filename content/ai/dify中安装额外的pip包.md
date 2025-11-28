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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664T6PKTCS%2F20251128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251128T024309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBXVu0ych1LDNHNplKrCJf5lFJj8dVEfkuYrXnzMhYQ%2FAiEAg6%2BOyZNQi9qilCsrwbTZa9Zn1yCCoHkiFIIbNl%2F1BPgqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEZH5H%2FgAjZeQ8MBnCrcA2e6iE7wfHKUtMaBayK2zQoCNnvmlN1mmDMWkAq%2Fg6thRMCe9qt%2BrxJGI0Bwt%2Fq2XCyPQd53FaoE1iEI92Jeq8Yhd4cjf0x4RfS02L41CCx2Vxwwhn4rTo921QaQNiPVi7MPCuINYdjKO78Yl31i4Vt1RWqgJS1PcTavojXFUtmcCJ6RyKrH9hBpgLGJKwe88aNUZxU%2FNtpnBItGzVu9c5ruTj585narq4N4nueVVkbr%2FmJjGgvjOIXkOYAH2NudgVv6rArYpndr349mm515yJDpebCBZcCAuaOIOxb0LX4zGsiMcOE0F1UB3CnfKnOFItb5%2BS2n2kvhHeSvZxxDaMyJxTYdQ98GtOpRiLgxB6S4OKSF6LcnJthG1ImPox7lP7hpjwYrJxiJGCtHrOBP9rlBr%2Flp0di3Z41TT1adDXIqSubWsPqkCdUeflDxy9UXe7yjgrWTsUQf3cFiT5DN9D%2FhoJI3aTNUZUO6WAvum0paYEsuQmiEV71Qi3hpoWUTyUePVHCM2j9eudU4r7KVR6dFw9P%2Ffn1UkBzXPem57velg7CCTqmC5i3yg6F%2FUQ2srijHwqtlVO59SxvLGNpJdvh1StOITEDRy95iryxs2nE1nWXLTUz%2BTXtbknS0MJfyo8kGOqUBuk2mrtOkWuZ0h6djM08VBVgkGfSZHqqQYW69kiiJPanNGFsNVnt3ts56qskHeEuWH5L6cWyrRFTlRCMarvMuuFF9X0byy7PLptCtEPxZn4cKADH099%2Fb6gJSHjwqTV0kM2PzgSw0VUhyjqOHYKcnVjT7yn3sKGfGj7RGrv4xxocZCBMcgSAAaMBSSWId9ewEL5Uj4IkvNfE8WuNgxSFOK%2FMbtTEc&X-Amz-Signature=204899a600155a8cfb579dc3e4d3f35f08e1e894268e7e4b7bebd6e88aa87a1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

