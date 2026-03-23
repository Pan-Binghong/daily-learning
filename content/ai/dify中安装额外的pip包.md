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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646VOVHEI%2F20260323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260323T034555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDU%2FvL%2BJQh3anWnyMiQwA%2BdyNUx59wUpWh9bqhGcgOU9QIgOPD6Oz4rHtTBROCEn6gHfvJ50lfn9ILhgOX6Ne%2BkW7Qq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDMDbOUJD45SXiaohACrcA6zgnmKNap8oiGqnJ%2FidRt67Vo%2F54EkPmWdMSuROhHEwMSO5DclXL3hsrEVl4MaupgyaNUJcV7wFkQTZcLHpF0e3VRFo4DFFGl33i8xWF9Lp0E4FYVukeSVoX4FVjXE%2Bz30k9jwwx8CthV7Q%2FNDeCNFI%2BIcpKRWDD%2FVOoZB63AajBr0hwj4q8AUr7kY3BeiFGAqkuggFSNXsmBDaMKlVzhaxEEO3mZ4qj%2BuBSUfPu8fRYAuh3P3VQLCeGcu29mAy6i1Iy20UdKzh0CIt8JDQBW9crioHVSb%2FRLp%2FD8GSy9IE0J9UiwibGV3MgPnbWXrFhoTanvk53jLJLdQxYckTND8KbACk2NG2xS1%2FEjK2GfAFfs%2FnGlx%2FU998R2%2FXD2wDzI9jtgdmCyPAP45CocSrc4MNKmfctdidV9UlKis%2BqbZaBQX5exgukY6Qo1LoxUfFwaRJ9yG78pBddDeMQ412XlzPHhe4P%2FKTBGhgdKvMa9VGd8JS0r6uDPPge9fa3E6gfxYJaelnKGhRlAYNkc4ikIZkVQg%2BHGsdhD0GU8dWBKY7k57GEudBBMQi%2BDhDZmtZ%2BIzp0fswXkeNXOwXkEAM1j%2FTTQrCX4IPTDVlfyjzWM5PphnmhapkxtJ8On1gMI%2Flgs4GOqUBrelnar3x%2F%2BPUqguJCSc5hoaozsLHIRplmxYuXye2n%2BuFd%2BTZT0TaNAEHx53UcWKm85uUEAsSS6u1XKnFFVfMfbPCyirRYa%2Bns3fb9XPWly8%2F8ggIYTYufGwXsHUeV7y1fy3rvf%2BYySGbUbxcYCusxhlLnj%2FOtTngcC9Uq3nEILhAM0KWjZqyYuU0PNmZGE8JhyVa3GTzL7pFN3WN2ADR9L0NxDIw&X-Amz-Signature=fc5690e58a96401aa1c96dd9e641f033fbe6c8609e92fdd7fffe55f8445fbeb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

