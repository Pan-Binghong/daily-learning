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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDMAJ5LY%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCh0mlG366d77BSQuMSPwrD5vNrrTMm%2F0lw%2FeY5BG%2F3kgIhANXq5HG21cZPrSiHRthsMO%2B3%2Bu7MWU15GqYnXBwPocu4Kv8DCBwQABoMNjM3NDIzMTgzODA1IgyjdagcoShgg97g1l0q3AOrngOBVyiRwNfmUO79AY615LADKc7FaTm8LG2f2yINvzs%2B%2BDHlDQ%2FUrPSC414PNZ%2FJEdC09VDf3Ob2K%2BrLQo4LT44%2F1SDcYptJQq%2Fi65eugHd9qfPZ8TQe6WyklX1Dsz4y2NxGFbGmgv3cIcq5Fhf9S7gSqdZw1X9JQeJRpYSkHZx9aeWTiwTnDyurvyAXcuxGtv1KSyih%2FQEkk3mwmi6UUiS2Rj5%2BLZ2P%2BHa9s6mOqkgQ6AZcIiM5wQhcAgQq07rna2t7X4Yyn7INRd91lWCFzDnYifVYw1Bc0sChGl63R4zOB5ieC6J6TRm29h9tyMLYaAPWDFqpd0%2FEqf3m4UBk0PXC2bqvGX8Nw49GTOPE6YfwwWz4TrcQZUkZ6ca3sTgVO%2FAHWZCmioE%2Bb3fF42F8zV6TjVrcjVhg6TuSmGEtJG0%2BEFOEOOxJiKzl%2ByjkFFSUsF85ZFxn%2BQEfXtIWJ%2FQqBk3mjNgk1KXWEi0OHfTBQ2Gd2q4txfW9qJp5Dhr3z6iQ%2Bst3NGD1zrrSonDvqKzOfAJzMWAhMoPJ2zpSDHOHG8w1lNKSQQQDrQPmYMVj91a7kQpxvnJGjLvN7EuoDY5CAeKS5%2FpLMNAFXp3MnZuNJJazE6%2Fq1SrqzaySYDDHyKfOBjqkAYguTnFrkgko9kXTNlTunI5iTKBpOAFOQz1v0iRN1ZJ5pXpDMmslwd4N7b0rUq9wU429GHT83bF9g67ha8Ax94YiMneCZWCkwUWbbxtrPoFaLqqPuxi33dEfdLed6QtIbd73rRj8yUP8mEVreN0MC0AmwwEhRJZaX2khP5LdMJBFfp5Y6tXemD3Ft2XBIlY%2BKcVSK1SLb8CIP15k78YMSf3fKWaW&X-Amz-Signature=2a14f0b7235e101cfa6a3f663be3d76ae4ccce1b0977c35a986044e73751b518&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

