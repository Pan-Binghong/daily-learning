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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7R2NL4W%2F20251120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251120T024422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCf6kahqxe3CO08vWBljyYbzLgDLxmEzAQVMENylP49wwIhAMLBRMfsPcug%2BhjipzFKwz%2BZkj95ndJyokfa6fVRnUsaKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwdwngInUn7Yzm93p8q3APDrwUKi%2B51klHpEHYxOHZoT6qEdtaDx3TUcMegORsDVJOuG%2BUI%2FuUsKNBxdnyeESTdmWRP6%2FvJ9QHEhBw5ErtXzWJIqNNONARaslyjK7q7PgTqX7d2JXYdva6856YkJfNJshITZkUXEcT4tQKxhPrCOd18Cb6LwzYDqDxCPXv0vSHVi29iBhmVAg94IrvLtlPmf5L9bcACtfu8pQvbgqLtYiWnCbUoFqYD%2F6eAbAnXWqpyKiB7lDCcpq4SrerDl6PXSVZFXQDdW27PmN07LDmx%2B%2FHuZzh5twS%2BSovV4bFRlzMhApgRkhz48RbNqE%2BIiH0bgTHPwf27IyyUcd1sUg%2FfQBSv4H4O0uh0nrgNjXjSNxNDsJz7CLNxXNt5piRIsDbXEQnYfCxYohaowp3oft5i0nXUSPwIg5V%2BiJCEY6jg9SARAfKxAYuVHkjBvItAERKQf%2FYhWRh5BVXk8IrFBzIxh1vAhtx7AUc4%2FbrCDwiJsyV6vOFO13%2F0VQ5DUk8RCBZM%2BsdelU3WwLiF5oudvNet6rV6TJTUfQ6iA46Qgkw6J6UBF7pBlLLO5RK44PynfZXuZxGYzF9ooxnSix9RNdJmtDjuh%2BJlO23HeMrwG9%2FA7a5zVr96hEuSF1mrITCA6vnIBjqkAUc5Yu9IUOjM6a6KsALWf9Iyu7NOkgu2POGj67VHmgjbpUhiUu%2B2wkrN8T3STTiT40vCYWfx1SMcAfBH9iA4uoYyXfMSgUiuLYpPGCVsnYvtFte69%2B%2Frp5eBftfITHJb2cbPZ86pHEKRzGUNfZiyMMMVEU511HGRoaR8wpcenaHG4HXhEvQXGKxLF5xqunsAhZHTixPTi5CuqfYar3TjPI4FhIyc&X-Amz-Signature=98e7421d15ea05b0573693868d35bc5ecf439ed622c8dcf986567b80c07b383d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

