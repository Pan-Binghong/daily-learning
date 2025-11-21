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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SW7IY2D%2F20251121%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251121T024302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIA0CoQy6F3FNITrVKxHZizTUoHE87eedeXjjeBhXvhHNAiBeSilt5llA%2BX92zhBOGlNUpdsBKRMNCxz7jYs2%2BSaakCr%2FAwgEEAAaDDYzNzQyMzE4MzgwNSIMOK23kzAlWffuX79sKtwDxTS9lxa1AI6iO5xVH2avg3i8bA9iqW73p%2B8jnpa%2FQ24hLCFHPysVKnS7%2BKkyuia8uO5H%2BkkUF%2FbVkxvTDN2a3%2FBVoqkiw%2B6MDhFjblUwf68AVIsxIcj2Ti77VnJLW%2FhQXQBtB1FnVPdSTgPOFqR4B%2BVp4DZAIv8yGpPXVK%2BlnZNjhQAxm%2BeMK5Wrm8jqGnB58aYPKxZg3aqtZHFvXLjElfMKjVRSY4KSlQF3o1c5knDsHJ7lcZjZ1wQABb3RVUD%2BU1o5VHbrtvgRBzWhew4fiCzfhjaMFqENxiXUfdODhc1nHSztIS56TRRffOA%2Fo5RLRWyiyyCsKQzRLYewjUbEcNEUMMb6h%2FL8v71wfIFr%2F1ZygH8zku3JFb4nBtVRp%2BiP7BqWkOAW%2Bg3CNSliRmH6cSzkqXV7lej9BwaPiDpGnlvLs6xWvA8qMIci10NtMvDnU7j0bTOj5o7%2B0guNLWaZW7ZM%2FWVpXjgfJtQvuRtIHrmByq%2FYbeRyfTJrgGvddMGkfQ4avFb3SKeuj2bJTlO9twvcjl9UAggup%2F0MNcE4t6338s9sGZV5Pz6zYfpOAPNEeikZsbqf4md6oriFJCDIAnmGiI6yCoqks6X15FZR%2B%2FXRwV9%2BFL8mLThv1eEw9Z7%2FyAY6pgEsZUHsf5pmuyQkOcUL1gzERk%2BKnWF8Jpu0m%2BVGPj4wZcpNizyslk5ZLuLvk2JeAmSF95ddr528bMHKSPPllqHtOIuBXMqoVgk8Fm8QmpmyAvJcJC8IN1XZf0XUOaEeOEhNvqth0BE1G1VCy%2BW4nW2DI%2B%2BS%2BU%2FoYafQVOFPn94O%2FThYS7%2BEOOYVLPhdFKYbbmYw9W5MwnLVqhs647EA65EztD6LOSZj&X-Amz-Signature=75e6d1013e7401788c743242a9ded24fbfcbbc28d4d1f558fef8d0495af10812&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

