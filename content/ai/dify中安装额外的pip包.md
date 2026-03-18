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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAZOLDUE%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJHMEUCIEFMWACbKlv1q4wlDu1ocQ%2BoVBeXUcmDp3QKg5qhlM%2FBAiEArIYEoNYPGtFpHk2MhfJxop9eMl0%2BXE5dObwCDshAzyUqiAQI%2FP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNIRPDGpFTilU02gQircA64ZlfqM1RKOMMbKAun5VPPPRFXeQdeTCz55E1%2FVoEAPBNMdglArwlQmhY8WvGeSkP0sMBldO9RqEg9DmfUgfagMKWKmYbjAn%2FEOyp9rZfXziTlfEljCGYDGZ19kQDIdAFnQKQNqtZf9A%2FZmOV3Fx%2FMl%2FyL4sKxhjeqc2ilMvzwAG0jNCQCS%2FD90aGACw1x3yW3da%2BDtWAiRahdOLWRTTJ8Do2f9g4Q9b7kLPhj%2FmRUfRh2oMZIEbO1UbwisqCxvQ%2Bn1%2BzuWRyMKbCFlTALcScTF7kCUCmOIOMF62Aovu7bqTyuh%2ButOOnnz%2BmvRJQjFigQr2yPH%2BkUpA%2BvE5vQS%2BsmXoiWA4pAqlLhqo2FxqZ6JJ9rIzz9rRzGbiP%2B%2F0zIjSdDqwXDlKCBpSDWgHZXrbhRHqFEVn6uEIO4vk2B9BE6xXjzNxmTRa6QcIc3tOrPgyUkLfrGW0TR1ETpMX69OjDJgn8GOECRG%2BfeCbBhTxcUIe7PGzBawJXtnC9wmCP57jKs0lryI8h03nN6zVCgtPHWWGreN4txNQWx5IfCcB6KgqtRTLzUnMMU7dpzKlrUDmrokwfuVLUkB8OZaY73ihirJb%2BWPATGtDuSvZ0W0Wf6OQER11juVlG5IEJ6YMJ6n6M0GOqUB89nMMAj2aeSCJTnvRbq6d9JJW8zDYdG04%2BXk8giyL60j1MsVc2IZCXT3f4mDFw0bbGplnM%2BVGcC9AwAtGhyEUT%2FH8dzjqo240DcEdOyGs8Nj2SFsxPB5CoruKBUxWdqNZpYRBE2TO4jpevFgqrHo1srn8gRPxda6Q%2B1QdoLQEiFLUIw6Wj8TBLMZgqX7zoxZtpiJ7p5f1UNIcBj7DdxCS3WdjMzW&X-Amz-Signature=eba8e762a11b08b82a63a5a28ce5e5aec81cac35971f977df0a2cabe86f739e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

