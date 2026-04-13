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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QATWPKQF%2F20260413%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260413T042309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5C2kynAEugZS5UybEIhpei2X3mhC%2F2VpctwX9db4v6wIhAKdHx7D6jzdVv4IDqTaqmZD1cKOL8DxSgJbiGuIEp3mPKv8DCGwQABoMNjM3NDIzMTgzODA1IgzNZ69hmC6TknYfJmQq3AMj6r7%2FWBzQ5i5YXB44JZW5YaIhL47%2FGXrNTlcCpYJGgriJe0ktfPMly1TTezHByHff4%2F%2Fa0u0cEbn7ld10w%2FA1divRz2MF2%2BtcTuFIus3s4DRdMz1u%2Bvy%2Fl7uSZBZ2pd2VVMAigoNCUMW9ufCYz%2BrOMh7AmhuE69f%2FIlecoDVXQus7jUMCEdEWx4ZNdroS0efaRGEdb6zmXzPr5Wd3%2Fz3sLGPONJl7VvaXbe%2FUcO3sILYNDoe8nPN%2FvFP5Izd%2FdjA6j2hX7KAG350TXKW26YUSNrTak%2BGZYb59sP0PjSaYOEP9bChTc%2BMdZEqLOXFWU1sTk%2BltKF3uj6LnD3V9IN%2BfNPHrXQgIb%2BDQXXB1%2BMvnRPdXttP%2FiciT7fecdMC1j8Azl5YLjPwq2BtUQ4Z%2B3zg9QMQoD3P3q42AVVCYRLEoq4gSvSWmiiVlrVkm%2FvLR8yZBXj7beCdeuzjolRm8X%2FCAuPUmFulzdahgBCbkWjMZB2NZGRwDf%2BTeaLsqwM1GjvxpIYIXMlUDFNHfKA8Yfl7JVXXndYCE4gomTWMPksWCRQ7mEehzN6x53Bwi4SwGu%2FsVC%2BtM8b1zl2aP3N84vLLhrKpDdFLQ1xHw7yvqmcHRYrMRL%2BKFDVXVNFjXLDCysvHOBjqkAeFhipFy1oqjL8gwqrUBRDzYzfFEub9YOQ%2BMgaN%2BTKnGx7NSyj7BkUbU%2F56teFX8IDhkQQMwjsZBX6fFXC8%2FmzhqTOBUY4yceMyPzwZfTJdfym%2Btko8sCO%2BtUPQ3tsaEFJ3%2FAzLxDn9gpbzJ4VhqPG0S1GM1MEywkjXa1rqPTNgFpHrfrAwfVVNW6hBwRE99Acn%2B%2Bjk%2B77HiT0aolrwrRu9Oldy9&X-Amz-Signature=60b3e2c4bad9aabeb7ed027c1ae464eced83cc8acd02c12ce6cfcf3ea40ccf3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

