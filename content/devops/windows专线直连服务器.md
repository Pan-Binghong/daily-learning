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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBLDNXTG%2F20260105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260105T031415Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIBK2GKyn4agAeqP5ozYAPwnKGyDn4sPV7d4YwUJaq1yzAiEApp%2FjMD0va%2FhiFoZSLUFcXjo1%2FyeS83ovfnghpyYqRZAq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDP5Jp%2Fl9bg5Hr1H%2BfCrcA1FDJ3H21nV9kB1XGOSHWeBrQTVliw0dSKRB%2Bp%2BrnMY3wQjX%2Blwxlqf3dcxTgCBk9MNf0Z5bLnUkD%2Buzwy2VHzR6JYzLfGEHSqYiPydIaO%2BjCFhRWGcS04F80dXMOamERT8ehgD79eGhHdr5M2A5NDZ92YH9nRkhK7Xbci3dVNnzNghxVWGrhPuGNy9T0bLIylTK7efYN0R63BBI%2FapQeqswhMgSiKt0FpNtzZtFYbPsLexKVy1UMjVQVUD53Z8xyZt9Vq%2BrtvBPhjkvTqqKsen0fEd0tG8H3qIRPCtfTKx1AtVj45jQfKtQxmhZeDVpiaQ6BTvr5UAlfHv77S%2Fl%2BMqeM79RzbdlpTF2dBJ9G89vsgclvyzwnpZ2hToLi5xwdDJ3Qvuhgnft%2Fv%2BCksRhimHnsRiUKZXB4jsnhpW9K2pv7vn%2B7f1h2ag2BzsPQ4uqAjN4HSIMSku2utOlcXDpr90fYttjoxWcOzOrvDRaKYjsV4ujZTVJMuwz0WG2RnK3%2Fakx0u98jxALo1TPPecxgkDxOHgG80ebJcGvdjpb4ylzIVL6yHwBlo2Y0xKI0tTmVKwyqEBaTHeO9IWBIzpMqXYQ%2F9TgjThPMseXJTf4hKPaQNzt9OubpOr8Rk%2BUMKmW7MoGOqUBfi%2FIQgKMkq8NKBsx72LGOVx35ARY91XvSgetABrOn8YaMfBQza4VUiFPcff1eT9DhA8If%2FCjV4BL6KrmHhh7%2BR8yEK8wwjsXtzyTwStdh2uI271AyqaIydYgnHHO3sJAgoYt2IQZlLEPdIrUL5Yqvx%2BdTFjhYQMkfDLQMTC0W0FAGcwzAiMpAD90OYOM9TlzZDAJXj4H2dF15KPxgQV1HSHBKfFX&X-Amz-Signature=509970ee2210338210f5336b6b5de1526fc40d6346fa5081ab24f982f0c793c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

