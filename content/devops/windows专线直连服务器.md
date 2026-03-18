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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4KHFANR%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T034420Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQDTqFQJM4Vfsk0n6clPVK1zhMusOv5PFBNnN%2Frk2YmDxAIhAL%2BBJ7k%2Bpl5w1vMUfn%2BchI5bwyZ27BgzhcB4IR9WV8aZKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwYO8X6MbT1YsnHCtEq3ANISuKRGk6m5p%2F6s7xmXKQ5eweSWMQV8zsDsbLw9bhMOEjdliN7Ygoo1upn2PKRElsECtOEwYwXt0l%2FBWdJgHuJitRy8ZTQv3HA3JtAZBmUdmn9Iaixp5%2FdAtl0%2BVdE%2FZLBdpOOzvXCMbjBK1E%2B%2FL5UCYPpXqAUrnXTJb9tjm5YIZNQZ7XO9Vzh9eCmZ6k8DnK6RmEWsr9M7%2BkbqJZlSiYXBRNE%2BqXo8hCtH%2F7Nu%2BuwjAHq%2FGPp8DwuZt%2Fshnutew%2F4YzvX70CmYHlhGqO1u%2BXdAHdVEEC156y3SvNQ78jyY%2BMzeP%2BfS8i6wIXx1HC%2BIID0JpU%2BVmiMdP3sS2JkRUBnbUyGUpVBR0Se%2FTMAVu3%2BRi4KZIfBqC3MRZPmdUY8vfcTWrqNTw7xrNpUTaChW4n4pKKqTmce0vD%2F7R9PoeGWq4%2FPu2099DwnOOC1sXI7pH1aVQDGESP8rkHV3swSpK3HgVE5oQZW9jxlzJx%2BtNaHpZyHW47OP35A9jFUNAYjI64inaQg1GbpGdn4wVsANhB%2F7ZmoAqc3RRnFUDaP%2BIxJ06mheOaefF6of293IWMO9txgHYav3MMe5CP1J2QwmCUn8vsQzDQq8AFe0734P5X3C0d8G3C1gBE7EyvCIDCwpejNBjqkASAwJxjjQme5vNO%2F8t%2F4v6GzP5fxXUGvhPi8nL0rZmrA8tMhyeW8ydHqXXHKvHUb80c%2F4khzGJGVQzC4ON9VLbqS3sAUXS4tkWBq3yr110JoogtivdTKVMuzyt0wxIY72pZnqjvRF9MPivc5ylHziWJlS6y38xFAqoNTG4SjL9FQf60%2FKBO%2BaHDndXg4HRGgosrClbxKzsr5f9Dl1XcYDaPHViP7&X-Amz-Signature=2b5850e093cf18db5789321ba833e18e222eac13231ea70a62deb565dcc9e67c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

