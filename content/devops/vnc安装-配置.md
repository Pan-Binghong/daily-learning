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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYTX7C73%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHxJF101QtiN%2BDe7USGd3IqDfBknqEp6pCfCgYDscFCAiEAuKZT6%2BbPYANvKSDco%2FLw01le%2F2%2Bvf8Lo7eCE4YJ%2BdSUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDGZSTb7b54d81HJYdSrcA0e6qdUg%2BNd4pOGITwN%2BAL4YoAO7A5Sg%2F%2Fn9%2FwxHerrH5tfd0JdtpNTOfoFP1jn5LEvYdVONmd%2B0i0Hg5YY6zTJvIxrzREZaPslxJZVtfW2%2FE58EbMtCBEVIZaaOEI%2B65kl2x6ddbRRsNQWCE23%2FPdwnxJ2cFmU7pPJ8LQuTvfCiC%2Fw9vnWX%2BvQ4WDhdZOoq%2BkLWlmJgYUGVhBp40MACSLRLhK82FgmYpPIMt4IQD2yc80qfQgGEjV58lkQH8NFjVLoKd6BLb7Pm5mocuYVer2gKWsvTH1YGu8lJzrcgbAU9DdsbnncQEYTMZdYK101JUwjDz%2FJ7SS9b13mRbrGufgND2BN2pIrkEQv03dp5SOGxbFoNc2XuI68sB%2BNcfHZG%2F5%2BKvOt%2FbAE48FTIoiQmShx8D9LKHF%2BMAfHY9kk66DbGwN7WWjbowqjy5J12XgIgHtnpuyDXdKn7OdWh5bDN8SyrW0ZWlWOLiwNevDNZf9K8YR7SvujeW3tCQIkeAjx%2FQM2KxMyHJGMnGn0%2FY4rNEgcGRtDUaOx2PqooY58X7V0DAdO9TsxFfdmk0sdcohZt8oC9UFYIgdWy2IURh2VKVRmSPTTlF%2Fc0YvrpqZsThCv1q62IxF%2FiAcFE5hEkMIjkwcoGOqUBlU9eglQNRV7lBhvLz4r9ecjsBtUkfTeA%2FkCTawUfK7rPvQ1kFiPHiwDWqhBFangOrOBWfGEjkofgIbYY7%2FJrI1ZNBDoCaPcYqR27hbnMofjc2V7Z3TdChU%2FdyRtND5L5NfGjIs1fUQR2jyhFlt7ZUQ1rC%2B4Y7lEbdupcOV%2BaGn7hG%2BX%2BPz4oLnT8sbv5nhmk0LQwmcX5FGlhD%2BF6VJo%2FYibDwA4w&X-Amz-Signature=544fd9d0e12d65acf5a6abc0ea78a0ff9de3002ab5e9f0d731de0a31e6c8cc0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYTX7C73%2F20251228%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251228T030822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHxJF101QtiN%2BDe7USGd3IqDfBknqEp6pCfCgYDscFCAiEAuKZT6%2BbPYANvKSDco%2FLw01le%2F2%2Bvf8Lo7eCE4YJ%2BdSUq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDGZSTb7b54d81HJYdSrcA0e6qdUg%2BNd4pOGITwN%2BAL4YoAO7A5Sg%2F%2Fn9%2FwxHerrH5tfd0JdtpNTOfoFP1jn5LEvYdVONmd%2B0i0Hg5YY6zTJvIxrzREZaPslxJZVtfW2%2FE58EbMtCBEVIZaaOEI%2B65kl2x6ddbRRsNQWCE23%2FPdwnxJ2cFmU7pPJ8LQuTvfCiC%2Fw9vnWX%2BvQ4WDhdZOoq%2BkLWlmJgYUGVhBp40MACSLRLhK82FgmYpPIMt4IQD2yc80qfQgGEjV58lkQH8NFjVLoKd6BLb7Pm5mocuYVer2gKWsvTH1YGu8lJzrcgbAU9DdsbnncQEYTMZdYK101JUwjDz%2FJ7SS9b13mRbrGufgND2BN2pIrkEQv03dp5SOGxbFoNc2XuI68sB%2BNcfHZG%2F5%2BKvOt%2FbAE48FTIoiQmShx8D9LKHF%2BMAfHY9kk66DbGwN7WWjbowqjy5J12XgIgHtnpuyDXdKn7OdWh5bDN8SyrW0ZWlWOLiwNevDNZf9K8YR7SvujeW3tCQIkeAjx%2FQM2KxMyHJGMnGn0%2FY4rNEgcGRtDUaOx2PqooY58X7V0DAdO9TsxFfdmk0sdcohZt8oC9UFYIgdWy2IURh2VKVRmSPTTlF%2Fc0YvrpqZsThCv1q62IxF%2FiAcFE5hEkMIjkwcoGOqUBlU9eglQNRV7lBhvLz4r9ecjsBtUkfTeA%2FkCTawUfK7rPvQ1kFiPHiwDWqhBFangOrOBWfGEjkofgIbYY7%2FJrI1ZNBDoCaPcYqR27hbnMofjc2V7Z3TdChU%2FdyRtND5L5NfGjIs1fUQR2jyhFlt7ZUQ1rC%2B4Y7lEbdupcOV%2BaGn7hG%2BX%2BPz4oLnT8sbv5nhmk0LQwmcX5FGlhD%2BF6VJo%2FYibDwA4w&X-Amz-Signature=603c5f023a784dc0339d9dc4831aab732005817a670252bb9e34980faf746794&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

