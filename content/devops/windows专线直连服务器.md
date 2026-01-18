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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WV77AOO%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T030907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDzTB0bVLQcNfEUswCs85c9sc96K%2FVQdUBOX7bG0PzDhAiB5kOUHMccGdhXxJYwiTSr8wKxAh9ksk5Ybzy%2BgilUd0ir%2FAwhzEAAaDDYzNzQyMzE4MzgwNSIM9%2B1%2F6TwOL400W4TfKtwDcPXI7vS05QCs4nn05w7Hz4Kt4ZmQHXyTj08jfiR30c4503d8zAHa4ikccoUHSnkxeDf2VcAhhS5NBel3AtcN6YozZiX0vtGbQsSEsG1WqVW5Xz5OJxqr0qrcCvNPfEySMKge3RfopEDLbnOzl4mt7WlDe3b2exK2mWX4bHk6NXurRe7r4EJ2jokvG4dvp18A%2Br8kq1nwPYVT3eaGg6gg4Y3vdlnbsXYFtdr0NUVjpBSHPGxqR3TdRv6WS6qWD90zTFbhLwWzghZa5LQ8YxIRgQgOhxSdRXpmmxCZ5xDwVzDXtLLiAndJ1fxU1UPBl6JEVLShWQg86hpOB9pHclWAey%2FBMNqpSKr5RYPbMDRWSb8e2XsHK0SCqqmKyn1MSbUTNmp5MnMcUirddTCdqBO31yF3nQJYjWOTnDQcmpCuUgiK2WqNLwdPvPYtS%2FjXLPABDPcXvVy3nWbcvKQ3SYqJysPqbVHcgAydTo6uF9giBVFl20PO%2B45iYLIkNTr6MvkMcuJ7VVbIdpC6bO1G%2Fli%2FCNa7Yry6XJrFB5gulwcLeTmPHoFiSThElNKz7yqNGUuK0V3kJ9QSVx0ZqLDHxQxpEy6EZ0z0QpASRPvGEjGLAkf8ypBDb5sHCxj4ikowyoGxywY6pgGzjaAAYR%2BgU6yh1Uo8SkT35DmxTgIZGKs09lQ0fMQ2iftPFtF37bvEZBMur6tETDPsRvu5DPzSAd%2Fv3LtzDtAGk1T08Oj%2Bd%2FEHooG12pqAHYbtzWmgNHoZuLdAFYe3OZZKYTQyhXuGXCbKO%2BRt7CyKPfNruoPZR7b0oUdzbphoB0R5tflj%2FsPjlfBy6sTPv4LotWesO0P915n4lQ%2BPb0WdfYxN0nB5&X-Amz-Signature=50edebad5c4dd76f64e250fb00f9a622ae9fc9882c5e5b06488b1f038e31a5ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

