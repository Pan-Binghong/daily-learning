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
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/863c402f-4ab1-45e1-a148-3d37932cc3bf/9c5d35113aa3fbe01deeff992970e27.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSMYCF3L%2F20251116%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251116T025038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBx77ndpt%2BFVlBNkqhUR9GTJ0k8l26nA%2FHA74u%2F2WlZSAiBCNH4vwm5nZ%2B21hb1J4u4sSMv5jMMKzf6HPXc%2BE48TgiqIBAiL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZkrUidLpUc4UmwqOKtwDZXEnc7bcWEBAWARKzeF0XaV5oR7RJmt0CYGLLcsIRhZmi63ky3B7yGezHHItGxuF0YsPEHAfBRbuON19FmYaHfDtkwe5WjTOMEw%2Fo1RJD1lwxuebFBvRzzyvq%2BOvORPasg0pX6Qj1RS%2BivG72cOQJBEm5t5OO7fLKn0dRTULN8bXgR4%2BgnJWsWmJtb0Xf1q6QsyIi7ep7VLlX0R2H6Hr0pUT%2F4Ms2TkUw6u2TNil%2FHmtFv80A%2FbCrckOa%2BmKJWfOmT9vwj0bpjx8OR5lI7flrpacNYTYYLVM7U%2FTyQnXea8U4pJmVHJzyqVc%2BI68tmBCIiDlitcskzNI7PTEftDbyNYr%2FNCMaikevkoYr2Xa%2FDbDFyFWH57tPA89Hj9Ny06hhxvH6eRJSKuaBXQ%2FJf4rdwo2wtGN07e%2FtQgGeljKS338OdKmLrNYtP9KTRmnSMD6%2B6DTPrI1mGYfu5ju6zy%2BIdwVULAzfY%2F2WefYFf9R1Fe%2FVCmXNwYukZ9wlPnXpsgSO%2FSLs38w3M7B7LskwsAFXyHp0OEo2HYd36vXxLkCWsufk5CN%2B02T4iWX3o8wg5ZrOrzIeq0L20%2BddhWjeckzreEwu%2BmkwuFI577c2PJpYdmvHhufPhKUBIPyI8gw0N%2FkyAY6pgHfdEj2f0cXRta3sAvtoNUi2%2BqmhAwLYbrliCDlkmWLFqva6UAXJRNhU0%2FcfXlh96wixuu%2BofsOWr7becbpOVkskyphlSZ5iz%2BUQ%2F%2F4QuYeUpwtBpbag3eEcUQzH2hVRME4qm0SvGI5igADB1emohBFmc2rv17reegaQ0V0CnqjDduwUmnJMxIGGoljKjm2ZkCWV9W2O%2FFeaCekoCAT%2FuWdMLqTSlIu&X-Amz-Signature=95a3cace20d6cdaff5b05ea74790e2f9af16be0234163c0ba8813b454d1f9921&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

