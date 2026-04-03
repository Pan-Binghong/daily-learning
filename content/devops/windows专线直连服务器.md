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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QV2AVRUZ%2F20260403%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260403T062758Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCt%2BysFHk61evt7LeIu85QkfwWgC64ThBO3VgkAVWVNlQIhANHxC%2F9d9Pcg2lNcJBxJkgP%2BShwTNX1%2BAlBS8NNNzKqQKv8DCH8QABoMNjM3NDIzMTgzODA1IgzI3G9MGNEYj9ML1ysq3APXZAkXlzxH4T29%2BQyerZ7MvrtZ6aeQxrFKyD5abykuAVbuIlinOX8616Pt%2Bcpj%2BFS8Yo0ZrNKTKViRkxt7CfMtm3kiQxcua6wHHDGatK3E2VAxGELPB5w5zUiBuoQw4y92meR0nmNeLTMa%2FJq9GwI5TJowqooPK2FiEjmhneO%2FrvS1YYFUViOseboFwIbJoY5g7WWdyH7Bu4UHKu7un%2BWT6eGb4anNCm9fbL8VBmhmd93ERxo3MkArz%2Bk14fnoxNOYS%2B7Fd2KTNPDSxsnfj1uV0zZx2n6ZZkYS8if6s9lFg53vEF%2FHXsQx5wsKB%2FhK0AIJgKst09tikWA0FYHgCpO54NRtul95aLwiIvNSyYaeyHKC3sOuJlXha9H%2BbOgqBlKddI07yXUA8kVzghfJtE1nLiSoVgYWic89BaH95xIDQfSiJq6PmYJXCebiTESFr9tsgwahqJEvxkSehThq4i5TgcjsnUnH6dZlHFMhwmhPfQcAqemWyHy7oTJSTGyR4Gj0speaOj6Kzu%2Bv1hAmqJnO6eh%2FeU%2FhppojWGOQtJCCmfUoYdMgWeGDlJk%2BKxBDatRCdY8oxyIw8BImZIrja%2BLSApd9D0NWzXs0BJj%2Fbgv52o5QSbb%2BnfH44uzrDDCVrr3OBjqkAbfnGpxYpSaubjS7quhmqOUAex6AOH1jvb%2FGXnWWMNBqarbjo5yxtD2Sixg9Pk4GvpnyfxKzG53fkDAukSDN6qTB7PxGOFY9N8t3MyOuOe3Iri%2BTBX9JSDcUeZjcMQ%2FrGnW%2Fsw1csQTOKy3Sv57g6Fd1eHemOHujMfS0TLzi7pF3TsmRCajQ5Wuf2eeDgU7NSOlrpH5lir1F6zmFw0HTVnSbaO2r&X-Amz-Signature=0aad76964009468dc8a7fb0b67bb8fd734e5d9a67100a8b5c2daf838325fa46b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

