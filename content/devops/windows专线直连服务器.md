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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVIQYBFI%2F20260401%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260401T041532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BPdZHhQzQMhDPFoHETS%2FdmPhwwQIRpQVRbukcrhgNDQIhAJHxW5DGBX6QX76tbE%2BbKd5ZplgcrTWK2t9qidLczaBsKv8DCE0QABoMNjM3NDIzMTgzODA1IgxxBG9tdt19D7%2Fy3GAq3AOGxtvtx5d4KcHokbeElvR2Yvh38EhhM8%2F4rtyrEbTLqRMJ1yOkaYwZjXmA%2BcPbkMERd663XcS6DfzWNZh47lldc9TQM4HkiUpAiD%2FLG7Y0tsU3J1U6OnTDbfGqHBbT06wUcmMv%2Bh94bfRWO9uOn6TQEAT%2FsThs3eWYQRPQNFRwrICDuHavksekjfN%2FVASas1%2BPdlmQ7lQW2fQiFQ6Mp362EqYWaOvULzTPjZ0hsawnN7FEncSNQk%2FUb05dA0lrab0PyzsXUNgUmd7DXEejpHBFXsEhEQvxqGU5GFhePhBUW36hLlEFhWuoMfbKhgBmqz1Q04o59whrnCfmioJIFtOCBt8b6XL06i%2FYcGMye%2B9ilArJp5e2sSLuOk4Ot18oOBosl6da4qbqJ1Z6%2F9pJi8I3nrKstBjule4dkwNr46pxPAFjFsBWwCkdkSlOZmBvXNv%2BGG1q5%2Fgu70FkSEyN8e%2FtgoGwknDUsrV53WKu8QiUT08LnCpNXPwbPy1rzGUqJ8jaXCulGx%2F8kFYgb4D%2FCoCuys52lFDZX3MDkmPEBUem2xPk7fedEzeMfsYnvylbwD4xM6RbL4VZIzTXbKdk%2F040l4wId8VG6EZEe3tHrIyAB0uO3Qd1n6WHZB6BOTCHobLOBjqkAZjkn5uA2Lr%2BAxQYW%2BqL1WWW2qaeAHSX4sO4YLUWv5Mmxg%2FH%2ByHecW%2B4EkYxHrYjFPKhlZgQ9kOtBvNKTUh9big7s1RSTDIxkxAwRlwOPJl5k7Yv4sQbCbzmtT%2B5%2FBBiSVQS4IaUOObpvc6O9TvWDeuwhI2IyCXisjHLBl%2FsNBkEhJF0JtBvX1dqafxIsPt0G4Ogs%2BePSPVhUDmw22F76urbKovC&X-Amz-Signature=7dd09df5896b65a6b2054c16b6a1d808207370d65d94b3b7e1c19d91519f9340&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

