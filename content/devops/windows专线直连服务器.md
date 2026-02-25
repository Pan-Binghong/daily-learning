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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZ2WD6WH%2F20260225%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260225T033954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIAe1yoGLqLS2N13coUv%2FjQEhoRB93cOjxc9uP7Kdp%2FzCAiEAq8%2Bdayf9iISNu3FyCxAopy2GXLqUqF1Ytb%2B3UNi%2FXjoq%2FwMIAhAAGgw2Mzc0MjMxODM4MDUiDCOTESNwR%2BCKaEa9oyrcA903%2BGjz4P1jnactuBeJgreab275Ph%2FC5yGbCnxAXG4204iCtaVWzY43rmRykv%2FQX6YZ%2BH%2FA%2Fiko%2Fj6MdlL%2Bse4ki%2FPLcNjb7Gwt4OdnuiyeUITPVxepDDmTv9vfT3hzoEuU5F4rn8NxdtOc0l6NB9%2F1%2Bh1gELX%2Bg8Ii7q4mwdR7IereZs6q4t%2BUVD4fhoiyiMncFCoDDVR5%2BJKVkz7tWndFVuEtzw7PHSEq%2BhUMtPn2zb7bRSFdlszwzVVCVIOInDuuIoqRsErWc6%2FFuus6tTaDyH6BMC6%2BaOyn3011pOA%2B43q6Kzfy6mGMiErGW8qr9V9txG5mg68MuZUPUnGGtII9Hb3aBSYCouFD9RZ437uxoFGq5y5IaHwd%2FZEncSIyW2od3kOEmnCdb3m4rhZMIaSVO41TbdAGvWnmmvZmeRqRmbWYWZv1LSXuJx%2FcCafYxeVQF5dPjZ5azoJwo%2BgcvXnJuSzW%2FMRO8x%2BsdmR0M6529YBEiK74wxREAI4%2BMWOmUQ%2BqPXTLiSmuZJoFpbxhFmGO7ik%2FkJMXXTlrA07%2FPyrc0nn4h8BAl93A0kr%2F2nDKZoKNS1ewP2ghTt6GmGrqEKVuB17yWht%2FHzHsuEuIfJgobh51vfU%2B8T%2BmGUbdMNyD%2BcwGOqUBqore1S%2Fe%2BfQBtjhT80JLMv6TuWFAxUsisNJxtQIndw0FlD1Ynx8TkvAM1uoOhRd4vkk6ed%2FN3EkNyeG5XOi6bon0pLU8xnrIvFXIRTa8QWHkyVheAy6%2FqqAt%2BpMCRuynpC9lO510reNWJssHk6Hl4hlbaWKw20kS3qk%2F8ilV9hXlalKOwofObwRNUALZZkEvKSG6yYtdOOgJM%2B%2BHcgHfScg7mXw3&X-Amz-Signature=5b6b7c7787f542fb2fe51b7ae9ab011f81ad1f1b29ad9f0be9eec945e7ab409b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

