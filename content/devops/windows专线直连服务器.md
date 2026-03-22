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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD7NHBAD%2F20260322%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260322T034317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbGTbhgk43HpOwtQ1OcPFKrfEqDJesesYB9fzhniQCTQIhAIScqder%2FLQh1f72lqm%2BbaU2n9Y0WhMIiAs%2Bm4XqHw%2B%2FKv8DCFwQABoMNjM3NDIzMTgzODA1IgxqZJWI1sQ%2B9s7MUVMq3AOtckK5B3fVfTlUmZcRjfO0zMBcrzwDKFtli%2BkyqJSFM6xu%2FvWczKuz0kFWK46hxi9sKTI%2FVwv9tcnrlRqixbQ8ib0buwQjDahEyj9yCZuNJMrCO%2F5itC2anzWAI6zFXdHgUj%2FdibhkMShRbw5M7qbagRd1B7GH2t1q5khNS%2BiqOiwO5UURQdNpcIVGG2a%2F%2BJt%2FyQRwPXwXy2u%2FUF7U7PYQnj28xk1Zj%2FnNb%2BdbQrlVIPqboEaK624vDdM9EMJUY1VvPgjsy0QctUTQCTRjlXABBL5qcz8%2BREm7%2Fe38t%2F72Yo9nc51hEh5goBQDuibymS9f%2BR0s%2BAlpCQvBdQ3i%2FNoEO907D20Z0a8kTrZp%2BrTqI25RsWwt6%2By4iSFWFhkixgnlnTHRk0ma97%2BFZ%2FT6SSYjNPKiX3b62G8PqStjX3JQQhHlKKaWb5altoSvYIURSLjwxpHw71xzKyNhXPxvPag2bp1laBP0ZmnX%2FjFOlN3PN6VC6vBySO01rDwROYgRF1Ode2%2B9r49qaYLXLAHRryzsUSwWdu93zB7Kld9NKK4kW%2BPwDVPJgp7E8eDUYz5ITnx5KByt5EbZ6w8QykX2cuS02CQCuHiuPwVXcb%2B4Kg%2Fs4NmRayBBBWCFKdnsojCHrf3NBjqkAfDbD4T6lnUcttsoVIowKtL4LUy6PQdceVKqWvbL7AOZTFUy2InWXexeei9lY0BQTJ9hWQzXbnUa3QiF1jm%2FBHya4WoUmJ7Cpjtd1AKVd67UJmePQOxofwfNZUS2MB2IKl8w%2FmsCxvHpbFUKkDm7OzBYvPIvYz3lk9SFfSix35LaYqgzCqW1OTF5czFePwEyVvQLkLCKy7%2FYwrXcFm70i4x0VJ%2Fo&X-Amz-Signature=c34d7739497fc3cd19a0e114c26a9ed3bef6c6320aa489e72ce85682d6b4bdd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

