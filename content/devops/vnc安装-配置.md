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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN466GOA%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCo%2FWzLNFUeHMhJzBEX9oAt9hx%2FFne5vI8sC%2FW3zSuhsAIhAO0vBbBAkrRK0SoONnQ1IPUGaBqNvBWffj9TmFxJ3r7mKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsendTCtUGCxJq5HMq3AMJ38Rt5bdpwEkHsEvT%2BBXo5pW1%2Bm6esWm7xLeYw5Owbrhjavu0VimvHrD0dl103VCMNg6PJCrSJcgAXKiBVmU%2FcKuUQEwVliO8L6Hd0RA6x%2BmwGE4lEgKWZ0gu4hA46QzddSXR%2F8zNqYKhRHQnoddIAADrKLzU54b%2BhZDNIe%2FwLVAbxH7P8jGOkfIPjKqsNb%2FcJ2EkxR%2FO%2FFv8%2F1V%2FJTLdGHd5t%2F7szBYmL%2FNCN5W9DNeKpI8uIBNxh5mRSdQ9zJ%2BlJ1crayn8mLUhzLVw%2BIoeTCB%2BA%2FVzZ%2BFsEAdPoPpHgSWXQOzvCK%2B8qT07LaRzbVI5z9lQi3AS01r4BX9d3AlY2uP0iUZNGIhPUpbhM1MFXyWqryY3elczd71wAOqZ14UcQYwkUN2mpJPIZ1At6bzmdD%2BDuimi36a8TEZjjmpPZ1unxDRKRZh97RkbDLzOalqOwg%2Be1hYCiVZHtOAZTqLTbZzipXawFYHon02nF3B38A%2FSFPIPim9ZvtSDHrI9toVuTWziziy58E0%2BzTOsc298QfkIVX%2FbW94PHUccuRQHMog3tQlI1XiCc1HpwptJ%2FWkDCgBOl2wcfim29On2NWttwzp%2FJQONbqVyCnALlgSS0chOlpR370LuEhoC9TDnrcvLBjqkAQglWRN0ujt0SwwYF06ioqgqHU51YB%2Fkr4kbYsk1KSmaoe6OgxJkLlBiVi53yitHqmz63GgTWfqmKnr7tUWA1ptWTjCfRp3i56Iip7V4i6WRd%2FNQ44VnO%2Ft%2FOpS9CNhokGgquPbvfz9hSXlJpNshLGZGY6qWPN8hMXDo%2Bv4zWsP6wvX%2FV%2BNvVXp%2BS%2B893E0Qm%2Bhc3hQb73XgC1jXDsiY8rKKmU%2BL&X-Amz-Signature=5ed6d39e8b767d40cc7e0889350e88d776c423ba2e0fdd4fee38cc011cc6ed62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN466GOA%2F20260123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260123T030352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCo%2FWzLNFUeHMhJzBEX9oAt9hx%2FFne5vI8sC%2FW3zSuhsAIhAO0vBbBAkrRK0SoONnQ1IPUGaBqNvBWffj9TmFxJ3r7mKogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsendTCtUGCxJq5HMq3AMJ38Rt5bdpwEkHsEvT%2BBXo5pW1%2Bm6esWm7xLeYw5Owbrhjavu0VimvHrD0dl103VCMNg6PJCrSJcgAXKiBVmU%2FcKuUQEwVliO8L6Hd0RA6x%2BmwGE4lEgKWZ0gu4hA46QzddSXR%2F8zNqYKhRHQnoddIAADrKLzU54b%2BhZDNIe%2FwLVAbxH7P8jGOkfIPjKqsNb%2FcJ2EkxR%2FO%2FFv8%2F1V%2FJTLdGHd5t%2F7szBYmL%2FNCN5W9DNeKpI8uIBNxh5mRSdQ9zJ%2BlJ1crayn8mLUhzLVw%2BIoeTCB%2BA%2FVzZ%2BFsEAdPoPpHgSWXQOzvCK%2B8qT07LaRzbVI5z9lQi3AS01r4BX9d3AlY2uP0iUZNGIhPUpbhM1MFXyWqryY3elczd71wAOqZ14UcQYwkUN2mpJPIZ1At6bzmdD%2BDuimi36a8TEZjjmpPZ1unxDRKRZh97RkbDLzOalqOwg%2Be1hYCiVZHtOAZTqLTbZzipXawFYHon02nF3B38A%2FSFPIPim9ZvtSDHrI9toVuTWziziy58E0%2BzTOsc298QfkIVX%2FbW94PHUccuRQHMog3tQlI1XiCc1HpwptJ%2FWkDCgBOl2wcfim29On2NWttwzp%2FJQONbqVyCnALlgSS0chOlpR370LuEhoC9TDnrcvLBjqkAQglWRN0ujt0SwwYF06ioqgqHU51YB%2Fkr4kbYsk1KSmaoe6OgxJkLlBiVi53yitHqmz63GgTWfqmKnr7tUWA1ptWTjCfRp3i56Iip7V4i6WRd%2FNQ44VnO%2Ft%2FOpS9CNhokGgquPbvfz9hSXlJpNshLGZGY6qWPN8hMXDo%2Bv4zWsP6wvX%2FV%2BNvVXp%2BS%2B893E0Qm%2Bhc3hQb73XgC1jXDsiY8rKKmU%2BL&X-Amz-Signature=abdf37be969dfcdf3645a097fcf86544c132402c66912e5c8a7a0e09c20c1e9a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

