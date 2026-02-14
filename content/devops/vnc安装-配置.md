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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VE3HCZX%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQC7CWyu%2Bmu6y7xHIXxl%2F2WCFDei%2FPozFvirnzDX3tYHnwIhAN05asXHFrTRAzieSfAllKJ7kIn6P8Al2uMiBU2E5LSIKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxF0bqZbfdjvnRJpRAq3ANWENvMfoyZHPJAF23sdHdaSL1RSpEEipmECDncB4fhk%2B9nNko6ygLokweC8gb%2F35Q629wooQX7u%2BB8w%2FzW%2F%2F4zosTyy1ZpKfmu%2Fh2AebNkniaU4psLZ5MHOerJx3dIel358U%2BU7vCa2hcFhFi4EVttvnySkuMwcuB6%2Fvdj20%2Fy86UiIuUuShoIsxBTvFARg46rnS5TXF5bDUycwphv3O9NAPjnjYFHIGo5hNQtNt4ZPZlRRMrfU81eGRBlFdGMqOzg%2FimtnWyyqxGovVFOS10wuvkR9KsRLTmO3pS9EHStqjH5y5qsM9DMx3pbJ%2FvpjZ5lAfHpEJgk5uWF%2BnbtDQBIWr%2F8dd35Evd1A2kojBhog5Ty9ev1M6cM%2B4ErVNZ4sshTb5s84Vinz5hWs6lIfJudBKeBS%2FJ4JU1bB9lAj%2BQZO9c7LvlUBTIJOZgiqGYpsclM5Lk%2BKD9Or%2F2LYoLxSiwynZLQkeCdXl%2BevxXHuGV4VLiMT6v1Ok0vaD2VwcaISo0xN6jNX65555Em9%2FYZL%2FXRxOyPzRTrpzBjFovEhT3afAJeGMo%2B767YNqJeUAILogetLgghinC5qHWkxfeJdOkPpUbVmeT4q0H2OHmL2widHlJUeJ2Vuefo0q%2BuSTD7wL%2FMBjqkARWqorXmcxfrcC%2B6DkUhqo7DWT8wl8wCQhDTvWnsyiKQ9HH8VV3sK%2BBHNHKJ%2BF0FDPxKBTwU6Mrs%2FFYCfSMv8TbrnKiERUqJLh5oQCJbEM42sn6QLoPkYW3rS4FTkkwY3HL4%2FOYEdJOx39hF5HAwkWBPUf%2B4Fw9mJBTvgdF9O7ZAEzLLuM38ECPe0n5L%2B5Evgz0y5RyTft3bXa14VQU8wjOudyp2&X-Amz-Signature=58af7fb2f13e7ba72daa932fc7bc1c63ebaf8e8feb180278116f46d4d9543ffd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VE3HCZX%2F20260214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260214T033112Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQC7CWyu%2Bmu6y7xHIXxl%2F2WCFDei%2FPozFvirnzDX3tYHnwIhAN05asXHFrTRAzieSfAllKJ7kIn6P8Al2uMiBU2E5LSIKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxF0bqZbfdjvnRJpRAq3ANWENvMfoyZHPJAF23sdHdaSL1RSpEEipmECDncB4fhk%2B9nNko6ygLokweC8gb%2F35Q629wooQX7u%2BB8w%2FzW%2F%2F4zosTyy1ZpKfmu%2Fh2AebNkniaU4psLZ5MHOerJx3dIel358U%2BU7vCa2hcFhFi4EVttvnySkuMwcuB6%2Fvdj20%2Fy86UiIuUuShoIsxBTvFARg46rnS5TXF5bDUycwphv3O9NAPjnjYFHIGo5hNQtNt4ZPZlRRMrfU81eGRBlFdGMqOzg%2FimtnWyyqxGovVFOS10wuvkR9KsRLTmO3pS9EHStqjH5y5qsM9DMx3pbJ%2FvpjZ5lAfHpEJgk5uWF%2BnbtDQBIWr%2F8dd35Evd1A2kojBhog5Ty9ev1M6cM%2B4ErVNZ4sshTb5s84Vinz5hWs6lIfJudBKeBS%2FJ4JU1bB9lAj%2BQZO9c7LvlUBTIJOZgiqGYpsclM5Lk%2BKD9Or%2F2LYoLxSiwynZLQkeCdXl%2BevxXHuGV4VLiMT6v1Ok0vaD2VwcaISo0xN6jNX65555Em9%2FYZL%2FXRxOyPzRTrpzBjFovEhT3afAJeGMo%2B767YNqJeUAILogetLgghinC5qHWkxfeJdOkPpUbVmeT4q0H2OHmL2widHlJUeJ2Vuefo0q%2BuSTD7wL%2FMBjqkARWqorXmcxfrcC%2B6DkUhqo7DWT8wl8wCQhDTvWnsyiKQ9HH8VV3sK%2BBHNHKJ%2BF0FDPxKBTwU6Mrs%2FFYCfSMv8TbrnKiERUqJLh5oQCJbEM42sn6QLoPkYW3rS4FTkkwY3HL4%2FOYEdJOx39hF5HAwkWBPUf%2B4Fw9mJBTvgdF9O7ZAEzLLuM38ECPe0n5L%2B5Evgz0y5RyTft3bXa14VQU8wjOudyp2&X-Amz-Signature=4802901ca8aafacfecad42ddaa7c7a75c0b7097e8c1d7002ad7ccef5dad9d23d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

