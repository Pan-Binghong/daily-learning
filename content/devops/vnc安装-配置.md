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

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/e5533731-6b04-4ab5-baeb-4a6dcb57f177/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOB4UY4S%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6PvKTfVkUtxm6w6O35nkat0dEjgiFGUS5xKxsQMuTBgIhAIZQIfojenNc1ToGfExSwArBFaoRIj89XC%2FvwL%2FV%2Bm%2B%2FKv8DCGwQABoMNjM3NDIzMTgzODA1IgyyjJU9VF7DOAO%2F23Iq3APAEcCevH6Gtr%2Fi%2FY5wWqDikSAjz3H%2BNBuuuVm5%2BfqxmIrq310QZl%2FBvfKPsLEPjX4jPXeySm8jVWpH8hh8svjBr7H8%2BtpmlzCEd%2BlolnDTe2A1i2YBysm%2Fa%2FO9dS4njBshAvbN5r6GEBlCAu8UXN0WXmb201fO2QT10VKrbiVAXt0V0BIRg68AUOPni4AOvSViYy4T3tZEUEvnPNMEvDu3G37vbAqQoztAb81ztVXD0PNco%2BCGrSCMst5pFPE4E9SplAsUYbs%2FlwNVHEHU2cco3bsB9kYg6qcdF8pkY%2Bod32ntbcxuhd3SCcmYsmHvPPEJNe5IizeucJsdmsNDpUDYQSRzubbv%2BafK8xbZBwZYVMSvaDVta5fWC28UdutCRCsX0ptunqrkz8%2B1DUZT%2FL5R2iVXR6ad0zI639bCkgiz5BfwCaJ4R1dZmab2gv7aAnYOdzBjY2ailF5EniNkErRBtag6ZCsPSwFBvq8SsCtR44%2FdOCXA7pCqxXMi3FsvUMQuKC0dgoKYJ7tuzJgTY2srOumzbg845HAwl46%2BILhnR%2B167f1KVKwy0ibljq0Zoc4g7k4fgtugK31MpGM6G09pPNp%2BTrdkcSuaNcJSpYfk8EmB14W664DTpBpPCzC1p87JBjqkAbmdkeUTCzfcf7LUCaRoCe9yo0JV6vWooqjo3jnlZnU16kokUHIkQeZ7pknK4IRiiPHZgHXVHN3NESzR564uaDjV7CF8IVvN4FpoWcS7Xbso23QynXpFoiwLKfwBxuYMJ07rmANhobaW8ywI2tUFxihk7HQDP5RN1Zp1c0eAHEgVKfp2vA08OLgqt8ZRjw3xtOwSRGRpTSD5hLRW8MbgdDP0PSYZ&X-Amz-Signature=f22ac9286e818f025e1d93e1ab589d66e48f1a1eea99405a78e4a9ab381b6d2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

---

## 两台 Windows 电脑内下载并安装

- TightVNC官网地址
---

## TightVNC 服务端 (被连接端) 配置

- 启动
---

## TightVNC 客户端 (连接端) 配置

- 打开客户端
![](https://prod-files-secure.s3.us-west-2.amazonaws.com/fc187c04-cf34-444f-b5f2-bdcdfad76660/501a68f3-43c8-4924-9dc5-0e6e1bb6fe39/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VOB4UY4S%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T024225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6PvKTfVkUtxm6w6O35nkat0dEjgiFGUS5xKxsQMuTBgIhAIZQIfojenNc1ToGfExSwArBFaoRIj89XC%2FvwL%2FV%2Bm%2B%2FKv8DCGwQABoMNjM3NDIzMTgzODA1IgyyjJU9VF7DOAO%2F23Iq3APAEcCevH6Gtr%2Fi%2FY5wWqDikSAjz3H%2BNBuuuVm5%2BfqxmIrq310QZl%2FBvfKPsLEPjX4jPXeySm8jVWpH8hh8svjBr7H8%2BtpmlzCEd%2BlolnDTe2A1i2YBysm%2Fa%2FO9dS4njBshAvbN5r6GEBlCAu8UXN0WXmb201fO2QT10VKrbiVAXt0V0BIRg68AUOPni4AOvSViYy4T3tZEUEvnPNMEvDu3G37vbAqQoztAb81ztVXD0PNco%2BCGrSCMst5pFPE4E9SplAsUYbs%2FlwNVHEHU2cco3bsB9kYg6qcdF8pkY%2Bod32ntbcxuhd3SCcmYsmHvPPEJNe5IizeucJsdmsNDpUDYQSRzubbv%2BafK8xbZBwZYVMSvaDVta5fWC28UdutCRCsX0ptunqrkz8%2B1DUZT%2FL5R2iVXR6ad0zI639bCkgiz5BfwCaJ4R1dZmab2gv7aAnYOdzBjY2ailF5EniNkErRBtag6ZCsPSwFBvq8SsCtR44%2FdOCXA7pCqxXMi3FsvUMQuKC0dgoKYJ7tuzJgTY2srOumzbg845HAwl46%2BILhnR%2B167f1KVKwy0ibljq0Zoc4g7k4fgtugK31MpGM6G09pPNp%2BTrdkcSuaNcJSpYfk8EmB14W664DTpBpPCzC1p87JBjqkAbmdkeUTCzfcf7LUCaRoCe9yo0JV6vWooqjo3jnlZnU16kokUHIkQeZ7pknK4IRiiPHZgHXVHN3NESzR564uaDjV7CF8IVvN4FpoWcS7Xbso23QynXpFoiwLKfwBxuYMJ07rmANhobaW8ywI2tUFxihk7HQDP5RN1Zp1c0eAHEgVKfp2vA08OLgqt8ZRjw3xtOwSRGRpTSD5hLRW8MbgdDP0PSYZ&X-Amz-Signature=49da9b791fe721486e1b0905e570622c6ce3bbd10fae75de4a0cac640e75e22f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

- 输入IP端口点击“Connect”连接即可。


---

> References

