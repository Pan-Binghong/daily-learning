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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC75LHKN%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T034933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDrNWvSX9BRjgOP3nf1j34%2BbXv4CRuD1JoNT732m79fhwIgWqyGbz5wRk0OAQ65H8B1FQ%2BK40wXm0I%2Fcy%2FF0x%2FV3v4q%2FwMIfBAAGgw2Mzc0MjMxODM4MDUiDM7rg%2BCGCq9jv%2B8nUircAyjLHOsTrpHe6V%2BjtmUE8Av1n1ggbS8ptI9posLrXoim4AVBePaJZazkX%2FgnCyrOsejo8e%2FMBrT9QpbOf6TcY%2BOxX%2FjC61iNT5xRDRzGIfSZ6G%2FseuysM%2FNi6UJ4DNr5TPtTibP9pJWpNws%2FLiuABAgPOtxbnRQdQ6kvKkRUZ6knWq45%2BjYP%2FwW4l8%2BLo%2BpDMX48Y624RT6IjKSSBZRVfGv3rXoLvF%2BoFR8UQRsWUedQOyZyXv%2BCV2qUqJtDFNqtss4LrsSSEiLn%2Bo5eA%2FV7W9LAzfRb29barmuCjnT%2B4LAPwYJr4cTdoxABUHi%2FNGvx1IYy%2FzsW5MNmTA0Uumz4qsCN%2BepKVYQQbQEwz%2BatO4XTUl4sAdVl3g1adPdYT8IUwFhewuM1KLuoswTuGwLrsudNM8k1yA4YJUoQibGXFcW%2B2Ji%2B2WtyAAubFkotvRRykr8HKP%2FgobxHaU8qgpMtdu31CR8nGH1dk1w4TPKgPEhE5sC0FpRxyehtGl5NhAbqc%2BDOy6yju%2B1toqSPPTQ7MmPDGqK140%2F764CGZNhiu4nJkqopcnk%2F200ByTdumncrWaOsIdTH645qHvC5v33Ci6HmqeHiDiVhNsc%2B5tuMEkJnZlQ8OJQe9%2BLim82jMJvivM4GOqUBXup7dyWL3jgAgMEkemjnab4dQCUHdStUB5gbgtyyHluv1H2iRmPOWwmEVCct4WIvaMbpwrf%2F0nzkqLFeFtlL%2Bcx8CxFp7oqgYaGC12FkFV%2BynSCP8JpSMVQT92xVuquUXXicah7xwzSBoLIaTcFgC0HA6Z84FUMZFqsYTZ8Q6IcKIH19sAaHAtNWFlIHPEHUr%2BgfOEmRoeYb6fker6oHHLV02SXv&X-Amz-Signature=dc7ac5294640dd4316950ff5e378a5229ec2bb0a8e0427af2d20ddbbadfa8b2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

