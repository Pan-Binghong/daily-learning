---
title: VNC安装 | 配置
date: '2024-11-19T08:34:00.000Z'
lastmod: '2024-11-19T08:46:00.000Z'
draft: false
标签:
- Windows
- Linux
- VNC
categories:
- DevOps
---

> 💡 使用两台 windows 电脑进行远程控制，配置 VNC 的详细教程。

VNC（Virtual Network Computing），为一种使用 RFB 协议的屏幕画面分享及远程操作软件。此软件借由网络，可发送键盘与鼠标的动作及即时的屏幕画面。

VNC 与操作系统无关，因此可跨平台使用，例如可用 Windows 连线到某 Linux 的电脑，反之亦同。甚至在没有安装客户端程序的电脑中，只要有支持 JAVA 的浏览器，也可使用。

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632HCGZNJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGhTYtyXIQywgjagxPu75CitWw2QCAxM6XFyJZmPQQYAiEAvsDqfDlF1xk2sbenDqszUeOmP7p%2BMxMAQcrUTVFUqeYqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbYEK1aedCEHgyy1SrcAyM%2BVVle8v%2Bcv8%2FfI%2Fx4ZC%2Fp87Ff3vLpi05sqcMQH6Exk5tJwDCnAQNi0MJCuiVS5aehXFh06k8RVgLO%2BhIOOHN4Ig6w7b%2FJA6MajvXY6Z5p5onxuPn3KJWuTWckUKY86MvnX7oFsfJBnmhvaC78fUtv3QZMW%2B8wzkAZXvC08I4uGRK0yVVmg9IKXYL2ycsGi1CKckNJcx%2FfymhbI1enrki79UridZmF27qu%2B3RGk5wyNDAn5g27d8L0mI9HH3NOJwwyzSO8VjrMfahb3YXNmisy3a7xcFld5CfgUNqkhfEuYDirp0iG8J1X6JV0Zk4qYI72uATWaJBrK9EiIQlPYYpkQQYOuOlpBTFpS9oftpbGWB6LjG9%2BaE7yAJhNepDjEMnP%2B6fQCocPsmROT00oKgFaaeb7X9xhkroZtBpwUhi7vt7DHdZqK6D3Fvo0NWCKLUoE8zHMz6MndLPLGzZkc0QK%2BiJZLjPfSE8AlK%2F3Rj4foKNJqHJLMEvxCDEvDbKkqYH5C1JUiPZjY2rqp01bbRzNNXMrUpFUlJWner1kE1xh5ooIFI9V1s3o9gD3baQyrSUgA2%2FXb5P%2B4yy2%2BJwpdhHV%2BUALelPKS9oUnFvVMliSPqBc3Bk%2BP9c5TYqvMNiirMgGOqUBPlEaVySsErgaSrcyFZvVZo5jI609jcbpDfqSWxImTQTiJYMxdEDT1szblKfPn%2FxLnS86mIwieRuDpOu6JDPihv8ivtoTW6ZoGwzG0Xtz%2B1tFpoA3LC6lOoE4yQuZ0DgICr1K7DmgCyvkej%2F89%2FyUedZZ4BJBJW1PtYoGewZ1xBqHnkJ61alVazlvxobs9W%2BCPPWjoeR6rNzKD6%2BSNw%2Fc87ZqIyAC&X-Amz-Signature=c5f04886d991b828324bfe08e264b307ec209211bd9f1ae7eda2144445dbdd0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46632HCGZNJ%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T100808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBGhTYtyXIQywgjagxPu75CitWw2QCAxM6XFyJZmPQQYAiEAvsDqfDlF1xk2sbenDqszUeOmP7p%2BMxMAQcrUTVFUqeYqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKbYEK1aedCEHgyy1SrcAyM%2BVVle8v%2Bcv8%2FfI%2Fx4ZC%2Fp87Ff3vLpi05sqcMQH6Exk5tJwDCnAQNi0MJCuiVS5aehXFh06k8RVgLO%2BhIOOHN4Ig6w7b%2FJA6MajvXY6Z5p5onxuPn3KJWuTWckUKY86MvnX7oFsfJBnmhvaC78fUtv3QZMW%2B8wzkAZXvC08I4uGRK0yVVmg9IKXYL2ycsGi1CKckNJcx%2FfymhbI1enrki79UridZmF27qu%2B3RGk5wyNDAn5g27d8L0mI9HH3NOJwwyzSO8VjrMfahb3YXNmisy3a7xcFld5CfgUNqkhfEuYDirp0iG8J1X6JV0Zk4qYI72uATWaJBrK9EiIQlPYYpkQQYOuOlpBTFpS9oftpbGWB6LjG9%2BaE7yAJhNepDjEMnP%2B6fQCocPsmROT00oKgFaaeb7X9xhkroZtBpwUhi7vt7DHdZqK6D3Fvo0NWCKLUoE8zHMz6MndLPLGzZkc0QK%2BiJZLjPfSE8AlK%2F3Rj4foKNJqHJLMEvxCDEvDbKkqYH5C1JUiPZjY2rqp01bbRzNNXMrUpFUlJWner1kE1xh5ooIFI9V1s3o9gD3baQyrSUgA2%2FXb5P%2B4yy2%2BJwpdhHV%2BUALelPKS9oUnFvVMliSPqBc3Bk%2BP9c5TYqvMNiirMgGOqUBPlEaVySsErgaSrcyFZvVZo5jI609jcbpDfqSWxImTQTiJYMxdEDT1szblKfPn%2FxLnS86mIwieRuDpOu6JDPihv8ivtoTW6ZoGwzG0Xtz%2B1tFpoA3LC6lOoE4yQuZ0DgICr1K7DmgCyvkej%2F89%2FyUedZZ4BJBJW1PtYoGewZ1xBqHnkJ61alVazlvxobs9W%2BCPPWjoeR6rNzKD6%2BSNw%2Fc87ZqIyAC&X-Amz-Signature=e6cac735170df753fdaa6e6e4d7aebdc25a8c4b1410a1ca819f54a47fe5b92bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

