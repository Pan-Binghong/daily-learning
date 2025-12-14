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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NVLN3HW%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCCvthqZq3srFdUOFUPWyPVCa73UkWeOnbllUZf%2FZQjQwIgBERrk1PYqFjWZgYwq0eupffDJS5%2FL5gfpLk%2FB7T8oa8q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDFEO8xOQ9xbw41t7NCrcAwd3xlcERR53g8NtV3tYjqvgu4fX9cvB6hUoPelCsSQ080hh6hoCWUOCilXwDlflSMnVZT%2Fvwap8%2FPeWOYccSjFaiJRivRk2bWZADNujEdxP7iS5Af9p9TxBxx797R2UVoQtTojCxv3JpoMJFTDzejBoxNqAO2hhPNQpaBx%2Fq2ttO9M6LbqBnUSaJcRJ0lUZhO%2BJJA%2FaGX4xbmMD%2BpWyNIJxlJPchXrmv2G%2BiEHMC%2Fybqymhc1QcGeQjwi5G9YA1MsCHekM1t5b1ffwsN4jGCRPtSRUC3KSEGJpc%2BYlnC2jiRHb8TXKPkEm0op%2BzxRO52CkJC6wKpAs88GVDG2YGs5YhjiW0RKFAXhhgW19P9n%2FytDZXVc42cp7T1fbO94E8AfjV7NqcYzM3kXhhqLFD%2FUk0GptqJgeDi%2FlL%2Fv66ai5O6ulVaMXjfD%2FY0LKldybfflblXbOP8J6%2FDEpWSf%2BFoI5lxI%2FMgJMuxfaSyCyxGgTWbt4WZ8lBfqkPqUBQY4NNvDfQqc4IOTVROjaslh8d4B5z9mHY7ZP1QSWucnGd5l07UQUpVhxbBZ04y%2FlFumSEgdZdOYLONgI1DPP3CJSmoYcWC3fDCDk6YIMqY0ceI0zn1gXbbBKzd3pUzZ%2BeMLaw%2BMkGOqUB%2B1Iy9Ce7WKUR%2Bzto%2BfdvwftMz1SupiyWs3go07vrHJrOlrrYmSX%2FVvTlVQfIh%2BaF%2B8w4GVAZxHiPXlRR%2BSGLr%2BsIhLhI3U2KXJ34az83PKTNQS1aA4r4f3%2BTic6Smc0pIeBKW6QRq9qb3OEDX%2BmA3CQoKrOhQJcN9l3czwmO5nvig2kObJMJKAqjBlWNzykr3nJwNoqQEdd0paaHeW7wXg9Dw1xO&X-Amz-Signature=de0189d342aa76f8c1727395ee657c6cc40eb8c18bc8945ffb1d3ddbee63bbdf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NVLN3HW%2F20251214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251214T030042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQCCvthqZq3srFdUOFUPWyPVCa73UkWeOnbllUZf%2FZQjQwIgBERrk1PYqFjWZgYwq0eupffDJS5%2FL5gfpLk%2FB7T8oa8q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDFEO8xOQ9xbw41t7NCrcAwd3xlcERR53g8NtV3tYjqvgu4fX9cvB6hUoPelCsSQ080hh6hoCWUOCilXwDlflSMnVZT%2Fvwap8%2FPeWOYccSjFaiJRivRk2bWZADNujEdxP7iS5Af9p9TxBxx797R2UVoQtTojCxv3JpoMJFTDzejBoxNqAO2hhPNQpaBx%2Fq2ttO9M6LbqBnUSaJcRJ0lUZhO%2BJJA%2FaGX4xbmMD%2BpWyNIJxlJPchXrmv2G%2BiEHMC%2Fybqymhc1QcGeQjwi5G9YA1MsCHekM1t5b1ffwsN4jGCRPtSRUC3KSEGJpc%2BYlnC2jiRHb8TXKPkEm0op%2BzxRO52CkJC6wKpAs88GVDG2YGs5YhjiW0RKFAXhhgW19P9n%2FytDZXVc42cp7T1fbO94E8AfjV7NqcYzM3kXhhqLFD%2FUk0GptqJgeDi%2FlL%2Fv66ai5O6ulVaMXjfD%2FY0LKldybfflblXbOP8J6%2FDEpWSf%2BFoI5lxI%2FMgJMuxfaSyCyxGgTWbt4WZ8lBfqkPqUBQY4NNvDfQqc4IOTVROjaslh8d4B5z9mHY7ZP1QSWucnGd5l07UQUpVhxbBZ04y%2FlFumSEgdZdOYLONgI1DPP3CJSmoYcWC3fDCDk6YIMqY0ceI0zn1gXbbBKzd3pUzZ%2BeMLaw%2BMkGOqUB%2B1Iy9Ce7WKUR%2Bzto%2BfdvwftMz1SupiyWs3go07vrHJrOlrrYmSX%2FVvTlVQfIh%2BaF%2B8w4GVAZxHiPXlRR%2BSGLr%2BsIhLhI3U2KXJ34az83PKTNQS1aA4r4f3%2BTic6Smc0pIeBKW6QRq9qb3OEDX%2BmA3CQoKrOhQJcN9l3czwmO5nvig2kObJMJKAqjBlWNzykr3nJwNoqQEdd0paaHeW7wXg9Dw1xO&X-Amz-Signature=b2d8dc523565acbf0070d3c0a58a210cc4c7af52144e8beb295462b5c2c6b16a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

