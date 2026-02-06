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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X46QCTHB%2F20260206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260206T033536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIB9h26399KKBqaURJjtGAST07DT4l1DMeRIdDZ2u5sqnAiEAt%2BQiOlSki8avQIqhUyzeN0NzCP9dlMgu8bkazAnovtEq%2FwMIPBAAGgw2Mzc0MjMxODM4MDUiDMdUBus9R9AukW2L4ircAxFQgbAK7o873lI2QPJjnN6SdO7w6SgutS9S%2B4Qda%2BY4nI7cNGyfLyK0UeH1KHU0nR9N9CZhs1XSaItMAixOwsxU6zBQUdJ3JSQ33q0FiPyJqzSCkaqZaDmmQq0q%2Bpw2%2BbAwnLk6LpKHH4fS5y2jIeLQ2K1CFy1MFrRbPLv3hK353EoYSKUTlpBo0kOA84SGq8DKMSvFiaTJYmkm4XsBSoQoxC5ag2CJHR%2FimpWREj1mVc2DbVeQNPx50uvU93ckArPtrwO4sQcKPaiVYvXjG1wm9f2MHQBlSy%2FLjasb5sMeiMIU%2F79qDLh%2FlOGqC7unkZ%2F4uECUoT4F7SwodDYBLlfofOcf1T%2BUS5J8xH5irKvnk%2BCA5NREKXhQm7fzA%2BR8u%2FSmT8JmQ%2BFqwJRuAUFyBegPoakElu5K8%2B3zEt4QTT9qfbDnrIKdCKEAFXzn8icdGlDjj9wPudqxL9HmrNFnwUpPCygnkYVI7dS7mBJ%2FUlqjmJij2PwjKrofRnwlu%2Bqga05jDeoNXsZRgTCR3tHG8hK9fE%2BaGM%2BwbHW07XFelRr8Eb6gj8gHQsY3Gbd%2F6kuJainJA6uO8p0rb%2Bx0qJ0LBc0oTS8GjpqYo9Oe1YPzTAmUGRJmNwzovFN0JWm8MLq7lcwGOqUBQKmIwbSc89BnxrdQPJ8lXbk0GtgGjZYIsllTd0QtxclvROoi6OHy9vQfpwXsVs3TOaId9cPCQrRYNYI1IM6rrggzHzW0Mq84CmmZlcWVRCx4QjG5hVLRx%2FuyTeajuPZV6%2BD3L%2Fow6TbtmNFeJTeQ2zjoj7hAD09SOwiTNkNbjikhIbmQvquhHJaP1FnuCj%2BI1A1%2B9ePp9LNe7qPtC9cfAO9T12za&X-Amz-Signature=3a4dca5d96dddb9c5ceefdacd82fe0a0eea0b489ef890ab49bf5248abe82570d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

