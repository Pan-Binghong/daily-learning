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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSSYZTAS%2F20251115%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251115T024012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAmrHOB%2BhfoPyefqYAQadI4PZ8328bcJInhJN8BMdVgYAiAtvH7WuacEJjSlYgDBoxE5P8uVdTYo8kYPTp3RjUxLSir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIMZ%2B4Mv6bKjCNdQn3VKtwDsWUbebKEv%2B%2FWXZlmShAu%2Bjjx78zTi%2B8JL2ChIE2L2WC78OarZYs4YHBS0ctwUCuM5RjvAdrrblBwRO%2FQYuP45%2FhblvSed0GSLBPZUZMPCd0K4N5bahzK%2BUsktu1RuFOhTA5spt087wS4wlBdHuiaDYJgpvN4a4u%2B61V6Mi0ogzi4fd4FCnrNTgOg80gBZNQszF%2Fe3RG2eaXC0GWRTbdlzhZGGUYHs2LhzrVQ%2FI4b7supLXlzeGP3INa%2FpXwe%2FOeAluRHGOu53X%2BHHJZiumRjatv3kfzfsW8Oh3oxnCG5wamfGjyeYl%2BSk5m6iWYKEbh7Qb5qKCJEL5%2B4lbBXrkolq7za519rof7qBLsbXFlesTlAPpWEPexhhDHpRgAxgqQm0v4cmmRz3UDaD2M7IdqLysc25sbj0ivESat0NXDNLsryeCoRRjhKbX4RYYD6FAs9VrmAldtoP5wCD0g%2BRL3CW%2FXQF7Ns0mw8O7ATGlrF%2F4itb5iq8WR6nm9iZNyXpH9QtQkXvwmn9Ttd0G9iwyyKMJ666jbyjzFcpyRjmOXCJFKofR18zT7O86Ynw%2FxFXilSuHBGtff2FYCCscE7Kh0RbkG9oBQyj5WJtygUlE%2ByYr6yva%2FFTsu4Pz1EcpEwpsDfyAY6pgHQgE60qMk48l5ZSXhzON0CtWh8HmbDlkO74yz7f9VIILUC92rCL1BNbWOcLuUfeNGrUYUR5eqz8hnZUjGwpIXZKRVZSsM0%2BGk4iLu%2FmuuxqdbmSA5okwmkuTgygB%2BZikBu%2FqcuZAg3fJ2AYVPoHIMUl049BByD4kDPEboU%2FFJAHz0KraNIZHb5kAX34fwmWdvNhnZIGxu%2B3Q5d9OESZNBYxYPcQyEB&X-Amz-Signature=ebac89275bb5935032d7229975ee4efba1a4a3bcf6e3a907b60b4b92d32c4da3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

