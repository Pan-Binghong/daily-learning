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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6SZCAPV%2F20260222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260222T033935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDaN0ckfQCSz0ofI3BjlBR0HdxRZYFe5Vq8IqabGPDYjgIhAL2%2B2qglQJEARg8hPX6ilqwzxZU8S6d%2Fjp7ZMfHUcawjKogECL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzkt7%2BgdWaACt%2Fu2MEq3APetEPDcC6HnvG0N1W%2BPvgHRjCr3qqAdifB7WPDmaTwCPwUHr1WhsA1DA14H%2FSNHpmOCo6fzqsU%2B1MOgOFLQXahb9FeBDHZtLl2PqyleF%2B%2BikHWmYdcFj2DH4cdqdxOGUxQpgX3brmFpyAohfSEghzmx75oPva7g4jBctcR5HLOv8clkTMm%2FQN2JBrU6vUbU7e%2BSCF6ovatBENRONAx4fl88BBlAy99hHqKQLe210faSdNpsi79SLL5PpT3wO%2FNS93EjwQTKDsRv5Y8EI8IY4ZxhRR8kK9%2FBHpeLdo94iQuLXuzHeNGEE14FW%2FYolMIxsAq3Kqn3s%2F92A%2BPkzVif6HhjQUikSwPSBPsGd8lK244hrhkR%2BdC7KhBb7RGPKnWz6BzpACBzahk3j0WP%2BcjujAm3caO9rcneZh7fT1CtZwfn7%2BEsYx55dAt4hGJMhyo%2BQTrdkwjm1%2F4kezqy48SGRdJctSplBRdUO74hfPK8QfdtTOk5h2saVVn8ICVVoNTX7LOL7cYjNpRnbdGkHNv3XY4vkVZ5GhCBtXHwylefwV5%2BhHfYSOQd%2BFBku4ePd7xj1BV3FDxKvjKgFn0i97Kk124jtcdBCVzvV2KwxICFGqe16fGfWWIt7FPAJdAYzCA9OnMBjqkAdR4fRO5JH2Q%2Fh2cscjM0VooGoq%2F1PMJzj7RNTCpqf%2FIBOKw8Msf2AldsEs49I2uYbMF3rjx%2FT9UjgSWmkqluamVNFt7OG%2FQexMrHoMrRBnYVyafQeB4SR9ufhEJUogQZXKKG0hCkuv%2BZn88thBJFAM76zVNk%2BHZNSg32iLD%2F9SVl8k1DkgoZuWnnUNqB9Uf0ByZDUl6fTJ7E5cxVZ0%2B2u0w5Pd7&X-Amz-Signature=2b72f228314d67b4e10aadeb571138571fedf81468ef37d58b272f329bdc25b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

