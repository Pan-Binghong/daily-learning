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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEATNBRR%2F20251117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251117T024801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDZLUQuXIHx75YJDSgkXb2IHPDSKB8jfCUy%2Fu5Eu0CMpQIgG5M8RGLC1fAdWMPV%2FkzORgweRPYfN06Qxbo6di7BUYUqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJf9q8n1%2F7UM0kTtbSrcA9bQE73PmqT82983gVCSxAbAMeKsvTPw%2F%2BUNIhUtaT0ziplANjAYeaT9g9j%2BTeqytwZQ7lTUCYG4kFZnFshgRRgWKGxeAZmOW%2FEhFB8LDgr9Y5CHyPP%2BvYEzVuOtfhJGfEVRuggHl3SZG40AWe9rGoIPMiL0ikjQPYEkDc2vxXgDpce5CP%2B5Okg49xP1pU6dIuWE2BBiKoxMSb7gEAGeUdhsADsHCRZ2nIP1AA7efDoxQ0d8%2Bmw97DIOJohd%2BokbHoXa4slji%2BrqBiWFTzaeJsZuVPwiDxG4iDdTFtT1WAKzkOGfzTUvkbvIWgxDnkupt43nMhq84mbE%2F3njQYGXpGTnRTDYbTNlKVcS6OUUjx1NM0Jo8ySHDtSkO1yv1%2BA3PXjxO1xbnarP8VGaRRxIjChGuJwuqCzXc%2FkPOfpSnnJCk2zmChLrO%2BsPkE6jjBLfsdUBzT1Qeii1rT5lhWBaUcvRFohPda8VqdSgqOnNmkGJNf7qtZU947fWvpoyAFssAijrE09oRWr1TCwiD%2BHc%2BfH6WoFxY15c1yOwoPg2sZJHHdP7SHBIDZGDuBNRHnU0ZFq0dSrbvVeLhEuzegGA99xQGMegg%2B0YFD1yhA2IjyhlNa%2BTIfuXO9IF1oDeMPOG6sgGOqUB%2F9FJF8E5q6Fwnhrdu78e5uZeDoBZ%2BQ760I%2BTS4s61i9dIyCYbLWeNY82PwzRXq0R0UG%2FMjBDTr2RAUpHd41TcRoN7N%2FcoR3q750Bmmhh5fRTF2AB0Ayeo3%2FHSMYIkEliLYfavkcr6XwJNXdpGBU8l6iLSOTxrfEo4RvX8ppEmXzYbFXchSvOY2jXBtzOkOz%2FpMIOo8Dn0J7Cuo3h6Ni1VkKeYszr&X-Amz-Signature=5dbc7e308d70b659a9537adc89a103b9f2c56a41f40ec25ee504d117eb194dcc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

