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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WEVVT2%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCqbo834gaXFCR%2FaQ68M4OU7BShGGFCsd7BuErdmSNFngIhAJIycAFQ4Nua3IRsE%2BbuliT%2F2IJ1iJXtc5uQ5ahuAZTkKv8DCBwQABoMNjM3NDIzMTgzODA1IgwP%2FsEzB3HeoBf0NzYq3APrt25TS72OjVx4huWGKArjttDftPduRpobSqZRVJH5F6%2BDtst0DgKNBzV9jLAbUMTEfmwxj6LOIwUuNTOaTrkTnUqOI30YYS2P8v1gds7nu6OViEwQSgXNbPQPIjlPJP4tVdhAVVwi67mE7tCYX2IiP7MkqiDIHSCOhmpWwgRs0nhKNbVEh68Ne4iyQQyRTn6m3io55SJSLCVBIdgr3VEOgYA7C28MfC48Iqh5JZH9m0OQKGR3K3HtuCSwLP86sElwJnq8%2BWxPBUf40cQVoyzFFbN1ZLucda570TDUXAWNMRPszWDox7aorZ4iol2psxa63ef5cLoiMnxm29ClaN%2BVsCy3AjGIMsbFQ6M2S70hewfOTLPlh5ROLefjHhBFxvtrALEuzHo1zH%2BmxZCV6ifZcwUZ9m6GkxHMjyC13CrJeyGOxwTLrpiBhYtK%2FNjLgLpka8KaWiiqPHEkPwSkI6TBvnFP2RktP%2Biw0fS1Xg%2FbDsL7mMpQMCo%2FG9UOSthjGTNwbGRNRc4y7a7VLmO%2F9hyo6%2BkZgcvLksWiHf9StVecr9R44Z6JpliemVnYNSNWuPXbm6YvwNrI5nfz56HKDDxd1zf3VHDoiDnOhUCFQNCYCIyRvuxF71UuhPsYnjCQhdbLBjqkAdnoUrZ4VOst5LjAZyY7Nc9zW7jQ4DjgA%2FZ%2BYLE1oPgDRMEtvyrOoZfIIq4pLjPsjxA6GZlTZinlFi9Q2VqPXGh7NdQSVIk1h8o8dIJp7l9nbG9euwdwMJI8%2F%2Bm19S8SOwd%2Bm3MN6Bs2n%2FiRMTqAL09zMsbsk9nNMJnsQUL7I6%2FvNXA5Qomdi5HPrz7Aj9ygvX0zR9PcPYunDN3eEGrkYBoBM1U0&X-Amz-Signature=a58e8f9a37b35afecf8aa540d10d52aba5f0b10f6b67d13fdee32294d27242a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3WEVVT2%2F20260125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260125T031432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJIMEYCIQCqbo834gaXFCR%2FaQ68M4OU7BShGGFCsd7BuErdmSNFngIhAJIycAFQ4Nua3IRsE%2BbuliT%2F2IJ1iJXtc5uQ5ahuAZTkKv8DCBwQABoMNjM3NDIzMTgzODA1IgwP%2FsEzB3HeoBf0NzYq3APrt25TS72OjVx4huWGKArjttDftPduRpobSqZRVJH5F6%2BDtst0DgKNBzV9jLAbUMTEfmwxj6LOIwUuNTOaTrkTnUqOI30YYS2P8v1gds7nu6OViEwQSgXNbPQPIjlPJP4tVdhAVVwi67mE7tCYX2IiP7MkqiDIHSCOhmpWwgRs0nhKNbVEh68Ne4iyQQyRTn6m3io55SJSLCVBIdgr3VEOgYA7C28MfC48Iqh5JZH9m0OQKGR3K3HtuCSwLP86sElwJnq8%2BWxPBUf40cQVoyzFFbN1ZLucda570TDUXAWNMRPszWDox7aorZ4iol2psxa63ef5cLoiMnxm29ClaN%2BVsCy3AjGIMsbFQ6M2S70hewfOTLPlh5ROLefjHhBFxvtrALEuzHo1zH%2BmxZCV6ifZcwUZ9m6GkxHMjyC13CrJeyGOxwTLrpiBhYtK%2FNjLgLpka8KaWiiqPHEkPwSkI6TBvnFP2RktP%2Biw0fS1Xg%2FbDsL7mMpQMCo%2FG9UOSthjGTNwbGRNRc4y7a7VLmO%2F9hyo6%2BkZgcvLksWiHf9StVecr9R44Z6JpliemVnYNSNWuPXbm6YvwNrI5nfz56HKDDxd1zf3VHDoiDnOhUCFQNCYCIyRvuxF71UuhPsYnjCQhdbLBjqkAdnoUrZ4VOst5LjAZyY7Nc9zW7jQ4DjgA%2FZ%2BYLE1oPgDRMEtvyrOoZfIIq4pLjPsjxA6GZlTZinlFi9Q2VqPXGh7NdQSVIk1h8o8dIJp7l9nbG9euwdwMJI8%2F%2Bm19S8SOwd%2Bm3MN6Bs2n%2FiRMTqAL09zMsbsk9nNMJnsQUL7I6%2FvNXA5Qomdi5HPrz7Aj9ygvX0zR9PcPYunDN3eEGrkYBoBM1U0&X-Amz-Signature=c758ee16a64a426a726a26dda82ae3f551a7813d6f52073f78590d8aa6776fb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

