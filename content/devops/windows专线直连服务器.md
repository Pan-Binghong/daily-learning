---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
tags:
- Windows
- Linux
categories:
- DevOps
---

> 💡 记录一下如何解决的。

---

## 前置条件

需已知服务器的静态IP和子网掩码，自己配置也行。

---

1. Windows电脑和服务器网线连接
1. 打开网络和共享中心-进入适配器设置
1. 找到对应的网络连接，右键属性，双击internet协议版本4（TCP4/IP)
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHD25H4T%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T033825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJIMEYCIQCECuQb%2FS8e8KmFBp%2FAzNwLyQXWFlfFdIGXi4Sy1dG%2FZgIhANeqn%2Fua5yvtIYXRYvllSa%2FVZ6xMxIDqcOJfD6aCMVw%2BKogECPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzN1wiBYAxQjJZc0SQq3AN9rXperJLpWoogb7z5iI68endXy2f3ueXUzAqMcmLOSuyAheVL6cFRzNpLq%2B668L%2B1EbSNynQrhnQthd0Hs0fV3I3ahrwye7jhPT1chmBRUnOS1bnK8rQF%2BiKMKH2Ma0g6rzSDjPxv1UW2yl3DqGAW76y4prM%2FxwaFq366uL8DJ91qglFwG23SolvyY1TvafiwghAz5T25P3OB5FUQgNpyYK%2Bvr1CSaVof6L13wL07KFrh4Sngf76GGNCg56YtR9fSuPBH%2F7Lc%2B30m%2B%2BHN7MFzelNQLvufg4v36T5wkrbUyBoWrDtNFsPQU7ACFOKMOAUTszVS%2FHveMtW3t19%2F1KHDvZPQvaUzGj%2BbulqHPasso%2F6msQZLeZsRdK5OPYGpQ0%2BggOGogXiXww7B7Q8PtSYOTCXFUA20lGLO1QrCx%2BfrAMpbGXSYFj6X6Y9QC4yaWNxbbuYomZNF2GDFqJhd3m2nNvTIoq2xxQb%2BGpy9EtPM8sTWlugjgyRLm9CKfAPhZmBOgxciUp7qYNYII%2FdtD3b63BBEbxlu3zzeqHF9Qg5vmd6le%2BtqZgHQIS9pBJp3HuRb6nvRRY0m%2Bs1dqLtm31zSVDSUiC%2BzCWzovxt6R8M5TgTdnSxEevBpkFE8tTCg2YXMBjqkAQICOaBoxNJmCCfGy0L2BSAdfWtjElvZ9pNZ4PKdeuDWwdy8y7JpyM9JsCpTi2IOTs0aBnOhuOo33w5pSaHJoS2gVj7MP9fQUpV4pPvnLyvriko5gajIrZyR9dUGM8JavJQc16p%2BwxaUAk35KUp09wdN%2Bhsuij%2BHOGwI3LAOhNeyzjOEb9EHdVmcd1D5Rc5NvMnjRaoohojsg%2BBm47Iw%2BscmAdxw&X-Amz-Signature=3ea7da907cfa572db730f9d69d0f6c4ceb45443bbbb15fad99adf2e9ca6edfbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

