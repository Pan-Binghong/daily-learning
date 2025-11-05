---
title: Windows专线直连服务器
date: '2025-03-14T08:07:00.000Z'
lastmod: '2025-03-14T08:36:00.000Z'
draft: false
标签:
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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664SFP7C7C%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100820Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFY%2FuH8bl%2FVjHbJhErZqCEqNfwVTVJM%2Bei1kZHShYYPoAiEA%2FsIcALG8vPrbn17ft7ATJITAr8JmSIiIwDKlXKLo1jwqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNuuUfCD1gTi8i1bQSrcA2OBbZJI6GKxxgixHhavG7XZK3G9x6DGICH3o21fAylFw9f8tCW1Cbl6bwjdwCALE3idOSAN7ACnjAfg5oz9aeEzHs4lZmElmsgSd4ly9YFvmx5AeCW1GdnLVIKZm1fnlgBnIaeQtfxu77gkSr2zV0JDIa5FbeNk%2F5jj27JRotndZcehst0Ub2loYf68mTcXS8rwKZbB3OGOlsYkurYvdN2ZtWoBG0Q27tDXgGFEetQGahCNmL2nY39RkvdY8hi5re72c2O2SSf5NtCrjXCGkqMmRJYg2JbZYavfn20TYwCo9mOOc6LO4WNoxsYii%2BScp7vTMhB46mI6QiNxPf1Eu3QVHAbD1ljtSEvPthsTOYx%2BECAljOrkCLuF1PIaIRl2hpP684UfyXmKy1pysgOfbuGy1Y5RYjPvuxGydZm%2BlFna7cDAxOr0MIkLmdfc86lT7uV0halXsYbRwSZTX8vP5xzL1C6OE9wvYEe3LHO7l4rnz78xCILDNGu1WHRVu0PcvKYBhqEDKseLoATHjpojePRtWvFnkrUAgKYhxHYkM48kejCFQCnlIfC27lVkBksRYJkqizu8ykjgpUFh%2BWHsMNzkhKlLINyoso23bgqYSwdYmVy5u6iKmdjg7xENMLmirMgGOqUBuTkjUm6dXsxUOaSoJP5pl4fwYsMVFzAQEKuTtJghK06K3qcNcIcIAWx4LuItId090ElctW4%2Fcu1tb4AxiCxELC7rBhVh3KY67F7iLn1Cs2SeODyrebPvD2OZisIa4y2H0Y%2BQFEuTnTAzPikhzxP4223QDD4cx2KSH%2Fs8b3qx4ymsl302K0SSO2%2FSqIg4d8X5xVkz%2FKHvcTqXR3wtWnvaJypRhiD4&X-Amz-Signature=1f2957c90ec8587f22eddbb83b380bac23736a95cace4b8596b5a09a1d35cf4e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

