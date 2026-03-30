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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTRUPKVJ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCEsGCtaDLTvUILSFUi7QpY4B84HFt%2F6igVlYa%2FFnXbtwIgNJVm2ivDrB8uwy76APV1SS7InBqbA3dQYMW%2F98Fgu7oq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDOM7MyrkQnWJJyjTnircA32OzIKIrnGuvpyUcz6Of8qmmWLpXOKKNIMZ5jFbj7%2F2xzTp5tu9bMLSLBhRIAVnv6jYbTofkthbIOckVMSQXiSAG17TfYyyLX0KIsjZiajs7RBVJjerX7oeaTBqqwRoBB3RVmyqAH6mUeOLLsi%2BnhJcEC%2FuDroyINyjwgIX2Aucdj30sY5%2BQG7peFxA1XsPhPxhXhbMzxNb%2BKBSsRBwkfXNlJvYWl6NbkbSdw%2FszZf0RTw%2BY8ORZyG6W5fKdgWz%2BexcI3sTksP5iqKzX6qXiGIE5MBtabNbinhbdSBFyym52jLGDqRxBgjOjlxA1FpPCT%2FWp4YBxdW5cllOok%2BD3lOH72PCe%2FeLlTI01rXIwOkMrL6qeB%2BQuAkzLBGIxx944ZEPr%2Bw6XfUrcntxKXPfUHAT%2FEwPwWC8TjeqTzOxdUYlfADmC2ZSwqqydZ8nm2p5Dge21sQ%2FdfkAJ90SZdOmjZPs6VXdPTe7ZeqF%2FMH2vOlAbGeWQVMYqENcLcfbNIY8KIObhXNeJNKURg9qi0Bu2wBveSuX78wtsMBcc5lvCj6%2BAw8DCM4o%2FbWrFYmHQnrt1f1SVRfFX42trVdoPqI3BKkFkOhUogfxQhhWTJY7hakjNU%2FmoUk%2Bo%2B9nExpyMOzHp84GOqUBgN3ZRerZe8s2DldNCHJHuSNWKH2C2ofR9RcyNxJg8H4OapTtOc6nabRY%2F3fhC4Omet1R1Cf0Y2QAImjTTAVQOYp%2FufC2TSyRnw5WkWsA4eaFLYp6fv4ua4Lwjwny4m6OfDKTUjIH2xAn7w9hjQcQnmw91My%2FsU9dThtpud7bqS%2BOJdJcBXgqtSnsdSQGwc1Yoz9VouBD21lfQUP10ME9h3QBvSvv&X-Amz-Signature=1f90cb080defb35e662ccf8bd272fe97f40dad701eb965017a573bb447398171&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTRUPKVJ%2F20260330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260330T041143Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIQCEsGCtaDLTvUILSFUi7QpY4B84HFt%2F6igVlYa%2FFnXbtwIgNJVm2ivDrB8uwy76APV1SS7InBqbA3dQYMW%2F98Fgu7oq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDOM7MyrkQnWJJyjTnircA32OzIKIrnGuvpyUcz6Of8qmmWLpXOKKNIMZ5jFbj7%2F2xzTp5tu9bMLSLBhRIAVnv6jYbTofkthbIOckVMSQXiSAG17TfYyyLX0KIsjZiajs7RBVJjerX7oeaTBqqwRoBB3RVmyqAH6mUeOLLsi%2BnhJcEC%2FuDroyINyjwgIX2Aucdj30sY5%2BQG7peFxA1XsPhPxhXhbMzxNb%2BKBSsRBwkfXNlJvYWl6NbkbSdw%2FszZf0RTw%2BY8ORZyG6W5fKdgWz%2BexcI3sTksP5iqKzX6qXiGIE5MBtabNbinhbdSBFyym52jLGDqRxBgjOjlxA1FpPCT%2FWp4YBxdW5cllOok%2BD3lOH72PCe%2FeLlTI01rXIwOkMrL6qeB%2BQuAkzLBGIxx944ZEPr%2Bw6XfUrcntxKXPfUHAT%2FEwPwWC8TjeqTzOxdUYlfADmC2ZSwqqydZ8nm2p5Dge21sQ%2FdfkAJ90SZdOmjZPs6VXdPTe7ZeqF%2FMH2vOlAbGeWQVMYqENcLcfbNIY8KIObhXNeJNKURg9qi0Bu2wBveSuX78wtsMBcc5lvCj6%2BAw8DCM4o%2FbWrFYmHQnrt1f1SVRfFX42trVdoPqI3BKkFkOhUogfxQhhWTJY7hakjNU%2FmoUk%2Bo%2B9nExpyMOzHp84GOqUBgN3ZRerZe8s2DldNCHJHuSNWKH2C2ofR9RcyNxJg8H4OapTtOc6nabRY%2F3fhC4Omet1R1Cf0Y2QAImjTTAVQOYp%2FufC2TSyRnw5WkWsA4eaFLYp6fv4ua4Lwjwny4m6OfDKTUjIH2xAn7w9hjQcQnmw91My%2FsU9dThtpud7bqS%2BOJdJcBXgqtSnsdSQGwc1Yoz9VouBD21lfQUP10ME9h3QBvSvv&X-Amz-Signature=0a4a21266adccc64e1ff01d8bed36538c8d96b24ba644b81260482da382bcca4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

