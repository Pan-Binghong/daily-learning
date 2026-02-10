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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMZWXVRM%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T035315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEL%2BUcbvr%2FlaIxUXbSLwi5vbztprAC9Uo%2FM5jmkYDz%2FgIhAJQmvzMB9TJVMGEO5DiJy7DIog%2BoXYsZaMU%2FSjtrLI%2F9KogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7o2j4AijVRhPZpHsq3ANV78ZwMKWUKIAP4FxEI%2FfERe62ZJDJzc2UJppyLgcbqam1Y9tkIgvrGP7%2FN51p5PpSBqu9SROHsj63WBecnoV8f0XFNpa3zKdp4x8CcA1MB3MnJBJeqvwuTXorqTtdqkPnV3sRbZKv7kC1H7zncY%2BLBXcFGEYhlVlhsS3zxvwWmcwrLIN4AoTCclh344E7k4NTJ4wpUmFAhkui5Vb6GipdLC61JV%2BSTMFOkXpYuGVFNw7uHZzQKP1DQADygnFszIRvFQtXkDxDtBvaFo7eMrB1PoXRJ%2BjMDNrcIl%2Brm9nPinEKN3ORAfaANHGkLYSq0BXZupXZhzdhfxj3WoM%2BwjoGbMfzI%2BRjgMyqHEC5hBnTGbK0WQkGGEGE5CQ0qdiSFxOUgTC5jLoVoDcrAENlmzYEy2IgNlg6fT8EPMZn7gdGzbDETUlvMNXrCBn8oGZ93YfSheobNfY28Th55DpEwjFOvmzvTmh%2BmAKjOjLrWqtKKmUY0Xg8%2F%2Bm0nSmHwOoN4VFVZ%2Bgra%2FqE%2FSiidoE8DJs0ttOO4pap3%2FTmbLIAUZs%2BHAlaNFc7F%2Fr29XM%2F3j2zTEqIXf0oXW4eoHofWaXrBTYWIH4pzm%2FAiKeyugGMgroneftxvFD8%2FMlFDxU31jDPw6rMBjqkAUXYoJlC6mfWnV48cXCh%2Bjf2KVW5m6AtGd6%2B%2FiXKk%2BdKKQWLJ7Dei3V9bJ1fz8DhGbSU%2FWrwTKZwtzQDqwNNMTdbcqFCL4kjShcBS8uKWRVnXagkr%2BMm8MZYbIEaw1GezACxjJGe07YaAGR5K3c3aqmYT9nSdWr0qxtqduOBADJ7qfbqkOMyXGAAc5zbHdTn4To84ySugqpglsgzKR2lnFTRs7zX&X-Amz-Signature=a22c97fb8f3e27409162be39bfc67eec9465cf07eb3bdf18232c2a136aded2e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

