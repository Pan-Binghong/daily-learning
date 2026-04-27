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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCD3YPX%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkn%2FSsGI2CBp00Vpf3duSMqW%2Fzsezd0fndf1cBkbu4jAiBENG2sh4Mk2v4gBwj3DU632zCO6TSF8RtD%2BOyuDRkmEyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlq2T%2BHzBxGnUtLSKtwDhrboxKddchdIA8h%2BuCcUSeiK8obfkh%2BZkxta7%2FtM7agHqpdGOlq92ygvy6mZ3D3%2FwMq8klauO4kpiGXFobQCzOb3u6vYbgFNalOFQ0Uh02LZ1BhvWtRHpU%2BVrbv2jjyANJUFjjW2gTaGB3f396TKqbAZhWQrG%2F5elzjJpMtNEPA0m9l37ovX2L01n7WJXtXltEV1LLRJG1wsH1TJRlHPm7AfAHho3ajs4A%2FjyjwHjUViWyv%2F3qcjxM%2FDUVcncp63fUzUF3WNCr2R8hX8VZQSl8PBv0GsaqQhFvgLyDBnHkvc4QMICijfiIRUX%2BaM6BbH4v1UvQLmaOyRCb8PCrMO9Vb2oUFfaOv2crPyGAILpkKaByuYZtCumY1l6TKtFLVb9WwBmQjRK77Lysf3FX2965MacT653JjQ3tK8Ke%2FBrXqnh8lVWnPcTNk0Qb3JCSm6aCgj3hc8BI9VfTWJE9AyCz7NU2ynof0pJoEvwBXvQwuFZ5iPovsssSuMNZ00WNCD8xvYvYvS58WhhJ4qujA66peX8YJw7M%2FXYF8KjtYtzxvXi5EGu6ZT90GJZ%2F%2BACgc%2BBZj6I7klOcC98yjKEargfkhCUXygXXO5RR%2FmJSKo0wx8mwD2aLxlq7%2BTSXIw9bS7zwY6pgGAPJ5qGkLIhJi3xDrWKC9kgwYrOhGtt7hzZnHBjo2OJUM%2Bu6DXGb0G44JpoD6LR4v5nJ0WJOxr8JgOa9ShIvsvc47cB9rU3sTFOeFlrHg3jr0AtM4H%2FhWdXs0HGrqOoEu5cxH7lhavAJ2b9Xul37ZcFMnS5zjXnehB4ucySFqeW22DCaoPuVYbpfSb7jiEJzQMxdQq2kW5QfGbIDy2xAd7xsa21jqe&X-Amz-Signature=f64b4bd40b578a8cb72b4e175b2efbf82fd853f416a119ccedec5865ab5c71e8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCD3YPX%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T043326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAkn%2FSsGI2CBp00Vpf3duSMqW%2Fzsezd0fndf1cBkbu4jAiBENG2sh4Mk2v4gBwj3DU632zCO6TSF8RtD%2BOyuDRkmEyqIBAi9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMYlq2T%2BHzBxGnUtLSKtwDhrboxKddchdIA8h%2BuCcUSeiK8obfkh%2BZkxta7%2FtM7agHqpdGOlq92ygvy6mZ3D3%2FwMq8klauO4kpiGXFobQCzOb3u6vYbgFNalOFQ0Uh02LZ1BhvWtRHpU%2BVrbv2jjyANJUFjjW2gTaGB3f396TKqbAZhWQrG%2F5elzjJpMtNEPA0m9l37ovX2L01n7WJXtXltEV1LLRJG1wsH1TJRlHPm7AfAHho3ajs4A%2FjyjwHjUViWyv%2F3qcjxM%2FDUVcncp63fUzUF3WNCr2R8hX8VZQSl8PBv0GsaqQhFvgLyDBnHkvc4QMICijfiIRUX%2BaM6BbH4v1UvQLmaOyRCb8PCrMO9Vb2oUFfaOv2crPyGAILpkKaByuYZtCumY1l6TKtFLVb9WwBmQjRK77Lysf3FX2965MacT653JjQ3tK8Ke%2FBrXqnh8lVWnPcTNk0Qb3JCSm6aCgj3hc8BI9VfTWJE9AyCz7NU2ynof0pJoEvwBXvQwuFZ5iPovsssSuMNZ00WNCD8xvYvYvS58WhhJ4qujA66peX8YJw7M%2FXYF8KjtYtzxvXi5EGu6ZT90GJZ%2F%2BACgc%2BBZj6I7klOcC98yjKEargfkhCUXygXXO5RR%2FmJSKo0wx8mwD2aLxlq7%2BTSXIw9bS7zwY6pgGAPJ5qGkLIhJi3xDrWKC9kgwYrOhGtt7hzZnHBjo2OJUM%2Bu6DXGb0G44JpoD6LR4v5nJ0WJOxr8JgOa9ShIvsvc47cB9rU3sTFOeFlrHg3jr0AtM4H%2FhWdXs0HGrqOoEu5cxH7lhavAJ2b9Xul37ZcFMnS5zjXnehB4ucySFqeW22DCaoPuVYbpfSb7jiEJzQMxdQq2kW5QfGbIDy2xAd7xsa21jqe&X-Amz-Signature=ac102e137bc9be2f9becdd251c28a89e7f6053826bcac8d42b5c8db089f58c64&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

