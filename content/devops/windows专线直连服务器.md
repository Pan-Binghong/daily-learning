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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4GNBA2C%2F20260202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260202T034431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIAYgQiPV9JRwX5UcKQ38PuSROFtpVWpuf5zHdFBum71JAiEAzeq66y19WzaMiBk9CxTK9aG%2Fvjs7o3risrNDr%2BrrRZUqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCcU3HgilM%2BmkVgG7SrcAwR4Mqid4da1yspqngJhwzqr69Ee22kirqpKWsU7HVAscp5hHh8DlsOLhklF%2Bq1etzeyKxMuJor7jcdxeGc3ad7wbAJ4uBPWh9nO4GfvSpA%2Bw1kdNhUQ8hkVctkG9cE%2FDRjWYRZMQuc4VjsjbLzXNWWMJ5NoT3WR8ONkaVubv22tYtpMkTNTGtsztmkTNQCVDe6iRUIVIOzZ3Hf8P4Xu%2BJGG4AQ%2FgwtD0hpxe2LPoObU3l492Y03148P1yYx9zjcy5zGRFIgJxB32eclY0hNi3e9sujH97o1Dl4hDR%2BqlwllFGlWpuuToCafgSHdvIc9oQB8mjD4vuZn1mtTE2aaquWGAqgW8OUgAeLls%2B7mWOJ1zCquZUQmyl0MxkCLpVnmBz2dUSLRbY2stXcj8mM2JmEq7rHRk4f5zs9nKlfY10nFmSQ5hL2b7Zz9CyzGFIfskeQCixU48eoPCx0IXDDz%2FXsYbeHi33PoyKeF2vlJl9PQJ73iBdOaCqawhIAgIpTzkMYdMeRvzYkMiqHdFEv5SFZqn91A16i%2B6vaHDa8ts5Q75KqsPFqWMsVt0rgfH2DXm9WlIpxUrmUqfXH18wK0cEG1VaGn07YaRyiDDJbdLMRMXlDetqtR1Xb9cHJyMJiIgMwGOqUBJvwjq9eAS1fzTqAnxulp4ZikiUyi7WBLxuhkRZm2%2FaBlzzr%2B%2FO1SVeiYkKtaMoxN2OK%2BFC8IsA7shuBC3TM1kenRmSnxofYANBb3Wd0aOFhHvT1A5rSvXOXb%2Fm%2BNoYx%2BeD9SDjMDjPk7Y1LAls4Bdq8Cx7yGefY8Vc6QpF0%2FpDwuFGYNHw3hf7q9vyn%2FS826SqfnLL%2FiICDmKMyK1ZIHpShlhosV&X-Amz-Signature=30e859ed985f4a6f9f3c20a6cef3b6f17e96b421c2e69f953a8f4dd9095c5008&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

