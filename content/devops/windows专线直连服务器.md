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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466754UQTFB%2F20260409%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260409T035019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEMaCXVzLXdlc3QtMiJIMEYCIQDZV%2FNvbpLP0TH44tXdXI2lHs%2FCEIz9qldWsn%2FSoQy3EAIhAI5xtzyI9A%2FjbGfnzfLf4mZhGW8A50OCrKUEDuBs9aTXKv8DCAwQABoMNjM3NDIzMTgzODA1Igzuuf%2BMXy3iSgltpM8q3AOY1kPb%2BZvvgfYgrJBCyncvQVkwbrb%2F%2Bf1Tn1Q2v%2FSAJ6ldqqJqJyDZ9wuwBH7cIKPILmJoZOlza6l%2FaMcmvLgshG3r4gFsFK04nTwUGQBC%2B6Zq3CmNFs3maAKRI72rBSDh6xeTBNFEE0lm9OFcaX8m8hlt31kF9EobUbTAmtEoPK1b68vZWwO4wclIMrsdY5M%2BPDF6bIGcgI3VmKc3QNaVM6JP2QfN7b3HCWDF3WLgnFk0ynazhBQ8J4bFYgBOYoyQKD3zMPkP5sDh6tH22JL4TeTa89xoslKCGDO0lOR2XUFzlT3cYpIqtKIQeMLs0D772FAyluqEE9muD5WEIPkIDAJ1x5vSjskkoz8I3gL%2BPxuajfFcMm2uKD0Qxc4N3Oyo14tEaLIzvfdOTbW8L6t4jXXCs%2BBUZC6TeNrS2DEOPXae3ORagKydvn%2FODMnYHQ2zJy7L3h0Mj0RdDTQs%2BcyszFTIPiZstyvAWPnj%2FzwjuzXOCxY2O3Sn31SHTYct%2BAzSL7WxfoZBTL43hIOsdUCL7wplxK6le1yBSXsQPjvCrtlnZYGtO5LFSC9hoNqm8HLi3%2FHCo4xl6gArJQvfFEzECvfeoswcwCnbdqQmdkqbreihJtwi37IjP7ZD9DCvtNzOBjqkAaBO1DDEn4Ehb8JtYja%2B%2Fqyt%2FwSCx2krOIHMR1iSnORJIMzP9pnZYCVWkZd627hN9vP4ZiLWZqmfbtc%2BBgSM1fWDcq2UVLksNS99fu66gCegiYm9ZymJlT48T14wiPL6F1gRJmq6J77f6StbRpWHiN1Qs4fdOXmyFkLivmBhL%2BJMkHTRAamNvrv4BTW0bQiH7GV9tobm6pQizo1k8TjnaNYrk8BR&X-Amz-Signature=e769e69617fa79a970bf0e339be7db252fa273a41f8864c95e26335712eb697f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

