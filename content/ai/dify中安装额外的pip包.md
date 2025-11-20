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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NNKM7OA%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIQCgSaJwOEhc8f87Yw5hCrYiNTZV9lGUWRAeFUvaV3aHggIgMRXCtTXagEu2F90BaPTi8SMVsgpKQmbuvikLaCmyofwqiAQI6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIu1NxEkC0pDr3N6GSrcA7zHP%2B18lZRJT4yoGsyxYdDvalT9JSygbvDuLTbTTLlPFL3fySTESz%2FWt8BZGbiIEUJ%2FnhCYbSwoJlqsWQLTYydfuCwFHtITGwvFtyf7%2FhwbW3LcUVsYbduW0HW79SbDru9Tf7j65l2dRRHJazoLLrHZJkz9%2F5jHdvED40tMyM1sPRJ9OjTXFQ%2B2m1rIYCBXmBB4AiXNO7w5BgwxqtzXZTKWrUHaXJkV1WQ3WO%2FeFj4Wa4a52%2FsVLuyy%2Bgo%2F1clVcOPY8vjfVPrNHeM%2BjlDemIu%2BpoQdOidZdLazPIU%2FqTHZsWve9%2BoTHknx4BLZnVSUZ0OyTskKxmQoaRh9mJjE6ERHdOB4TUJjPhM80lQoA9dhBBFcOtvY16qwY6%2FLS9f81xvdokIVv364LBMO4g0WvOmqL60u7yuBx6ZxjIflSy%2BtCYwytvnMqDbkPD0KjsSMRolvazeji2Z3tdX%2FQ2MA%2BZg0XDRWc8GYuqnFb05rp180RKfseeU49ZWK%2FGBjOARs64fxD5nMnwYJdyCVaBamXFQv1sHcmjaYO4smiAgIxVhPcg851h5pb%2Bl8Zr4498u%2BVo31MkwseYcziUtCknSXTWVwm5xgmGQc1EFDFJokk%2Bcmkm%2FAATs4ayIxQgQ%2FMInp%2BcgGOqUBNWuJJ%2BLfYHKHVV8iYf2U5%2B48sZxr4aGCkOc21dLQgWuJ8c5iF%2B5SaqPV3b0gS%2BoQYnPGbwHqqKPQNUjXx4F1VYcW%2FFbAjUwHVpSq%2B%2B1M%2FENNu39NTpb3qmLKG6gRY4xXyP8Bddq2Kdxpq78oUnrfl0fXfDC4%2BnSmGx2qXr%2BMyHBlrcnHrCeFUF2gU5u9rZilkCwKo87Lz0qzF4822%2Bt2jBm9DNHd&X-Amz-Signature=00d24272abfb91f633ddac1d9ce42baa015f7b3356c0f754b27ae86abff8d50e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

