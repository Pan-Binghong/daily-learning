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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/936e47ea-45b6-4eea-9424-e90d2e6939a1/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6QJMD5N%2F20251208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251208T025215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFDVBQJZcC36cifTFZe8s4OB2DV3p9q5nt1sMA3NjqG2AiEAzRqMgdr%2FLZsU4FwhQ6yCthW6QMy08yp2%2BY%2BvGPMjOiEqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDiMnQ0xYLMOLys0nCrcA2gxCrHkBablAjnDwGU18lrvOcKowHyASnGX0VGVFJ4dNLLonUMmrsKC2ExhNhBseM2oOId6zcuKypSoI%2Fa2c2nEPLedTpYAaApGyE9wJM%2FAwR5cI7O58ITawJg%2BlmWJ%2Fiv6Kjz8oIWNBqAOa2sBhRXhUGcn9BqGJ1AkLx3Q17KYCZkKveGCBv477qUBliFICEG0efUwo9xD2dCxYcW3Z%2BUXPvva9TQRGAgBuosYMwov2gZx%2FXdPzTxFmjwjS%2FmBI8I0kHXcEdJ7ibClpqBqMMBXeZvKsqKFCWztVF6FJ1gPka5jQEqJ%2FuXXHnS4Clk0aH5VjlLxWvK94SfesCC1tBI8Mx4FSuu%2FssA8pajDxOlwMFa%2BcOBYJa%2FisFWA9FPyhznjuTo5xN9DLlEFGu4jEz5T%2FYHsnu4qGkSQ0WRTcYtMM3ejkCavqxGDu%2Bn0nJjsirybmpF04oiY0JfVx%2F4%2FWtByTO8RhL7CUspKhtsODEpqs8NEL34Brv1%2BwWBUnta4a%2Fl8QPbrdTWZKqfVet9sK9ysHJ55Sz1LyV9dARTxV%2FU1%2BR9nlbvb6xR4Yx6d3h1JTsp3iIEXWN9IrnOm6Pb3auuo4OzNC96aXBufcUAXRk9fBzbWxOV6k3bnwuXYMNrv2MkGOqUBvqhzehinjJq53%2BVYaPEtl4WwBM1byfHKS9S2M40e5305adPKBfk9oQs%2F0%2FaxCGzGSLJ0Uo5ylsVTTnCugJav1VNLygjpk%2BMQsfGUmAz0HkIV0TK28dIMlyBYOpMupi7w7qzJoYyLUgr84nXryhDgmKcnyPCzidXRKgGZdN8cpjC3mCypSN5h4MYITHW9rBrdXrL8sVgXkqmfOnMgS7DqHDmgN3qF&X-Amz-Signature=7a657263ebc15c4d8cc52945ed756b444aae5ca9af21bf5d9d9bd9305a80c52a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 2. 重启docker

```javascript
docker compose restart
```

