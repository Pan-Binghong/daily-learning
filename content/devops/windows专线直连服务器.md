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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYQH6LGY%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T071623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJFMEMCH0H5aT%2BR0l6BliKz1qGfR4Hqw5dgdhqD6JChuJHJYywCIB81y%2BOp6jj9w09y%2FQf7w4%2FG%2BjUbkx9CsYpqCpfExmTyKv8DCH8QABoMNjM3NDIzMTgzODA1IgxjMibbwX%2BkIgPegWsq3AOlmqoLkd%2FlobuUbZsEa5Pgkj2AI5oWJLIy%2Bqo0HhaiKnaSH6o72eK%2BGUtofEyOTeghJYgwXUB3w643YlCGIDJgk%2FshPJD95JaDyLC4TQieCCvSVM6gUnvlA7kxTZ%2BGeZDUAeFFoKNpi5%2FxevDqh09LXQDHgPKteJfQj6%2BHqSojU4oTpzYUmwRGmPScFs6Bsj3fmJD6p1TJzWE5OrqCT%2B6dfCBvqz%2Bn8yJQzJOVVXEXMi6xCu5%2BX9HXvHLdzrdIPUd6ZA6R%2BvsWWzIpr92vsfgOlkjEJ%2BKTQ26o%2BasKQGgYEzVBFSv%2F1HSKm4P8v8TmncHS0DTTPRVJ3yy%2FuGDEv17PUL4JVNfpSRAewICyrOJFUW2Ohk9Fz6PMUlNFQ8Q0v354QhCklO3NTE7Nogm%2BgVNKrzoSruseJMwPna%2Fw5rYmTYIPzgsFFCcRb032hUp3jgyajgl5onXo8PgEHTbyPxg0Kz1xD0auJmuFQPUfLCjC0c4KRXPkaqdaOzqCWkmVMxQ5%2BjiD%2Fpw7J2RM1V3vrD8gYyPKrCDmJK%2BDURZvARVNcHzX09Gx%2Fc0j1cU3Tl05uMM9NBE7Ic0i82cOsaVLd%2Bdt20Atg2XbsjD31dnn6G7dqDqBPXrWrT5u8SGESjCUrb3OBjqnATXECmE%2BTDCjt%2B5A4QEg%2FtoRTAMbLT%2BF8GS2XQ2IkOjUPzu1HnAmVEZvudzlCxzPeiLx%2Fr9UJmlIr5a6ADXm0%2FOzsqJ1%2B4kaydWrwXzRAhlJPL4laaWHSkAtreLu2dLu6BeLQpR9yi67ZlnGovJMh8PZ6DR0v%2FYCkY0AvMlRJ8cpT3950E8Hv2mnDczfMMvIW9Psi5Q7QKIQvVRkzi52HwJfDMuhTixv&X-Amz-Signature=b8775a8c79da115e3c058221a21fc9f99be64d85c1b85339261408309c478fd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

