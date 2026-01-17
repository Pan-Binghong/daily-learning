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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD2VMNB4%2F20260117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260117T025355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHeoIALkm3gM80gTRjOkkL1OF1GLS3KVsJ5koOWstuRtAiAYXlxfDV7i2troBh%2FgaLuJi1%2Bta1jt8YK%2FGvorselzeCr%2FAwhbEAAaDDYzNzQyMzE4MzgwNSIMhId%2BWYMjnJ7qF9GpKtwDorFkQxNlnn7V%2F8MEgbcMsRwx9pylAKuCQfalwfSLa4Nqgug22a61kwLDT%2BQ41lCxCvRx4iXn1HXEBkNye%2Fb%2FJvWjbzUbDd9%2BeaKJB9k3RLaN7%2BchUI2Fid43huyT8rhTazAs%2FtPKO6ZT3D%2B3yQ%2FFSdQA9x4lA8g4xCiwe%2BIFNExR5%2BXZ8EspPj5IbR8SvluwAGOpPkmXe%2F4X1sFFUP%2FoBdYCyQPnYtdCPyajqGHD4bXTKS5YAQmm6k3%2BPvoxvuK7mN6tpJrqpr86dmmdphknXzPfSDgs0P3Q5jiHtfyQJpmXFHa1JZiLZZ461gQKhgIIs9epJhxiegcPHQJf15%2BsZpJVL9LNh7N%2BGus1%2BQuuZrq2cTbeMKlFgc%2FpXLu1tLjy%2Bc%2BqNbJeTn09zb%2FTieOV%2B4u2YbIbEzhIpgs39ly5NxIU7jPcVjUbi8KgzNb62yteDcvBvFIdTA35%2BiSpwsygRPtkfX4u0qHstJaVHe1VEU1jjGNHvUIcM7p9SmNk7PikvIxBeTUvSeSUr8B70L7gnhND0MmQ6Xi%2FTESNjOYdvnD%2BwPBFENeQ7S%2FZ4FiI%2FWkkrPp6bXbFeid%2BI1yfjJKl7cC37TVymRTvE%2FnBrE8PKBTp6bvYD3eWVAcPevkwjNKrywY6pgGWk9CqU4WLGNT785qW4GF19UmF9hdBLylP0RJeZiPvM7DniAiy%2FUxwcvLXaB%2FU3yn%2F0xVIc8pclKJrJzXLyDgTvvg%2Bd4NZbY6yNKcqf0b09ipr%2F3jc4nrBfSjLLbetynRTLFG%2B2Nn3c8qAjomEnpCvcvKDYv8grfRYtD4G0lLmlOC016IrCP%2FjDU8JVxc8nUoUQjc%2B4vxoE%2FkmTWrBahy1vTc%2BYW5E&X-Amz-Signature=d5702d7b9d1c7c28aa080f2de3d6caa299fa4fd99f3b7c975853b822484f4897&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

