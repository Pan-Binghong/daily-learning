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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z6NVVTM%2F20251106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251106T014305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDnBsw2XcYwdi2PCVA%2Fn1jr61VYm5nZ%2BcnVcazf197d7AiEAlLDetKGhnf3%2Fxeie1MS%2FrjQlSdiJ716oiYIxRYCZ5s8qiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFndDBPa2BX6XNJ40ircAwTE1JWccY9pxk5lw01yFjk32p9GnMv1E6dZILs%2FZMoESFuk22TJo4WSBiveegb18wSRReCN2K3SM9gH%2Bwa%2Ff11Rj3wpqgFpJHit2WFP0v%2BryrxBmCj45bMEQNipt%2BaX6Gv7AwX4UzUrtcGnMFD8C6kj4z7msG8LZPDbbqiOjKXmIYa1%2BZa%2BYPXSRaftICtnAouuaztiMkPoncyVm05eyrYBawzaNRS7DCHb3lnj5shZBskDqxohw5Prl7ZYt87mSgJiVYMXqBmHd%2Bq4fSM%2FSR2zf%2F4R%2FlW%2BKSvu8v6ZJz1vft61StzBkmodMY7yso8a6Yy72Zd9HhlnSKEGWPZUO5RibA2vgafl6PoGohzCnJfEf1YVDF6QQD1vBZAA9D9hIlAvID6r5IQmRWTkSBQaHVq4QtmWBg3sHLBFQoMoQogwIT6bU9JUEJQKximpTbxs3ph9yn%2BvHPjhVqcf9gfMwE8PwnsExfTIDszqnKN%2BtHI8Kgiw0dRsKlax5l%2B%2FN2IMYWX%2FpIVcvTl%2BxPQ0PzlziRplJMh03wFsv918rfUcZ5UPo3RFSsI4I%2FlSY6n2JlO99lz1%2ByiSNW6aqoSP2gR3qezCappsWIQ9l6gawvkQnCTKlysXsDTIz1oRZRIgMLHyr8gGOqUBYAagyUw%2FpKuOIgmBJ89n6HDvzxAYA5W86rdwYXTZaba8NvfCZ%2Bv52E9Pqz9imJ2LkLif1N4Qhvzxc2neGlK%2BG%2BMU8JwdBmEKYdqs%2FQ9U5c2HgkB2kzAOHd73ZBk0MaR9p9WALo0%2F5Va1bzE6yVIEvLmnhoceUnHJGHKdeAuUmaujcYfVdhj7P%2BubMUer82yNH%2FsctYSwzU1iv60OeF4dCmwFk5dP&X-Amz-Signature=c7d0afb7461884306bab563a88527de751857e71a333c5a50988606bd836cda6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

