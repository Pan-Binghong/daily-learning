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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466765X4H5E%2F20260314%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260314T033053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICUqwLRpZXcHG8yq4ThKoLR2SxfabpEBhZBl%2FPXUFpNzAiBLqssaZdznozyK%2BhrTLXLtzn0HnT%2FT3Qe6nt0vG65zLyqIBAib%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRIgn%2Bp081jAJd4uEKtwDxlqE5wTMMphZXr48wY4Md1tgMbnDUqCZbNpTW6wPzMr09eSWrs53nEcac6VoynjkkEGwsmY%2B8HAmIoxNDX2TYD9Amziu1N0tj0wo42bR2yBljLr7tCMPmmxXncQ%2BVAgqIXomexPFfEF76%2FLV17r8Tw0SnWE%2FzMF50Ha87KCjd13GFTTIkW4ikLs9Myq6F9AtMCciCBQKGIue8Io8lqMFd2nr%2FJ5An%2B8fTenJAFNqUmESPOOM%2Bq5KJN2LDMeqZo8sswJpAbzCIuw%2FopG9lYv9nJIanDI%2BelSyS5Afe6CvmbyToykQs8Gm%2FWgCmvtRn6qtauMvFqujSJCqsqm1mzZIZhw3vhqNaoFjfMMVovWv4WbPsmSwGOL5ATkorQySmHpfDSwkngJfR4k%2FySZf%2F9WOSYnzlxYtg1aaLLdTa%2Bg8IXySBufZacFMXz%2FNaLr4Gcr1%2BfRL8SNDLyMjbEXXgY7mI6cXgyW33mMNtK8TcMNR7gyosgTjpngdyvtpqN2%2FnJ2xpZLpaMQTGE8JE1NQ%2FXmNYwGtjfiHW9tJU3L6tooEaGs07RCoHv53u4MNR%2BOh4BCKBsau3S2raDuDBbIAtyDZ2ZAi9wRslCvE2tr%2BHWHbZGGXQl2UzMyDCVrfNwkwsoLTzQY6pgGDRkprhs%2FB2q7fT4w4YUhAwasGxxUDggxYrOJniJ9LYUkdFN3rqV%2BgLytROIpgHVj8K9CVYCos5ssyT1U9nNQnpScNg9Zh7kL%2B%2BXDRZsarvZHmXlCEbvF0Q6JOUiUmn1VKYqNli0vns61TgBqujkj65vvjJSGz3jthCO3wkG3507y%2BYgNI46wfCCcI5UyAw0NLTMSxQRoCau24WFIPX8mGAXtGyGHj&X-Amz-Signature=f3e9b27f87276f03d94594bd5f1e833c0391f848c6369c14d21890fc1faa9f1e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

