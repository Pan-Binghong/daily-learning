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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHI63JDX%2F20260109%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260109T030035Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWI7iLc4Dvlznmv3lI02ec3vOYY2Aw3Mt7FZ4fkVw%2FCgIhAOEkCPlSdLw6U0W27qzjlC6s1I3UMCbhQXueMTHlu9IOKogECJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyu9I1NHKILDQCV6Ocq3AOmnpnKKdRGsL2OnZLx53F3%2FD4tFaaHs2qygXPq6JAeGelkNj7ZQmUU%2FVRyuefriz1gPvtVehIzuTA6Lv7QGA36hgnspyFY1pIzEr94lrMVu8vrWtdrh7iR71lmuSXgWYfGF2mwsXHQ66Ugy5%2BCZO%2F7x5vS5t50S04hMpfO%2FLk1FXAzEFp0LDdavmn5dacXbXa9dbp7LSP%2FzC0Cq198yjbLOTq8zlQLAGSqMJSCLtYXtWJGcbiMZ0tuOn1ZIv7lXmN0jSbQgLY7XHZneTK2vk1ecGL5sa3WcFW%2FIODWSd%2Bi1TZybq%2B6J0aq9rsYA5aswZszGKvSO8VEyMInIFz4H98i%2FsxWfsOKvsGWY4m9f8v19%2B97lQc5vychCyXuUneY65P7j1j%2FEfa6cr35pjkC2VXNoXgHmHvelLFHNzXJDQfPsQKxYCa%2FFxd0xKIW7%2B48kPWIaIKNIuMhOl%2BRQk50ItLTDo2RrWcaIkqLCnVyQQ5wv%2FNeBa1r5k%2B%2FVH6VdKrfZ8ktdjIbHAptNZBM63CT%2BS6UrQkYxJKVHg0YiWV7Nid2%2FUtukI0RbzfTEbB6DAB4bjPj2TdDIQ3GFVul0N5woo2k5bRgbeWf4D0klsRWfdzZkeFa1s3%2FyJn7aenlSTD0w4HLBjqkAWTrSjbYya%2B8MkmA2KJMvksw9Zgwt3WuFfaTc5asMQ8ihaiPJJ4whCfj9myK%2FGFVDT1zeGpENbDCy3SU5U9WQa0F25vMzYGRTptn7V%2BdWdAvULNPePTE593Y5kizhLO0GgNOuz1TW9dtQhMEqQMG0eq32m3%2BQLTkasgzsf%2BLv1M5COIuDo47VehrUqkyBbDJgfMWiXMf9R8zHuxUbEgS7XQZ4lvY&X-Amz-Signature=254146ba72f7ea7ffc9497f4ddd6b919548def9a97f1dda9eac3e9ddc067dfc3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

