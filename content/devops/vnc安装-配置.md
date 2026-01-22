---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
tags:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQWGYOAY%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDEbpU3Nt5%2FazhJ4jhuaSlyjuIeodvCkcKdgUZ7gMI%2BtwIhAKokznbH2IPdirHad%2Bd%2BfXLHSAoMEL2RELLLk8i4frYIKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPV0qdDbr2D7loTAMq3AMV0Cz03HIt7AIWYzKxCBvUVqzx6Jml8PH%2BRA8%2FIu5cFwjOs9RDrriv%2BCbSEYqLuY4HVA%2Bez42BfXsWRFm5UFH6KTlP98sRgXCX%2BCkDm0Btq4J2%2FPq9Syyc4TSgANSfaAmwBndZB603LIe1njkutIQMzCa9LhrxVnQwasBMZxIWpEtiTjFLailBjjMzcv67El4hH17l2qGi15vZIHxpmpDLZwW3EPc%2F%2FXEWv1esi7xZh6s9ucS8IbGJdsLKMR%2FeshoTwULRrsySMwnHqTPXj1dF4t%2FxPj7UEC7RflFAmfWcBPNL3KvOjfhMqQEYSUfyN4VIb7%2FPlH5wQ5UEkWZZMICg8MoDB%2BHcMdeWU8fE1Co%2BIW11FjQdOZojk4i4nE61F8wIrL1hQwKB0hgv%2FcyZWtsgJNAGc30tlXbQXqeUs4SOmFq7XhhPcnIeeZUtJDxmmBRf3%2FC38n4CWqh8T2GWqjL7bN0Z%2FNEMcGs8dzl9oiVFGlkUV0RHqPx%2FtXM%2BEt9YsN8xwVVnXMGyRscKDvSynM3ycNtOeplcjGRdbbbCxyOpF4MdDDZU%2B%2BRxzfx3zxVQ0KcfuxGbpO5Fx9jZBtFXcH0aQAq6nZaEhxfgXaryCZhAmyYZGdTiT1uMqeMN6DCe18XLBjqkAUCuqI2jVuobLOtpuPGGvbK13MfnRO5CUsFzXtjpl3D7nhxsYzZnC%2BVsjp4n%2F4A9Xr7vlYsg0AzRc1KvSe1XkNwGZ9WafPSheZIhX15ebVhnLBmFZ3JRsTo%2F1Y5Ik7NyAsU6nBVtjN1%2Fp0Ekxx9ty5hZwLjvE%2F%2BY2lNQPSAxxpH%2FeAWSUysCtO%2FlnQZnJLZ0vzw%2FBpinrbuMuGjG1NWZMFcFrTK6&X-Amz-Signature=4c1369463d7ce0b3d46cd8906ae322a329ef77d063fc0142bee6144a47ed0996&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQWGYOAY%2F20260122%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260122T030801Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQDEbpU3Nt5%2FazhJ4jhuaSlyjuIeodvCkcKdgUZ7gMI%2BtwIhAKokznbH2IPdirHad%2Bd%2BfXLHSAoMEL2RELLLk8i4frYIKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwPV0qdDbr2D7loTAMq3AMV0Cz03HIt7AIWYzKxCBvUVqzx6Jml8PH%2BRA8%2FIu5cFwjOs9RDrriv%2BCbSEYqLuY4HVA%2Bez42BfXsWRFm5UFH6KTlP98sRgXCX%2BCkDm0Btq4J2%2FPq9Syyc4TSgANSfaAmwBndZB603LIe1njkutIQMzCa9LhrxVnQwasBMZxIWpEtiTjFLailBjjMzcv67El4hH17l2qGi15vZIHxpmpDLZwW3EPc%2F%2FXEWv1esi7xZh6s9ucS8IbGJdsLKMR%2FeshoTwULRrsySMwnHqTPXj1dF4t%2FxPj7UEC7RflFAmfWcBPNL3KvOjfhMqQEYSUfyN4VIb7%2FPlH5wQ5UEkWZZMICg8MoDB%2BHcMdeWU8fE1Co%2BIW11FjQdOZojk4i4nE61F8wIrL1hQwKB0hgv%2FcyZWtsgJNAGc30tlXbQXqeUs4SOmFq7XhhPcnIeeZUtJDxmmBRf3%2FC38n4CWqh8T2GWqjL7bN0Z%2FNEMcGs8dzl9oiVFGlkUV0RHqPx%2FtXM%2BEt9YsN8xwVVnXMGyRscKDvSynM3ycNtOeplcjGRdbbbCxyOpF4MdDDZU%2B%2BRxzfx3zxVQ0KcfuxGbpO5Fx9jZBtFXcH0aQAq6nZaEhxfgXaryCZhAmyYZGdTiT1uMqeMN6DCe18XLBjqkAUCuqI2jVuobLOtpuPGGvbK13MfnRO5CUsFzXtjpl3D7nhxsYzZnC%2BVsjp4n%2F4A9Xr7vlYsg0AzRc1KvSe1XkNwGZ9WafPSheZIhX15ebVhnLBmFZ3JRsTo%2F1Y5Ik7NyAsU6nBVtjN1%2Fp0Ekxx9ty5hZwLjvE%2F%2BY2lNQPSAxxpH%2FeAWSUysCtO%2FlnQZnJLZ0vzw%2FBpinrbuMuGjG1NWZMFcFrTK6&X-Amz-Signature=9ad4ae1642e76296a0c608b662225cc33bc91120d2d7abca0f47277293519e26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

