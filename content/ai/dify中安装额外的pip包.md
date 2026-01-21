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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662EFDH7G2%2F20260121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260121T030209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGTTzCX52SYdoUpiBTBRXpS3%2FDPeprcDobzwomIoKpdDAiEA95Kk0BctTxNmAKOH4ICv%2FQ%2FBLxKiEAu69Ux3H8oN8%2BQqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB5nLJG%2FhBrZZEesgircA1g0McMrjgFsAqOgZBCEFn5hpYH4cwdf5u5xZ3L1YGBUNVOuUHdJpzLWsMdzjXYUIpuWMxwKMcUfXD%2FPbxzBrkL4Bfy4sLCn%2BL1r1txgaW4vqDja4HglOwcOlX01K04HXwTSrvuhDqJdLgSItvNxRR6QgHBHfpDhDegwV1e9fYvYW2txz3uDzovCnkIeK9TxR5e8SdP%2BpIlZRrT6VQQ62ma5Om5xwD3%2B3gcyHRoFtlPPg8Ydgo%2F4WPH%2F%2FbMD2g5XJFJJ2bEslfKyEnymDY45e68ONgr3RiWJZnA9llMWyNFuNxUjsKG2YY%2Bw92HadIQrDYh9FJi2ChAjN9pxPJoTmxAA91g3BvyfPUfoqLZtF0QyDblfZDtZivbntj5PV3S1XGSBMvL73InMLW1XUI1tQaoZ8paXrkaw2pHdw5R1eACBfoxNxRWSow%2Blb9GsQCxb5V%2Bv%2B8pDe17VRPG16wESf2uCqEzWJN7BfdZXeBRdWjgYeR%2FGkuILHfgYbuhIIamdct1L3KGh9mArwfuO3o5FPzBuTT9hUcMhAoPKC5dI%2Fwxksj%2FjblRm%2BoMhNoftQR%2B%2FstT%2FfS2mEaG62%2B%2ByVjw67Cz7PQ5fmVxZ1OVnZvy6V0xpiRtALk7%2F5OfmKDR%2BMOTXwMsGOqUBxnNddUKRKKPB4MbKoARPb3E1vhAaccQ0Upw5W59maf0vVpL%2FtgNAGsiEYdZy1ZNzuxlT%2Fh3x8%2Bjfh1aySLJKdk1MXzLOvTcY3ukDhOJGZ3eSbGy3S%2FKkzRRXJFKsO81voy7MxBFRFglN6W7%2BUHMwDrNgrz9xe0V5B0snVqFI2J6a5HxGKfj731PBbzLo4YM6N4Ah1Ogp344ZiOkNemj26NmbhMqH&X-Amz-Signature=658cc61c0a6d1f8f12d54eb920115ed3bbd230cb109b2bc5d02182ff570a2d5a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

